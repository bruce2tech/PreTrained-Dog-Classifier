#!/bin/sh
#                                                                             
# PROGRAMMER: Patrick Bruce
# DATE CREATED: 01/26/2023
# REVISED DATE: 01/26/2023  -
# PURPOSE: Runs all three models to test which provides 'best' solution on the Uploaded Images.
#          Output from each run is piped into a text file.
#
# Usage: sh run_models_batch_uploaded.sh
#  
python check_images.py --dir uploaded_images/ --arch resnet  --dogfile dognames.txt > resnet_uploaded-images.txt
python check_images.py --dir uploaded_images/ --arch alexnet --dogfile dognames.txt > alexnet_uploaded-images.txt
python check_images.py --dir uploaded_images/ --arch vgg  --dogfile dognames.txt > vgg_uploaded-images.txt
