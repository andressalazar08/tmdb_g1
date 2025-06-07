import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

series_bp = Blueprint("series", __name__)

@series_bp.route("/series")
def series():
    url = f"https://api.themoviedb.org/3/tv/popular?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    datos = response.json()["results"]
    return render_template("d_series.html", datos=datos)