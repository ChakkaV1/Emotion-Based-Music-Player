import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator


class ModelHandler:
    def __init__(self, model_path, test_dir, image_height, image_width, batch_size):
        self.model_path = model_path
        self.test_dir = test_dir
        self.image_height = image_height
        self.image_width = image_width
        self.batch_size = batch_size
        self.model = load_model(model_path)
    
    def evaluate_model(self):
        test_datagen = ImageDataGenerator(rescale=1./255)  # Normalize images
        
        test_generator = test_datagen.flow_from_directory(
            self.test_dir,
            target_size=(self.image_height, self.image_width),
            batch_size=self.batch_size,
            class_mode='binary'  # or 'categorical', depending on your classification system
        )
        
        loss, accuracy = self.model.evaluate(test_generator, steps=np.ceil(test_generator.samples/test_generator.batch_size))
        print(f"Test Loss: {loss}")
        print(f"Test Accuracy: {accuracy}")

# Usage
model_handler = ModelHandler(
    model_path='Tensorflow/model_complete1.h5',
    test_dir='data/test',
    image_height=48,
    image_width=48,
    batch_size=64
)


model_handler.evaluate_model()
