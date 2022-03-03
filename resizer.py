from pathlib import Path
from PIL import Image

print('By what do you want to multiply your Textures?')
multipl = input()
print('How is your texture foler named?')
dname = input()
if dname == '':
    dname = 'textures'
print('Remove half-transparent? y/n')
rht = input().lower()

input_dir = Path.cwd() / dname
files = list(input_dir.rglob('*.png*'))

def removehlftransp(pixel_Data):
    new_Data = []
    for item in pixel_Data:
        if item[3] > 0:
            new_Data.append((item[0], item[1], item[2], 255))
        else:
            new_Data.append(item)
    return(new_Data)

for file in files:
    path = str(file)
    print(path)
    if path.endswith('.png'):
        img = Image.open(file)
        img = img.convert('RGBA')
        width, height = img.size
        width *= float(multipl)
        height *= float(multipl)
        new_img = img.resize((int(width), int(height)))
        if(rht == 'y'):
            pixel_Data = new_img.getdata()
            new_img.putdata(removehlftransp(pixel_Data))
        new_img.save(file)
        pass
    else:
        continue

print('Done!')
