from djitellopy import Tello
import cv2
import time
import keyboard



"""Tello Drone Baglantıları"""

me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0


takeLand=False
print(me.get_battery())

me.streamoff()
me.streamon()

width = 720  # WIDTH OF THE IMAGE
height = 640  # HEIGHT OF THE IMAGE
startCounter =0   #  0 FOR FIGHT 1 FOR TESTING
def adress():
    a=me.get_udp_video_address()
    return a

""" İmage get """
def imgCap():
    
    frame_read = me.get_frame_read()
    myFrame = frame_read.frame
    
    return myFrame


""" Otomatik olarak Keyborad Kotnrol Sağlama"""
def keyBoardInput(xyxy,im0):
    
    global takeLand
    if ( not takeLand):
        return im0
    firstDir,secondDir=int((int(xyxy[2])+int(xyxy[0]))/2),int((int(xyxy[3])+int(xyxy[1]))/2)
    # c1, c2 = (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3]))     
    detectimageShapeX,detectimageShapeY=(abs(int(xyxy[3])-int(xyxy[1])),abs(int(xyxy[2])-int(xyxy[0])))
    cv2.circle(im0,(firstDir,secondDir),5,(255,0,0),cv2.FILLED)
    cv2.line(im0,(firstDir,secondDir),(320,240),(255,0,0),2)
               
    speed=40
    lr,fb,ud,yv=0,0,0,0
    tresholdLeftRight=90
    
    
    
    """ kendi Etradında Sağa ve Sola Dönüş  """
    if(320-firstDir>tresholdLeftRight):
        print("Sola Dönüş")
        yv=-speed
       
        me.send_rc_control(lr,fb,ud,yv)
        time.sleep(0.5)
        print(firstDir,secondDir)

    if(firstDir-320>tresholdLeftRight):
        print("Sağa Dönüş")  
        yv=speed
        
        me.send_rc_control(lr,fb,ud,yv)
        time.sleep(0.5)
        print(firstDir,secondDir) 
        
        
        
    """ İleri Geri Haraket  """    
    if detectimageShapeX < 150 or detectimageShapeY <150:
        fb=speed
        # me.send_rc_control(lr,fb,ud,yv)
        time.sleep(0.05)
        print("Forwand")
    elif   detectimageShapeX > 250 or detectimageShapeY >250:   
        fb=-speed
        # me.send_rc_control(lr,fb,ud,yv)
        time.sleep(0.05)
        print("BackWard")        

    
    if  keyboard.is_pressed("z"):
        cv2.imwrite(f"./images/photoTello/{time.time()}.jpg",im0)
        time.sleep(0.3)   
        print("Take Photo") 
        
        
     
    lr,fb,ud,yv=0,0,0,0    
    me.send_rc_control(lr,fb,ud,yv)
        
    return(im0)  

""" Zorunlu Durumlarda Direk Keyborad Kontrol"""
def KeyBoardControl():
    speed=30
    lr,fb,ud,yv=0,0,0,0
    if keyboard.is_pressed("LEFT"): lr=-speed; print("Left")  
    elif  keyboard.is_pressed("RIGHT"): lr=speed; print("RIGHT")  
    
    if keyboard.is_pressed("UP"): fb=speed   ; print("UP")  
    elif  keyboard.is_pressed("DOWN"): fb=-speed  ; print("DOWN")  
          
    if keyboard.is_pressed("w"): ud=speed   ; print("w")  
    elif  keyboard.is_pressed("s"): ud=-speed ; print("s")  
    
    if keyboard.is_pressed("a"): yv=speed   ; print("a")  
    elif  keyboard.is_pressed("d"): yv=-speed   ; print("d")   
    global takeLand
    if(not takeLand):
        if keyboard.is_pressed("e"): 
            me.takeoff()
            
            takeLand=True   
            print("takeoff")
    
    
    else:                  
        if  keyboard.is_pressed("q"):
            me.land()   
            print("land")    
    
    me.send_rc_control(lr,fb,ud,yv)
    time.sleep(0.05) 
    
    return takeLand  
  

     
""" Person bulamadıgı zaman Kendi etrafıdan sola dogru dön"""
def keyBoardInputTurn(TurnLeft=None):
    lr,fb,ud,yv=0,0,0,0
    leftSp=50
    yv=-leftSp
    me.send_rc_control(lr,fb,ud,yv)
    print("Kendi Etrandında Dön")
    time.sleep(1)
    lr,fb,ud,yv=0,0,0,0    
    me.send_rc_control(lr,fb,ud,yv)
    time.sleep(0.5)
    





