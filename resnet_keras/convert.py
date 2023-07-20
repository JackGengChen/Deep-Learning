import os
import h5py
from PIL import Image


def convert_h5_to_jpeg(h5_file_path, output_folder):
    with h5py.File(h5_file_path, 'r') as h5_file:
        dataset = h5_file['test_set_x']
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        for i in range(len(dataset)):
            image_data = dataset[i]
            image = Image.fromarray(image_data)
            image_path = f"{output_folder}/image_{i}.jpg"
            image.save(image_path)
            print(f"Saved image {i + 1}/{len(dataset)} as {image_path}")


# Specify the paths to the H5 file and the output folder
h5_file_path = 'datasets/test_signs.h5'
output_folder = 'output_images'

# Call the function to perform the conversion
convert_h5_to_jpeg(h5_file_path, output_folder)
