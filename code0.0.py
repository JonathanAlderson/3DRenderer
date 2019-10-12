import tkinter


def render():
    mycanvas.delete('all')
    for point in allPoints:
        createPoint(point[0],point[1],point[2])
    #mycanvas.create_rectangle(100,100,200,200)


def createPoint(x,y,z):
    #print(x,y,z)
    try:
        twoDX = ((screenHeight/2)/(x/z))+(screenWidth/2)
    except:
        twoDX = 0
        
    try:
        twoDY = ((screenHeight/2)/(y/z))+(screenHeight/2)
    except:
        twoDY = 0

    print(twoDX,twoDY)
    mycanvas.create_rectangle(twoDX,twoDY,twoDX,twoDY,fill="red")


def update():
    render()
    window.after(16,update)



allPoints = [[0,0,1],
             [10,0,1],[-10,0,1],
             [0,10,1],[0,-10,1],
             [0,0,10],[0,0,-10],
             ]

maxSize = 100

screenWidth = 700
screenHeight = 700


window = tkinter.Tk()
mycanvas = tkinter.Canvas(width=screenWidth,height=screenHeight)
mycanvas.pack()

update()


tkinter.mainloop()
