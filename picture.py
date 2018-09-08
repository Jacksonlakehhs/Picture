"""
picture.py
Author: Jackson Lake
Credit: Schoology tutorial

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset


red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
grey = Color(0xCDC0B0, 1.0)
turq = Color(0x00EEEE, 1.0)

thinline = LineStyle(1, black)

head = RectangleAsset(120, 100, thinline, grey)
neck = RectangleAsset(40, 28, thinline, grey)
body = RectangleAsset(200, 200, thinline, grey)
leg1 = RectangleAsset(45, 90, thinline, grey)
leg2 = RectangleAsset(45, 90, thinline, grey)
eye1 = CircleAsset(15, thinline, turq)
eye2 = CircleAsset(15, thinline, turq)
shoulder1 = CircleAsset(20, thinline, black)
shoulder2 = CircleAsset(20, thinline, black)



Sprite(head, (432, 100))
Sprite(neck, (470, 200))
Sprite(body, (400, 228))
Sprite(leg1, (400, 428))
Sprite(leg2, (555, 428))
Sprite(eye1, (440, 115))
Sprite(eye2, (510, 115))
Sprite

# add your code here /\  /\  /\


myapp = App()
myapp.run()
