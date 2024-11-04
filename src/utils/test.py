from models.auto_encoder import YAutoEncoder
from data_preprocessing.data_loader import FaceForensicsDataset
from utils.save_load_model import load_model

def test(model, dataloader):
    model.eval()
    with torch.no_grad():
        for images, masks in dataloader:
            seg_output, rec_output = model(images)
            # Compute and print metrics
