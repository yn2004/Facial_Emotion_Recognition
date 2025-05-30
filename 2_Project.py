import streamlit as st
import numpy as np
import cvlib as cv
import tensorflow as tf
import pandas as pd
import cv2
import json
import av
from tensorflow.keras.preprocessing.image import img_to_array
from streamlit_webrtc import webrtc_streamer
from PIL import Image
from streamlit_lottie import st_lottie
from deepface import DeepFace


st.set_page_config(layout='wide')
con1 = st.container()

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


#animation loading using pre defined function
ai = load_lottiefile("Animation files/ai.json")
file = load_lottiefile("Animation files/upload-files.json")
camera = load_lottiefile("Animation files/camera.json")
deep = load_lottiefile('Animation files/deep.json')
male = load_lottiefile('Animation files/MALE.json')
female = load_lottiefile('Animation files/FEMALE.json')
happy = load_lottiefile("Animation files/happy_face.json")
sad = load_lottiefile("Animation files/sad_face.json")
angry = load_lottiefile("Animation files/angry_face.json")
fear = load_lottiefile("Animation files/fear_face.json")
surprise = load_lottiefile("Animation files/surprise.json")
neutral = load_lottiefile("Animation files/neutral_face.json")


model = tf.keras.models.load_model('gender_detection.model')


choice = None
mode = None
image = None
emotio = []
classes = ['male', 'female']
person = []




def web_emotion_detection(frame):
    image_np = frame.to_ndarray(format="bgr24")
    #Detectes Faces
    faces, confidences = cv.detect_face(image_np)
    for idx, f in enumerate(faces):
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]
        #Crop the face
        face_img = image_np[startY:endY, startX:endX]
        #Detects Emotions of cropped face
        obj = DeepFace.analyze(face_img, actions=['emotion'], enforce_detection=False)
        emotions=(d["dominant_emotion"] for d in obj)
        #Draw rectangle over face
        cv2.rectangle(image_np, (startX,startY), (endX,endY), (0,255,0), 2)
        for i, emotion in enumerate(emotions):
            label = emotion
            #Keep text on Face
            cv2.putText(image_np, label, (startX, startY-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            
    return av.VideoFrame.from_ndarray(image_np, format="bgr24")

def object_detection(frame):
    image_np = frame.to_ndarray(format="bgr24")
    bbox, label, conf = cv.detect_common_objects(image_np)
    for i in range(len(bbox)):
        cv2.rectangle(image_np, (bbox[i][0], bbox[i][1]), (bbox[i][2], bbox[i][3]), (0, 255, 0), 2)

        text = f"{label[i]}: {conf[i]*100:.2f}%"
        cv2.putText(image_np, text, (bbox[i][0], bbox[i][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return av.VideoFrame.from_ndarray(image_np, format="bgr24")




def emotion_detection(image):
    if image is not None:
        o_image = Image.open(image)
        image_np = np.array(o_image)
        #Detectes Faces
        faces, confidences = cv.detect_face(image_np)
        for idx, f in enumerate(faces):
                (startX, startY) = f[0], f[1]
                (endX, endY) = f[2], f[3]
                 #Crop the face
                face_img = image_np[startY:endY, startX:endX]
                #Detects Emotions of cropped face
                obj = DeepFace.analyze(face_img, actions=['emotion'], enforce_detection=False)
                emotions=(d["dominant_emotion"] for d in obj)
                for i, emotion in enumerate(emotions):
                    emotio.append(emotion)
                    print(emotion)
                # draw rectangle around face
                rec = cv2.rectangle(image_np, (startX, startY), (endX, endY), (0,255,0), 2)
        return image_np

        
with st.sidebar:
        
    st.header("Experience the Power of Computer Vison")
    task1 = ["Emotion Detection","Object Detection"]
    choice = st.selectbox("Select option",task1)
    task2 = ['Image','Capture','Web-Cam']
    if choice == 'Object Detection':
        del task2[0:2]
    mode = st.radio('Select Mode',task2)
    if mode == 'Image':
        image = st.file_uploader('')
    
    
    
with con1:
    c1,c2,c3 = st.columns([1,3,1])
    with c2:
        text = choice
        title = f"""
        <div style='
            font-family: maiandra gd;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
        '>{text}
        </div>
        
        """
        st.markdown(title, unsafe_allow_html=True)

if mode=='Image' or mode == 'Capture':
    st.write("<br>","<br>",unsafe_allow_html=True)
    co1, co2, co3 = st.columns([3,3,3])
    
    
    with co1:
        if mode == 'Capture':
            text = 'Capture Image'
            title = f"""<div style='
                    font-family: monospace;
                    font-size: 25px;
                    font-weight: bold;'>{text}</div>"""
            st.markdown(title, unsafe_allow_html=True)
            image = st.camera_input("")

        else:
            if image is not None:
                text = 'Uploaded Image'
                title = f"""<div style='
                    font-family: monospace;
                    font-size: 25px;
                    font-weight: bold;'>{text}</div>"""
                st.markdown(title, unsafe_allow_html=True)
                st.write("<br>",unsafe_allow_html=True)
                st.image(image)
        with co2:
            if choice == 'Emotion Detection' :
                if image is not None:
                    image_np0 = emotion_detection(image)
                    text = 'Predicted Image'
                    title = f"""<div style='
                    font-family: monospace;
                    font-size: 25px;
                    font-weight: bold;'>{text}</div>"""
                    st.markdown(title, unsafe_allow_html=True)
                    st.write("<br>",unsafe_allow_html=True)
                    st.image(image_np0)
                    st.write("Detected Persons:", len(emotio))
                    if st.button("Predict"):
                        with co3:
                            if(len(emotio) == 1):
                                if(emotio[0]=='happy'):
                                    st_lottie(happy, speed=1, reverse=False, quality="low",loop=True, height=400)
                                elif(emotio[0]=='sad'):
                                    st_lottie(sad, speed=1, reverse=False, quality="low",loop=True, height=400)
                                elif(emotio[0]=='angry'):
                                    st_lottie(angry, speed=1, reverse=False, quality="low",loop=True, height=400)
                                elif(emotio[0]=='surprise'):
                                    st_lottie(surprise, speed=1, reverse=False, quality="low",loop=True, height=400)
                                elif(emotio[0]=='neutral'):
                                    st_lottie(neutral, speed=1, reverse=False, quality="low",loop=True, height=400)
                                elif(emotio[0]=='fear'):
                                    st_lottie(fear, speed=1, reverse=False, quality="low",loop=True, height=400)
                        
                            else:
                                st.write("<br>","<br>","<br>",unsafe_allow_html=True)
                                df = pd.DataFrame(columns=("Persons","emotions"))
                                for i in range(len(emotio)):
                                    var = "Person "+str((i+1))
                                    df.loc[len(df.index)] = [var,emotio[i]] 
                                st.table(df)
                else:

                    if mode == "Image":
                            st_lottie(file, speed=1, reverse=False, quality="low",loop=True, height=400)
                        
                    with co3:
                        if mode == "Capture":
                            st_lottie(camera, speed=1, reverse=False, quality="low",loop=True, height=400)

if mode == 'Web-Cam':
    c_1, c_2, c_3 = st.columns([1,3,1])
    with c_2:
        if choice == 'Emotion Detection':
            webrtc_streamer(key="example", video_frame_callback=web_emotion_detection)

        if choice == 'Object Detection':
            webrtc_streamer(key="example", video_frame_callback=object_detection)

