#!/usr/bin/python
# -*- coding: utf -8 -*-

import turtle
# Es un modulo de python que sirve para generar programas gráficos

# Decirle a turtle que queremos generar una ventana
window = turtle.Screen()

#vamos a crear un cuadrado
crithian = turtle.Turtle()
crithian.forward(50)
crithian.left(90)
crithian.forward(50)
crithian.left(90)
crithian.forward(50)
crithian.left(90)
crithian.forward(50)
crithian.left(90)

# para que turtle no cierrre el programa
turtle.mainloop()