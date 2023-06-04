#imports
import os
import torch
import torch.nn as nn
import torch.optim as optim #optimisation algorithmes
import torch.nn.functional as F
from torch.utils.data import DataLoader
from numpy import mean, std 
import torchvision.datasets as datasets #import datsets 
import torchvision.transforms as transforms
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, models, transforms
import time
import os
import copy

#create fully connected network
class NN(nn.Module):
    def __init__(self, input_size, num_classes): #1 layer (28x28 = 784 nodes)
        super(NN,self).__init__()
        self.fc1 = nn.Linear(input_size, 50)
        self.fc2 = nn.Linear(50,num_classes)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

#set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#hyperparameters
input_size = 784
num_classes = 10
learning_rate = 0.001
batch_size = 64
num_epochs = 1
# Define data transformations
data_transforms = {
    "train": transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    "validation": transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
}

# Set the path to your vegetable images folder
data_dir = "neural_network/dataset/vegetables"

# Load the dataset from the folder
image_datasets = {x: datasets.ImageFolder(f"{data_dir}/{x}", data_transforms[x])
                  for x in ["train", "validation"]}
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4, shuffle=True, num_workers=4)
               for x in ["train", "validation"]}
dataset_sizes = {x: len(image_datasets[x]) for x in ["train", "validation"]}
class_names = image_datasets["train"].classes
num_classes = len(class_names)

#initialize network 
#model = NN(input_size=input_size, num_classes=num_classes).to(device)
model = models.resnet18(pretrained=True)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, num_classes)
model = model.to(device)

#loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

#train network
for epoch in range(num_epochs): #epoch is a number of all pictures in dataset
    for batch_idx, (data, targets) in enumerate(train_loader):
        #get data to cuda if possible
        data = data.to(device = device)
        targets = targets.to(device = device)

        #get to correct shape
        data = data.reshape(data.shape[0], -1)

        # forward
        scores = model(data)
        loss = criterion(scores, targets)

        #backward
        optimizer.zero_grad()
        loss.backward()

        #gradient descent or adam step
        optimizer.step()


#check accuracy on training and test to see how good our model

def check_accuracy(loader, model):
    if loader.dataset.train: 
        print("Checking accuracy on training data")
    else:
        print("Checking accuracy on test data")

    num_correct = 0
    num_samples = 0
    model.eval()

    with torch.no_grad():
        for x,y in loader:
            x = x.to(device = device)
            y = y.to(device = device)
            x = x.reshape(x.shape[0], -1)

            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples +=  predictions.size(0)

        print(f'Got {num_correct} / {num_samples} with accuracy {float(num_correct)/float(num_samples)*100:.2f}')
             
    model.train()
  
check_accuracy(train_loader, model) 
check_accuracy(test_loader, model)


