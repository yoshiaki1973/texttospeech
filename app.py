from flask import Flask, render_template, request, redirect, url_for
import pathlib
import gtts
import os

app = Flask(__name__, static_folder='./mp3')
#app = Flask(__name__)

@app.route('/')
def top():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    a = request.form['text']
    tts = gtts.gTTS(a, lang="ja")
    title = "sound.mp3"
    tts.save( "./mp3/{0}".format(title))
    return render_template('done.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), threaded=True)
