import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from doc_format import html_page
from bottle import HTTPError

DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()

class Album(Base):
    __tablename__ = "album"

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def find(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums

@html_page
def albums_get(artist):

    def to_div(string):
        return '<div class="disk-field disk"><p class="label">{}</p></div>'.format(string)

    albums_list = find(artist)
    if not albums_list:
        message = "Альбомов {} в нашей базе не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = list(map(to_div,[album.album for album in albums_list]))
        result = "<h2>В нашей дискографии {} количество альбомов - {}</h2>".format(artist, len(album_names))
        result += '<div class="grid-wrapper">{}</div>'.format("\n".join(album_names))
    return result