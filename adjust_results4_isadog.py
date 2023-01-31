#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#                                                                             
# PROGRAMMER: Patrick Bruce
# DATE CREATED: 01/24/2023                          
# REVISED DATE: 
# PURPOSE: Creates a function that adjusts the results dictionary to indicate
#          whether or not the pet image label is of-a-dog, and to indicate
#          whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file.
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main.
##
#Defines adjust_results4_isadog
def adjust_results4_isadog(results_dic, dogfile):
    
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    This function uses the extend function to add items to the list
    that's the 'value' of the results dictionary.
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line. Dog names are all in lowercase with
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    dogfile_dic = {}
    with open(dogfile) as f:
        for line in f:
            dogfile_dic[line.strip()] = 1
    for key in results_dic:
        image_label = results_dic[key]
        if image_label[0] in dogfile_dic:
            image_label.append(1)
        else:
            image_label.append(0)
        if image_label[1] in dogfile_dic:
            image_label.append(1)
        else:
            image_label.append(0)    
         
    print(dogfile_dic.items())
