#!/bin/env python3
# -*- coding: utf-8 -*-
import turtle
import colorsys

def hsv_to_hex(h, s, v):
    # 这个函数DeekSeek写的
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return '#{:02x}{:02x}{:02x}'.format(
        int(r * 255), int(g * 255), int(b * 255)
    )

def draw_square(length):
    for i in range(4):
        turtle.fd(length)
        turtle.left(90)

length = 5
color = 0

turtle.bgcolor("black")
turtle.speed(0)

while color <= 1000:
    turtle.color(hsv_to_hex((color % 360) / 360, 1, 1))
    draw_square(length)
    turtle.left(5)
    color += 5
    length += 2

turtle.done()
