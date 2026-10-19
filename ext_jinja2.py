from jinja2 import Template


def render_t():
    return Template("Hi {{n}}").render(n="Stas")