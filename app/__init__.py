import os
from flask import Flask #, jsonify, request, redirect, render_template, url_for
app = Flask(__name__)

from app import routes

if __name__ == '__main__':
    app.run()
