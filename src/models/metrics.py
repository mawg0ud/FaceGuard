import torch

def compute_accuracy(pred, target):
    return (pred.argmax(dim=1) == target).float().mean().item()

def compute_eer(pred, target):
    # Example code to calculate the Equal Error Rate
    return 0.0  # Placeholder
