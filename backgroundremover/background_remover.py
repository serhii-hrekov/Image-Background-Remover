import os
from PIL import Image
from rembg import remove

def remove_background(input_path, output_path):
    """
    Removes the background from an image and saves it in PNG format.

    Args:
        input_path (str): The path to the image file with a background.
        output_path (str): The desired path for the output image without a background.
    """
    try:
        # Open the image using Pillow
        input_image = Image.open(input_path)

        # Remove the background
        output_image = remove(input_image)

        # Save the image in PNG format (PNG supports transparency)
        output_image.save(output_path, format="PNG")
        print(f"Background removed successfully! Image saved to: {output_path}")

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # --- Configuration ---
    # You can change these paths as needed
    input_image_name = "input.jpg"  # Replace with your input image file name
    output_image_name = "output_no_bg.png"

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct full paths for input and output images
    input_image_path = os.path.join(script_dir, input_image_name)
    output_image_path = os.path.join(script_dir, output_image_name)

    print(f"Looking for input image at: {input_image_path}")

    # Call the function to remove the background
    remove_background(input_image_path, output_image_path)

    print("\n--- Usage Instructions ---")
    print(f"1. Place your input image (e.g., '{input_image_name}') in the same directory as this script.")
    print(f"2. Run the script: python {os.path.basename(__file__)}")
    print(f"3. The background-removed image will be saved as '{output_image_name}' in the same directory.")
    print("-------------------------")