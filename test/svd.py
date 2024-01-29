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
# Save the grayscale image to a folder
output_folder = os.path.join(current_directory, "output_folder")
os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist
output_image_path = os.path.join(output_folder, "grayscale_image.png")  # Change the extension as needed
Image.fromarray(image_data).save(output_image_path)

print("Grayscale image saved to:", output_image_path)

# Use image_data directly
u, s, vt = np.linalg.svd(image_data, full_matrices=False)
scopy = s.copy()
scopy = scopy[:50] 
compressed_image = u.dot(np.diag(scopy)).dot(vt)

# Save compressed image
compressed_image_path = os.path.join(output_folder, "compressed_image.png")
Image.fromarray(compressed_image.astype(np.uint8)).save(compressed_image_path)

original_image_size = image_data.size
compressed_image_size = compressed_image.size

percent_compression = (1 - (compressed_image_size)/(original_image_size)) * 100

print("Percent Compression: " + str(percent_compression) + "%")



