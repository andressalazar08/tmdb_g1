import os
import requests
from flask import Blueprint, render_template,request
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

detalles_bp = Blueprint("detalles", __name__)

@detalles_bp.route("/detalles", methods=['GET', 'POST'])
def detalles():
    if request.method == "POST":
        id = int(request.form.get("id"))
        print(type(id))
        if id:
            url = f"https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY}&language=es-ES"
            response = requests.get(url)
            print(response)
            datos = response.json()
            if datos:
                return render_template("detalles.html", datos=datos)
    # if "genres" in response_json:
    #     datos = response_json["genres"]
    # else:
    #     datos = []  # Manejar el error apropiadamente
    
    return render_template("detalles.html")