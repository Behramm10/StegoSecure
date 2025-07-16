from PIL import Image

def text_to_bits(text):
    return ''.join(f"{ord(c):08b}" for c in text)

def hide_data(image_path, text, output_path):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    data = text_to_bits(text) + '1111111111111110'  
    data_idx = 0
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            if data_idx >= len(data):
                break
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(data[data_idx])
            data_idx += 1
            if data_idx < len(data):
                g = (g & ~1) | int(data[data_idx])
                data_idx += 1
            if data_idx < len(data):
                b = (b & ~1) | int(data[data_idx])
                data_idx += 1
            pixels[x, y] = (r, g, b)
    img.save(output_path)
