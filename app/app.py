from flask import Flask
from resources.user_resource import user_bp

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
