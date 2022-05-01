import cv2
import dlib
def facedetection(video_source,hog_face):
    
    while True:
        # Capture frame-by-frame
        check,frame = video_cascade.read()
        #converting to gray image for faster video processing
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #detect face function and it's give points value of rectnagle in the class '_dlib_pybind11.rectangles' 
        rect_face = hog_face_detector(gray_img, 0)
        # Loop through each face detected in the image.
        for bbox in rect_face:
            x1 = bbox.left()
            y1 = bbox.top()
            x2 = bbox.right()
            y2 = bbox.bottom()
            # Draw bounding box around the face on the copy of the input image using the retrieved coordinates.
            cv2.rectangle(frame, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=3)
        # Display the resulting frame
        cv2.imshow('Face Detection', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video_cascade.release()
    cv2.destroyAllWindows()

#creating hob face detctor object
hog_face_detector = dlib.get_frontal_face_detector()

#video path if it is webcam then give how much web cam 0,1,2,3 or if it video path then give video path in it.
video_cascade = cv2.VideoCapture(0)

#calling function.
facedetection(video_cascade,hog_face_detector)

