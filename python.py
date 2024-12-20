from PIL import Image, ImageFilter

COLORS = {
    "B":(255,255,255),
    "G":(229,57,53),
    "L":(237,105,25),
    "Q":(244,166,41),
    "V":(114,176,48),
    "a":(28,164,180),
    "f":(105,31,155),
    "k":(214,36,104),
    "p":(21,100,191)
}
BASE_URL = "https://santatracker.google.com/santaselfie.html?beard="

def color_distance(c1, c2):
    return int(((c1[0]-c2[0])**2+(c1[1]-c2[1])**2+(c1[2]-c2[2])**2)**0.5)

def color_to_code(color: 'tuple[int, int, int]') -> str:
    closest = min(COLORS.items(), key=lambda x: color_distance(x[1], color))
    return closest[0]

def compress(encoded):
    out = ""
    count = 0
    last = encoded[0]
    i = 0
    while i < len(encoded):
        if encoded[i] != last:
            out += str(count) + last
            last = encoded[i]
            count = 1
        else:
            count += 1
            i += 1
    return out[1:]

img = Image.open("bear.jpg")
blurred = img.filter(ImageFilter.GaussianBlur(radius=15))
blurred.save("blurred.jpg")
resized = img.resize((23, 26))
resized.save("resized.jpg")

encoded = ""
for y in range(26):
    for x in range(23):
        encoded += "1" + color_to_code(resized.getpixel((x,y)))
print(BASE_URL+encoded)
