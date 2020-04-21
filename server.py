from bottle import route
from bottle import run
from bottle import HTTPError

import album


@route("/albums/<artist>")
def albums(artist):
    return str(album.albums_get(artist))

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)