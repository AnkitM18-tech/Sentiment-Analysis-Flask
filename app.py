from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap
from textblob import TextBlob,Word
import random
import time

app = Flask(__name__)
Bootstrap(app)