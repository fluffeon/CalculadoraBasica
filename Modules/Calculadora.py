import pygame

from UIElements.Buttons import Button
from UIElements.InputBox import TextBox

# Actividad para la semana:

# Actividad:

# 1. Crear un proyecto “Calculadora” siguiendo todo el workflow explicado
# 2. Hacer cambios en el proyecto y commitearlos (mínimo 3/4 commits distintos)
# 3. Crear una rama que se llame: “nombre_usuario/testing_branches”
# 4. Hacer cambios en la rama y luego mergear los cambios a main/master
# 5. Compartir link del repositorio con la clase

# Opcional: hacer lo mismo usando ‘pipenv’

Fondo=(0,153,255)

Width=800
Height=600

ConsoleX=Width/2-234/2
ConsoleY=Height/2-292/2

buffer=int()

pygame.init()
mainscreen = pygame.display.set_mode((Width,Height))

calculatortextbox=TextBox(x=ConsoleX-2, y=ConsoleY, w=234, h=50)

buttons=[
    Button(x=ConsoleX, y=ConsoleY+60, screen=mainscreen, h=50, w=50, label="1", function=calculatortextbox.writeinto, functionArguments=('1')),
    Button(x=ConsoleX+60, y=ConsoleY+60, screen=mainscreen, h=50, w=50, label="2", function=calculatortextbox.writeinto, functionArguments=('2')),
    Button(x=ConsoleX+120, y=ConsoleY+60, screen=mainscreen, h=50, w=50, label="3", function=calculatortextbox.writeinto, functionArguments=('3')),
    Button(x=ConsoleX, y=ConsoleY+120, screen=mainscreen, h=50, w=50, label="4", function=calculatortextbox.writeinto, functionArguments=('4')),
    Button(x=ConsoleX+60, y=ConsoleY+120, screen=mainscreen, h=50, w=50, label="5", function=calculatortextbox.writeinto, functionArguments=('5')),
    Button(x=ConsoleX+120, y=ConsoleY+120, screen=mainscreen, h=50, w=50, label="6", function=calculatortextbox.writeinto, functionArguments=('6')),
    Button(x=ConsoleX, y=ConsoleY+180, screen=mainscreen, h=50, w=50, label="7", function=calculatortextbox.writeinto, functionArguments=('7')),
    Button(x=ConsoleX+60, y=ConsoleY+180, screen=mainscreen, h=50, w=50, label="8", function=calculatortextbox.writeinto, functionArguments=('8')),
    Button(x=ConsoleX+120, y=ConsoleY+180, screen=mainscreen, h=50, w=50, label="9", function=calculatortextbox.writeinto, functionArguments=('9')),

    Button(x=ConsoleX+180, y=ConsoleY+60, screen=mainscreen, h=50, w=50, label="+"),
    Button(x=ConsoleX+180, y=ConsoleY+120, screen=mainscreen, h=50, w=50, label="-"),
    Button(x=ConsoleX+180, y=ConsoleY+180, screen=mainscreen, h=50, w=50, label="/"),
    Button(x=ConsoleX+180, y=ConsoleY+240, screen=mainscreen, h=50, w=50, label="="),
    Button(x=ConsoleX+120, y=ConsoleY+240, screen=mainscreen, h=50, w=50, label="DEL", function=calculatortextbox.backspace)
]

clock = pygame.time.Clock()

while True:
    mainscreen.fill(Fondo)

    for eachbutton in buttons:
        eachbutton.showButton()
        eachbutton.render()

    for event in pygame.event.get():
        for eachbutton in buttons:
            eachbutton.checkPress(event)

    calculatortextbox.draw(mainscreen)
    calculatortextbox.update()
    
    clock.tick(60)
    pygame.display.update() 