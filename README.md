# Emotion Based Music Player

## Overview 
An Emotion-Based Music Player Website uses facial recognition to detect a user's emotions in real-time. The application analyzes these emotions and plays songs that match the user's mood, creating a more enjoyable and personalized music experience.

## Product Features
1. Registration: Users will be able to create a new account by providing necessary details such as username, email, phone number and password. 
2. Login: Registered users can securely log in to their accounts using their username/email and password. The system will authenticate their credentials and grant access to their
personalized profile.
3. Human Face Detection: Once the user logs in, the system will be capable of identifying and locating faces within a given image using advanced facial recognition technology.
4. Emotion Detection: Upon successful face detection, the system will proceed to analyze facial expressions such as eye movement, smiles, and frowns to accurately determine the
emotional state of the user. This analysis will be powered by machine learning models that are specifically trained for real-time emotion detection, ensuring precise and
responsive results.
5. Music Player: Once the user’s emotional state is detected, the system will automatically select music that matches their mood and play an appropriate song.
6. Contact Page Feature: Users will have the option to use the contact page to send feedback, report issues, or seek support regarding the system's functionalities.
7. Features Page: A dedicated page will showcase the features of both current and upcoming versions in a clear and informative manner, helping users understand the system's
capabilities.
8. Team Info Page: The system will include a dedicated team information page where users can access details about the development team behind the project.
9. Logout: Users will securely log out of their accounts, ensuring the clearance of authentication tokens to prevent unauthorized access.

## Built With
Flask: Web framework used to build the application and serve the interface.
OpenCV: Library for real-time facial recognition to detect user emotions.
Python-VLC: Library for playing and managing music based on detected emotions.
SQLAlchemy: ORM (Object-Relational Mapping) library for managing interactions with the database.
TensorFlow: Machine learning framework used for training and implementing emotion detection models.

## Getting Started
Follow these steps to get a copy of the project up and running on your local machine.

## Prerequisites
Python 3.6+   
A modern web browser (e.g., Chrome, Firefox, or Edge).

## Setup
```bash
Clone the Repository:
git clone https://github.com/ChakkaV1/TAX-TRACKING-FINAL-PROJECT.git
cd TAX-TRACKING-FINAL-PROJECT

Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install required Python packages:
■ pip3 install flask
■ pip3 install opencv-python
■ pip3 install numpy
■ pip3 install python-vlc
■ pip3 install Flask-SQLAlchemy
■ pip3 install Flask-Mail
■ pip3 install tensorflow
■ pip3 bcrypt
■ pip3 install tk

Run the Application:
python emotions.py

Access the Application:
Open your browser and go to http://127.0.0.1:5000.



