from PIL import Image, ImageDraw
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

def add_rounded_corners(image, radius):
    """Add rounded corners to an image."""
    # Create a mask with rounded corners
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, image.size[0], image.size[1]), radius=radius, fill=255)

    # Apply the mask to the image
    rounded_image = Image.new("RGBA", image.size)
    rounded_image.paste(image, mask=mask)
    return rounded_image

def resize_icon(input_icon, output_dir, sizes):
    """Resize the icon to multiple sizes with rounded corners and save them."""
    try:
        # Open the original icon
        img = Image.open(input_icon).convert("RGBA")
        for size in sizes:
            # Resize the image
            resized_img = img.resize(size, Image.LANCZOS)

            # Apply rounded corners (radius is 20% of the size)
            radius = int(min(size) * 0.2)
            rounded_img = add_rounded_corners(resized_img, radius)

            # Save the image
            filename = f"icon_{size[0]}x{size[1]}.png"
            output_path = os.path.join(output_dir, filename)
            rounded_img.save(output_path, format="PNG")
            print(f"Saved: {output_path}")
        print("All icons resized with rounded corners successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Run the resize function
resize_icon(INPUT_ICON, OUTPUT_DIR, ICON_SIZES)
