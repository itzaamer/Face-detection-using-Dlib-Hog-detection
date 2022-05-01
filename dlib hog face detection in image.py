import cv2
import dlib
def face_detection(image,model):
        #converting to gray image for faster processing
        grey_image = cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)
        #detect face function and it's give points value of rectnagle in the class '_dlib_pybind11.rectangles' 
        results = hog_face_detector(grey_image, 0)
        print("Number of faces detected: {}".format(len(results)))
        print(results)
        # Loop through each face detected in the image.
        for bbox in results:
                x1 = bbox.left()
                y1 = bbox.top()
                x2 = bbox.right()
                y2 = bbox.bottom()
                print(x1,y1,x2,y2)
                # Draw bounding box around the face on the copy of the input image using the retrieved coordinates.
                cv2.rectangle(input_image, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=3)
        image_resize = cv2.resize(input_image,(int(input_image.shape[1]/2),int(input_image.shape[0]/2)))
        cv2.imshow('Detected faces', image_resize) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()
#creating hob face detctor object
hog_face_detector = dlib.get_frontal_face_detector()
#load the image
input_image = cv2.imread(r"C:\Users\user\Desktop\AAmer works\test1.jpg")
face_detection(input_image,hog_face_detector)
