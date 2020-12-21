"""
This file holds functions that reproduce the commands available in the editor (http://zetaflow.skylogic.ca/game/edit)
"""

# Note: argument 'parts' is a string of comma separated part IDs. e.g. '1,2,3'
	
def randomRotate(speed):
	return 'randomRotate, %d' % speed

def makeInvincible(parts):
	return 'makeInvincible, %s' % parts
	
def makeTriggerRepeat(START_FRAME, REPEAT_AFTER_FRAMES, ANY_COMMAND):
	return 'makeTrigger, timeRepeat, %d, %d, %s' % (START_FRAME, REPEAT_AFTER_FRAMES, ANY_COMMAND)

def disableGun(parts):
	return 'disableGun, ' + parts
def enableGun(parts):
	return 'enableGun, ' + parts
	
def rotatePartToShip(parts):
	return 'rotatePartToShip, ' + parts
	
def setDistance(parts, dist):
	return 'setDistance, %d, %s' % (dist, parts)

def setGunTime(parts, time):
	return 'setGunTime, %d, %s' % (time, parts)

def setWidth(parts, widthPercentage):
	return 'setWidth, %d, %s' % (widthPercentage, parts)

def setHeight(parts, heightPercentage):
	return 'setHeight, %d, %s' % (heightPercentage, parts)

def setSize(parts, percentage):
	strs = []
	strs.append( setWidth(parts, percentage) )
	strs.append( setHeight(parts, percentage) )
	return strs

def rotatePartToShip(parts):
	return 'rotatePartToShip, %s' % (parts)
	
def stop(cmd):
	return 'stop, %s' % cmd