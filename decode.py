# @author: Arpan Pathak
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

''' method for decoding the original message from the image '''
def decode_image(img):
    width, height = img.size
    msg = ""
    index = 0
    img= img.convert('RGB')
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                r, g, b, a = img.getpixel((col, row))       
            if row == 0 and col == 0:
                length = r
            elif index < length:
                msg += chr(r)
                index+=1
            else:
                return msg
    return msg

def main():
    root=tk.Tk()
    label1=tk.Label(root,fg="blue")
    label1.pack()
    file_path = filedialog.askopenfilename()
    head, tail = os.path.split(file_path)
    imgname=tail
    img2 = Image.open("output/"+imgname)

    msg=decode_image(img2)
    print(msg)
    label1.config(text=msg)
    root.mainloop()

if __name__=="__main__":
    main()
