"""
CV Generator

"""
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('gencv', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('legacy_cv.html')

print template.render(name="Caleb");