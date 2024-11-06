import torch
from torch.utils.data import DataLoader
from models.auto_encoder import YAutoEncoder
from data_preprocessing.data_loader import FaceForensicsDataset
from data_preprocessing.augmentation import get_train_augmentations
from utils.config_loader import load_config
from utils.logger import setup_logger
from models.loss_functions import activation_loss, segmentation_loss, reconstruction_loss
from utils.save_load_model import save_model
import os

def run_tuning_experiment():
    config = load_config('configs/experiment2_hyperparameter_tuning.yaml')
    logger = setup_logger('logs/experiment2_hyperparameter_tuning.log')

    # Load dataset and DataLoader with augmented settings
    train_augmentations = get_train_augmentations(config['image_size'])
    train_dataset = FaceForensicsDataset(config['data_dir'], phase='train', augmentations=train_augmentations)
    train_loader = DataLoader(train_dataset, batch_size=config['batch_size'], shuffle=True, num_workers=config['num_workers'])

    # Initialize model and optimizer with tuned learning rate
    model = YAutoEncoder().to(config['device'])
    optimizer = torch.optim.Adam(model.parameters(), lr=config['learning_rate'])
    
    logger.info("Starting hyperparameter tuning experiment...")
    for epoch in range(config['epochs']):
        model.train()
        epoch_loss = 0
        for images, masks in train_loader:
            images, masks = images.to(config['device']), masks.to(config['device'])
            optimizer.zero_grad()
            seg_output, rec_output = model(images)
            
            # Compute tuned loss
            loss = (activation_loss(seg_output, masks) * config['activation_weight'] +
                    segmentation_loss(seg_output, masks) * config['segmentation_weight'] +
                    reconstruction_loss(rec_output, images) * config['reconstruction_weight'])
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()
        logger.info(f"Epoch {epoch+1}/{config['epochs']}, Loss: {epoch_loss/len(train_loader)}")

    # Save tuned model checkpoint
    model_path = os.path.join(config['output_dir'], 'tuned_model.pth')
    save_model(model, model_path)
    logger.info(f"Tuned model saved to {model_path}")

if __name__ == "__main__":
    run_tuning_experiment()
