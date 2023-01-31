# PreTrained-Dog-Classifier
# PROGRAMMER: Patrick Bruce
# DATE CREATED: 01/22/2023                            
# REVISED DATE: 01/23/2023
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. The program
#          extracts the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
#   Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
#   Example call for default arguments:
#    python check_images.py
#
#
# This program implements an image classifier function to identify breeds of dogs. 
# This programmed in python 3.9.16 using anaconda 23.1. An environment is providd.
# download myenv3.yaml and use the requirements.txt file to intall the required packages.
#
# To run in your python environment, download all files to a single folder and
# make sure you are in the directory 
# 
# For deeper understanding of the code I encourage you to read the comments in the function files.
# It is well documented.
