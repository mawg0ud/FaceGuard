import torch
from torch.optim import Adam
from models.auto_encoder import YAutoEncoder
from data_preprocessing.data_loader import FaceForensicsDataset
from utils.logger import setup_logger
from models.loss_functions import activation_loss, segmentation_loss, reconstruction_loss

def train(model, dataloader, epochs, learning_rate):
    optimizer = Adam(model.parameters(), lr=learning_rate)
    logger = setup_logger('training.log')
    for epoch in range(epochs):
        for images, masks in dataloader:
            seg_output, rec_output = model(images)
            # Compute loss and backpropagate
            optimizer.zero_grad()
            # Combined losses
            loss = activation_loss(seg_output, masks) + reconstruction_loss(rec_output, images)
            loss.backward()
            optimizer.step()
            logger.info(f"Epoch {epoch}, Loss: {loss.item()}")
