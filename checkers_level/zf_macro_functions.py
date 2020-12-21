"""
This file is for special functions for advanced functionality. 
These are functions that build upon the basic components to build something more interesting.
"""

import math

# Note: argument 'parts' is a string of comma separated part IDs. e.g. '1,2,3'

def printAll(arr):
	for str in arr:
		print(str)
		
def secToFrames(sec):
	return math.floor(sec * 30)

def macro_setSize(parts, size, START_FRAME, REPEAT_AFTER_FRAMES):
	strs = []

	strs.append(makeTriggerRepeat(START_FRAME, REPEAT_AFTER_FRAMES, setWidth(parts, size)))
	strs.append(makeTriggerRepeat(START_FRAME, REPEAT_AFTER_FRAMES, setHeight(parts, size)))

	return strs
	
# parts: list of Single Shot guns
def macro_machineGun(parts):
	return makeTriggerRepeat(0,5, setGunTime(parts, 98))

# parts: list of Single Shot guns
def macro_stopMachineGun(parts):
	return stop(makeTriggerRepeat(0,5, setGunTime(parts, 98)))
	
# parts: list of Single Shot guns
def macro_machineGunOnOff(parts):
	strs = []
	
	phaseDuration = secToFrames(6)
	strs.append( makeTriggerRepeat(secToFrames(0), phaseDuration, disableGun(parts)) )
	strs.append( makeTriggerRepeat(secToFrames(0), phaseDuration, macro_stopMachineGun(parts)) )
	strs.append( makeTriggerRepeat(secToFrames(4), phaseDuration, enableGun(parts)) )
	strs.append( makeTriggerRepeat(secToFrames(4), phaseDuration, macro_machineGun(parts)) )
	
	return strs

def macro_linearMove(parts, waitTimeDuration, moveTimeDuration, startDist, endDist, waitDist = None, startTimeOffset = 0):
	strs = []
	
	startMoveTime = int(waitTimeDuration)
	totalTime = int(waitTimeDuration) + int(moveTimeDuration)
	
	distToTravel = endDist - startDist
	distPerStep = float(distToTravel) / moveTimeDuration
	
	# Wait: set distance to static location
	if (waitDist != None):
		setDistCmd = setDistance(parts, waitDist)
		strs.append(
			makeTriggerRepeat(0, totalTime, setDistCmd)
		)
	
	# Move: distance changes over time
	for time in range(startMoveTime, totalTime):
		timeDelta = time - startMoveTime
		
		newDist = startDist + timeDelta*distPerStep
	
		setDistCmd = setDistance(parts, newDist)
		strs.append(
			makeTriggerRepeat(time+startTimeOffset, totalTime, setDistCmd)
		)
	
	return strs
	
GUNTIME_SINGULARITY_FIRST_SHOT = 109
def macro_singularityFire(parts, timeToFire):
	strs = []
	strs.append( makeTriggerRepeat(timeToFire, timeToFire, enableGun(parts)) )
	strs.append( makeTriggerRepeat(timeToFire, timeToFire, setGunTime(parts, GUNTIME_SINGULARITY_FIRST_SHOT)) )
	strs.append( makeTriggerRepeat(4, timeToFire, disableGun(parts)) )
	
	return strs
	
def macro_rotateToShipOnceRepeating(parts, rotateTime, cycleTime):
	strs = []
	strs.append( makeTriggerRepeat(rotateTime, cycleTime, rotatePartToShip(parts)) )
	strs.append( makeTriggerRepeat(rotateTime+1, cycleTime, stop(rotatePartToShip(parts))) )
	return strs
