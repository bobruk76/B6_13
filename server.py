from bottle import route
from bottle import run
from bottle import HTTPError

from album import albums_get


#@route("/albums/<artist>")
def albums(artist):
    result = albums_get(artist)
    return result

if __name__ == "__main__":
#    run(host="localhost", port=8080, debug=True)
    print(albums('Queen'))