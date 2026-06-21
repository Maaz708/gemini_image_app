#Image extracter

from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def get_response(input,image, prompt):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = [input, image, prompt]
        )

    return response.text 

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = types.Part.from_bytes(
            data = bytes_data,
            mime_type = uploaded_file.type
        )
        return image_parts
    else: 
        raise FileNotFoundError("No file uploaded")
    

st.set_page_config(page_title="Image Extraction")

st.header("Gemini Image App")

input = st.text_input("Input Prompt:",key = "input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image = ""

if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image, caption= "Uploaded Image.", width="stretch")

submit = st.button("Extract Information")

input_prompt ="""
    You are an expert in extracting information from images. 
    You will recieve input images and 
    you will have to answer questions based on the input image

    
"""

if submit:
    image_data= input_image_setup(uploaded_file)
    
    # st.write(type(image_data))
    
    response = get_response(input_prompt, image_data, input)

    st.subheader("The Response is: ")
    st.write(response)