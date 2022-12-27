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