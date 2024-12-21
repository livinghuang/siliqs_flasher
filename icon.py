from PIL import Image
import os

# Define the sizes for macOS icons
ICON_SIZES = [
    (16, 16),
    (32, 32),
    (64, 64),
    (128, 128),
    (256, 256),
    (512, 512),
    (1024, 1024)  # Retina size
]

# Input and output settings
INPUT_ICON = "original_icon.png"  # Path to the original icon
OUTPUT_DIR = "resized_icons"      # Directory to save resized icons

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def resize_icon(input_icon, output_dir, sizes):
    """Resize the icon to multiple sizes and save them."""
    try:
        # Open the original icon
        img = Image.open(input_icon)
        for size in sizes:
            resized_img = img.resize(size, Image.LANCZOS)
            filename = f"icon_{size[0]}x{size[1]}.png"
            output_path = os.path.join(output_dir, filename)
            resized_img.save(output_path, format="PNG")
            print(f"Saved: {output_path}")
        print("All icons resized successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Run the resize function
resize_icon(INPUT_ICON, OUTPUT_DIR, ICON_SIZES)
