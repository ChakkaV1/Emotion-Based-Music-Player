from flask import Flask, render_template, request,flash, redirect, url_for, session
from flask_mail import Mail, Message as FlaskMessage
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
import os
import vlc
import time
from pathlib import Path
from random import randint
from subprocess import call
from tkinter import *
import statistics as st
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import bcrypt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4'


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'vyshnavi.kantheti97@gmail.com'
app.config['MAIL_PASSWORD'] = 'kpaz zbbt ajcv ekbj'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

app.secret_key = '12345678'
text = ""

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

#music player function
def music_player(emotion_str):
    from musicplayer import MusicPlayer
    root = Tk()
    print('\nPlaying ' + emotion_str + ' songs')
    MusicPlayer(root,emotion_str)
    root.mainloop()
    
@app.route('/music')
def music():
    text = request.args.get('final_output')  
    music_player(text)
    return redirect('/home')

# Create the model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(6, activation='softmax'))
model.load_weights('model_complete1.h5')

# dictionary which assigns each label an emotion (alphabetical order)
# emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Happy", 3: "Neutral", 4: "Sad", 5: "Surprised"}
# emotion_dict = {0: "Angry", 1: "Happy", 2: "Neutral", 3: "Sad", 4: "Surprised"}

# Function to display timer and emotions on video frame
def display_info(frame, timer_text, emotion_text):
    # Check if emotion is recognized, otherwise display an error message
    print(emotion_text)
    if not emotion_text or emotion_text not in emotion_dict.values():
        error_text = "Emotion not recognized. Please clarify."
        cv2.putText(frame, error_text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, timer_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    return frame

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    phone = db.Column(db.String(20))

    def __init__(self,email,password,name,phone):
        self.name = name
        self.email = email        
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.phone = phone
            
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def index1():
    return render_template('home.html')

@app.route('/team_info')
def team_info():
    return render_template('team_info.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
     try:
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/home')
        elif user is None:
            error_msg = 'Email ID is not registered. Please use a registered email ID'
        elif not is_valid_password(password):
            error_msg = 'Password should be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.'
        else:
            error_msg = 'Incorrect username or password'
            
        return render_template('login.html',error=error_msg)
     except SQLAlchemyError as e:
            # Handle specific database-related errors
            return render_template('login.html', error_message='Database error: ' + str(e))
     except Exception as e:
            # Handle other unexpected errors
            return render_template('login.html', error_message='An unexpected error occurred: ' + str(e))
            
    return render_template('login.html', error=session.pop('error', None))

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password'] 
        confirmpwd = request.form['confirmpwd'] 

        # Checks if email already exists in the database
        if User.query.filter_by(email=email).first():
            return render_template('register.html', error='This email id is already registered. Please log in or use a different email id to register.') 
        elif User.query.filter_by(phone=phone).first():
            return render_template('register.html', error='This phone number is already registered. Please use a different phone number to register.') 
        # Checks if mobile number is exactly 10 digits
        elif not phone.isdigit():
           return render_template('register.html', error='Mobile numbers must be numeric.')  
        # Checks if mobile number is exactly 10 digits       
        elif len(phone) != 10:        
           return render_template('register.html', error='Kindly enter a 10 digit mobile number.')  
        elif not is_valid_password(password):
           return render_template('register.html',error='Password should be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.')  
        # Checks if passwords match
        elif password != confirmpwd:
            return render_template('register.html',error='Password and confirm password are not matching.')
               
        new_user = User(name=name,email=email,phone=phone,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/home')
    return render_template('register.html')

def is_valid_password(password):
    # Check password length and character requirements
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in password):
        return False

    return True

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact_form', methods=['GET', 'POST'])
def submit_contact_form():
    if request.method == 'POST':
        msg = FlaskMessage("Query", sender='vyshnavi.kantheti97@gmail.com',
                            recipients=['vyshnavi.kantheti97@gmail.com'])
        msg.body = request.form['message']
        email = request.form['email']       

        # Check if the email exists in the User table
        user = User.query.filter_by(email=email).first()

        if user:
            # Email exists, we can proceed with sending the email
            mail.send(msg)
            flash('Message sent successfully!')        
            return redirect(url_for('contact'))   
        else:
            # Email does not exist in the User table
            return render_template('contact.html', error='Email not registered. Please enter a valid email.') 
         
    # No message on GET request, only shown after POST
    return render_template('contact.html')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/features')
def application():
    return render_template('features.html')

@app.route('/start_detection', methods = ['GET','POST'])
def start_detection():
    global text, final_emotion
    cap = cv2.VideoCapture(0)
    now = time.time()
    future = now + 10  # Detect emotions for 10 seconds
    emotion_file = open(str(Path.cwd()) + r"\emotion.txt", "w")
    camera_on = True

    while camera_on:
        ret, frame = cap.read()
        if not ret:
            break
        facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facecasc.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
            prediction = model.predict(cropped_img)
            maxindex = int(np.argmax(prediction))
            cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            text = emotion_dict[maxindex]           
            emotion_file.write(emotion_dict[maxindex]+"\n")
            emotion_file.flush()
        
        # Calculate remaining time for the timer
        remaining_time = max(0, int(future - time.time()))
        timer_text = f"Time left: {remaining_time} sec"
        print(text)
        frame = display_info(frame, timer_text, text)

        cv2.imshow('Video', cv2.resize(frame,(1600,960),interpolation = cv2.INTER_CUBIC))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 

        if time.time() >= future:  ##after 10 second music will play
            cv2.destroyAllWindows()
            camera_on = False
            # music_player(text)  
            future = time.time() + 10
           
    cap.release()
    emotion_file.close()
    cv2.destroyAllWindows()
    print(text)
    return render_template("buttons.html", final_output=text)
    

# @app.route('/buttons', methods = ['GET','POST'])
# def buttons():
#     return render_template("buttons.html")

if __name__ == '__main__':
    app.run(debug=True)

