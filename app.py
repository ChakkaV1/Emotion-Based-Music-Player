from flask import Flask,request,redirect, render_template, session
from flask_mail import Mail
import os
import subprocess
# import emotions

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vyshnavi.chakka@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# def route(rule, **options):
#     def decorator(f):
#         app.add_url_rule(rule, f.__name__, f, **options)
#         return f
#     return decorator



# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/templates/index.html')
# def index1():
#     return render_template('index.html')

# @app.route('/templates/register.html')
# def register():
#     return render_template('register.html')

# @app.route('/templates/team_info.html')
# def team_info():
#     return render_template('team_info.html')

# @app.route('/templates/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/submit_contact_form', methods=['GET', 'POST'])
# def submit_contact_form():
#     if request.method == 'POST':
#         # Process the form data (send email, save to database, etc.)
#         # For now, just print it to the console
#         print(request.form)
#         # Redirect to the same page with a success message
#         flash('Message sent successfully!')
#         return redirect(url_for('contact'))
    
#     # No message on GET request, only shown after POST
#     return render_template('contact.html')
    
# @app.route('/start_detection', methods = ['GET', 'POST'])
# def start_detection():
#     return render_template('buttons.html')

# @app.route('/buttons', methods = ['GET','POST'])
# def buttons():
#     return render_template("buttons.html")

# @app.route('/templates/application.html')
# def application():
#     return render_template('application.html')



if __name__ == '__main__':
    app.run(debug=True)
