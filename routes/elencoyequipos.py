import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

credits_bp = Blueprint("elencoyequipos", __name__)

@credits_bp.route("/credits")
def credits():
    url = f"https://api.themoviedb.org/3/movie/550/credits?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    datos = response.json()
    cast = datos.get("cast")
    crew = datos.get("crew")
    return render_template("elencoyequipos.html", cast=cast, crew=crew)
