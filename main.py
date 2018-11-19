from flask import Flask, request, redirect, render_template, session, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT= 465,
    MAIL_USE_SSL= True,
    MAIL_USERNAME= 'briantpt30@gmail.com',
    MAIL_PASSWORD='Casa1948'
)
mail = Mail(app)
app.secret_key = 'y337kGcys&zP3B' 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():

    if request.method == 'POST':
        sender = request.form['email']
        body = request.form['body']

        msg = Message(subject='test', recipients=['briantpt30@gmail.com'])
        msg.body = body
        mail.sender = sender
        mail.send(msg)

        return "Mail Sent"


    return render_template('contact.html')

@app.route('/images')
def images():
    return render_template('images.html')


if __name__ == '__main__':
    app.run()
