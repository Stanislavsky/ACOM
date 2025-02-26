import cv2


def Cam():
    input_video = cv2.VideoCapture(r'C:\Users\Stanislavsky\Videos\Captures\123.mp4')

    width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = input_video.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    output_video = cv2.VideoWriter(r'C:\Users\Stanislavsky\Videos\Captures\123.mp4', fourcc, fps, (width, height))
    ret, frame = input_video.read()

    gaus = cv2.GaussianBlur(frame, (15, 15), 1)
    bin  = cv2.cvtColor(gaus, cv2.COLOR_BGR2GRAY)

    while True:
        ret,frame = input_video.read()
        if not ret:
            break

        gaus2fr = cv2.GaussianBlur(frame, (15, 15), 1)
        bin2 = cv2.cvtColor(gaus2fr, cv2.COLOR_BGR2GRAY)

        # Сравнение гауссовских кадров
        frame_diff = cv2.absdiff(bin2, bin)
        _, threshFrame = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)

        cont,_ = cv2.findContours(threshFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        Flag = False

        for conturs in cont:

            print(cv2.contourArea(conturs))
            if cv2.contourArea(conturs) > 400:
                Flag = True
                break

        if Flag == True:
            output_video.write(frame)
            cv2.imshow("Output", frame)

        cv2.imshow("Video",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        bin = bin2

    input_video.release()
    output_video.release()
    cv2.destroyAllWindows()


Cam()