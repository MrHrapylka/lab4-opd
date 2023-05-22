from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    shape = request.form['shape']
    precision = int(request.form['precision'])

    if shape == 'cube':
        side = float(request.form['side'])
        if precision == 0:
            volume = int(side ** 3)
        else:
            volume = round(side ** 3, precision)
    elif shape == 'sphere':
        radius = float(request.form['radius'])
        if precision == 0:
            volume = int((4 / 3) * 3.14159 * radius ** 3)
        else:
            volume = round((4 / 3) * 3.14159 * radius ** 3, precision)
    elif shape == 'cylinder':
        radius = float(request.form['radius'])
        height = float(request.form['height'])
        if precision == 0:
            volume = int(3.14159 * radius ** 2 * height)
        else:
            volume = round(3.14159 * radius ** 2 * height, precision)
    elif shape == 'cone':
        radius = float(request.form['radius'])
        height = float(request.form['height'])
        if precision == 0:
            volume = int((1 / 3) * 3.14159 * radius ** 2 * height)
        else:
            volume = round((1 / 3) * 3.14159 * radius ** 2 * height, precision)
    elif shape == 'pyramid':
        base_length = float(request.form['base_length'])
        base_width = float(request.form['base_width'])
        height = float(request.form['height'])
        if precision == 0:
            volume = int((1 / 3) * base_length * base_width * height)
        else:
            volume = round((1 / 3) * base_length * base_width * height, precision)
    else:
        volume = None

    return render_template('index.html', volume=volume)


if __name__ == '__main__':
    app.run(debug=True)
