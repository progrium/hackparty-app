from flask import Flask
import settings

app = Flask('application')
app.config.from_object('application.settings')

import views