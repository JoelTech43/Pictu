import tkinter as tk
from PIL import Image
from tkinter import filedialog as fd
import conversions as con

hex_dict = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}

bin_dict = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'a','1011':'b','1100':'c','1101':'d','1110':'e','1111':'f'}

def Encrypt():
	try:
		message = entry1.get("1.0","end")
		binary = con.toBin(message)
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
					hex = con.rgbToHex((r, g, b))
					blueBin = hex_dict[hex[5]]
					blueBin2 = blueBin[:2] + binaryList[x]
					hex2 = hex[:5]+bin_dict[blueBin2]
					c = con.hexToRgb(hex2)
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
				hex = con.rgbToHex((r, g, b))
				blueBin = hex_dict[hex[5]]
				messageList.append(str(blueBin[2:]))
				pixel_map[j, i] = (r, g, b)
		fullList = ''.join(messageList)
		n = 8
		finalMessage = []
		message = [fullList[i:i+n] for i in range(0, len(fullList), n)]
		
		for item in message:
			finalMessage.append(con.toString(item))
		finalMessage = ''.join(finalMessage)
		
		output.insert("end",'The end may look garbled. If it is, the message didn\'t fill all the image\'s pixels. Just ignore it!\nYour message is: %s' % finalMessage)
	except AttributeError:
		output.insert("end","Oops, something went wrong!\nPlease try again! :(")

def selectFile():
	filetypes = (('png files', '*.png'),('jpg files', '*.jpg'),('jpeg files', '*.jpeg'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
	fileEdit = ""
	for char in filename:
		if char =="/":
			fileEdit += "\\"
		else:
			fileEdit += char
	reverse = fileEdit[::-1]
	nameOfFile = []
	for char in reverse:
		if char != "\\":
			nameOfFile.append(char)
		else:
			break
	nameOfFileString = ""
	nameOfFile=nameOfFile[::-1]
	for abc in nameOfFile:
		nameOfFileString+=abc
		print(abc)
	print(nameOfFile)
	print(nameOfFileString)
	selectedFileName["text"]= "Selected file: " + nameOfFileString
	return fileEdit

window = tk.Tk()
window.geometry("500x420")
window.config(background="#0066ff")
window.title("Picture Encrypt")
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file="spy.png"))

Instruct1 = tk.Label(window, text="Enter message:",font=("Arial", 12, "bold"),background="#0066ff",foreground="#ffffff")
Instruct1.pack(padx=10,pady=5,anchor="w")
entry1 = tk.Text(window, width=60, height=7,background="#99c2ff",foreground="#ffffff", font=("Arial", 12, "bold"))
entry1.pack(padx=10, pady=10)
btnFrame = tk.Frame(window)
btnFrame.columnconfigure(0, weight=1)
btnFrame.columnconfigure(1, weight=1)
EncryptBtn = tk.Button(btnFrame, text="Encrypt", font=("Arial", 12, "bold"), command=Encrypt,background="#99c2ff",foreground="#ffffff")
EncryptBtn.grid(column=0,row=1, sticky=tk.E+tk.W)
DecryptBtn = tk.Button(btnFrame, text="Decrypt", font=("Arial", 12, "bold"), command=Decrypt,background="#99c2ff", foreground="#ffffff")
DecryptBtn.grid(column=1,row=1, sticky=tk.E+tk.W)
btnFrame.pack(fill="x",padx=10)
selectedFileName = tk.Label(window,background="#0066ff",foreground="#ffffff",font=("Arial",12,"bold"),text="Selected File: ")
selectedFileName.pack(padx=10,pady=10,anchor="w")
scrollbar = tk.Scrollbar(window,orient="vertical")
scrollbar.pack(side = tk.RIGHT, fill = "y" )

output = tk.Text(window, font = ("Arial", 12, "bold"), width=60, height=7, background="#99c2ff", foreground="#ffffff")
output.pack(padx=10, anchor="w",side=tk.LEFT)

output.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output.yview)
window.mainloop()