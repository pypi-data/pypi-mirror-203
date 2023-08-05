# markov_chain.py
# Author: Jacob Schreiber <jmschreiber91@gmail.com>

import torch

from ._utils import _cast_as_tensor
from ._utils import _update_parameter
from ._utils import _check_parameter
from ._utils import _reshape_weights

from .distributions._distribution import Distribution
from .distributions import Categorical
from .distributions import ConditionalCategorical


class MarkovChain(Distribution):
	def __init__(self, distributions=None, k=None, n_categories=None, 
		inertia=0.0, frozen=False):
		super().__init__(inertia=inertia, frozen=frozen)
		self.name = "MarkovChain"

		self.distributions = _check_parameter(distributions, "distributions",
			dtypes=(list, tuple))
		self.k = _check_parameter(_cast_as_tensor(k, dtype=torch.int32), "k",
			ndim=0)
		self.n_categories = _check_parameter(n_categories, "n_categories",
			dtypes=(list, tuple))

		if distributions is None and k is None:
			raise ValueError("Must provide one of 'distributions', or 'k'.")

		if distributions is not None:
			self.k = len(distributions) - 1
		
		if n_categories is None:
			self.n_categories = [None for i in range(self.k+1)]

		self.d = None
		self._initialized = distributions is not None and distributions[0]._initialized
		self._reset_cache()

	def _initialize(self, d):
		self.distributions = [Categorical(n_categories=self.n_categories[0])]
		for i in range(self.k):
			self.distributions.append(ConditionalCategorical(n_categories=self.n_categories[i+1]))

		self._initialized = True
		super()._initialize(d)

	def _reset_cache(self):
		if self._initialized:
			for distribution in self.distributions:
				distribution._reset_cache()

	def log_probability(self, X):
		X = _check_parameter(_cast_as_tensor(X), "X", ndim=3)
		self.d = X.shape[1]

		logps = self.distributions[0].log_probability(X[:, 0])
		for i, distribution in enumerate(self.distributions[1:-1]):
			logps += distribution.log_probability(X[:, :i+2])

		for i in range(X.shape[1] - self.k):
			j = i + self.k + 1
			logps += self.distributions[-1].log_probability(X[:, i:j])

		return logps

	def fit(self, X, sample_weight=None):
		self.summarize(X, sample_weight=sample_weight)
		self.from_summaries()
		return self

	def summarize(self, X, sample_weight=None):
		if self.frozen:
			return

		if not self._initialized:
			self._initialize(len(X[0]))

		X = _check_parameter(_cast_as_tensor(X), "X", ndim=3)
		sample_weight = _check_parameter(_cast_as_tensor(sample_weight), 
			"sample_weight", min_value=0, ndim=(1, 2))

		if sample_weight is None:
			sample_weight = torch.ones_like(X[:, 0])
		elif len(sample_weight.shape) == 1: 
			sample_weight = sample_weight.reshape(-1, 1).expand(-1, X.shape[2])
		elif sample_weight.shape[1] == 1:
			sample_weight = sample_weight.expand(-1, X.shape[2])

		_check_parameter(_cast_as_tensor(sample_weight), "sample_weight", 
			min_value=0, ndim=2, shape=(X.shape[0], X.shape[2]))

		self.distributions[0].summarize(X[:, 0], sample_weight=sample_weight)
		for i, distribution in enumerate(self.distributions[1:-1]):
			distribution.summarize(X[:, :i+2], sample_weight=sample_weight)

		distribution = self.distributions[-1]
		for i in range(X.shape[1] - self.k):
			j = i + self.k + 1
			distribution.summarize(X[:, i:j], sample_weight=sample_weight)

	def from_summaries(self):
		if self.frozen:
			return

		for distribution in self.distributions:
			distribution.from_summaries()