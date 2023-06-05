import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# Load the saved model
class NNModel: 
     #load model
    def __init__(self, path):

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.class_names = ['Bean', 'Bitter_Gourd', 'Bottle_Gourd', 'Brinjal', 
                            'Broccoli', 'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 
                            'Cucumber', 'Papaya', 'Potato', 'Pumpkin', 'Radish', 'Tomato']
        
        self.model = models.resnet18(pretrained=False)
        self.num_classes = len(self.class_names)
        self.model.fc = nn.Linear(self.model.fc.in_features, self.num_classes)
        self.model.load_state_dict(torch.load(path))        #"neural_network/save/first_model.pth"

        #self.model.to(self.device)
        self.model.eval()
        print(self.class_names)
        print(self.num_classes)

    def input_image(self, path): #"resources/image.jpg"
        # Define the image transformations
        preprocess = transforms.Compose([
            transforms.Resize(224),
            #transforms.CenterCrop(224),
            transforms.ToTensor(),
            #transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        
        # Preprocess the input image
        self.input_image = Image.open(path).convert("RGB")
        self.input_tensor = preprocess(self.input_image)
        print("Input image shape:", self.input_image.size)
        input_batch = self.input_tensor.unsqueeze(0) 
        return input_batch

    def predicte(self, input_batch):
        with torch.no_grad():
            self.input_batch = input_batch.to(self.device)
            self.output = self.model(self.input_batch)

            print("Output shape:", self.output.shape)
            print("Number of classes:", self.num_classes)

         # Get the predicted class probabilities and labels
        self.probabilities = torch.nn.functional.softmax(self.output[0], dim=0)
        self.predicted_class_index = torch.argmax(self.probabilities).item()
        self.predicted_class = self.class_names[self.predicted_class_index]

        # Use the predicted class in your game logic
        print(f"The predicted class is: {self.predicted_class}")