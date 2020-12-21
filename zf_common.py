
import math
from pyperclip import copy

# Note: argument 'parts' is a string of comma separated part IDs. e.g. '1,2,3'

def copy_to_clipboard(arr):
	final_txt = '\n'.join(arr)
	print(final_txt)
	copy(final_txt)
		
def secToFrames(sec):
	return math.floor(sec * 30)