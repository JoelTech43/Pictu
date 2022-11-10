from PIL import Image

# Two dictionaries to convert one hex character to its equivalent binary nibble (hex_dict) and vice versa (bin_dict)
hex_dict = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}
bin_dict = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'a','1011':'b','1100':'c','1101':'d','1110':'e','1111':'f'}

# Function to convert a string to 8-bit binary. Input must be a string.
def toBin(a):
	a_bytes = bytes(a, 'ascii')
	binary = ''.join(bin(b)[2:].zfill(8) for b in a_bytes)
	return binary

# Function to convert 8-bit binary to string. May give OverflowError if data too long. Input must be a string.
def toString(a):
	a_list = a.split(' ')
	string = ''
	for i in a_list:
		p = chr(int(i,2))
		string = string + p
	return string

# Function to convert any length hex code to RGB as long as it is valid. Input should be a string in format #XXXXXX with any number of Xs(as long
# as it is still valid) and # is not mandatory.
def hexToRgb(value):
	value = value.lstrip('#')
	lv = len(value)
	return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# Function to convert any size RGB. Input should be a tuple in format (r, g, b).
def rgbToHex(rgb):
	return '%02x%02x%02x' % rgb


# Main function used to hide message in a given image. Input should be string. It should contain the file name if the file is in the same folder as
# the program or the entire path of the file. Each stage of the path should be seperated by \\ not just \
def Encrypt(imageFile):
	message = input('Enter message: ')
	binary = toBin(message)
	n = 2
	binaryList = [binary[i:i+n] for i in range(0, len(binary), n)]
	length = len(binaryList)-1
	x = 0
	
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

def Decrypt(imageFile):
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
	
	print('The end may look garbled. If it is, the message didn\'t fill all the image\'s pixels. Just ignore it!\nYour message is: %s' % finalMessage)

print("Welcome to Picture Encrypt!\nThis is a useful program that hides messages in images. THIS IS NOT ENCRYPTED (yet) AND SHOULD NOT BE USED TO TRANSFER SENSITIVE DATA!")