# Configuración
from flask import Flask

import uuid

app = Flask(__name__)

# Controlador (API)
@app.route('/', methods = ['GET'])
def index():
    return '¡Hola, mundo! Esta es mi primera API con Flask y veremos animes.'

id = uuid.uuid1()

anime = [{"id":id, "titulo":"Dragon Ball",
        "poster":"https://s4.anilist.co/file/anilistcdn/user/avatar/large/default.png",
        "genero":"Action","rating":10000,"reviews":10,"season":"GIT","tipo":"serie"}]


@app.route('/anime', methods = ['GET'])
def list_animes():
    return anime

@app.route('/anime/<int:anime_id>', methods = ['GET'])
def list_anime(anime_id):
    return anime[anime_id]

@app.route('/anime/<string:anime_titulo>/<string:anime_poster>/<string:anime_genero>/<int:anime_rating>/<int:anime_reviews>/<string:anime_season>/<string:anime_tipo>', methods = ['POST'])
def create_anime(anime_titulo,anime_poster,anime_genero,anime_rating,anime_reviews,anime_season,anime_tipo):
    id = uuid.uuid1()
    new_anime = {"id":id,"titulo":anime_titulo,"poster":anime_poster,"genero":anime_genero, "rating":anime_rating,"reviews":anime_reviews,"season":anime_season,"tipo":anime_tipo}
    anime.append(new_anime)
    return "Agregado exitosamente"

@app.route('/anime/<string:id>/<string:anime_titulo>/<string:anime_poster>/<string:anime_genero>/<int:anime_rating>/<int:anime_reviews>/<string:anime_season>/<string:anime_tipo>', methods = ['PUT'])
def actualizar_total(id,anime_titulo,anime_poster,anime_genero,anime_rating,anime_reviews,anime_season,anime_tipo):

    for i in anime:
        if str(i["id"]) == id:
            i["titulo"] = anime_titulo
            i["poster"] = anime_poster
            i["genero"] = anime_genero
            i["rating"] = anime_rating
            i["reviews"] = anime_reviews
            i["season"] = anime_season
            i["tipo"] = anime_tipo  
            return 'Actualizado correctamente!!!'
    return 'No se encontró el anime!!' 

@app.route('/anime/<string:id>/<string:anime_titulo>/<int:bool_titulo>/<string:anime_poster>/<int:bool_poster>/<string:anime_genero>/<int:bool_genero>/<int:anime_rating>/<int:bool_rating>/<int:anime_reviews>/<int:bool_reviews>/<string:anime_season>/<int:bool_season>/<string:anime_tipo>/<int:bool_tipo>', methods = ['PATCH'])
def actualizar_parcial(id,anime_titulo,bool_titulo,anime_poster,bool_poster, anime_genero, bool_genero, anime_rating, bool_rating, anime_reviews, bool_reviews, anime_season, bool_season,anime_tipo, bool_tipo):
    for i in anime:
        if str(i["id"]) == id:
            if bool_titulo == 1:
                i["titulo"] = anime_titulo
            if bool_poster == 1:
                i["poster"] = anime_poster
            if bool_genero == 1:
                i["genero"] = anime_genero
            if bool_rating == 1:
                i["rating"] = anime_rating
            if bool_reviews == 1:
                i["reviews"] = anime_reviews
            if bool_season == 1:
                i["season"] = anime_season
            if bool_tipo == 1:
                i["tipo"] = anime_tipo 
            return 'Actualizado correctamente!!!'
    return 'No se encontró el anime!!' 
    
@app.route('/anime/<string:id>', methods = ['DELETE'])
def delete_anime(id):
    for i in anime:
        if str(i["id"]) == id:
            i.clear()
            return "Eliminado exitosamente!!!"
    return "No se encontró el anime!!"
            
    

if __name__ == '__main__':
    app.run(debug=True)


  