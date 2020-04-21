from bottle import *

import album

# Static CSS Files
@route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static/css')

@route("/albums/<artist>")
def albums(artist):
    return str(album.albums_get(artist))

@route("/")
@view('index')
def index():
    return {'ref_artists':album.ref_artists()}

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)