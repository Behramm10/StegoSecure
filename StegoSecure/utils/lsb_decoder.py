from PIL import Image

def bits_to_text(bits):
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)

def extract_data(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    bits = ""

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            bits += str(r & 1)
            bits += str(g & 1)
            bits += str(b & 1)

    eof = bits.find("1111111111111110")
    if eof != -1:
        bits = bits[:eof]
    return bits_to_text(bits)
