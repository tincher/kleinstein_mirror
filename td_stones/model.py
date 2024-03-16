from torch import nn


class TDStones(nn.Module):
    def __init__(self, hidden_units, input_units=40):
        super().__init__()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(input_units, hidden_units),
            nn.ReLU(),
            nn.Linear(hidden_units, hidden_units),
            nn.ReLU(),
            nn.Linear(hidden_units, 2),
            nn.Softmax(dim=0)
        )

    def forward(self, x):
        probs = self.linear_relu_stack(x)
        return probs
