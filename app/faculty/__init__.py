from flask import Blueprint

faculty = Blueprint('faculty', __name__)

from . import views