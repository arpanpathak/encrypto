# @author: Arpan Pathak
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image
from tkinter import messagebox
import sys

''' Method for encrypting message inside  image'''
def encode_image(img, msg):
    length = len(msg)
    if img.mode != 'RGB':
        print("image mode needs to be RGB")
        return False
    img = img.convert('RGB')
    encoded = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                try:
                    r, g, b = img.getpixel((col, row))
                except ValueError:
                    r, g, b, a = img.getpixel((col, row)) 
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index < length:
                    c = msg[index]
                    asc = ord(c)
                    index+=1
                else:
                    return encoded
                encoded.putpixel((col, row), (asc, g , b))
            except:
                message.showinfo(message="Unable to encode image... please select a valid image",)
    return encoded

def test(args):
	secret_msg=args[0]
	head=args[1]
	tail=args[2]
	original_image_file = tail
	img = Image.open(head+"/"+original_image_file)
	print(img, img.mode) 
	encoded_image_file = "enc_" + original_image_file
	print(len(secret_msg))
	img_encoded = encode_image(img, secret_msg)
	if img_encoded:
	    img_encoded.save("output/"+encoded_image_file+".bmp")
	    print("{} saved!".format(encoded_image_file))
	    try:
	    	os.startfile(encoded_image_file+".bmp")
	    except:
	    	print("Unable to open encrypted image..encrypted image is available in output directory")
def main():
	root = tk.Tk()
	lbl1=tk.Label(root,font=("Arial",20),text="Write Your Message Below..")
	lbl1.pack()
	msg=tk.Text(root,height=20,width=50)
	msg.pack()
	root.title("Encrypt Message in Image")
	lbl=tk.Label(text="Chose an RGB Image",font=("Helvetica", 20),fg="white",bg="black")
	lbl.pack()
	file_path = filedialog.askopenfilename()
	head, tail = os.path.split(file_path)
	btn=tk.Button(text="ENCRYPT",bg="black",fg="white",command=lambda: test([msg.get('1.0',tk.END),head,tail] ))
	btn.pack()
	print(head,"\n",tail)
	
	root.mainloop()

if __name__=="__main__":
	main()
