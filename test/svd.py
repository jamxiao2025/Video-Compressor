import os
import numpy as np
from PIL import Image

# Specify the filename
input_filename = "chicken_rice.JPG"

# Get the current working directory
current_directory = os.getcwd()
print(current_directory)
# Construct the full path
input_image_path = os.path.join(current_directory, "images", input_filename)
print(input_image_path)
# Convert image to grayscale
image = Image.open(input_image_path).convert('L')  # Convert to grayscale
image_data = np.array(image)

print("Done converting from JPG to dat")

# Use image_data directly
u, s, vt = np.linalg.svd(image_data, full_matrices=False)
print(s)



