'''Module 3: count black and white pixels and compute the percentage of white pixels in a .jpg image and extrapolate points'''

from termcolor import colored
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import pandas as pd

# Load the images you want to analyze

filenames = [
    r"../images/MASK_SK658 Llobe ch010039.jpg",
    r"../images/MASK_SK658 Slobe ch010066.jpg",
    r"../images/MASK_SK658 Slobe ch010147.jpg",
    r"../images/MASK_SK658 Slobe ch010110.jpg",
    r"../images/MASK_SK658 Slobe ch010130.jpg",
    r"../images/MASK_SK658 Slobe ch010114.jpg",
]

# Enter the depth of each image (in the same order that the images are listed above; you can find these in the .csv file provided to you which is tilted: "Filenames and Depths for Students")

depths = [
    15,
    1000,
    3000,
    5300,
    7000,
    9900
]

# Make the lists that will be used
white_counts = []
black_counts = []
white_percents = []

# Instead of looping through each task, for all the calculation, it is done through one loop. This makes the efficiency slightly better.

for filename in filenames:
    img = cv2.imread(filename, 0) #Read the file and give it in 2D matrix array. Can be a range of numbers. 
    # No longer store the matrix, it is not needed for anything

    # For each image (until the end of the list of images), calculate the number of black and white pixels and make a list that contains this information for each filename.
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)   #Cut off is 127, output either 255 or 0 for easy computation
    #Compute how much has the code of 255 (white), nd how much have black.
    white = np.sum(binary == 255)
    black = np.sum(binary == 0)

    #Add those values to a list.
    white_counts.append(white)
    black_counts.append(black)

    # Calculate the percentage of pixels in each image that are white and make a list that contains these percentages for each filename
    white_percent = (100 * (white/ (black + white)))
    white_percents.append(white_percent)

# Print the number of white and black pixels in each image.
# Print the filename (on one line in red font), and below that line print the percent white pixels and depth into the lung where the image was obtained
for x in range(len(filenames)):
    
    print(colored(f'{filenames[x]}:', "red"))
    print()
    print(colored("Pixel count in Image:", "yellow"))
    print(colored(f"White pixels in image {filename[x]}: {white_counts[x]}", "white"))
    print(colored(f"Black pixels in image {filename[x]}: {black_counts[x]}", "black"))
    print()
    print(colored("Percent white px:", "yellow"))
    print(f'{white_percents[x]:.2f}% White | Depth: {depths[x]} microns')
    print()

'''Write your data to a .csv file'''

# Create a DataFrame that includes the filenames, depths, and percentage of white pixels
df = pd.DataFrame({
    'Filenames': filenames,
    'Depths': depths,
    'White percents': white_percents
})

# Write that DataFrame to a .csv file

df.to_csv('Percent_White_Pixels.csv', index=False)

print("The .csv file 'Percent_White_Pixels.csv' has been created.")

'''the .csv writing subroutine ends here'''


##############
# LECTURE 2: UNCOMMENT BELOW

# # Interpolate a point: given a depth, find the corresponding white pixel percentage

# interpolate_depth = float(input(colored(
#     "Enter the depth at which you want to interpolate a point (in microns): ", "yellow")))

# x = depths
# y = white_percents

# # You can also use 'quadratic', 'cubic', etc.
# i = interp1d(x, y, kind='linear')
# interpolate_point = i(interpolate_depth)
# print(colored(
#     f'The interpolated point is at the x-coordinate {interpolate_depth} and y-coordinate {interpolate_point}.', "green"))

# depths_i = depths[:]
# depths_i.append(interpolate_depth)
# white_percents_i = white_percents[:]
# white_percents_i.append(interpolate_point)


# # make two plots: one that doesn't contain the interpolated point, just the data calculated from your images, and one that also contains the interpolated point (shown in red)
# fig, axs = plt.subplots(2, 1)

# axs[0].scatter(depths, white_percents, marker='o', linestyle='-', color='blue')
# axs[0].set_title('Plot of depth of image vs percentage white pixels')
# axs[0].set_xlabel('depth of image (in microns)')
# axs[0].set_ylabel('white pixels as a percentage of total pixels')
# axs[0].grid(True)


# axs[1].scatter(depths_i, white_percents_i, marker='o',
#                linestyle='-', color='blue')
# axs[1].set_title(
#     'Plot of depth of image vs percentage white pixels with interpolated point (in red)')
# axs[1].set_xlabel('depth of image (in microns)')
# axs[1].set_ylabel('white pixels as a percentage of total pixels')
# axs[1].grid(True)
# axs[1].scatter(depths_i[len(depths_i)-1], white_percents_i[len(white_percents_i)-1],
#                color='red', s=100, label='Highlighted point')


# # Adjust layout to prevent overlap
# plt.tight_layout()
# plt.show()
