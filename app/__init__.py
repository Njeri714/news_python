from flask import Flask
from .config import DevConfig

#  initializing app
app = Flask(__name__, instance_relative_config=True)

# setting configarations
app.config.from_object(DevConfig)

