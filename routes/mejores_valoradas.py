import os
import requests
from flask import Blueprint, render_template,request
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

mejoresvaloradas_bp = Blueprint("mejores_valoradas", __name__)
cantidad=0
@mejoresvaloradas_bp.route("/mejores_valoradas",methods=["GET", "POST"])
def mejores_valoradas():
    global cantidad
    datos_totales=[]
    for page in range (1,20):
        url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=es-ES&page={page}"
        response = requests.get(url)
        datos_totales.extend (response.json()["results"])
    if request.method=="POST":
        cantidad+=20
        datos=datos_totales[:cantidad]
    return render_template("mejores_valoradas.html", datos=datos)