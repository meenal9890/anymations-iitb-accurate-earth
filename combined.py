## TODO
# Modify earth using all functions to make a full model
#	# Add camera
#	# Add clouds, weather
# Render an image/animation instead of just saving the blend file

## Init script
import * from scripts
import os
from datetime import timedelta, datetime
import sys
import argparse

try:
	import bpy
except ModuleNotFoundError:
	sys.exit("Please run this script using Blender python.\nExample Usage:\nblender --background --python " + __file__ + " -- [options]")

'''
	------------------------------------------------------------------------------------------------------------
	This part is to store the directory information in a variable.
	The first part of this is to check if blender is returning a directory on it's own.
	The second part is to use the path of this script.
'''
dir = os.path.dirname(bpy.data.filepath)
if not dir or dir != "":
	dir = os.path.dirname(__file__)
if dir not in sys.path:
	sys.path.append(dir)
print(os.path.dirname(__file__))


def clean_slate():
	'''
	Simple function to clean up the scene,
	it deletes all objects and material from the scene
	'''
	for o in bpy.context.scene.objects:
		if o.type in ['MESH', 'EMPTY']:
			o.select_set(True)
		else:
			o.select_set(False)
	#
	bpy.ops.object.delete()
	bpy.data.lights.remove(bpy.data.lights[0])
	bpy.data.cameras.remove(bpy.data.cameras[0])
	#
	for m in bpy.data.materials:
		bpy.data.materials.remove(m)

if __name__ == "__main__":

    argv = sys.argv
    print(argv)

    if "--" not in argv:
        argv = []
    else:
        argv = argv[argv.index("--") + 1:]

    usage_text = (
        "Run Blender to get an astrophysically accurate Earth:"
        "  blender --background --python " + __file__ + " -- [options]"
        )

    parser = argparse.ArgumentParser(description=usage_text)
    parser.add_argument("--time", "-t", nargs=1, type=makeTimeArr, default=[['00','00']], help="Time to be inputted in the format 'HH:MM'", dest="time")
    parser.add_argument("--date", "-d", nargs=1, type=makeDateArr, default=[['2021','07','26']], help="Date to be inputted in the format YYYY:MM:DD", dest="date")
    args = parser.parse_args(argv)
    time = timedelta(hours=int(args.time[0][0]), minutes=int(args.time[0][1]))
    date = datetime(year=int(args.date[0][0]), month=int(args.date[0][1]), day=int(args.date[0][2]))
    finalTime = Time(date + time)

    clean_slate()

    # earth = makeEarth()
    # earth_atmo = makeAtmosphere(earth)
    # sun = makeSun(earth=earth, dateTime=finalTime)

    # bpy.ops.wm.save_as_mainfile(filepath="./realistic_earth.blend")
