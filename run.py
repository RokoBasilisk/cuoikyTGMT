import dlib
from time import time 
import cv2
import face_recognition
from matplotlib import pyplot as plt
import os
import numpy as np

hog_face_detector = dlib.get_frontal_face_detector()

path = "images"
images = []
classNames = []
mylist = os.listdir(path)
namelist = []
newpath = ""

for x in mylist:
    newpath = path+"/"+x
    namelist = os.listdir(newpath)
    for cl in namelist:
        curlImg = cv2.imread(f'{newpath}/{cl}') #get image from local
        images.append(curlImg) 
        data = [os.path.splitext(cl)[0],x]
        classNames.append(data) 

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
print('Encoding Complete')

def check(arr):
    count = False
    for num in arr:
        if num == True:
            count = True
    return count  

def hogDetectFaces(image, hog_face_detector, display = True):
    
    # Get the height and width of the input image.
    height, width, _ = image.shape
    
    # Create a copy of the input image to draw bounding boxes on.
    output_image = image.copy()
    
    # Convert the image from BGR into RGB format.
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Get the current time before performing face detection.
    
    start = time()
 
    # Perform the face detection on the image.
    results = hog_face_detector(imgRGB, 0)
    # Get the current time after performing face detection.
    end = time()
    locs = []
 
    # Loop through the bounding boxes of each face detected in the image.
    for bbox in results:
        
        # Retrieve the left most x-coordinate of the bounding box.
        x1 = bbox.left()
        
        # Retrieve the top most y-coordinate of the bounding box.
        y1 = bbox.top()
        
        # Retrieve the right most x-coordinate of the bounding box.
        x2 = bbox.right()
        
        # Retrieve the bottom most y-coordinate of the bounding box.       
        y2 = bbox.bottom()
 
        # Draw a rectangle around a face on the copy of the image using the retrieved coordinates.
        cv2.rectangle(output_image, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=width//200)
        location = [y1,x2,y2,x1]
        locs.append(location)

    encodesCurFrame = face_recognition.face_encodings(imgRGB, locs)
    for encodeFace,faceLoc in zip(encodesCurFrame,locs):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance= 0.5)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(matches)
        print(faceDis)
        Check = check(matches)
        if Check:
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                name = classNames[matchIndex][0].upper()
                ID = classNames[matchIndex][1]
                y1,x2,y2,x1 = faceLoc
                cv2.putText(output_image,name+":"+ID,(x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        else:
            y1,x2,y2,x1 = faceLoc
            cv2.putText(output_image,"Unknown",(x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    # Check if the original input image and the output image are specified to be displayed.
    if display:
        
        # Write the time take by face detection process on the output image. 
        cv2.putText(output_image, text='Time taken: '+str(round(end - start, 2))+' Seconds.', org=(10, 65),
                    fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=width//700, color=(0,0,255), thickness=width//500)
        
        # Display the original input image and the output image.
        plt.figure(figsize=[15,15])
        plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title("Original Image");plt.axis('off');
        plt.subplot(122);plt.imshow(output_image[:,:,::-1]);plt.title("Output");plt.axis('off');
        
    # Otherwise
    else:
        
        # Return the output image and results of face detection.
        return output_image, results, str(round(end - start, 2)), width
