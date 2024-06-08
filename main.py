from PIL import Image, ImageDraw, ImageFont

def generate_signature(name, output_file):
    # Create a blank image with white background
    width, height = 400, 200
    img = Image.new('RGB', (width, height), color='white')

    # Initialize the drawing context
    draw = ImageDraw.Draw(img)

    # Choose a font and size
    font_size = 30
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calculate text size and position
    text_width, text_height = draw.textsize(name, font=font)
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2

    # Add text to the image
    draw.text((text_x, text_y), name, fill='black', font=font)

    # Save the image
    img.save(output_file)

if __name__ == "__main__":
    name = input("Enter your name: ")
    output_file = input("Enter the name of the output file (with extension): ")
    generate_signature(name, output_file)
    print("Signature created successfully!")

