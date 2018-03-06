#Display a route on a labeled Brandeis map and save the image to a file.
#Depending on the usage, the saved file will be Route.png or RouteCropped.png.
#To get back to the terminal prompt, close the display window.
#Usage may be any of:
#   python Display.py
#      (defaults to use BrandeisMapLabeledCropped.png)
#   python Display.py png
#      (defaults to use BrandeisMapLabeledCropped.png)
#   python Display.py jpg
#      (defaults to use BrandeisMapLabeledCropped.jpg)
#   python Display.py BrandeisMapLabeled.jpg
#   python Display.py BrandeisMapLabeled.png
#   python Display.py BrandeisMapLabeledCropped.jpg
#   python Display.py BrandeisMapLabeledCropped.png

import sys
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as img

MapName = 'BrandeisMapLabeledCropped.png'
if (len(sys.argv) > 1): MapName = sys.argv[1]
if (MapName=='png'): MapName='BrandeisMapLabeledCropped.png'
if (MapName=='jpg'): MapName='BrandeisMapLabeledCropped.jpg'

if ( (MapName != 'BrandeisMapLabeled.png') and \
     (MapName != 'BrandeisMapLabeled.jpg') and \
     (MapName != 'BrandeisMapLabeledCropped.png') and \
     (MapName !='BrandeisMapLabeledCropped.jpg') ):
     print ('\nIllegal map name - "' + MapName + '"\n')
     exit()

if ( (MapName=='BrandeisMapLabeled.png') or (MapName=='BrandeisMapLabeled.jpg') ):
   RouteData = 'Route.txt'
   RouteImage = 'Route.png'
if ( (MapName=='BrandeisMapLabeledCropped.png') or (MapName=='BrandeisMapLabeledCropped.jpg') ):
   RouteData = 'RouteCropped.txt'
   RouteImage = 'RouteCropped.png'

Brandeis = img.imread(MapName)

solution = open(RouteData).read().splitlines()

points = []
for line in solution:
    points.append(map(int, line.split()))

fig = plt.figure(figsize=(int(Brandeis.shape[1]/100),int(Brandeis.shape[0]/100)))
ax = fig.add_subplot(111)
ax.imshow(Brandeis, alpha=1.0)
for n in points:
    ax.arrow(n[0],n[1],n[2]-n[0],n[3]-n[1], fc='black',ec='magenta', lw=4)

print('\nMap used = ' + MapName)
print('Route data used = ' + RouteData)
print('Output image = ' + RouteImage + '\n')
plt.axis('off')
plt.subplots_adjust(left=0.0, right=1, top=1, bottom=0.0)
fig.savefig(RouteImage)

#A third argument can be included (value doesn't matter) to disable the image display.
if (len(sys.argv) < 3): plt.show()
