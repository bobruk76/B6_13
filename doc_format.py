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
        with HTML(output=None) as doc:
            with TopLevelTag("head") as head:
                with Tag("title") as title:
                    title.text = "hello"
                    head += title
                doc += head

            with TopLevelTag("body") as body:
                with Tag("h1", klass=("main-text",)) as h1:
                    h1.text = "Test"
                    body += h1

                with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
                    div += fn(param)
                    body += div

                doc += body
                return doc
        return wrapp