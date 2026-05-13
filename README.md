# Automated-Helmet-Violation-Detection
Automated Helmet Violation Detection is a deep learning-based system that identifies motorcyclists without helmets using YOLOv11 and extracts license plate numbers using YOLOv8 and Tesseract OCR. It supports images, videos, and webcam input via a Streamlit web app for real-time traffic monitoring and enforcement.

# Project Workflow

The Automated Helmet Violation Detection System follows a structured pipeline from data collection to deployment. The complete workflow is described below:

# 1. Data Collection
Collected real-world traffic images and videos containing motorcyclists
Included various conditions:
Day and night scenes
Different camera angles
Multiple rider positions
Separate datasets prepared for:
Helmet detection
License plate detection
# 2. Data Annotation
Annotated images using tools like LabelImg / Roboflow
Bounding boxes created for:
Helmet
Non-helmet
Rider
Non-rider
License plate
Exported annotations in YOLO format
# 3. Data Preprocessing
Image resizing (e.g., 640×640 for YOLO)
Data augmentation applied:
Rotation
Brightness adjustment
Scaling
Flipping
Dataset split into:
Training set
Validation set
Test set
# 4. Model Development

Two models were used:

1. YOLOv11 Model
Detects:
Helmet
Non-helmet
Rider
Non-rider
License plate
2. YOLOv8 Model
Specialized for:
License plate detection
# 5. Model Training
Trained using Ultralytics YOLO framework
Key parameters:
Epochs: 100
Batch size: 16
Optimizer: AdamW
Loss functions:
Classification loss
Bounding box regression (CIoU)
# 6. Model Evaluation
Evaluated using:
Precision
Recall
mAP@50
mAP@50-95
Achieved high accuracy in:
Helmet detection
License plate recognition
# 7. Violation Detection Logic
Detect rider objects
Check if helmet is present
If non-helmet rider detected:
Trigger license plate detection
Apply filtering (IoU) to remove duplicates
# 8. License Plate Recognition (OCR)
Cropped license plate region
Used Tesseract OCR to extract text
Cleaned and formatted output
# 9. Application Development
Built using Streamlit
Features:
Image upload
Video upload
Live webcam detection
Displays:
Bounding boxes
Extracted license plate numbers
# 10. Deployment
Deployed as a Streamlit web application
Integrated components:
YOLOv11 model
YOLOv8 model
OCR engine
Outputs:
Real-time detection
CSV file with license plates
# 11. Output Generation
Detection results shown visually
License plate numbers displayed
Data stored in CSV format for further use

# Flow 
<img width="733" height="883" alt="image" src="https://github.com/user-attachments/assets/eb49309e-b228-463b-8fff-008822b13d9f" />

# Streamlit Interface
<img width="957" height="496" alt="image" src="https://github.com/user-attachments/assets/6c255d39-cdc4-4f14-8b86-f9a9cf537208" />

# Sample Outputs
<img width="311" height="311" alt="image" src="https://github.com/user-attachments/assets/0ceba710-6bfb-4235-823d-49b15418cb12" />
<img width="310" height="310" alt="image" src="https://github.com/user-attachments/assets/bc38d00e-8f75-415c-86f0-f82a6106ebb9" />
<img width="312" height="339" alt="image" src="https://github.com/user-attachments/assets/111acdf5-ccb2-4fa5-9650-223cd9f388e8" />

# Performance Evaluation
# Confusion Matrix

<img width="734" height="517" alt="image" src="https://github.com/user-attachments/assets/6499e20c-7ed7-471d-bd47-5c84d06bca30" />

# Precision-Confidence Curve 

<img width="831" height="538" alt="image" src="https://github.com/user-attachments/assets/749c2cee-2a43-47a5-acc7-1915a2f11cf2" />

# Precision-Recall Curve

<img width="868" height="579" alt="image" src="https://github.com/user-attachments/assets/e1b77c9c-4ffd-4b81-8fa6-36c3cc70bfcc" />

# F1- Confidence Curve 

<img width="930" height="620" alt="image" src="https://github.com/user-attachments/assets/9a71db18-ef3d-45e5-ba47-dbe72c7f53b1" />









