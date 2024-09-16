import cv2
import face_recognition
import numpy as np
from PIL import Image


image_eddy = face_recognition.load_image_file("D:\Codes\ML\Images\my_pictureLR.jpg")
localisation = face_recognition.face_locations(image_eddy)
encode_eddy = face_recognition.face_encodings(image_eddy,localisation)
encodages_connus = [encode_eddy]
nom_connus = ["EDDY"]
video_capture = cv2.VideoCapture(0)

while True:

    ret , frame = video_capture.read()
    petite_image = cv2.resize(frame, (0, 0), fx = 0.25, fy = 0.25)
    rgb_petite_image = np.ascontiguousarray(petite_image[:, :, ::-1])
    localisations_visage = face_recognition.face_locations(rgb_petite_image)


    try:
        encodages_visage = face_recognition.face_encodings(rgb_petite_image,localisations_visage)[0]

    except IndexError:
        encodages_visage = []

    for encodage_visage,localisation_visage in zip(encodages_visage,localisations_visage):
        
        corespondances = face_recognition.compare_faces(encodages_connus,encodage_visage)
        nom = "inconue"

        if True in corespondances:
            index_corespondance = corespondances.index(True)
            nom = nom_connus[index_corespondance]

        haut,droite,bas,gauche = localisations_visage[0]

        haut,droite,bas,gauche = haut*4,droite*4,bas*4,gauche*4

        cv2.rectangle(frame,(gauche,haut), (droite, bas), (0, 255,0), 2)
        cv2.putText(frame, nom, (gauche, haut - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow("Reconnaissance faciale",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()