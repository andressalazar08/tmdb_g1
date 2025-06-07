import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

estrenos_bp = Blueprint("estrenos", __name__)

@estrenos_bp.route("/estrenos")
def estrenos():
    url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=es-ES&page=1"
    response = requests.get(url)
    datos = response.json()["results"]
    return render_template("estrenos.html", datos=datos)