from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')

character = load_image('character.png')

x = 0
y = 0
r = 210

while True:
    
    while ( x < 800 ):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x += 2

        delay(0.005)

    while ( y < 600-90 ):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800,y+90)
        y += 2

        delay(0.005)

    while ( x > 0 ):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,600)
        x -= 2

        delay(0.005)

    while ( y > 0 ):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y+90)
        y -= 2

        delay(0.005)

    while ( x < 400 ):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x += 2

        delay(0.005)

    x = 400
    y = 300
    t = -90

    while (t < 270):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x + r * math.cos(t / 360 * 2 * math.pi), y + r * math.sin(t / 360 * 2 * math.pi))
        t += 1
        delay(0.005)
    x = 400

   



