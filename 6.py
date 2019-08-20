import os
import zipfile
import random
import wget
import tensorflow as tf
from shutil import copyfile
from tensorflow.python.keras.api._v2.keras.optimizers import RMSprop
from tensorflow.python.keras.api._v2.keras.preprocessing.image import ImageDataGenerator

#wget.download("https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip", "cats-and-dogs.zip")
##zip_ref   = zipfile.ZipFile(local_zip, 'r')
#zip_ref.extractall('PetImages')
#zip_ref.close()
print(len(os.listdir('PetImages/PetImages/Cat')))
print(len(os.listdir('PetImages/PetImages/Dog'))) 

try:
    os.mkdir('cats-v-dogs')
    os.mkdir('cats-v-dogs/training')
    os.mkdir('cats-v-dogs/testing')
    os.mkdir('cats-v-dogs/training/cats')
    os.mkdir('cats-v-dogs/training/dogs')
    os.mkdir('cats-v-dogs/testing/cats')
    os.mkdir('cats-v-dogs/testing/dogs')
except OSError:
    pass

def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
    files = []
    for filename in os.listdir(SOURCE):
        file = SOURCE + filename
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(filename + " is zero length, so ignoring.")
 
    training_length = int(len(files) * SPLIT_SIZE)
    testing_length = int(len(files) - training_length)
    shuffled_set = random.sample(files, len(files))
    training_set = shuffled_set[0:training_length]
    testing_set = shuffled_set[:testing_length]
 
    for filename in training_set:
        this_file = SOURCE + filename
        destination = TRAINING + filename
        copyfile(this_file, destination)
 
    for filename in testing_set:
        this_file = SOURCE + filename
        destination = TESTING + filename
        copyfile(this_file, destination)

CAT_SOURCE_DIR = "PetImages/PetImages/Cat"
TRAINING_CATS_DIR = "cats-v-dogs/training/cats"
TESTING_CATS_DIR = "cats-v-dogs/testing/cats"
DOG_SOURCE_DIR = "PetImages/PetImages/Dog"
TRAINING_DOGS_DIR = "cats-v-dogs/training/dogs"
TESTING_DOGS_DIR = "cats-v-dogs/testing/dogs"
 
split_size = .9
split_data(CAT_SOURCE_DIR, TRAINING_CATS_DIR, TESTING_CATS_DIR, split_size)
split_data(DOG_SOURCE_DIR, TRAINING_DOGS_DIR, TESTING_DOGS_DIR, split_size)

print(len(os.listdir('/tmp/cats-v-dogs/training/cats/')))
print(len(os.listdir('/tmp/cats-v-dogs/training/dogs/')))
print(len(os.listdir('/tmp/cats-v-dogs/testing/cats/')))
print(len(os.listdir('/tmp/cats-v-dogs/testing/dogs/')))

