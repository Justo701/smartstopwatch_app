from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

start_time = 0
distance = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    global start_time
    start_time = time.time()
    return jsonify({'status': 'success'})

@app.route('/stop', methods=['POST'])
def stop():
    global start_time, distance
    end_time = time.time()
    elapsed_time = end_time - start_time
    speed = calculate_speed(elapsed_time, distance)
    return jsonify({'status': 'success', 'time': elapsed_time, 'speed': speed})

@app.route('/set_distance', methods=['POST'])
def set_distance():
    global distance
    distance = float(request.form['distance'])
    return jsonify({'status': 'success'})

def calculate_speed(time, distance):
    return distance / time

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
