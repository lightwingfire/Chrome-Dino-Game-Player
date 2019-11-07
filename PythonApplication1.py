from PIL import Image, ImageGrab
import keyboard
import webbrowser
def main():
    #webbrowser.register(Chrome('chrome'))
    #webbrowser.open("google.com")
    #webbrowser.get('windows-default %s').open_new_tab('http://www.google.com')
    screen = ImageGrab.grab()
    screenWidth = screen.width
    screenHeight = screen.height
    detecting = False
    while True:
        if keyboard.is_pressed('m'):
            detecting = True 
        elif keyboard.is_pressed('n'):
            detecting = False
        if detecting == True: 
            detectObstacle(520,570,600,670)
        #print(backgroundColor(520, 800))
def detectObstacle(x1,y1,x2,y2):
   p = ImageGrab.grab(bbox = (x1,y1,x2,y2))
   j = p.getcolors()
   (num, tup) = j[0]
   print(num)
   if (num == ((x2-x1)*(y2-y1))):
       keyboard.release('space')
   else:
       keyboard.press('space')

def backgroundColor(x,y):
    pixel = ImageGrab.grab(bbox = (x,y,x+1,y+1))
    return pixel.getpixel((0,0))
if __name__== "__main__":
  main()