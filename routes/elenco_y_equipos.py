import os
import requests
from flask import Blueprint, render_template,request
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

credits_bp = Blueprint("elencoyequipos", __name__)

@credits_bp.route("/credits/<int:movie_id>")
def credits(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        return render_template("elenco y equipos.html", cast=data.get("cast", []), crew=data.get("crew", []))
    return "Error", response.status_code


