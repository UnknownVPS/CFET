from PIL import Image
import math
import numpy as np

def text_to_image(text):
    # Calculate the number of triplets needed
    num_triplets = math.ceil(len(text) / 3)
    colors = [(0, 0, 0)] * num_triplets  # Initialize with black RGB triplets

    for i, char in enumerate(text):
        triplet_index = i // 3
        if i % 3 == 0:
            colors[triplet_index] = (ord(char), colors[triplet_index][1], colors[triplet_index][2])
        elif i % 3 == 1:
            colors[triplet_index] = (colors[triplet_index][0], ord(char), colors[triplet_index][2])
        else:
            colors[triplet_index] = (colors[triplet_index][0], colors[triplet_index][1], ord(char))

    width = height = math.ceil(math.sqrt(num_triplets))
    
    img_data = np.zeros((height, width, 3), dtype=np.uint8)
    
    for i, (r, g, b) in enumerate(colors):
        x, y = i % width, i // width
        img_data[y, x, 0] = r
        img_data[y, x, 1] = g
        img_data[y, x, 2] = b

    img = Image.fromarray(img_data, 'RGB')
    img.save('output.png', optimize=True, quality=100)

def image_to_text(image_path):
    img = Image.open(image_path)
    width, height = img.size
    text = ''

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            text += chr(r) + chr(g) + chr(b)

    return text

# Read text from file
with open('encoded.txt', 'r', encoding='iso-8859-1') as file:
    text = file.read()

# Convert text to image
text_to_image(text)

# Convert image to text
decoded_text = image_to_text('output.png')
with open('decoded_text.txt', 'w', encoding='iso-8859-1') as filex:
    filex.write(decoded_text)
