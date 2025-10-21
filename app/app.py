from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='static')

# Load environment variables
BLUE_PORT = int(os.getenv('BLUE_PORT', 5051))
GREEN_PORT = int(os.getenv('GREEN_PORT', 5052))
NGINX_CONFIG_PATH = os.getenv('NGINX_CONFIG_PATH', '/etc/nginx/templates/default.conf.template')
NGINX_RELOAD_CMD = os.getenv('NGINX_RELOAD_CMD', 'nginx -s reload')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/switch/<int:port>', methods=['GET'])
def switch(port):
    if port not in [BLUE_PORT, GREEN_PORT]:
        return jsonify({'error': 'Invalid port'}), 400

    config = f"""
    server {{
        listen 5000;
        location / {{
            proxy_pass http://localhost:{port};
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }}
    }}
    """

    with open(NGINX_CONFIG_PATH, 'w') as f:
        f.write(config)

    os.system(NGINX_RELOAD_CMD)
    return jsonify({'message': f'Switched to port {port}'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('FLASK_PORT', 8000)))
