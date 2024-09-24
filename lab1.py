import cv2

# cv2.WINDOW_NORMAL,cv2.WINDOW_AUTOSIZE cv2.WINDOW_FREERATIO
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# cv2.resizeWindow("Image", 500, 500)
cv2.setWindowTitle("Image","lagyshka")
cv2.moveWindow("Image", 0, 0)

# cv2.IMREAD_COLOR cv2.IMREAD_ANYDEPTH
image = cv2.imread('C:/Users/Stanislavsky/Pictures/liagushka_glaza_kamen_1204734_1920x1080.jpg', cv2.IMREAD_REDUCED_COLOR_8)


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
    

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()



# видео камера 
# def readIPWriteTOFile():
#     video = cv2.VideoCapture("rtsp://10.220.139.72:8080/h264_pcm.sdp")
#     ok, img = video.read()
#     w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
#     h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     video_writer = cv2.VideoWriter("output.avi", fourcc, 25, (w, h))
    
#     while (True):
#         ok, img = video.read()
        
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         cv2.imshow('img', gray)
#         if not ok:
#             print("Failed to grab frame")
#             break
        
#         # cv2.imshow('img', img)
#         video_writer.write(img)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
        
#     video.release()
#     cv2.destroyAllWindows()
    
# readIPWriteTOFile()