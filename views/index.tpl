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
                <ul>
                    % for item in ref_artists:
                      <li><a href="/albums/{{item}}">{{item}}</a></li>
                    % end
                </ul>
                <div class="like-hr"></div>
                <div class="second-block">
                    <form id="album-form" class="album-form" action="" method="POST">
                        <input id="you-name"  class="form-field" type="text" name="you-name" required  placeholder="Name">
                        <input id="you-email"  class="form-field" type="email" name="you-email" required  placeholder="Your Mail">
                        <textarea name="you-message" id="you-message" cols="30" rows="10"  class="form-field" placeholder="Type your message"></textarea>
                        <button class="button" type="submit">subscribe</button>
                    </form>

                </div>
            </section>
        </main>
    </body>
</html>