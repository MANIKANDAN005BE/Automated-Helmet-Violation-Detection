import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pandas as pd
from ultralytics import YOLO
import easyocr
import tempfile
import os

# Set page config (MUST be first)
st.set_page_config(page_title="Helmet Violation Detection", layout="wide")

# Load YOLO model
model = YOLO("HelmetDetetlicenseplate_model.pt")
reader = easyocr.Reader(["en"])

# Class names (update if needed)
CLASSES = ["helmet", "non-helmet", "non-rider", "rider", "licence_plate"]

# Apply custom CSS
with open("custom_streamlit.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🚦 Non-Helmet Rider License Plate Detection")

# Radio for input option
option = st.radio("Choose an input type:", ["Image", "Video"])

# --------- Image Input Section ---------
if option == "Image":
    uploaded_image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("Processing... ⏳")

        img_array = np.array(image)
        results = model(img_array)[0]

        plate_texts = []
        for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
            x1, y1, x2, y2 = map(int, box)
            label = CLASSES[int(cls)]

            if label == "licence_plate":
                plate_crop = img_array[y1:y2, x1:x2]
                gray_plate = cv2.cvtColor(plate_crop, cv2.COLOR_BGR2GRAY)
                text = reader.readtext(gray_plate, detail=0)
                plate_texts.extend(text)

        st.image(results.plot(), use_column_width=True)

        if plate_texts:
            st.subheader("🔢 License Plates of Non-Helmet Riders:")
            df = pd.DataFrame({"License Plate": plate_texts})
            st.dataframe(df)
            df.to_csv("license_plates.csv", index=False)
            st.success("✅ CSV file saved as `license_plates.csv`")
        else:
            st.warning("No license plates detected for non-helmet riders.")

# --------- Video Input Section ---------
elif option == "Video":
    uploaded_video = st.file_uploader("Upload a video:", type=["mp4", "avi", "mov"])
    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        video_path = tfile.name

        st.video(video_path)
        st.write("Processing video... ⏳")

        cap = cv2.VideoCapture(video_path)
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out_path = "output_video.mp4"
        out = cv2.VideoWriter(out_path, fourcc, 20.0, (frame_width, frame_height))

        detected_plates = set()
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)[0]
            for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
                x1, y1, x2, y2 = map(int, box)
                label = CLASSES[int(cls)]

                if label == "licence_plate":
                    plate_crop = frame[y1:y2, x1:x2]
                    gray_plate = cv2.cvtColor(plate_crop, cv2.COLOR_BGR2GRAY)
                    text = reader.readtext(gray_plate, detail=0)
                    detected_plates.update(text)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 20, 147), 2)

            out.write(frame)

        cap.release()
        out.release()

        st.video(out_path)

        if detected_plates:
            st.subheader("🔢 License Plates of Non-Helmet Riders:")
            df = pd.DataFrame({"License Plate": list(detected_plates)})
            st.dataframe(df)
            df.to_csv("license_plates.csv", index=False)
            st.success("✅ CSV file saved as `license_plates.csv`")
        else:
            st.warning("No license plates detected for non-helmet riders.")
