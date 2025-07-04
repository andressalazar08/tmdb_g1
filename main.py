
from flask import Flask, Blueprint 

from routes.popular import popular_bp

from routes.genero_de_peliculas import genero_de_peliculas_bp #inporto

from flask import Flask, Blueprint

from routes.d_series import series_bp
from routes.mejores_valoradas import mejoresvaloradas_bp
from routes.popular import popular_bp

from routes.detalles_una_serie import detalles_una_serie_bp, detalles_una_serie_buscar_bp

from routes.estrenos import estrenos_bp
from routes.generos import generos_bp

from routes.detalles import detalles_bp


from routes.detalles import detalles_bp


from routes.detalles_una_serie import detalles_una_serie_bp
from routes.elenco_y_equipos import credits_bp


from routes.buscar_pelicula import buscar_bp # importo





import os

from dotenv import load_dotenv


load_dotenv()


app=Flask(__name__)


app.register_blueprint(popular_bp)

app.register_blueprint(genero_de_peliculas_bp)




app.register_blueprint(mejoresvaloradas_bp)
app.register_blueprint(series_bp)
app.register_blueprint(popular_bp)

app.register_blueprint(detalles_una_serie_bp)
app.register_blueprint(detalles_una_serie_buscar_bp)

app.register_blueprint(estrenos_bp)

app.register_blueprint(generos_bp)

app.register_blueprint(detalles_bp)


app.register_blueprint(credits_bp)

app.register_blueprint(detalles_una_serie_bp)


app.register_blueprint(buscar_bp) # importo la ruta





if __name__=="__main__":
    app.run(debug=True)