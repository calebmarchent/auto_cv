"""
CV Generator

"""
from jinja2 import Environment, PackageLoader, select_autoescape
import ruamel.yaml as yaml
from docx import Document
from docx.shared import Inches

skills_db = {}

with open("skills.yml", 'r') as stream:
    try:
        skills_db = yaml.load(stream, Loader=yaml.Loader)
    except yaml.YAMLError as exc:
        print(exc)


OUTPUT_DOCUMENT_TYPE = "word" # or "html"

if OUTPUT_DOCUMENT_TYPE == "html":

    env = Environment(
        loader=PackageLoader('gencv', 'templates'),
        autoescape=select_autoescape(['html', 'rtf'])
    )

    template = env.get_template('legacy_cv.html')

    # to save the results
    with open("generated_cv.html", "wb") as fh:
        fh.write(template.render(skills_db).encode('utf-8'))

elif OUTPUT_DOCUMENT_TYPE == "word":

    document = Document()

    document.add_heading('Caleb Marchent', 0)


    p = document.add_paragraph('9 Goldfinch Drive, Cottenham, Cambridge, CB24 8XY | 07803 296105 | caleb.marchent@iee.org')

    document.add_heading('Summary', level=2)
    p = document.add_paragraph('Software Engineer with 20 years experience, predominantly as a hands-on developer leading teams of highly skilled engineers to deliver products using whatever technology is required. Seeks another hands-on technical role, working closely in a team with other engineers to successfully deliver products that satisfy customers.')
    p = document.add_paragraph('Holds a rare combination of talents; a broad knowledge of the development, production and support of software, the ability to write code, script systems and use tools while at the same time - create, mentor and manage teams that can do this on a larger scale. Grace under pressure while dealing with demanding customers from around the world and delivering on tight deadlines.')

    document.add_heading('Key Skills', level=2)

    # Find the maximum number of skills in a group
    rows = max(len(skill_group) for skill_group in skills_db['skill_groups'])

    table = document.add_table(rows=rows, cols=len(skills_db['skill_groups']))
    col = 0
    for skill_group in skills_db['skill_groups']:
        row = 0
        hdr_cells = table.columns[col].cells
        for skill in skill_group:
            hdr_cells[row].text = skill
            row += 1
        col += 1

    document.add_heading('Experience', level=2)

    for position in skills_db['positions']:
        table = document.add_table(rows=1, cols=3)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = position['company_name']
        hdr_cells[1].text = position['title']
        hdr_cells[2].text = str(position['start']) + " - " + str(position['finish'])

        if 'company_summary' in position:
            document.add_paragraph(position['company_summary'])

        for achievement in skills_db['achievements'][position['brief']]:
            document.add_paragraph(achievement['desc'], style='ListBullet')

    document.add_heading('Education', level=2)

    for experience in skills_db['education']:
        table = document.add_table(rows=1, cols=2)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = experience['desc'] + (experience['additional_info'] if 'additional_info' in experience else "")
        hdr_cells[1].text = str(experience['date'])


    document.save('demo.docx')