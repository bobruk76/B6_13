import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from doc_format import html_page
from bottle import HTTPError
import datetime
import re
DB_PATH = "sqlite:///albums.sqlite3?charset=utf8"
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

def ref_artists():
    """
    Находит всех артистов в базе данных
    """
    session = connect_db()
    return set([item.artist for item in session.query(Album).all()])


def find(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums

@html_page
def albums_get(artist):
    """
    из старой практики берется обертка для начальной страницы
    """
    def to_div(string):
        return '<div class="disk-field disk"><p class="label">{}</p></div>'.format(string)

    albums_list = find(artist)
    error = False
    if not albums_list:
        message = "Альбомов {} в нашей базе не найдено".format(artist)
        result = HTTPError(404, message)
        error = True
    else:
        album_names = list(map(to_div,[album.album for album in albums_list]))
        result = "<h2>В нашей дискографии {} количество альбомов - {}</h2>".format(artist, len(album_names))
        result += '<div class="grid-wrapper">{}</div>'.format("\n".join(album_names))
    return {'error': error, 'result': result}

def request_data(album_data):
    # функции валидации данных
    def valid_year(year_text):
        pattern = re.compile('[1-2]\d\d\d')
        return pattern.match(year_text)

    # создаем новый альбом
    try:
        if valid_year(album_data['year']):
            new_album = Album(
                year = int(album_data['year']),
                artist = album_data['artist'],
                genre = album_data['genre'],
                album = album_data['album']
            )
            session = connect_db()
            search_list=list(session.query(Album).filter(Album.album == new_album.album).filter(Album.artist == new_album.artist).filter(Album.genre == new_album.genre).filter(Album.year == new_album.year))
            if len(search_list) != 0:
                message = "Альбом {} {} года в дискографии исполнителя {}  в жанре {} есть!".format(new_album.album,new_album.year,new_album.artist,new_album.genre)
                result = HTTPError(409, message)
            else:
                session.add(new_album)
                session.commit()
                result = 'Данные успешно внесены!'
        else:
            message = "Данные неверного формата!"
            result = HTTPError(409, message)
    except:
        message = "Внести данные не удалось!((("
        result = HTTPError(418, message)

    return result