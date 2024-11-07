import torch
from torch.utils.data import DataLoader
from models.auto_encoder import YAutoEncoder
from data_preprocessing.data_loader import FaceForensicsDataset
from data_preprocessing.augmentation import get_train_augmentations
from utils.config_loader import load_config
from utils.logger import setup_logger
from models.loss_functions import activation_loss, segmentation_loss, reconstruction_loss
from utils.save_load_model import load_model, save_model

def run_transfer_learning():
    config = load_config('configs/experiment4_transfer_learning.yaml')
    logger = setup_logger('logs/experiment4_transfer_learning.log')

    # Load and prepare dataset
    train_augmentations = get_train_augmentations(config['image_size'])
    train_dataset = FaceForensicsDataset(config['data_dir'], phase='train', augmentations=train_augmentations)
    train_loader = DataLoader(train_dataset, batch_size=config['batch_size'], shuffle=True, num_workers=config['num_workers'])

    # Load pretrained model and fine-tune it
    model = YAutoEncoder().to(config['device'])
    model = load_model(model, config['pretrained_model_path'])
    optimizer = torch.optim.Adam(model.parameters(), lr=config['learning_rate'])
    
    logger.info("Starting transfer learning experiment...")
    for epoch in range(config['fine_tune_epochs']):
        model.train()
        epoch_loss = 0
        for images, masks in train_loader:
            images, masks = images.to(config['device']), masks.to(config['device'])
            optimizer.zero_grad()
            seg_output, rec_output = model(images)
            
            # Calculate loss with transfer learning weights
            loss = (activation_loss(seg_output, masks) * config['activation_weight'] +
                    segmentation_loss(seg_output, masks) * config['segmentation_weight'] +
                    reconstruction_loss(rec_output, images) * config['reconstruction_weight'])
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()
        logger.info(f"Epoch {epoch+1}/{config['fine_tune_epochs']}, Loss: {epoch_loss/len(train_loader)}")

    # Save fine-tuned model
    model_path = os.path.join(config['output_dir'], 'fine_tuned_model.pth')
    save_model(model, model_path)
    logger.info(f"Fine-tuned model saved to {model_path}")

if __name__ == "__main__":
    run_transfer_learning()
