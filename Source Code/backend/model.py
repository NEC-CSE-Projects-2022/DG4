import torch
import torch.nn as nn
import numpy as np

class GatedLayer(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.fc = nn.Linear(input_dim, output_dim)
        self.gate = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.fc(x) * torch.sigmoid(self.gate(x))


class SelfAttention(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.q = nn.Linear(dim, dim)
        self.k = nn.Linear(dim, dim)
        self.v = nn.Linear(dim, dim)

    def forward(self, x):
        scores = torch.matmul(self.q(x), self.k(x).T) / np.sqrt(x.shape[1])
        weights = torch.softmax(scores, dim=-1)
        return torch.matmul(weights, self.v(x))


class SA_DGNet(nn.Module):
    def __init__(self, input_dim):
        super().__init__()

        # 🔑 NAMES MUST MATCH CHECKPOINT
        self.gate1 = GatedLayer(input_dim, 128)
        self.attn1 = SelfAttention(128)

        self.dropout = nn.Dropout(0.2)
        self.out = nn.Linear(128, 1)

    def forward(self, x):
        x = self.gate1(x)
        x = self.attn1(x)
        x = self.dropout(x)
        return self.out(x)