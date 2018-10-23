import numpy as np
from PIL import Image

def img2txt(image_path, output_size):
    try:
        ascii_spectrum = '.:-=+*#%@"'
        bins = np.linspace(0, 256, len(ascii_spectrum))
        image = Image.open(image_path)
        #greyscale image
        grim = image.resize(output_size).convert('L') #(8-bit pixels, black and white)
        ascii_data = np.array([ascii_spectrum[x] for x in np.digitize(grim.getdata(), bins)]).reshape(grim.size[::-1])
        return '\n'.join([''.join(row) for row in ascii_data])
    except Exception as e:
        print(e)
        return None