from flask import Flask, render_template, request, jsonify
import threading
import time
import os

app = Flask(__name__)

running = False

def beep():
    os.system("powershell -Command '(New-Object Media.SoundPlayer "
              "'C:\\Windows\\Media\\tada.wav').PlaySync()'")

def run_timer(minutes, seconds):
    global running
    for i in range(minutes * 60 + seconds, 0, -1):
        if not running:
            break
        mins, secs = divmod(i, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        label.config(text=time_str)
        root.update_idletasks()
        time.sleep(1)
    else:
        label.config(text="00:00")
        # Play the beep sound
        beep_sound.play()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_timer', methods=['POST'])
def start_timer():
    global running
    running = True
    minutes = int(request.form['minutes'])
    seconds = int(request.form['seconds'])
    threading.Thread(target=run_timer, args=(minutes, seconds)).start()
    return jsonify({'status': 'ok'})

@app.route('/stop_timer', methods=['POST'])
def stop_timer():
    global running
    running = False
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)