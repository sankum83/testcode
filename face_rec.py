
import face_recognition as fr
import os
import cv2

KNOWN_FACES_DIR = "known_face"
UNKNOWN_FACES_DIR = "unknown_face"
TOLERANCE = 0.6
FRAME_THICKENESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"

print("loading known faces")

known_faces = []
known_names = []

for name in os.listdir(KNOWN_FACES_DIR):
    print(name)
    for filename in os.listdir("{KNOWN_FACES_DIR}/{name}"):
         image = fr.load_image_file("{KNOWN_FACE_DIR}/{name}/{filename}")
        encoding = fr.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)


print("Processing Unknow Faces")
for filename in os.listdir(UNKNOWN_FACES_DIR):
    print(filename)
    image = fr.load_image_file("{UNKNOWN_FACES_DIR}/{filename}")
    locations = fr.face_locaions(image, model = MODEL)
    encoding = fr.face_encoding(image, locations)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    for face_encoding, face_location in zip(encodings ,locations):
        results = fr.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]
            print("Match Found:{match}")
            

            top_left = (face_location[3],face_location[2])
            botton_right = (face_location[1],face_location[2]+22)

#            color = [0,255,0]
            cv2.rectangle(image,top_left,botton_rigth, color, cv2.FILLED)
            cv2.putTex(image, match, (face_location[3]+10,face_location[2]+15,cv2.FONTHERSHEY_SIMPLEX,0.5,(200,200,200),FONT_THICKNESS))

    cv2.imshow(filename, image)
    cv2.waitKey(1000)




