#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIPND-revision/intropyproject-classify-pet-images/classify_images.py

Classifies pet images using a CNN model and updates results.
"""

from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Uses the classifier function to create classifier labels, compares the
    classifier labels to pet image labels, and updates the results dictionary.
    The classifier labels are formatted in lowercase and stripped of whitespace
    to match pet labels. Results are extended to include:
      - Classifier label at index 1
      - Match indicator at index 2 (1 for match, 0 for no match)

    Parameters:
        images_dir (str): The full path to the folder of images to classify.
        results_dic (dict): Dictionary with 'key' as image filename and 'value'
                            as a List. List index details:
                              - Index 0: Pet image label
                              - Index 1: Classifier label (added by this function)
                              - Index 2: Match indicator (1 for match, 0 otherwise)
        model (str): CNN model architecture ('resnet', 'alexnet', or 'vgg').

    Returns:
        None: The function updates the mutable results_dic directly.
    """
    for filename, label in results_dic.items():
        # Create full image path
        image_path = f"{images_dir}/{filename}"

        # Get classifier label, format it to lowercase, and strip whitespace
        classifier_label = classifier(image_path, model).lower().strip()

        # Update the results dictionary with the classifier label
        label.append(classifier_label)

        # Check if the pet label is found in the classifier label (match)
        match = 1 if label[0] in classifier_label else 0

        # Append the match result to the results dictionary
        label.append(match)
