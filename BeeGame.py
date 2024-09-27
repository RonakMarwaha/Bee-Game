import pgzrun
import random
WIDTH=500
HEIGHT=500
bee=Actor('bee')
bee.pos=(100,100)
flower=Actor('flower')
flower.pos=(250,250)
score=0
gameover=0
def draw():
    screen.blit('background',(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text('SCORE IS  '+str(score),color='black',topleft=(10,10))
    if gameover:
        screen.fill('red')
        screen.draw.text('Times Up!',color='black',topleft=(30,10))

def timeup():
 global gameover
 gameover=True 

def placeflower():
    flower.x=random.randint(70,WIDTH-70)
    flower.y=random.randint(70,HEIGHT-70)

def update():
    global score
    if keyboard.left:
        bee.x = bee.x-2
    if keyboard.right:
        bee.x = bee.x+2
    if keyboard.up:
        bee.y = bee.y-2
    if keyboard.down:
        bee.y = bee.y+2
    if bee.colliderect(flower):
        score=score+10
        placeflower()

#clock_schedule(timeup,60.0)




























pgzrun.go()