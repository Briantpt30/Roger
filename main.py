from flask import Flask, request, redirect, render_template, session, flash


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/images')
def images():
    return render_template('images.html')


if __name__ == '__main__':
    app.run()
