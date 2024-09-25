import pgzrun
import random
TITLE="Beegame"
WIDTH=500
HEIGHT=500
Score=0

bee=Actor('bee')
bee.pos=(100,100)
flower=Actor('flower')
flower.pos=(250,250)



def draw():
    screen.blit('background', (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+str(Score),color="Black",topleft=(10,10))
    if Score < 0:
        screen.fill("red")
        screen.draw.text("You Lose",color="white",center=(250,250))

def place_flower():
    x=random.randint(70,WIDTH-70)
    y=random.randint(70,HEIGHT-70)
    flower.x=x
    flower.y=y


def update():
    global Score
    if keyboard.left:
        bee.x=bee.x-(2+(Score/10))
    if keyboard.right:
        bee.x=bee.x+(2+(Score/10))
    if keyboard.up:
        bee.y=bee.y-(2+(Score/10))
    if keyboard.down:
        bee.y=bee.y+(2+(Score/10))

    flower_collected=bee.colliderect(flower)    
    if flower_collected:
        Score=Score+10
        place_flower()


    if bee.x > 500:
        bee.x=250
        Score=Score-10
    if bee.y > 500:
        bee.y=250
        Score=Score-10
   




pgzrun.go()