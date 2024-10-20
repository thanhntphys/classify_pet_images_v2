#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py

Calculates statistics from the results of the image classification.
"""


def calculates_results_stats(results_dic):
    """
    Calculates statistics of the program's classification results and returns
    them in a dictionary. The statistics include counts and percentages of
    various classification outcomes.

    Parameters:
        results_dic (dict): Dictionary with key as image filename and value as
                            a list:
                              - idx 0: Pet image label
                              - idx 1: Classifier label
                              - idx 2: Match indicator (1 for match, 0 otherwise)
                              - idx 3: 1/0 if pet image 'is-a' dog
                              - idx 4: 1/0 if classifier label 'is-a' dog

    Returns:
        dict: Dictionary containing the results statistics.
    """
    # Initialize counters for statistics
    n_images = len(results_dic)
    n_dogs_img = sum(1 for result in results_dic.values() if result[3] == 1)
    n_notdogs_img = n_images - n_dogs_img
    n_match = sum(1 for result in results_dic.values() if result[2] == 1)
    n_correct_dogs = sum(1 for result in results_dic.values() if result[3] == 1 and result[4] == 1)
    n_correct_notdogs = sum(1 for result in results_dic.values() if result[3] == 0 and result[4] == 0)
    n_correct_breed = sum(1 for result in results_dic.values() if result[2] == 1 and result[3] == 1)

    # Calculate percentages, avoiding division by zero
    pct_match = (n_match / n_images) * 100 if n_images > 0 else 0.0
    pct_correct_dogs = (n_correct_dogs / n_dogs_img) * 100 if n_dogs_img > 0 else 0.0
    pct_correct_breed = (n_correct_breed / n_dogs_img) * 100 if n_dogs_img > 0 else 0.0
    pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img) * 100 if n_notdogs_img > 0 else 0.0

    # Create results statistics dictionary
    results_stats_dic = {
        "n_images": n_images,
        "n_dogs_img": n_dogs_img,
        "n_notdogs_img": n_notdogs_img,
        "n_match": n_match,
        "n_correct_dogs": n_correct_dogs,
        "n_correct_notdogs": n_correct_notdogs,
        "n_correct_breed": n_correct_breed,
        "pct_match": pct_match,
        "pct_correct_dogs": pct_correct_dogs,
        "pct_correct_breed": pct_correct_breed,
        "pct_correct_notdogs": pct_correct_notdogs,
    }

    return results_stats_dic
