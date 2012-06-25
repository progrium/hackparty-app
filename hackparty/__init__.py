from flask import Flask
import settings

app = Flask('hackparty')
app.config.from_object('hackparty.settings')

import views
