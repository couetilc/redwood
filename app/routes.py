from flask import render_template
from app import application

@application.route('/')
@application.route('/index')
def index():
    return render_template('temp_index.html')

@application.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    application.run(debug=True)
