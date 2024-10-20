#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIPND-revision/intropyproject-classify-pet-images/get_input_args.py

Retrieves command line arguments for image classification.
"""

import argparse


def get_input_args():
    """
    Retrieves and parses 3 command line arguments provided by the user:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'

    If any arguments are missing, default values are used.

    Returns:
        argparse.Namespace: Parsed command line arguments
    """
    # Initialize ArgumentParser
    parser = argparse.ArgumentParser(
        description="Process command line arguments for image classification."
    )

    # Add command line arguments
    parser.add_argument('--dir', type=str, default='pet_images',
                        help='Path to the folder of pet images (default: pet_images)')
    parser.add_argument('--arch', type=str, default='vgg',
                        help='CNN model architecture to use (default: vgg)')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='File with the list of valid dog names (default: dognames.txt)')

    # Parse and return the arguments
    return parser.parse_args()
