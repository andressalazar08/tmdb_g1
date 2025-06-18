import os
import requests
from flask import Blueprint, render_template,request
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")

genero_de_peliculas_bp = Blueprint("genero_de_peliculas", __name__)

@genero_de_peliculas_bp.route("/genero_de_peliculas",methods={"GET","POST"})
def genero_de_peliculas():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=es-ES"
    print(url)
    response = requests.get(url)
    print(response)
    id=int(request.form.get("id"))
    print(id)
    datos = response.json()["genres"]
    for diccionario in datos:
        if diccionario["id"]==id:
            salida=diccionario

   
   
    print(datos)
    return render_template("genero_de_peliculas.html",salida=salida)