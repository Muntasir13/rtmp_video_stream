from flask import Flask, render_template, Response
import secrets

from getStream import Stream

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe()

stream = Stream('rtmp://localhost:1935/live/test')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/rtmp_stream", methods=['GET'])
def rtmp_stream():
    return Response(stream.return_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host='0.0.0.0', port=5000, debug=True)