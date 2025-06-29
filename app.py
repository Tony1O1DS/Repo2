import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.title("📝 Text Extractor")
st.write("Upload up to two images to extract text side by side.")

# Initialize reader once
reader = easyocr.Reader(['en'])

col1, col2 = st.columns(2)

with col1:
    uploaded_file1 = st.file_uploader("Upload Image 1", type=["png", "jpg", "jpeg"])

    if uploaded_file1 is not None:
        image1 = Image.open(uploaded_file1)
        st.image(image1, caption='Uploaded Image 1', use_container_width=True)

        with st.spinner('Reading...'):
            result1 = reader.readtext(np.array(image1), detail=0)
            text1 = '\n'.join(result1)

        st.subheader("Extracted Text from Image 1:")
        st.text_area("", text1, height=300)

with col2:
    uploaded_file2 = st.file_uploader("Upload Image 2", type=["png", "jpg", "jpeg"])

    if uploaded_file2 is not None:
        image2 = Image.open(uploaded_file2)
        st.image(image2, caption='Uploaded Image 2', use_container_width=True)

        with st.spinner('Reading...'):
            result2 = reader.readtext(np.array(image2), detail=0)
            text2 = '\n'.join(result2)

        st.subheader("Extracted Text from Image 2:")
        st.text_area("", text2, height=300)
