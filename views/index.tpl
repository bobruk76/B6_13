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
        <div class="wrapper-first-page">
            <header>
                <nav class="site-menu">
                    <ul>
                        <li><a href="#">home</a></li>
                        <li><a href="/albums/">Новый альбом</a></li>
                    </ul>
                </nav>
            </header>
        </div>
        <main>
            <section class="sixth-section">
                <h1>
                    Список артистов:
                </h1>
                <p>Выберите артиста из списка:</p>
                <ul>
                    % for item in ref_artists:
                      <li><a href="/albums/{{item}}">{{item}}</a></li>
                    % end
                </ul>
            </section>
        </main>
    </body>
</html>