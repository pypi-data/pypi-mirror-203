import torch


class TransformedModel(torch.nn.Module):
    """
    Fixed model that requires an input and outcome transform to evaluate
    Transformer objects must have a forward method that transforms tensors into input
    coordinates for model and an untransform method that does the reverse.
    """

    def __init__(self, model, input_transformer, outcome_transformer):
        """
        model: torch.nn.Module object
        input_transformer:
        """
        super().__init__()
        self.model = model
        self.model.eval()
        self.model.requires_grad_(False)
        self.input_transformer = input_transformer
        self.outcome_transformer = outcome_transformer

    def set_transformers(self, eval_mode=True):
        """set transformers to eval mode if they are torch.nn.Module objects -
        prevents transformer training during evaluation
        if `eval_mode` is true set to eval, otherwise set to train
        """
        modules = [self.input_transformer, self.outcome_transformer]
        for m in modules:
            if isinstance(m, torch.nn.Module):
                if eval_mode:
                    m.eval()
                else:
                    m.train()

    def evaluate_model(self, x):
        """Placeholder method which can be used to modify model calls."""
        return self.model(x)

    def forward(self, x):
        # set transformers to eval mode
        self.set_transformers(eval_mode=True)

        # transform inputs to model space
        x_model = self.input_transformer(x)

        # evaluate model
        y_model = self.evaluate_model(x_model)

        # transform outputs
        y = self.outcome_transformer.untransform(y_model)

        self.set_transformers(eval_mode=False)

        return y
