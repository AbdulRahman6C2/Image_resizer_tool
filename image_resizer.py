import os
from PIL import Image

# Set your folder paths
input_folder = "images"  # folder containing input images
output_folder = "resized_images"  # folder to save output images

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Desired size
new_size = (300, 300)

# Supported formats
allowed_formats = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(allowed_formats):
        try:
            # Open image
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                # Resize
                img_resized = img.resize(new_size)

                # Save with new name
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_resized.png"
                img_resized.save(os.path.join(output_folder, new_filename), "PNG")
                print(f"Resized and saved: {new_filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
