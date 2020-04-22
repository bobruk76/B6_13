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

    album_data = {
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album")
    }

    return album_data

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)