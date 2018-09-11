from flask import Blueprint

hod = Blueprint('hod', __name__)

from . import views