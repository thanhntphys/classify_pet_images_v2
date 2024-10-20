#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py

Adjusts the results dictionary to indicate if the pet and classifier labels
represent dogs based on the provided dog names file.
"""


def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to indicate whether the pet image label
    and the classifier label are dogs, based on the provided dog names file.

    Parameters:
        results_dic (dict): Dictionary with 'key' as image filename and 'value'
                            as a List. List index details:
                              - Index 0: Pet image label
                              - Index 1: Classifier label
                              - Index 2: Match indicator (1 for match, 0 otherwise)
                              - Index 3: 1/0 if pet image 'is-a' dog (added by this function)
                              - Index 4: 1/0 if classifier classified 'as-a' dog (added by this function)
        dogfile (str): Filename of the text file containing dog names, one per line.

    Returns:
        None: The function updates the mutable results_dic directly.
    """
    # Create a dictionary of dog names for quick lookup
    dognames_dict = {}

    # Read the dog names from the file and populate the dictionary
    with open(dogfile, "r") as f:
        for line in f:
            dog_name = line.strip().lower()
            dognames_dict[dog_name] = 1

    # Update the results_dic to indicate if the labels are dogs
    for values in results_dic.values():
        pet_label_is_dog = 1 if values[0] in dognames_dict else 0
        classifier_label_is_dog = 1 if values[1] in dognames_dict else 0

        # Append the dog indicators to the result list
        values.extend((pet_label_is_dog, classifier_label_is_dog))
