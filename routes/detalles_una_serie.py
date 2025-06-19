import os
import requests
from flask import Blueprint, render_template, request, url_for, redirect
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

detalles_una_serie_bp = Blueprint("detalles_una_serie", __name__)
detalles_una_serie_buscar_bp = Blueprint("detalles_una_serie_buscar", __name__)

@detalles_una_serie_buscar_bp.route("/serie", methods=["GET", "POST"])
def detalles_una_serie_buscar():
    if request.method=="POST":
        serie_id = request.form.get("Buscar") 
        if serie_id:
           return redirect(url_for("detalles_una_serie.detalles_una_serie", serie_id=serie_id))
    return render_template("detalles_buscar_una_serie.html")

@detalles_una_serie_bp.route("/serie/<int:serie_id>")
def detalles_una_serie(serie_id):
    url = f"https://api.themoviedb.org/3/tv/{serie_id}?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    response.status_code
    datos = response.json()
    return render_template("detalles_una_serie.html", datos=datos)