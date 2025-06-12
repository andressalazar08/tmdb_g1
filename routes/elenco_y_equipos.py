import os
import requests
from flask import Blueprint, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

credits_bp = Blueprint("elencoyequipos", __name__)

@credits_bp.route("/credits", methods=["GET", "POST"])
def search_form():
    if request.method == "POST":
        movie_id = request.form.get("movie_id")
        if movie_id and movie_id.isdigit():
            return redirect(url_for("elencoyequipos.credits", movie_id=movie_id))
    return render_template("elenco_y_equipos.html", cast=[], crew=[], show_form=True)

@credits_bp.route("/credits/<int:movie_id>")
def credits(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        cast = data.get("cast", [])
        crew = data.get("crew", [])
        return render_template(
            "elenco_y_equipos.html",
            cast=cast,
            crew=crew,
            show_form=True,
            cast_count=len(cast),
            crew_count=len(crew)
        )
    return "Error", response.status_code
