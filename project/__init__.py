from flask import Flask

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# import blueprints
from project.main.views import main_blueprint

app.register_blueprint(main_blueprint)
