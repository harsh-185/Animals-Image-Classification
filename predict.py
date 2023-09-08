import tensorflow as tf
from keras.models import load_model
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

animals={0: 'antelope', 1: 'badger', 2: 'bat', 3: 'bear', 4: 'bee', 5: 'beetle', 6: 'bison', 7: 'boar', 8: 'butterfly', 9: 'cat', 10: 'caterpillar', 11: 'chimpanzee', 12: 'cockroach', 13: 'cow', 14: 'coyote', 15: 'crab', 16: 'crow', 17: 'deer', 18: 'dog', 19: 'dolphin', 20: 'donkey', 21: 'dragonfly', 22: 'duck', 23: 'eagle', 24: 'elephant', 25: 'flamingo', 26: 'fly', 27: 'fox', 28: 'goat', 29: 'goldfish', 30: 'goose', 31: 'gorilla', 32: 'grasshopper', 33: 'hamster', 34: 'hare', 35: 'hedgehog', 36: 'hippopotamus', 37: 'hornbill', 38: 'horse', 39: 'hummingbird', 40: 'hyena', 41: 'jellyfish', 42: 'kangaroo', 43: 'koala', 44: 'ladybugs', 45: 'leopard', 46: 'lion', 47: 'lizard', 48: 'lobster', 49: 'mosquito', 50: 'moth', 51: 'mouse', 52: 'octopus', 53: 'okapi', 54: 'orangutan', 55: 'otter', 56: 'owl', 57: 'ox', 58: 'oyster', 59: 'panda', 60: 'parrot', 61: 'pelecaniformes', 62: 'penguin', 63: 'pig', 64: 'pigeon', 65: 'porcupine', 66: 'possum', 67: 'raccoon', 68: 'rat', 69: 'reindeer', 70: 'rhinoceros', 71: 'sandpiper', 72: 'seahorse', 73: 'seal', 74: 'shark', 75: 'sheep', 76: 'snake', 77: 'sparrow', 78: 'squid', 79: 'squirrel', 80: 'starfish', 81: 'swan', 82: 'tiger', 83: 'turkey', 84: 'turtle', 85: 'whale', 86: 'wolf', 87: 'wombat', 88: 'woodpecker', 89: 'zebra'}

model = load_model('FinalModel.h5', compile = True)
testing_datagen = ImageDataGenerator(rescale = 1./255,validation_split=0)
testing_data = testing_datagen.flow_from_directory('testing',
    target_size=(299,299),
    class_mode=None,
    batch_size=1,
    subset="training")

print(animals[np.argmax(model.predict(testing_data))])

