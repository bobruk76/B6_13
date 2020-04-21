import re
try:
    # Чтобы текст был лесенкой установите bs4
    # pip install bs4
    from bs4 import BeautifulSoup as bs

    def hhml_format(str = ''):
        return bs(str).prettify()
except:
    def hhml_format(str = ''):
        return str

class Tag:
    def __init__(self, tag, **kwargs):
        self.tag = tag
        self.text = ''
        self.attr = ''
        self.is_single = False

        for key, item in kwargs.items():
            if key == 'is_single':
                self.is_single = item
            elif key == 'klass':
                self.attr += ' class='
                cls = ''
                for cl in item:
                    cls += '%s ' % cl
                self.attr += '"%s"' % re.sub('_','-',cls.rstrip())

            else:
                self.attr += ' {}="{}"'.format(key, item)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return self

    def __str__(self):
        return ('\n<{tag}{attr}'+
            (' />' if self.is_single else '>{text}</{tag}>')).format(
            tag = self.tag,
            text = self.text,
            attr = self.attr
            )

    def __iadd__(self, other):
        self.text += str(other) + '\n'
        return self

class TopLevelTag(Tag):

    def __str__(self):
        return ('\n<{tag}>{text}</{tag}>').format(
            tag = self.tag,
            text = self.text
            )

class HTML(TopLevelTag):
    def __init__(self, output, tag = 'HTML'):
        Tag.__init__(self, tag)
        self.output = output

    def __exit__(self, type, value, traceback):
        out_str = hhml_format(re.sub('\n\n','\n',str(self)))
        if self.output  is None:
            print(out_str)
        else:
            with open(str(self.output), "w") as f:
                f.write(out_str)

def html_page(fn):
    def wrapp(param):
        result = ''
        with HTML(output=None) as doc:
            with TopLevelTag("head") as head:

                with Tag("meta", is_single=True, charset="utf-8") as meta:
                    head += meta

                with Tag("link", is_single=True, rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css") as link:
                    head += link

                with Tag("link", is_single=True, rel="stylesheet", href="https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap&subset=cyrillic") as link:
                    head += link

                with Tag("link", is_single=True, rel="stylesheet", href="/static/css/styles.css") as link:
                    head += link

                with Tag("title") as title:
                    title.text = "B6_13"
                    head += title

                doc += head

            with TopLevelTag("body") as body:
                with Tag("h1", klass=("main-text",)) as h1:
                    h1.text = param
                    body += h1
                    body += fn(param)

                with Tag("script", src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js") as script:
                    body += script

                with Tag("script", src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js") as script:
                    body += script

                with Tag("script", src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js") as script:
                    body += script


            doc += body
            result = doc
        return result
    return wrapp