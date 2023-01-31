#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Patrick Bruce
# DATE CREATED: 01/24/2023                                  
# REVISED DATE: 01/25/2023
# PURPOSE: This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This will allow the user of the program to determine
#          the 'best' model for classifying the images.
#
#          This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats
#             function and results for the function call within main.
##
# Defines calculates_results_stats function
def calculates_results_stats(results_dic):
    """
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value.
    """       
    n_dogs_img          = 0 # number of dog images
    n_notdogs_img       = 0 # number of NON-dog images
    n_match             = 0 # number of matches between pet & classifier labels
    n_correct_dogs      = 0 # number of correctly classified dog images
    n_correct_notdogs   = 0 # number of correctly classified NON-dog images
    n_correct_breed     = 0 # number of correctly classified dog breeds    
    pct_match           = 0.0 # percentage of correct matches
    pct_correct_dogs    = 0.0 # percentage of correctly classified dogs
    pct_correct_breed   = 0.0 # percentage of correctly classified dog breeds
    pct_correct_notdogs = 0.0 # percentage of correctly classified NON-dogs
    
    results_stats_dic = {"n_images": len(results_dic), "n_dogs_img": n_dogs_img, "n_notdogs_img": n_notdogs_img, "n_match": n_match, "n_correct_dogs": n_correct_dogs, "n_correct_notdogs": n_correct_notdogs, "n_correct_breed": n_correct_breed, "pct_match": pct_match, "pct_correct_dogs": pct_correct_dogs, "pct_correct_breed": pct_correct_breed, "pct_correct_notdogs": pct_correct_notdogs}
    
    for key in results_dic:    
        if results_dic[key][3] == 1:
            results_stats_dic["n_dogs_img"] += 1
        if results_dic[key][3] == 0:
            results_stats_dic["n_notdogs_img"] += 1
        if results_dic[key][2] == 1:
            results_stats_dic["n_match"] += 1
        if (results_dic[key][3] == 1) and  (results_dic[key][4] == 1): 
            results_stats_dic["n_correct_dogs"] += 1
        if (results_dic[key][3] == 0) and  (results_dic[key][4] == 0): 
            results_stats_dic["n_correct_notdogs"]  += 1
        if (results_dic[key][3] == 1) and  (results_dic[key][2] == 1): 
            results_stats_dic["n_correct_breed"] += 1
        
     
    results_stats_dic["pct_match"] = results_stats_dic["n_match"] / results_stats_dic["n_images"] * 100
    results_stats_dic["pct_correct_dogs"] = results_stats_dic["n_correct_dogs"] / results_stats_dic["n_dogs_img"] * 100
    results_stats_dic["pct_correct_breed"] = results_stats_dic["n_correct_breed"] / results_stats_dic["n_dogs_img"] * 100
    results_stats_dic["pct_correct_notdogs"] = results_stats_dic["n_correct_notdogs"] / results_stats_dic["n_notdogs_img"] * 100
    
    print(results_stats_dic.items())
    return results_stats_dic
