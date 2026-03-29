from flask import Flask, request
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Hello from my container!",
        "hostname": socket.gethostname(),
        "time": datetime.utcnow().isoformat(),
        "client_ip": request.remote_addr,
        "headers": dict(request.headers)
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)