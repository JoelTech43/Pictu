import tkinter as tk
from PIL import Image
from tkinter import filedialog as fd

hex_dict = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}

bin_dict = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'a','1011':'b','1100':'c','1101':'d','1110':'e','1111':'f'}

def toBin(a):
	a_bytes = bytes(a, 'ascii')
	binary = ''.join(bin(b)[2:].zfill(8) for b in a_bytes)
	return binary

def toString(a):
	a_list = a.split(' ')
	string = ''
	for i in a_list:
		p = chr(int(i,2))
		string = string + p
	return string

def hexToRgb(value):
	value = value.lstrip('#')
	lv = len(value)
	return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgbToHex(rgb):
	return '%02x%02x%02x' % rgb

def Encrypt():
	try:
		message = entry1.get("1.0","end")
		binary = toBin(message)
		n = 2
		binaryList = [binary[i:i+n] for i in range(0, len(binary), n)]
		length = len(binaryList)-1
		x = 0
		
		imageFile = selectFile()
		input_image = Image.open(imageFile) 
		pixel_map = input_image.load() 
		width, height = input_image.size
		
		for i in range(height): 
			for j in range(width):
				r, g, b = input_image.getpixel((j, i)) 
				if x <= length:
					hex = rgbToHex((r, g, b))
					blueBin = hex_dict[hex[5]]
					blueBin2 = blueBin[:2] + binaryList[x]
					hex2 = hex[:5]+bin_dict[blueBin2]
					c = hexToRgb(hex2)
					r = c[0]
					g = c[1]
					b = c[2]
					x += 1
				else:
					pass
				pixel_map[j, i] = (r, g, b) 
		
		input_image.save("encrypt.png", format="png")
		input_image.show()
	except AttributeError:
		print("Oops, something went wrong!\nPlease try again! :(")

def Decrypt():
	try:
		imageFile = selectFile()
		input_image = Image.open(imageFile) 
		pixel_map = input_image.load() 
		width, height = input_image.size
		messageList = []
		
		for i in range(height): 
			for j in range(width):
				r, g, b = input_image.getpixel((j, i)) 
				hex = rgbToHex((r, g, b))
				blueBin = hex_dict[hex[5]]
				messageList.append(str(blueBin[2:]))
				pixel_map[j, i] = (r, g, b)
		fullList = ''.join(messageList)
		n = 8
		finalMessage = []
		message = [fullList[i:i+n] for i in range(0, len(fullList), n)]
		
		for item in message:
			finalMessage.append(toString(item))
		finalMessage = ''.join(finalMessage)
		
		output["text"] = 'The end may look garbled. If it is, the message didn\'t fill all the image\'s pixels. Just ignore it!\nYour message is: %s' % finalMessage
	except AttributeError:
		print("Oops, something went wrong!\nPlease try again! :(")

def selectFile():
	filetypes = (('png files', '*.png'),('jpg files', '*.jpg'),('jpeg files', '*.jpeg'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
	fileEdit = ""
	for char in filename:
		if char =="/":
			fileEdit += "\\"
		else:
			fileEdit += char
	return fileEdit

window = tk.Tk()
window.geometry("500x455")

Instruct1 = tk.Label(window, text="Enter message:",font=("Arial", 12))
Instruct1.pack(padx=10,pady=5,anchor="w")
entry1 = tk.Text(window, width=60, height=7)
entry1.pack(padx=10, pady=10)
btnFrame = tk.Frame(window)
btnFrame.columnconfigure(0, weight=1)
btnFrame.columnconfigure(1, weight=1)
EncryptBtn = tk.Button(btnFrame, text="Encrypt", font=("Arial", 12), command=Encrypt)
EncryptBtn.grid(column=0,row=1, sticky=tk.E+tk.W)
DecryptBtn = tk.Button(btnFrame, text="Decrypt", font=("Arial", 12), command=Decrypt)
DecryptBtn.grid(column=1,row=1, sticky=tk.E+tk.W)
btnFrame.pack(pady=10,fill="x")
scroll = tk.Scrollbar(window)
scroll.pack(side='right')
output = tk.Label(window, text = "", font = ("Arial", 12))
output.pack(padx=10, pady=10, anchor="w")

window.mainloop()