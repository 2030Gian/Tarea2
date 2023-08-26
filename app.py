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
    new_anime = {"titulo":anime_titulo,"poster":anime_poster,"genero":anime_genero, "rating":anime_rating,"reviews":anime_reviews,"season":anime_season,"tipo":anime_tipo}
    anime.append(new_anime)
    return "Agregado exitosamente"
'''
@app.route('/anime/<id>', methods = ['PUT'])
def actualizar_parcial():
    pass

@app.route('/anime/<id>', methods = ['PATCH'])
def actualizar_total():
    pass


@app.route('/anime/<id>', methods = ['DELETE'])
def delete_anime():
    anime.clear()
'''

if __name__ == '__main__':
    app.run(debug=True)


  