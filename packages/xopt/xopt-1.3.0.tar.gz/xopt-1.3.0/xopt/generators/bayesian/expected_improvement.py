import pandas as pd
import torch
from botorch.acquisition import qExpectedImprovement

from xopt.generators.bayesian.bayesian_generator import BayesianGenerator
from xopt.generators.bayesian.custom_botorch.constrained_acqusition import (
    ConstrainedMCAcquisitionFunction,
)
from xopt.generators.bayesian.options import BayesianOptions
from xopt.utils import format_option_descriptions
from xopt.vocs import VOCS


class ExpectedImprovementGenerator(BayesianGenerator):
    alias = "expected_improvement"
    __doc__ = (
        """Implements Bayeisan Optimization using the Upper Confidence Bound
        acquisition function"""
        + f"{format_option_descriptions(BayesianOptions())}"
    )

    def __init__(self, vocs: VOCS, options: BayesianOptions = None):
        """
        Generator using Expected improvement acquisition function

        Parameters
        ----------
        vocs: dict
            Standard vocs dictionary for xopt

        options: BayesianOptions
            Specific options for this generator
        """
        options = options or BayesianOptions()
        if not type(options) is BayesianOptions:
            raise ValueError("options must be a `BayesianOptions` object")

        if vocs.n_objectives != 1:
            raise ValueError("vocs must have one objective for optimization")

        super().__init__(vocs, options)

    @staticmethod
    def default_options() -> BayesianOptions:
        return BayesianOptions()

    def _get_acquisition(self, model):
        valid_data = self.data[
            pd.unique(self.vocs.variable_names + self.vocs.output_names)
        ].dropna()
        objective_data = self.vocs.objective_data(valid_data, "")

        best_f = torch.tensor(objective_data.max(), **self._tkwargs)

        qEI = qExpectedImprovement(
            model,
            best_f=best_f,
            sampler=self.sampler,
            objective=self._get_objective(),
        )

        cqUCB = ConstrainedMCAcquisitionFunction(
            model,
            qEI,
            self._get_constraint_callables(),
        )

        return cqUCB
