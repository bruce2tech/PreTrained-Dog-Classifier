#!/bin/sh
#
# PROGRAMMER: Patrick Bruce
# DATE CREATED: 01/26/2018
# REVISED DATE: 01/26/2018  -
# PURPOSE: Runs all three models to test which provides 'best' solution.
#          Output from each run has been piped into a text file.
#
# Usage: sh run_models_batch.sh
#  
python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > resnet_pet-images.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt
python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt > vgg_pet-images.txt
