import torch
import torch.nn as nn

class YAutoEncoder(nn.Module):
    def __init__(self):
        super(YAutoEncoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            # additional layers
        )
        self.decoder_seg = nn.Sequential(
            nn.ConvTranspose2d(64, 3, kernel_size=3, padding=1),
            nn.Softmax(dim=1)
        )
        self.decoder_rec = nn.Sequential(
            nn.ConvTranspose2d(64, 3, kernel_size=3, padding=1),
            nn.Tanh()
        )

    def forward(self, x):
        encoded = self.encoder(x)
        seg_output = self.decoder_seg(encoded)
        rec_output = self.decoder_rec(encoded)
        return seg_output, rec_output
