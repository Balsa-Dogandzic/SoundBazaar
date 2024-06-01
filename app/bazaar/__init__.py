from flask import Blueprint

bp = Blueprint('main', __name__)

from app.bazaar import common, login, songs