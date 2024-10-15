import numpy as np
import cv2

def main():
    cap = cv2.VideoCapture("rtsp://10.78.42.62:8080/h264_pcm.sdp")

    while True:
        ret, frame = cap.read()
        
        if not ret: 
            print("Не удалось захватить кадр")
            break

        if cv2.waitKey(1) & 0xFF == 27:
            break
        
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_red_1 = np.array([0, 150, 100])    
        upper_red_1 = np.array([5, 255, 255])   

        lower_red_2 = np.array([175, 150, 100])  
        upper_red_2 = np.array([180, 255, 255])   

        mask1 = cv2.inRange(hsv_frame, lower_red_1, upper_red_1)
        mask2 = cv2.inRange(hsv_frame, lower_red_2, upper_red_2)
        red_mask = cv2.bitwise_or(mask1, mask2)  

        kernel = np.ones((5, 5), np.uint8)

        opening = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)  
        closing = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)  

        moments = cv2.moments(closing)

        if moments['m00'] > 0:
            area = moments['m00']
            cX = int(moments['m10'] / area)  
            cY = int(moments['m01'] / area) 
            
            x, y, w, h = cv2.boundingRect(closing)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2) 

            cv2.circle(frame, (cX, cY), 5, (255, 0, 0), -1)  

            cv2.putText(frame, f"Area: {int(area)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow('hsv_frame', hsv_frame) 
        cv2.imshow('red_mask', red_mask) 
        cv2.imshow('closing', closing)  
        cv2.imshow('main', frame)    
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
