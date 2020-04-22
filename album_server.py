    # для форматирования HTML можно установить bs4
    # pip install bs4
    # многие решения взяты из предыдущих уроков
    # запустите
    # http://localhost:8080/
    # там и GET и POST запросы можно сделать)))
    # пояснений много не писал...сразу сорри!!

from bottle import *

import album

# Static CSS Files
@route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static/css')

@get("/albums/<artist>")
def albums(artist):
    return album.albums_get(artist)

@get("/")
@view('index')
def index():
    return {'ref_artists':album.ref_artists()}

@get("/albums/")
@view('form')
def get_form():

    return {}

@post("/albums/")
def set_form():

    form_data = {
        "year": request.forms.year,
        "artist": request.forms.artist,
        "genre": request.forms.genre,
        "album": request.forms.album
    }

    return album.request_data(form_data)

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)