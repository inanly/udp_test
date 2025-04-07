from flask import Flask, render_template, request, redirect
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form_data.db'
db = SQLAlchemy(app)

class FormSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    message = db.Column(db.String(200))

def create_app():
    db.init_app(app)
    return app

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        
        if not name or not email or not message:
            return 'Please fill out all fields'
        elif len(name) > 50 or len(email) > 50 or len(message) > 200:
            return 'Please limit input length to 50 characters for name and email, and 200 characters for message'
        elif '@' not in email or '.' not in email:
            return 'Please enter a valid email address'
        
        
        data = {'name': name, 'email': email, 'message': message}
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        
        submission = FormSubmission(name=name, email=email, message=message)
        db.session.add(submission)
        db.session.commit()
        
        return redirect('/thank-you')
    
    return render_template('form.html')

@app.route('/thank-you')
def thank_you():
    return 'Thank you for submitting the form!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
