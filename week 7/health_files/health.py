# CREATE TABLE health_file(
# 	id SERIAL PRIMARY KEY,
# 	f_name  VARCHAR(50),
# 	l_name  VARCHAR(100),
# 	doctor  BOOL
	
# );


from flask import Flask
import psycopg2

health = Flask(__name__)

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'goldp613@gmail.com'
DATABASE = 'health_files'

@health.route('/', methods=['GET''POST'])
def health_file():
    if request.method == 'GET':
       return render_template('login.html')
    else:
        f_name = request.form.get('f_name')
		l_name = request.form.get('l_name')
        connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        query = f"SELECT doctor FROM health_file;"
        doctor = cursor.fetchall()
        connection.close()
        if doctor == True:
            return redirect(url_for('doctors'))
        elif doctor == False:
            return redirect(url_for('patients'))
        else:
            return 'Sorry, you do not have an account.'

@health.doctors('/doctors')
def doctors():
    render_template('doctors.html')



@health.patients('/patients')
def patients():
    render_template('patients.html')



if __name__ == "__main__":
    health.run(debug=True)

