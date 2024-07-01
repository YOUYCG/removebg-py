from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def remove_white_background(image_path, output_path):
    # Open the image file
    img = Image.open(image_path)

    # Convert image to RGBA if not already in that mode
    img = img.convert("RGBA")

    # Get the image data
    data = img.getdata()

    # Replace white background with transparency
    new_data = []
    for item in data:
        # Change all white (also shades of whites) pixels to transparent
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    # Update image data
    img.putdata(new_data)

    # Save the image with transparency
    img.save(output_path, "PNG")

def main():
    # Hide the root window
    Tk().withdraw()

    # Ask the user to select an input file
    input_image_path = askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not input_image_path:
        print("No input file selected. Exiting.")
        return

    # Ask the user to select an output file
    output_image_path = asksaveasfilename(title="Save image as", defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if not output_image_path:
        print("No output file selected. Exiting.")
        return

    # Remove white background
    remove_white_background(input_image_path, output_image_path)

    print(f"Image saved with removed background at: {output_image_path}")

if __name__ == "__main__":
    main()
    # 打包成带第三方运行依赖库的exe文件
    # pyinstaller -F -w -i 1.ico -p "C:\Users\YOU\AppData\Local\Programs\Python\Python312\Lib\site-packages" removebg.py
