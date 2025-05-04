
# 🎯 Face Recognition Project

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=mslouma88.Face_Recognition&left_color=blue&right_color=green)

This project implements a complete face recognition system with logging, real-time detection, and smart face encoding.

## 📌 Features

- ✅ Real-time face detection and recognition via webcam  
- 🧠 Smart face encoding with duplicate management  
- 🗂️ Save known faces with automatic naming  
- 📝 Encoding logging (`encode_log.txt`)  
- 📋 Attendance logging in `recognition_log.csv`  
- 🔧 Customizable tolerance rate for better accuracy  
- 📦 Simple command-line interface  

## 🧰 Technologies Used

- [Python 3.8+](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [NumPy](https://numpy.org/)

## 🛠️ Installation

1. Clone the project:

```bash
git clone https://github.com/mslouma88/Face_Recognition.git
cd Face_Recognition
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # ou venv\\Scripts\\activate sous Windows
pip install -r requirements.txt
```

## 🚀 Usage
### Add a known face:

1. Add an image to the `known_faces/` directory with a filename that represents the identity (e.g., `salam.jpg`).

2. Run the encoding script:

```bash
python encode_faces.py
```

Results will be saved in:

- `face_encodings.pkl` (encoding database)

- `encode_log.txt` (encoding log)

## Start face recognition:

```bash
python recognize.py
```

Recognized faces will be saved in `recognition_log.csv` with the format:

```
timestamp,name

```

## 🗂️ Project Structure


```bash
face-recognition-project/
├── known_faces/             # Known face images (named by user)
├── encode_faces.py          # Encoding script with logs
├── recognize.py             # Main script with attendance logging
├── recognition_log.csv      # Recognition log
├── encode_log.txt           # Encoding log
├── requirements.txt
└── README.md
```

## 📜 License

This project is licensed under the MIT License. See the  [LICENSE](License) file for more details.

## 👤 Author
| 🔹 MEJRI Salam  [![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/salam-mejri/)  | [![GitHub](https://img.shields.io/badge/-GitHub-black?logo=github&logoColor=white)](https://github.com/mslouma88)  |
|:-------------------------------------------------------------:|:-------------------------------------------------------------:|
