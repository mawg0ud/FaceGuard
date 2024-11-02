import torch.nn.functional as F

def activation_loss(pred, target):
    return F.binary_cross_entropy(pred, target)

def segmentation_loss(pred, target):
    return F.cross_entropy(pred, target)

def reconstruction_loss(pred, target):
    return F.mse_loss(pred, target)
