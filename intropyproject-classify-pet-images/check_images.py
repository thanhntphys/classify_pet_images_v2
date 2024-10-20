#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIPND-revision/intropyproject-classify-pet-images/check_images.py

Classifies pet images using a pretrained CNN model, compares classifications
to the true identity of the pets, and summarizes the CNN's performance.
"""

import time
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Lab checks import
from print_functions_for_lab_checks import (
    check_command_line_arguments, check_creating_pet_image_labels,
    check_classifying_images, check_classifying_labels_as_dogs,
    check_calculating_results
)


def main():
    # Measure start time
    start_time = time.time()

    # Get command line arguments
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # Create pet image labels
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

    # Classify images and update results
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)

    # Adjust results for dog classification
    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    # Calculate results statistics
    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)

    # Print results
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure end time and compute runtime
    end_time = time.time()
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          f"{int(tot_time // 3600)}:{int((tot_time % 3600) // 60)}:{int((tot_time % 3600) % 60)}")


# Call to main function to run the program
if __name__ == "__main__":
    main()
