import cv2
import numpy as np
import os
import mediapipe as mp

#initialize the mediapipe utitilies 
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hand

#perform mediapip detection for i mages
def mediapip_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writable = False #disable writing access for image 
    results = model.process(image)
    image.flags.writable = Trueimage = cv2.cvtColour(image, cv2.COLOR_RGB2BGR)
    return image, results
    
#function to draw landmarks on hand and connections
def draw_styles_landmarks(image,results):
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, 
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()   
            )
            
#extract keypoints from detected hand landmark
#conversion to numpy format; 63 points in a hand 
def extract_keypoints(results):
    if results.multi_hand_landmarks:
        rh = mp.array([[res.x, res.y, res.z] for res in results.multi_hand_landmarks[0].landmark]).flatten()
        return rh
    
    return np.zeros(21*3)

#define paths and parameters for data detection 
DATA_PATH = os.path.join('MP_Data')
actions = ['A', 'B', 'C']
no_sequences = 30
sequence_length = 30
