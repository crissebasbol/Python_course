import turtle


def main():
    window = turtle.Screen()
    cristhian = turtle.Turtle()
    make_rectangle(cristhian)
    # Para que mantenga la pantalla abierta
    turtle.mainloop()


def make_rectangle(cristhian):
    length = int(input("Input a size for one side of the square: "))
    for i in range(4):
        make_line_and_turn(cristhian, length)


def make_line_and_turn(cristhian, length):
    cristhian.forward(length)
    cristhian.left(90)


# Esta es una forma de definir donde tien que comenzar los programas en python
# Si el nombre de este archivo internamente python le llama main, entonces ejecute la seria de instrucciones
if __name__ == '__main__':
    main()
# Cuadno python importa un módulo, siempre lo hace con el nombre del archivo (a excepción si el archivo que
# se está corriendo es el punto de entrada )
