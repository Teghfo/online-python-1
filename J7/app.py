from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
import logging

path = 'log/app.log'

logging.basicConfig(format="[ %(asctime)s ]: %(levelname)s: path: %(pathname)s - filename: %(filename)s - [%(funcName)s] line_number: %(lineno)d - message: %(message)s",
                    datefmt="%Y:%m:%d - %H:%M" ,filename=path ,level='WARNING')




##### log--->  DEBUG, INFO, WARNING, ERROR, CRITICAL



BASE_DIR = os.path.dirname(__file__)

app = Flask(__name__)


# route
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        number1 = int(request.form['num1'])
        number2 = int(request.form['num2'])
        oper = request.form['operation']

        if oper == '+':
            result = number1 + number2

        if oper == '-':
            result = number1 - number2

        if oper == '*':
            result = number1 * number2

        return render_template('index.html', result=result)


@app.route('/khoshumadi')
def welcome():
    return 'khosh umadi!'

@app.route('/10multiply', methods=['GET', 'POST'])
@app.route('/10multiply/<int:num>')
def mul(num=None):
    if request.method == 'POST':
        data = request.form['number']
        mult = int(data)* 10 
        return str(mult)
    if num:
        return str(num * 10)
    return 'adad nadadi'


@app.route('/upload', methods=['GET', 'POST'])
def uploading_file():
    if request.method == 'POST':
        try: 
            f = request.files['uploadedData']
            uploading_dir = os.path.join(BASE_DIR, 'upload')
            logging.info(f'user upload {f.filename}')
            f.save(uploading_dir + f'/{secure_filename(f.filename)}')
            return 'filet be khubi va khoshi upload shod boro be zendegit beres'
        except Exception as err:
            logging.error(f'user upload {f.filename} failed. {err}')

    films_list = ['shawsheng redem', 'interstellar', 'inception', 'seven', 'seperation', 'predestination', 'leon']
    return render_template('uploading.html', films_list=films_list)

@app.route('/api/filmList')
def film_list_api():
    films_list = ['shawsheng redem', 'interstellar', 'inception', 'seven', 'seperation', 'predestination', 'leon']
    return jsonify({'films': films_list})


if __name__ == '__main__':
    logging.info('hello logger')
    app.run(debug=True,host='localhost', port='5001')