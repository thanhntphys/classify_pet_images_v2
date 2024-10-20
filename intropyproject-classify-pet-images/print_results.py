def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and dog breeds if requested.

    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
                    (idx 0: pet image label (string),
                     idx 1: classifier label (string),
                     idx 2: 1/0 (int) - match between pet and classifier labels,
                     idx 3: 1/0 (int) - pet image is a dog,
                     idx 4: 1/0 (int) - classifier labels image as a dog).
      results_stats_dic - Dictionary containing results statistics (percentage or count).
      model - CNN model architecture used for classification (resnet, alexnet, vgg).
      print_incorrect_dogs - If True, prints incorrectly classified dog images (default: False).
      print_incorrect_breed - If True, prints incorrectly classified dog breeds (default: False).

    Returns:
      None - simply prints the results.
    """
    # Print model architecture and summary statistics
    print(f"\nUsing the {model.upper()} CNN model architecture")
    print(f"Number of Images: {results_stats_dic['n_images']}")
    print(f"Number of Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Number of 'Not-a' Dog Images: {results_stats_dic['n_notdogs_img']}\n")

    # Print percentage statistics
    for stat in ['pct_correct_dogs', 'pct_correct_breed', 'pct_correct_notdogs', 'pct_match']:
        print(f"{stat.replace('pct_', '').replace('_', ' ').title()}: {results_stats_dic[stat]:.2f}%")

    # Check and print misclassified dogs if requested
    if print_incorrect_dogs:
        misclassified_dogs = [image for image, values in results_dic.items()
                              if sum((values[3], values[4])) == 1]
        if misclassified_dogs:
            print("\nMisclassified Dogs:")
            for image in misclassified_dogs:
                print(f"Image: {image}, Classifier Label: {results_dic[image][1]}")
        else:
            print("\nNo misclassified dogs found.")

    # Check and print misclassified dog breeds if requested
    if print_incorrect_breed:
        misclassified_breeds = [image for image, values in results_dic.items()
                                if sum((values[3], values[4])) == 2 and values[2] == 0]
        if misclassified_breeds:
            print("\nMisclassified Dog Breeds:")
            for image in misclassified_breeds:
                print(f"Image: {image}, Classifier Label: {results_dic[image][1]}")
        else:
            print("\nNo misclassified dog breeds found.")
