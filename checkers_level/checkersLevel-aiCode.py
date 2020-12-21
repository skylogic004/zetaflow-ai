from zf_function_wrappers import *
from zf_macro_functions import *

REPEAT_AFTER = 30

# PARTS
parts_checkers = '3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19'
parts_rear = '1,2,26,27'
parts_rearRockets = '28,29'
parts_coveredSingles = '20,21,22,23,24,25'
parts_singularityBombPivot = '39'
parts_singularityBombCore = '31'
parts_singularityBomb_guns = '34,35,36,37,38'
parts_singularityBomb = parts_singularityBombCore + ',32,33,' + parts_singularityBomb_guns + ',' + parts_singularityBombPivot

print randomRotate(5)

# Checkers blocks resize
startSize = 31
for i in range(0,14):
	printAll(macro_setSize(parts_checkers, startSize+3*i, i, REPEAT_AFTER))
	
for i in range(15,29):
	printAll(macro_setSize(parts_checkers, startSize+3*(29-i), i, REPEAT_AFTER))
	
# Invincible pieces
parts = parts_checkers + ', ' + parts_rear + ', ' + parts_rearRockets + ', ' + parts_singularityBomb
print makeInvincible(parts)

# Machine guns
print rotatePartToShip(parts_coveredSingles)
printAll(macro_machineGunOnOff(parts_coveredSingles))

# Singularity bomb
time_singBombWaitDur = time_singBombMoveStart = secToFrames(3)
time_singBombMoveDur = secToFrames(1.5)
time_singBombTotalDur = time_singBombWaitDur + time_singBombMoveDur
time_singBombExplode = time_singBombTotalDur - 1 # minus 1 b/c we need the gun to still be in position (not moved to the waiting area)

printAll(setSize(parts_singularityBomb_guns + ',' + parts_singularityBombPivot, 0)) # Hide all the guns and pivot at the start
printAll(macro_linearMove(parts_singularityBombCore, time_singBombWaitDur, time_singBombMoveDur, 10, 300, 9999))
printAll(macro_singularityFire(parts_singularityBomb_guns, time_singBombExplode))
printAll(macro_rotateToShipOnceRepeating(parts_singularityBombPivot, time_singBombMoveStart, time_singBombTotalDur))
