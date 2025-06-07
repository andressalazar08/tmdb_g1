import os
import requests
from flask import Blueprint, render_template, request
from dotenv import load_dotenv

# Cargar variables del archivo .env (donde tienes la API_KEY guardada)
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Crear un Blueprint para las rutas de búsqueda de películas
buscar_bp = Blueprint("buscar_pelicula", __name__)

# Ruta para mostrar el formulario y buscar películas
@buscar_bp.route("/buscar_pelicula", methods=["GET", "POST"])
def buscar_peliculas():
    datos = []  # Creamos una lista vacía para los resultados

    # Si se envió un formulario (POST), buscamos en la API
    if request.method == "POST":
        consulta = request.form.get("consulta")  # Obtenemos el texto buscado
        if consulta:  # Si hay algo escrito
            url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={consulta}&language=es-ES"
            response = requests.get(url)

            # Si la respuesta fue exitosa (código 200)
            if response.status_code == 200:
                datos = response.json().get("results", [])

    # Siempre retornamos el template con los datos (vacío o con resultados)
    return render_template("buscar_pelicula.html", datos=datos)
