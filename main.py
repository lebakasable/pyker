#!/usr/bin/env python3

import math
import tkinter as tk
from PIL import Image, ImageTk
from pyker import Canvas

WIDTH = 800
HEIGHT = 600

GRID_COUNT = 10
GRID_PAD = 0.5/GRID_COUNT
GRID_SIZE = ((GRID_COUNT - 1)*GRID_PAD)
CIRCLE_RADIUS = 5
Z_START = 0.25

if __name__ == '__main__':
    root = tk.Tk()

    canvas = Canvas(WIDTH, HEIGHT, 0x000000)

    image = Image.new("RGB", (canvas.width, canvas.height))
    image.putdata(canvas.pixels)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo, borderwidth=0)
    label.pack()

    angle = 0

    def update_image():
        global photo, angle

        angle += 0.025 * math.pi

        canvas.fill(0x000000)
        for ix in range(10):
            for iy in range(10):
                for iz in range(10):
                    x = ix*GRID_PAD - GRID_SIZE/2
                    y = iy*GRID_PAD - GRID_SIZE/2
                    z = Z_START * iz*GRID_PAD

                    cx = 0
                    cz = Z_START + GRID_SIZE/2

                    dx = x - cx
                    dz = z - cz

                    a = math.atan2(dz, dx)
                    m = math.sqrt(dx*dx + dz*dz)

                    dx = math.cos(a + angle)*m
                    dz = math.sin(a + angle)*m

                    x = dx + cx
                    z = dz + cz

                    x /= z
                    y /= z

                    r = int(ix*255/GRID_COUNT)
                    g = int(iy*255/GRID_COUNT)
                    b = int(iz*255/GRID_COUNT)
                    color = 0xFF000000 | (r<<(0*8)) | (g<<(1*8)) | (b<<(2*8))
                    canvas.circle(int((x + 1)/2*WIDTH), int((y + 1)/2*HEIGHT), CIRCLE_RADIUS, color)

        image.putdata(canvas.pixels)
        photo = ImageTk.PhotoImage(image)

        label.configure(image=photo)

        root.after(1, update_image)

    update_image()
    root.mainloop()
