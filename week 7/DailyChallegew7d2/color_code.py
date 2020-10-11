import json

from flask import Flask, render_template

code = Flask(__name__)

def load_database(src_file='colors_db.json'):
    with open(src_file, 'r') as file_obj:
        data = json.load(file_obj)
    return data

data = load_database()

@code.route('/main')
@code.route('/')
def main_page():
    return render_template('main.html', colors= data)

@code.route('/display_color/<color_name>')
def display_color(color_name):
    for color_dicts in data['colors']:
        if color_name == color_dicts['color']:
            return render_template('color_display.html',  color_dict= color_dicts)
    

if __name__== ("__main__"):
    code.run(debug=True)