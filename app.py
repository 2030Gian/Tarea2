from flask import Flask, request

import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return '¡Hola, mundo! Esta es mi primera API con Flask.'


@app.route('/anime', methods =['GET'])
def crear_anime():
    u = uuid.uuid1()
    anime = {"id":u, "titulo":"Dragon Ball",
             "poster":"https://s4.anilist.co/file/anilistcdn/user/avatar/large/default.png",
             "genero":"Action","rating":10000,"reviews":10,"season":"GIT","tipo":"serie"}
    
    print(list(anime.values()))
    
    return list(anime.values())

if __name__ == '__main__':
    app.run(debug=True)


  