#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py

Creates pet labels from image filenames.
"""

from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based on image filenames.
    The labels are formatted to be all lowercase and stripped of any leading
    or trailing whitespace.

    Parameters:
        image_dir (str): The full path to the folder of images to be classified.

    Returns:
        dict: Dictionary where the key is the image filename and the value
              is a list containing the pet label.
    """
    # Retrieve filenames from the specified directory
    filename_list = listdir(image_dir)

    # Initialize results dictionary
    results_dic = {}

    # Process each file in the directory
    for filename in filename_list:
        # Ignore files that don't have a valid extension
        if filename.startswith('.'):
            continue

        # Generate the pet label from the filename
        pet_label = ' '.join([word for word in filename.lower().split('_') if word.isalpha()]).strip()

        # Add to dictionary if filename is not already a key
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print(f"** Warning: Key={filename} already exists in results_dic with value={results_dic[filename]}")

    return results_dic
