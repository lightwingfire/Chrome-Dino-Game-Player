from PIL import Image, ImageGrab #pip install Pillow
import keyboard #pip install keyboard
import threading

class Player(object):
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.dayNight = True
        self.numberOfDayNight = 0

    def __str__(self):
        return ("we good")

    def run(self):
        print("Welcome to Dinosaur Game Autoplayer, to begin open chrome and go to chrome://dino and fullscreen the application")
        print("Press 'm' when you want it to start playing")
        print("Press 'n' when you want it to stop playing")
        print("Press 'q' when you want to close the program")

        screen = ImageGrab.grab()
        screenWidth = screen.width
        screenHeight = screen.height

        detecting = False
        bounce = True # prevents the if statements for the keyboard to go off several times instead of once

        #self.timer = threading.Timer(60.0, self.moveDetectingSquare)
    
        while True:
            #Starts detecting
            if keyboard.is_pressed('m') and bounce == True:
                #Set the start location for the detection square
                self.dayNight = True
                self.numberOfDayNight = 0
                self.x1 = (520/1920) * screenWidth
                y1 = (570/1080) * screenHeight
                self.x2 = (600/1920) * screenWidth
                y2 = (670/1080) * screenHeight
            
                #self.timer.start()

                bounce = False
                print("start")
                detecting = True 
            #Stops detecting
            if keyboard.is_pressed('n') and bounce == False:

                #timer.cancel()

                bounce = True
                print("stop")
                detecting = False
            #Closes Program
            if keyboard.is_pressed('q'):
                print("goodbye!")
                sys.exit()
            if detecting == True: 
                self.detectObstacle(self.x1,y1,self.x2,y2)
       
    def detectObstacle(self,x1,y1,x2,y2):
       #Screenshots screan at coordinates
       p = ImageGrab.grab(bbox = (x1,y1,x2,y2))
       #Gets the colors that are in the Screenshot
       j = p.getcolors()
       (num, tup) = j[0]
       #if all the pixels in the screenshot are the same color it releases the spacebar but if they aren't, it holds down the spacebar
       if (num == ((x2-x1)*(y2-y1))):
           keyboard.release('space')
       else:
           keyboard.press('space')
           print("jump!")

       if tup == (255, 255, 255) and self.dayNight == False:
           self.moveDetectingSquare()
           self.dayNight = True
       if tup == (0, 0, 0) and self.dayNight ==True and self.numberOfDayNight < 8:
           self.moveDetectingSquare()
           self.dayNight = False

    def moveDetectingSquare(self):
        if self.numberOfDayNight == 0:
            shift = 150
        else:
            shift = 75
        #self.x1 = self.x1 + shift
        self.numberOfDayNight = self.numberOfDayNight + 1
        self.x2 = self.x2 + shift
        print("shifting detecting square over",shift,"pixels","(",self.x2,")")
    

def main():
    dino = Player()
    dino.run()

if __name__== "__main__":
  main()
