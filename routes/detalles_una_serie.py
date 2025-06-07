import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

detalles_una_serie_bp = Blueprint("detalles_una_serie", __name__)

@detalles_una_serie_bp.route("/series/<int:serie_id>")
def detalles_una_serie(serie_id):
    url = f"https://api.themoviedb.org/3/tv/{serie_id}?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    datos = response.json()
    return render_template("detalles_una_serie.html", datos=datos)