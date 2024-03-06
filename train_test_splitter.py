import os
import shutil
import numpy as np
# Read classes.txt to create a dictionary mapping class numbers to class names
class_mapping = {}
with open('D:/mtech/2nd sem/GNR/mini project/CUB_200_2011/CUB_200_2011/classes.txt', 'r') as f:
    for line in f:
        class_num, class_name = line.strip().split()
        class_mapping[int(class_num)] = class_name

# Read image_class_label.txt to create a dictionary mapping image filenames to class labels
image_class_mapping = {}
with open('D:/mtech/2nd sem/GNR/mini project/CUB_200_2011/CUB_200_2011/image_class_labels.txt', 'r') as f:
    for line in f:
        image_num, class_num = line.strip().split()
        image_class_mapping[int(image_num)] = int(class_num)


# Read images.txt to create a dictionary mapping image numbers to image filenames
image_filename_mapping = {}
with open('D:/mtech/2nd sem/GNR/mini project/CUB_200_2011/CUB_200_2011/images.txt', 'r') as f:
    for line in f:
        
        image_num, image_filename = line.strip().split()
        image_filename_mapping[int(image_num)] = image_filename

# Read traintestsplit.txt to create a dictionary mapping image filenames to train/test split indicators
train_test_split_mapping = {}
with open('D:/mtech/2nd sem/GNR/mini project/CUB_200_2011/CUB_200_2011/train_test_split.txt', 'r') as f:
    for line in f:
        image_num, split_indicator = line.strip().split()
        image_filename = image_filename_mapping[int(image_num)]
        train_test_split_mapping[image_filename] = int(split_indicator)

# Create directories for train and test images
train_dir = 'D:/mtech/2nd sem/GNR/mini project/train_test_split/train'
test_dir = 'D:/mtech/2nd sem/GNR/mini project/train_test_split/test'
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
  
    
count = np.zeros(200)
class_tag = 1
count_3 = 0
for image_index, class_indicator in image_class_mapping.items():
    count[class_indicator-1] += 1


    
for image_index, split_indicator in train_test_split_mapping.items():
    # Source file path
    source_folder_path = "D:\\mtech\\2nd sem\\GNR\\mini project\\CUB_200_2011\\CUB_200_2011\\images"
    print(f'{image_index}')
    # class_index = image_class_mapping[image_index]
    path_temp = image_index.split('/')
    source_file = os.path.join(source_folder_path, path_temp[0], path_temp[1])
     

    # Destination folder path
    dest_train = "D:\\mtech\\2nd sem\\GNR\\mini project\\train_test_split\\train"
    dest_test = "D:\\mtech\\2nd sem\\GNR\\mini project\\train_test_split\\test"
    
    if split_indicator: # Train
        destination_folder = dest_train
    else:
        destination_folder = dest_test

    # Copy the file to the destination folder
    class_name = image_index.split('/')[0]
    final_path = os.path.join(destination_folder, class_name)
    print(f"{class_name}")
    os.makedirs(final_path, exist_ok=True)
    shutil.copy(source_file, final_path)
        
# Now you can use train_dir and test_dir as the root directories for your train and test datasets
