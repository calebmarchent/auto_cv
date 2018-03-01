"""
CV Generator

"""
from jinja2 import Environment, PackageLoader, select_autoescape
import ruamel.yaml as yaml

skills_db = {}

with open("skills.yml", 'r') as stream:
    try:
        skills_db = yaml.load(stream, Loader=yaml.Loader)
    except yaml.YAMLError as exc:
        print(exc)


env = Environment(
    loader=PackageLoader('gencv', 'templates'),
    autoescape=select_autoescape(['html', 'rtf'])
)

template = env.get_template('legacy_cv.html')

# to save the results
with open("generated_cv.html", "wb") as fh:
    fh.write(template.render(skills_db).encode('utf-8'))