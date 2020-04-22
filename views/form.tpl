<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <title>Практика</title>
        <meta name="description" content="">
        <meta name="author" content="Vladimir Poliakov">
        <link rel="stylesheet" href="/static/css/form_style.css">
    </head>
    <body>
        <main>
            <section class="sixth-section">
                <h1>
                    Форма ввода нового диска
                </h1>
                <div class="like-hr"></div>
                <div class="second-block">
                    <form id="album-form" class="like-form" action="/albums/" method="POST">
                        <input id="year"  class="form-field" type="text" name="year" required  placeholder="Год">
                        <input id="artist"  class="form-field" type="text" name="artist" required  placeholder="Исполнитель">
                        <input id="genre"  class="form-field" type="text" name="genre" required  placeholder="Жанр">
                        <input id="album"  class="form-field" type="text" name="album" required  placeholder="Альбом">
                        <button class="button" type="submit">subscribe</button>
                    </form>
                </div>
            </section>
        </main>
    </body>
</html>