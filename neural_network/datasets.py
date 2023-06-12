import torchvision
import torch
import torchvision.transforms as transforms

from torch.utils.data import DataLoader

BATCH_SIZE = 64


train_transform = transforms.Compose([
    transforms.Resize((224, 224)), #validate that all images are 224x244
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomVerticalFlip(p=0.5),
    transforms.GaussianBlur(kernel_size=(5, 9), sigma=(0.1, 5)),
    transforms.RandomRotation(degrees=(30, 70)), #random effects are applied to prevent overfitting
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.5, 0.5, 0.5],
        std=[0.5, 0.5, 0.5]
    )
])

valid_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.5, 0.5, 0.5],
        std=[0.5, 0.5, 0.5]
    )
])

train_dataset = torchvision.datasets.ImageFolder(root='./images/train', transform=train_transform)

validation_dataset = torchvision.datasets.ImageFolder(root='./images/validation', transform=valid_transform)

train_loader = DataLoader(
    train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0, pin_memory=True
)

valid_loader = DataLoader(
    validation_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=0, pin_memory=True
)