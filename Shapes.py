import pgzrun, random
TITLE="gradient"
WIDTH,HEIGHT=400,400
def draw():
    r,g,b,a=255,0,random.randint(0,255),0.1
    w=350
    h=100
    for i in range(25):
         box=Rect((0,0),(w,h))
         box.center=200,200
         screen.draw.rect(box,(r,g,b,a))
         r=r-10
         g=g+10
         w=w-10
         h=h+10


   
pgzrun.go()
