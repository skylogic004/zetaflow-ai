"""
This file is for special functions for advanced functionality. 
These are functions that build upon the basic components to build something more interesting.
"""
from zf_common import secToFrames
from zf_function_wrappers import *

firing_time = {
	'single': 100, # 100, 120
	'spread': 300, # 300, 320, 480-492
	'square': 111, # 110, 170
}

def macro_setSize(parts, size, START_FRAME, REPEAT_AFTER_FRAMES):
	strs = []

	strs.append(makeTriggerRepeat(START_FRAME, REPEAT_AFTER_FRAMES, setWidth(parts, size)))
	strs.append(makeTriggerRepeat(START_FRAME, REPEAT_AFTER_FRAMES, setHeight(parts, size)))

	return strs
	
# parts: list of Single Shot guns
def macro_machineGun(parts, gun_type, cooldown=5):
	"""
	cooldown: 2 is super frequent shots, 5 has nice delay while still being rapid
	"""
	t = firing_time[gun_type] - 2
	return makeTriggerRepeat(0, cooldown, setGunTime(parts, t))

# parts: list of Single Shot guns
def macro_stopMachineGun(parts, gun_type, cooldown=5):
	t = firing_time[gun_type] - 2
	return stop(makeTriggerRepeat(0, cooldown, setGunTime(parts, t)))
	
# parts: list of Single Shot guns
def macro_machineGunOnOff(parts, gun_type='single', off_seconds=6, on_seconds=4, cooldown=5, offset_seconds=0):
	strs = []

	if (cooldown <= 1):
		print('WARNING: I dont think cooldown can be this low')
	
	phaseDuration = secToFrames(off_seconds+on_seconds)

	# OLD VERSION
	# this creates and disbands the repeating trigger REPEATEDLY
	# strs.append( makeTriggerRepeat(secToFrames(offset_seconds), phaseDuration, disableGun(parts)) )
	# strs.append( makeTriggerRepeat(secToFrames(offset_seconds), phaseDuration, macro_stopMachineGun(parts, gun_type, cooldown)) )
	# strs.append( makeTriggerRepeat(secToFrames(offset_seconds+off_seconds), phaseDuration, enableGun(parts)) )
	# strs.append( makeTriggerRepeat(secToFrames(offset_seconds+off_seconds), phaseDuration, macro_machineGun(parts, gun_type, cooldown)) )

	# NEW VERSION
	# this one lets the machine gun fire *all the time* but enables and disables the gun upon request
	strs.append( makeTriggerRepeat(secToFrames(offset_seconds), phaseDuration, enableGun(parts)) )
	strs.append( makeTriggerRepeat(secToFrames(offset_seconds+on_seconds), phaseDuration, disableGun(parts)) )
	strs.append( macro_machineGun(parts, gun_type, cooldown) )


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

""" FRAME NUMBERS FOR setGunTime
Spread
40, 60
Start spin
173, ends 307


Missile
20 and 40
Ends at 60

Single shot keyframes at
1,2,3,11

Singu keyframes at
1,2,10
"""