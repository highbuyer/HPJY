import torch

import torch.optim as optim

import torch.nn as nn

# from torchviz import make_dot

devices = 'cuda' if torch.cuda.is_available() else 'cpu'
x_train = torch.randn(1)
x_train_tensor = torch.from_numpy(x_train).float().to(devices)
