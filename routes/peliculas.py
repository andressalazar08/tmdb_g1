from flask import Flask, render_template, url_for, redirect, jsonify, Blueprint
import requests, json, os
from dotenv import load_dotenv


load_dotenv()
peliculas_bp = Blueprint("peliculas", __name__)

@peliculas_bp.route("/peliculas", methods=["GET", "POST"])
def peliculas():
    api_key = os.getenv("URL_KEY")
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=es-ES&page=1"
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
      data = response.json()
      peliculas = data['results']
      return render_template("cartelera.html", peliculas=peliculas )
    else:
       return jsonify({"error": "Error al obtener las películas"}), 500