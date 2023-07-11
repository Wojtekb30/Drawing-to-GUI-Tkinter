prefiks = "import tkinter as tk\n\nroot = tk.Tk()\n\nroot.title('GUIfromDrawing program')\n\n"


from PIL import Image, ImageDraw
print("Blue (RGB 0,0,255) - button")

picdata = Image.open(input("Type filename: "))
pic = picdata.load()
szerokosc, wysokosc = picdata.size
x=0
y=0

def createbutton(pic, startx, starty):
    x=startx
    y=starty
    r, g, b = pic[x,y]
    while r==0 and g==0 and b==255:
        r, g, b = pic[x,y]
        x=x+1
    r, g, b = pic[startx,starty]
    while r==0 and g==0 and b==255:
        r, g, b = pic[startx,y]
        y=y+1
    tekst = "button"+str(x)+"x"+str(y)+" = tk.Button(root, text='button', fg='white', bg='blue')"+"\n\nbutton"
    tekst = tekst+str(x)+str(y)+".place(x="+str(startx)+", y=" + str(starty) +", height="+str(y-starty)+", width="+str(x-startx)+")\n\n"
    
    return x-startx, y-starty, x, y, tekst



f = open("wynik.py", "w")
f.write(prefiks)
f.close()
f = open("wynik.py", "a")
f.write("root.geometry('"+str(szerokosc)+"x"+str(wysokosc)+"')\n\n")
while x!=szerokosc and y!=wysokosc:
    r, g, b = pic[x,y]
    if r==0 and g==0 and b==255:
        drawx, drawy, enddrawx, enddrawy, text = createbutton(pic, x, y)
        f.write(text)
        draw = ImageDraw.Draw(picdata)
        draw.rectangle((x, y, enddrawx, enddrawy), fill=(255,255,255), outline=(0,0,0))
        pic = picdata.load()
     
    x=x+1
    if x==szerokosc-1:
        y=y+1
        x=0

f.write("root.mainloop()")
f.close()
print("done")
#picdata.show()
