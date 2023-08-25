from flask import Flask, request

import uuid

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return '¡Hola, mundo! Esta es mi primera API con Flask y veremos animes.'

id = uuid.uuid1()
anime = {"id":id, "titulo":"Dragon Ball",
        "poster":"https://s4.anilist.co/file/anilistcdn/user/avatar/large/default.png",
        "genero":"Action","rating":10000,"reviews":10,"season":"GIT","tipo":"serie"}    

@app.route('/anime', methods =['GET'])
def list_animes():
    return list(anime.values())

@app.route('/anime/<id>', methods = ['POST'])
def create_anime():
    pass

@app.route('/anime/<id>', methods = ['DELETE'])
def delete_anime():
    anime.clear()

if __name__ == '__main__':
    app.run(debug=True)


  