"""
This file holds functions that reproduce the commands available in the editor (http://zetaflow.skylogic.ca/game/edit)
"""

# Note: argument 'parts' is EITHER a single part number (string or int) OR a list (array) of part numbers

def parts_to_string(parts):
	if (isinstance(parts, list)):
		return ','.join([str(x) for x in parts])
	else:
		return f'{parts}'

	
def randomRotate(speed):
	return f'randomRotate, {speed:d}'

def makeInvincible(parts):
	parts_str = parts_to_string(parts)
	return f'makeInvincible, {parts_str}'

def makeVulnerable(parts):
	parts_str = parts_to_string(parts)
	return f'makeVulnerable, {parts_str}'
	
def makeTriggerRepeat(START_FRAME, REPEAT_AFTER_FRAMES, ANY_COMMAND):
	return 'makeTrigger, timeRepeat, %d, %d, %s' % (START_FRAME, REPEAT_AFTER_FRAMES, ANY_COMMAND)
	
def makeTriggerDeath(part_num, any_command):
	return f'makeTrigger, death, {part_num}, {any_command}'

def makeTriggerTime(START_FRAME, ANY_COMMAND):
	return f'makeTrigger, time, {START_FRAME}, {ANY_COMMAND}'

def disableGun(parts):
	parts_str = parts_to_string(parts)
	return f'disableGun, {parts_str}'
def enableGun(parts):
	parts_str = parts_to_string(parts)
	return f'enableGun, {parts_str}'
	
def setDistance(parts, dist):
	parts_str = parts_to_string(parts)
	return f'setDistance, {dist}, {parts_str}'

def setGunTime(parts, time):
	parts_str = parts_to_string(parts)
	return f'setGunTime, {time:d}, {parts_str}'

def setWidth(parts, width_percent):
	parts_str = parts_to_string(parts)
	return f'setWidth, {width_percent:d}, {parts_str}'

def setHeight(parts, height_percent):
	parts_str = parts_to_string(parts)
	return f'setHeight, {height_percent:d}, {parts_str}'

def setHP(parts, hp):
	parts_str = parts_to_string(parts)
	return f'setHP, {hp}, {parts_str}'

def setColor(parts, hex_color):
	"""
	color_hex: e.g. FF0000 for red
	"""
	parts_str = parts_to_string(parts)
	return f'col, {hex_color}, {parts_str}'

def destroy(parts):
	parts_str = parts_to_string(parts)
	return f'destroy, {parts_str}'

def setSize(parts, percentage):
	strs = []
	strs.append( setWidth(parts, percentage) )
	strs.append( setHeight(parts, percentage) )
	return strs

def rotatePartToShip(parts):
	parts_str = parts_to_string(parts)
	return f'rotatePartToShip, {parts_str}'

def rotate(part, speed, min_angle=None, max_angle=None, start_angle=None):
	assert isinstance(part, int)
	if (min_angle is None and max_angle is None and start_angle is None):
		return f'rotatePart, {part}, {speed}'
	else:
		assert min_angle is not None
		assert max_angle is not None
		assert start_angle is not None
		return f'rotatePart, {part}, {speed}, {min_angle}, {max_angle}, {start_angle}'
	
def stop(cmd):
	return 'stop, %s' % cmd