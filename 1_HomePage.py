import streamlit as st
import json
import base64


from PIL import Image
from streamlit_lottie import st_lottie

#Animation files load funcion
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

face = load_lottiefile("Animation files/face id.json")
app = load_lottiefile("Animation files/app.json")
face_rec = load_lottiefile("Animation files/face recognition.json")
ai1 = load_lottiefile("Animation files/ai (1).json")
ai2 = load_lottiefile("Animation files/ai (2).json")

st.set_page_config(layout='wide')

title = st.container()
info1 = st.container()
info2 = st.container()
info3 = st.container()
info4 = st.container()



text = None

with title:    
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    .heading {
        text-align: center;
    }
    
    </style>
    """,
    unsafe_allow_html=True
    )
        # Display the title with the "title" class
        st.markdown('<h1 class="title">FaceVision App</h1>', unsafe_allow_html=True)
        st.markdown('<h2 class="heading">Integrated with Animations</h2>',unsafe_allow_html=True)
       
with info1:
    st.write("<br>",unsafe_allow_html=True)
    st.write("<br>",unsafe_allow_html=True)
    c11,c22 = st.columns([3,1])
    with c11:

        st.markdown(
        """
        <style>
        .paragaph1{
        font-family: monospace; 
        font-size: 25px;
        
        }
        .highlight {
     
        font-weight: bold;
        }

        </style>
        """,
        unsafe_allow_html=True)
        st.markdown("<p class='paragaph1'>This project aims to develop a system that can perform <span class = 'highlight'>Real-time face emotion recognition,gender classification</span> and provide an animated output. The system will leverage state-of-the-art machine learning techniques and computer vision algorithms to accurately identify and analyze objects and facial features.</p>", unsafe_allow_html=True)
        with c22:
            st_lottie(face, speed=1, reverse=False, quality="low",loop=True, height=250)
                          
with info2:
    c_11,c_22 = st.columns([1,3])
    with c_22:

        st.markdown(
        """
        <style>
        .paragaph1{
        font-family: monospace; 
        font-size: 25px;
        
        }
        .highlight {
     
        font-weight: bold;
        }

        </style>
        """,
        unsafe_allow_html=True)
        st.markdown("<p class='paragaph1'>The App is designed to be user-friendly and accessible to a wide range of users. It could be used by <span class = 'highlight'>law enforcement agencies for identifying suspects, by marketers for analyzing customer emotions and behaviors, </span>or by individuals for analyzing their personal photos. The potential applications of this technology are endless, and we believe that it has the potential to revolutionize the way we interact with each other and the world around us.</p>",unsafe_allow_html=True)
        with c_11:
            st_lottie(app, speed=1, reverse=False, quality="low",loop=True, height=250)

with info3:
    st.write("<br>",unsafe_allow_html=True)
    st.write("<br>",unsafe_allow_html=True)
    st.markdown("""
        <style>
        .title2 {
            font-family: maiandra gd;
            text-align: left;
        }
        </style>
        """,
        unsafe_allow_html=True)
    st.markdown('<h2 class="title2">Algorithms used</h2>', unsafe_allow_html=True)
    co1, co2 = st.columns([3,1])

    with co1:
        title = "Computer Vision - cvlib"
        text = "Computer vision is an exciting field that has been rapidly advancing in recent years. It involves the use of algorithms and machine learning techniques to analyze and interpret visual data from the world around us. With the growing availability of high-quality cameras and sensors, there are now more opportunities than ever to apply computer vision techniques to a wide range of applications.In this project, we will be using CVlib, an open-source computer vision library for Python, to perform various computer vision tasks such as face detection, gender detection, and object detection. By using pre-trained models provided by CVlib, we can quickly and easily integrate computer vision functionality into our applications without the need for extensive training or development."


        html_code = f"""
<div style='
    background-color: #f2f2f2;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    font-family: Arial, sans-serif;
    font-size: 20px;
'>
    <h3>{title}</h3>
    <div style='
        font-family: monospace;
        font-size: 18px;
    '>
    {text}</div>
    </div>
        """

        st.markdown(html_code, unsafe_allow_html=True)
        with co2:
            st_lottie(ai2, speed=1, reverse=False, quality="low",loop=True, height=400)
            #st.image('image1.jpg')



with info4:
    st.write("<br>",unsafe_allow_html=True)
    co1, co2 = st.columns([1,3])

    with co2:
        title = "Deep Face - deepface"
        text = "DeepFace is a deep learning facial recognition algorithm developed by Facebook's Artificial Intelligence Research (FAIR) team. It uses a deep convolutional neural network (CNN) to analyze facial features and map them into a multidimensional space, where the distances between the vectors of different faces can be compared to determine similarity.The algorithm has achieved impressive results in benchmark tests, outperforming other state-of-the-art facial recognition systems. It can recognize faces with high accuracy even when they are partially occluded or viewed from different angles. In fact, DeepFace has an accuracy rate of 97.35% on the Labeled Faces in the Wild (LFW) dataset, which is considered to be one of the most challenging datasets for facial recognition."

        html_code = f"""
<div style='
    background-color: #f2f2f2;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    font-family: Arial, sans-serif;
    font-size: 20px;
'>
    <h3>{title}</h3>
    <div style='
        font-family: monospace;
        font-size: 18px;
    '>
    {text}</div>
    </div>
        """

        st.markdown(html_code, unsafe_allow_html=True)
        with co1:
            st_lottie(ai1, speed=1, reverse=False, quality="low",loop=True, height=400)

