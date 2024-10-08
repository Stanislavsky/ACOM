import cv2
import os

import numpy as np

def videoAndPicture():
    # cv2.WINDOW_NORMAL,cv2.WINDOW_AUTOSIZE cv2.WINDOW_FREERATIO
    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('HSV Image', cv2.WINDOW_NORMAL)

    # cv2.IMREAD_COLOR cv2.IMREAD_ANYDEPTH
    image = cv2.imread('C:/Users/Stanislavsky/Pictures/liagushka_glaza_kamen_1204734_1920x1080.jpg', cv2.IMREAD_REDUCED_COLOR_8)


    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    cv2.imshow('Original Image', image)


    cv2.imshow('HSV Image', hsvImage)


    cv2.resizeWindow('Original Image', 800, 600)  
    cv2.resizeWindow('HSV Image', 800, 600)     


    cv2.waitKey(0)


    cv2.destroyAllWindows()



    cap = cv2.VideoCapture('C:/Users/Stanislavsky/Downloads/rutube/1940.mp4', cv2.CAP_ANY)


    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()
        
    
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)


    video_width = 840  
    video_height = 480  
    cv2.resizeWindow('Video', video_width, video_height)


    while True:
        
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (video_width, video_height))

        if not(ret):
            break
        
        # cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff == 27:
            break
        
        cv2.imshow('Video', resized_frame)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cap.release()

def readIPWriteTOFile():
    video = cv2.VideoCapture("rtsp://10.22.255.232:8080/h264_pcm.sdp")
    
    if not video.isOpened():
        print("Не удалось подключиться к видеопотоку")
        return

    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_size = (frame_width - 200, frame_height - 200)
    fps = 20
    
    

    
    output_path = 'C:/Users/Stanislavsky/DigitalMultiprocessingAlgorithms/output.avi'

    
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

   
    try:
        output = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, frame_size)
    except:
        print("error")
    
    if not output.isOpened():
        print(f"Не удалось открыть файл для записи видео: {output_path}")
        return

    while True:
        ret, frame = video.read()
        
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('gray', gray)
        
        center_x = 600
        center_y = 100
        
        color = (0, 0, 255) 
        thickness = 2 

      
        cv2.line(frame, (200 + center_x, 200 + center_y), (300 + center_x, 200 + center_y), color, thickness)
        cv2.line(frame, (300 + center_x, 200 + center_y), (300 + center_x, 400 + center_y), color, thickness)
        cv2.line(frame, (200 + center_x, 200 + center_y), (200 + center_x, 400 + center_y), color, thickness)
        
        cv2.line(frame, (0 + center_x, 400 + center_y), (500 + center_x, 400 + center_y), color, thickness)
        cv2.line(frame, (500 + center_x, 400 + center_y), (500 + center_x, 500 + center_y), color, thickness)
        cv2.line(frame, (500 + center_x, 500 + center_y), (0 + center_x, 500 + center_y), color, thickness)
        cv2.line(frame, (0 + center_x, 500 + center_y), (0 + center_x, 400 + center_y), color, thickness)
        
        cv2.line(frame, (300 + center_x, 500 + center_y), (300 + center_x, 700 + center_y), color, thickness)
        cv2.line(frame, (300 + center_x, 700 + center_y), (200 + center_x, 700 + center_y), color, thickness)
        cv2.line(frame, (200 + center_x, 700 + center_y), (200 + center_x, 500 + center_y), color, thickness)
        
        
        pts = np.array([[0 + center_x, 400 + center_y], 
                        [500 + center_x, 400 + center_y], 
                        [500 + center_x, 500 + center_y], 
                        [0 + center_x, 500 + center_y]], np.int32)

       
        fill_color = (0, 255, 0) 
        cv2.fillPoly(frame, [pts], fill_color)
        
        
        cv2.imshow('img', gray)

        
        output.write(frame)
        
        
        if cv2.waitKey(1) == ord('q'):
            break

   
    video.release()
    output.release()
    cv2.destroyAllWindows()



# videoAndPicture()
# readIPWriteTOFile()