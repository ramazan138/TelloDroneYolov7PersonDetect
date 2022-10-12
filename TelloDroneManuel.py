from ast import Try
from djitellopy import Tello
import cv2
import time
import keyboard
import sys

def keyBoardInput(im0):
    speed=45
    lr,fb,ud,yv=0,0,0,0
    
    if keyboard.is_pressed("LEFT"): lr=-speed; print("Left")  
    elif  keyboard.is_pressed("RIGHT"): lr=speed; print("RIGHT")  
    
    if keyboard.is_pressed("UP"): fb=speed   ; print("UP")  
    elif  keyboard.is_pressed("DOWN"): fb=-speed  ; print("DOWN")  
          
    if keyboard.is_pressed("w"): ud=speed   ; print("w")  
    elif  keyboard.is_pressed("s"): ud=-speed ; print("s")  
    
    if keyboard.is_pressed("a"): yv=speed   ; print("a")  
    elif  keyboard.is_pressed("d"): yv=-speed   ; print("d")    


    if  keyboard.is_pressed("z"):
        cv2.imwrite(f"./images/photoTello/{time.time()}.jpg",im0)
        time.sleep(0.3)   
        print("Take Photo") 

    if keyboard.is_pressed("e"): 
        me.takeoff()   
        print("takeoff")  
    if  keyboard.is_pressed("q"):
        me.land()   
        print("land")    
        
    
        
    return(lr,fb,ud,yv)       

    
######################################################################
width = 640  # WIDTH OF THE IMAGE
height = 480  # HEIGHT OF THE IMAGE
startCounter =0   #  0 FOR FIGHT 1 FOR TESTING
######################################################################




# CONNECT TO TELLO
me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0



print(me.get_battery())

me.streamoff()
me.streamon()


    
        


while True:
    try:

        
        frame_read = me.get_frame_read()
        myFrame = frame_read.frame
        img = cv2.resize(myFrame, (width, height))
        val=keyBoardInput(img)
        me.send_rc_control(val[0], val[1], val[2], val[3])
        time.sleep(0.05)  
        cv2.imshow("MyResult", img)
        cv2 .waitKey(1)  # 1 millisecond
        
        if(int(me.get_battery())<15):
            print("UYARI...")
        
        if(int(me.get_battery())<5):
            print("Zorunlu iniş")
            me.land()
        
        # WAIT FOR THE 'Q' BUTTON TO STOP

    except:
        me.land()
        sys.exit()

    
    