from flask import Flask, render_template, redirect
import subprocess
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NGINX_TEMPLATE = os.path.join(BASE_DIR, "nginx_template.conf")
NGINX_CONFIG = os.path.join(BASE_DIR, "../nginx/nginx.conf")

def update_nginx(target_port):
    with open(NGINX_TEMPLATE, "r") as template:
        config = template.read().replace("{{TARGET_PORT}}", str(target_port))
    with open(NGINX_CONFIG, "w") as f:
        f.write(config)
    subprocess.run(["nginx", "-s", "reload"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/switch/<int:port>")
def switch(port):
    update_nginx(port)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
