from tkinter import *
import tkinter

class Test(Frame):
    def printit(self):
        print("hi")

    def createWidgets(self):
        self.QUIT = Button(self, text='QUIT',
                           background='red',
                           foreground='white',
                           height=3,
                           command=self.quit)
        self.QUIT.pack(side=BOTTOM, fill=BOTH)

        self.canvasObject = Canvas(self, width=self.WIDTH, height=self.HEIGHT, bg = "#000000")
        self.canvasObject.pack(side=LEFT)

    def mouseDown(self, event):
        # canvas x and y take the screen coords from the event and translate
        # them into the coordinate system of the canvas object
        self.startx = self.canvasObject.canvasx(event.x)
        self.starty = self.canvasObject.canvasy(event.y)

    def mouseMotion(self, event):
        # canvas x and y take the screen coords from the event and translate
        # them into the coordinate system of the canvas object
        x = self.canvasObject.canvasx(event.x)
        y = self.canvasObject.canvasy(event.y)
        self.x_end = x
        self.y_end = y


        if (self.startx != event.x)  and (self.starty != event.y) :
            self.canvasObject.delete(self.rubberbandBox)
            self.rubberbandBox = self.canvasObject.create_rectangle(
                self.startx, self.starty, x, y)
            # this flushes the output, making sure that
            # the rectangle makes it to the screen
            # before the next event is handled
            self.update_idletasks()

    def mouseUp(self, event):
        self.canvasObject.delete(self.rubberbandBox)


        self.xa = ((self.startx / self.WIDTH) * (self.xb-self.xa)) -2.0;
        self.xb = ((self.x_end / self.WIDTH) * (self.xb-self.xa)) -2.0

        self.ya = ((self.starty / self.HEIGHT) * (self.yb-self.ya)) -1.5;
        self.yb = ((self.y_end / self.HEIGHT) * (self.yb-self.ya)) -1.5

        self.drawMandel()




    def drawMandel(self):

        maxIt = 256

        #        window = self #Tk()
        #        self.canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")
        self.img = PhotoImage(width = self.WIDTH, height = self.HEIGHT)
        self.canvasObject.create_image((0, 0), image = self.img, state = "normal", anchor = tkinter.NW)

        for ky in range(self.HEIGHT):
            for kx in range(self.WIDTH):
                c = complex(self.xa + (self.xb - self.xa) * kx / self.WIDTH, self.ya + (self.yb - self.ya) * ky / self.HEIGHT)
                z = complex(0.0, 0.0)
                for i in range(maxIt):
                    z = z * z + c
                    if abs(z) >= 2.0:
                        break
                rd = hex(i % 4 * 64)[2:].zfill(2)
                gr = hex(i % 8 * 32)[2:].zfill(2)
                bl = hex(i % 16 * 16)[2:].zfill(2)
                self.img.put("#" + rd + gr + bl, (kx, ky))

        self.canvasObject.pack()

    def __init__(self, master=None):
        self.WIDTH = 640; self.HEIGHT = 480
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()

        # this is a "tagOrId" for the rectangle we draw on the canvas
        self.rubberbandBox = None

        # and the bindings that make it work..
        Widget.bind(self.canvasObject, "<Button-1>", self.mouseDown)
        Widget.bind(self.canvasObject, "<Button1-Motion>", self.mouseMotion)
        Widget.bind(self.canvasObject, "<Button1-ButtonRelease>", self.mouseUp)
        self.xa = -2.0; self.xb = 1.0
        self.ya = -1.5; self.yb = 1.5

        self.drawMandel()


test = Test()

test.mainloop()

