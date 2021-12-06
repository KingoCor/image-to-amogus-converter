from PIL import Image as img

amogus_size=int(100*float(input("scale of one amogus (1=100%=100px): ")))
print("resizing...")
amoguses=[img.open(f"amogus.{i}.png") for i in range(1,6)]
[amogus.thumbnail((amogus_size,amogus_size)) for amogus in amoguses]

print("geting amogus brightness...")
#get amoguses brightness
abm = [] #amoguses  brightness map
for amogus in amoguses:
    amogus_brightness=[]
    for y in range(amogus_size):
        brightness_layer=[]
        for x in range(amogus_size):
            color=amogus.getpixel((x,y))
            b_percentage=((color[0]+color[1]+color[2])/2*100)/255

            brightness_layer.append(b_percentage)
        
        amogus_brightness.append(brightness_layer)
    abm.append(amogus_brightness)

image_name = input("choose image to convert in programm folder: ")
image_2_convert = img.open(image_name)

#pixels per amogus
ppa=int(input("how many pixels per amogus will be: "))

print("resizing img...")
#resizing picture
soi=image_2_convert.size
image_2_convert.thumbnail((int(soi[0]/ppa),int(soi[1]/ppa)))
soi=image_2_convert.size

def get_colored_amogus(color,amogus,abm):
    for y in range(amogus_size):
        for x in range(amogus_size):
            brightness=((color[0]+color[1]+color[2])/3*100)/255
            d_brightness=100+(abm[y][x]-brightness)

            r=(color[0]*d_brightness)/100
            g=(color[1]*d_brightness)/100
            b=(color[2]*d_brightness)/100
            amogus.putpixel((x,y),(int(r),int(g),int(b)))

    return amogus

#creating frames
frames=[]

work_to_do=soi[0]*soi[1]*5
count=0
done_percent=int((100*count)/work_to_do*100)/100
text=f"rendering: {done_percent}%" 
print(text, end="", flush=True)
for amogus in range(len(amoguses)):
    frame = img.new("RGB", (soi[0]*amogus_size,soi[1]*amogus_size))
    
    for y in range(soi[1]):
        for x in range(soi[0]):
            amogus_img = get_colored_amogus(image_2_convert.getpixel((x,y)),amoguses[amogus],abm[amogus])

            frame.paste(amogus_img, (x*amogus_size,y*amogus_size))

            count+=1
            done_percent=int((100*count)/work_to_do*100)/100
            print('\b' * len(text), end='', flush=True)
            text=f"rendering: {done_percent}%" 
            print(text, end="", flush=True)

    frames.append(frame)

print("\nDone")

frames[0].save(
    image_name + ' amogus.gif',
    save_all=True,
    append_images=frames[1:],
    optimize=False,
    duration=75,
    loop=0
)
