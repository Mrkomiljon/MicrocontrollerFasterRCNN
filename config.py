import torch

BATCH_SIZE = 8
RESIZE_TO = 512 
NUM_EPOCHS = 50

DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# Path for data
TRAIN_DIR = 'C:\\Users\\USER\\Desktop\\MicrocontrollerDetection\\dataset\\train'
VALID_DIR = 'C:\\Users\\USER\\Desktop\\MicrocontrollerDetection\\dataset\\test'

# Classes: 0 index is given for background
CLASSES = [
    'background', 'Arduino_Nano', 'ESP8266', 'Raspberry_Pi_3', 'Heltec_ESP32_Lora'
]

NUM_CLASSES = 5

# visualization transformed images
VISUALIZE_TRANSFORMED_IMAGES = False 

# location for save models and plots
OUT_DIR = 'C:\\Users\\USER\\Desktop\\MicrocontrollerDetection\\\outputs'
SAVE_PLOTS_EPOCH = 2
SAVE_MODEL_EPOCH = 2