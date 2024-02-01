import os
import sys
import numpy as np
from PIL import Image
import time

def calculate_file_size(filepath):
    return os.path.getsize(filepath)

def compress_image(input_filename, output_folder, k):
    # Construct the full path
    input_image_path = os.path.join("images", input_filename)

    image = Image.open(input_image_path)
    image_data = np.array(image)

    # Separate color channels
    channels = [image_data[:, :, i] for i in range(image_data.shape[2])]

    compressed_channels = []
    for channel in channels:
        # Reshape data for SVD
        original_shape = channel.shape
        reshaped_data = channel.reshape((-1,1))

        # Apply SVD to reshaped data
        u, s, vt = np.linalg.svd(reshaped_data, full_matrices=False)
        scopy = s.copy()
        scopy[k:] = 0.0
        compressed_data = u.dot(np.diag(scopy)).dot(vt)

        # Reshape data to the original state
        compressed_channel = compressed_data.reshape(original_shape)
        compressed_channels.append(compressed_channel)

    # Combine compressed channels back into a color image
    compressed_image_data = np.stack(compressed_channels, axis=-1)

    # Save compressed image
    compressed_image_path = os.path.join(output_folder, f"compressed_image_rank_{k}.jpg")
    Image.fromarray(compressed_image_data.astype(np.uint8)).save(compressed_image_path, "JPEG")

    original_file_size = calculate_file_size(input_image_path)
    compressed_file_size = calculate_file_size(compressed_image_path)

    print(f"Original File Size: {original_file_size} bytes")
    print(f"Compressed File Size (Rank {k}): {compressed_file_size} bytes")

    percent_compression = (1 - (compressed_file_size / original_file_size)) * 100
    print(f"Percent Compression (Rank {k}): {percent_compression}%")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python svd.py <k>")
		sys.exit(1)
	k = int(sys.argv[1])
	input_filename = "chicken_rice.JPG"
	output_folder = "output_folder"
	start_time = time.time()
	compress_image(input_filename, output_folder, k)
	end_time = time.time()
	print(f"Time Elapsed: {end_time-start_time} seconds")

