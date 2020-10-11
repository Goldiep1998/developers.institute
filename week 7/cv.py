import flask

cv = flask.Flask(__name__)

@cv.route('/name')
def name():
    return '<h1>Goldie Perlmann</h1>'

@cv.route('/pic')
def pic():
    return 'picture'

@cv.route('/hobbies')
def hobbies():
    return '<p></p>'

@cv.route('/skills')
def skills():
    return '<p></p>'

if __name__ == "__main__":
    cv.run()