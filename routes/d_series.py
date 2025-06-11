import os
import requests
from flask import Blueprint, render_template, request
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

#BUSCADOR 

@series_bp.route("/buscar_series")
def buscar_series():
    query = request.args.get("query")
    if not query:
        return render_template("d_series.html", datos=[])
    
    url = f"https://api.themoviedb.org/3/search/tv?api_key={API_KEY}&language=es-ES&query={query}"
    response = requests.get(url)
    datos = response.json().get("results", [])
    return render_template("d_series.html", datos=datos)



#serie por proveedor

@series_bp.route("/series_por_proveedor")
def series_por_proveedor():
    provider = request.args.get("provider", "")
    page = request.args.get("page", 1)
    region = "CO"

    url = f"https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=es-ES&watch_region={region}&with_watch_providers={provider}&page={page}"
    response = requests.get(url)
    datos = response.json().get("results", [])
    return {"results": datos}




#SERIE POR GENERO

@series_bp.route("/series_por_genero")
def series_por_genero():
    genre_id = request.args.get("genre", "")
    page = request.args.get("page", 1)
    region = "CO"

    url = f"https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=es-ES&with_genres={genre_id}&watch_region={region}&page={page}"
    response = requests.get(url)
    datos = response.json().get("results", [])
    return {"results": datos}



#MENU- POPULARES

@series_bp.route("/series_populares")
def series_populares():
    page = request.args.get("page", 1)
    url = f"https://api.themoviedb.org/3/tv/popular?api_key={API_KEY}&page={page}"
    response = requests.get(url)
    datos = response.json().get("results", [])
    return {"results": datos}

@series_bp.route("/series_transmitiendo")
def series_transmitiendo():
    page = request.args.get("page", 1)
    url = f"https://api.themoviedb.org/3/tv/on_the_air?api_key={API_KEY}&page={page}"
    response = requests.get(url)
    datos = response.json().get("results", [])
    return {"results": datos}

@series_bp.route("/series_en_tv")
def series_en_tv():
    page = request.args.get("page", 1)
    url = f"https://api.themoviedb.org/3/tv/airing_today?api_key={API_KEY}&page={page}"
    response = requests.get(url)
    datos = response.json().get("results", [])
    return {"results": datos}

@series_bp.route("/series_mejor_calificadas")
def series_mejor_calificadas():
    page = request.args.get("page", 1)
    url = f"https://api.themoviedb.org/3/tv/top_rated?api_key={API_KEY}&page={page}"
    response = requests.get(url)
    datos = response.json().get("results", [])
    return {"results": datos}
