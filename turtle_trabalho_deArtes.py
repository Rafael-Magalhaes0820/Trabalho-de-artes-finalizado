#  Trabalho de Artes : Arte e Tecnologia.

# Rafael Araújo Magalhães  3A


#  Algoritmo que contém imagens feitas com turtle
#  Apresenta as posibilidades ao usuário e pede para que escolha uma das opçoes
#  Após o usuario escolher a opção, apresentar a imagem.

import turtle
import time

print("")
print("")
print("")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Trabalho de artes : Arte e Tecnologia\nO trabalho consiste em diversas formas geométricas perfeitas desenhadas")
print("pelo computador")
print("")
print("Cinco figuras geométricas perfeitas podem ser desenhadas pelo computador no momento...")
escolha = input("\nEscolha uma: 1, 2, 3, 4 ou 5: ")

if escolha == str(1):
    s = turtle.Screen()
    s.bgcolor("black")
    s.title("Opção 1 : Estrela")

    t = turtle.Turtle()
    t.speed(0)

    for i in range(200):
        for colours in ["yellow", "orange", "red"]:
            t.color(colours)
            t.forward(i + 2)
            t.right(175)
            t.forward(i + 4)
            t.right(30)

    turtle.done


if escolha == str(2):

    t = turtle.Turtle()
    s = turtle.Screen()

    s.title("Opção 2 : Holograma")

    t.speed(0)
    s.bgcolor("black")
    t.pencolor("cyan")

    for i in range(240):
        t.color("cyan")
        t.circle(i)
        t.left(5)

    turtle.done()


if escolha == str(3):
    t = turtle.Turtle()
    s = turtle.Screen()
    s.title("Opção 3 : Spirograph")

    s.bgcolor("black")
    t.pensize(2)
    t.speed(0)

    for i in range(6):
        for colours in ["red", "blue", "cyan", "yellow", "green", "white", "magenta"]:
            t.color(colours)
            t.circle(100)
            t.left(10)

    t.hideturtle()
    turtle.done()


if escolha == str(4):
    t = turtle.Turtle()
    s = turtle.Screen()
    s.title("Opção 4 : Vortex")


    s.bgcolor("black")
    t.pensize(2)
    t.speed(0)

    for i in range(300):
        for colours in ["white", "pink", "cyan"]:
            t.color(colours)
            t.forward(i * 4)
            t.right(121)

    t.hideturtle()
    turtle.done


if escolha == str(5):
    t = turtle.Turtle()
    s = turtle.Screen()
    s.title("Opção 5 : RGB")

    s.bgcolor("black")
    t.pensize(2)
    t.speed(0)

    for i in range(100):
        for col in ["blue", "yellow", "red"]:
            t.color(col)
            t.circle(70)
            t.forward(2)
            t.right(2)

    t.hideturtle()
    turtle.done



#fim
