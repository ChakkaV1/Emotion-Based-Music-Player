# Emotion Based Music Player

## Overview 
An Emotion-Based Music Player Website uses facial recognition to detect a user's emotions in real-time. The application analyzes these emotions and plays songs that match the user's mood, creating a more enjoyable and personalized music experience.

## Product Features
1. Registration: Users can create an account with username, email, phone number, and password.
2. Login: Registered users can log in securely using their credentials.
3. Human Face Detection: The system detects and locates faces within an image using facial recognition.
4. Emotion Detection: Analyzes facial expressions to determine emotional state with machine learning models.
5. Music Player: Plays music based on the detected emotional state of the user.
6. Contact Page Feature: Users can send feedback or seek support via the contact page.
7. Features Page: Displays information about current and upcoming features of the system.
8. Team Info Page: Provides details about the development team.
9. Logout: Users securely log out, clearing authentication tokens.

## Built With
Flask: Web framework used to build the application and serve the interface.
OpenCV: Library for real-time facial recognition to detect user emotions.
Python-VLC: Library for playing and managing music based on detected emotions.
SQLAlchemy: ORM (Object-Relational Mapping) library for managing interactions with the database.
TensorFlow: Machine learning framework for training and implementing emotion detection models.

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



