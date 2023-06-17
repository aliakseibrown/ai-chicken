import torch
import cv2
import torchvision.transforms as transforms
import argparse
from agent.neural_network.model import CNNModel
# construct the argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', 
    default='',
    help='path to the input image')
args = vars(parser.parse_args())

def main(path):
    # the computation device
    device = ('cuda' if torch.cuda.is_available() else 'cpu')
    # list containing all the class labels
    labels = [
        'bean', 'bitter gourd', 'bottle gourd', 'brinjal', 'broccoli',
        'cabbage', 'capsicum', 'carrot', 'cauliflower', 'cucumber',
        'papaya', 'potato', 'pumpkin', 'radish', 'tomato'
        ]

    # initialize the model and load the trained weights
    model = CNNModel().to(device)
    checkpoint = torch.load('./agent/neural_network/outputs/model.pth', map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()

    # define preprocess transforms
    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.5, 0.5, 0.5],
            std=[0.5, 0.5, 0.5]
        )
    ])  


    # read and preprocess the image
    image = cv2.imread(path)
    # get the ground truth class
    gt_class = path.split('/')[-2]
    orig_image = image.copy()
    # convert to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = transform(image)
    # add batch dimension
    image = torch.unsqueeze(image, 0)
    with torch.no_grad():
        outputs = model(image.to(device))
    output_label = torch.topk(outputs, 1)
    pred_class = labels[int(output_label.indices)]
    
    return pred_class

if __name__ == "__main__":
    main(args['input'])