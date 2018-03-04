"""
CV Generator

"""
from jinja2 import Environment, PackageLoader, select_autoescape
import ruamel.yaml as yaml
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.text import WD_ALIGN_PARAGRAPH

import datetime

cvdb = {}

with open("skills.yml", 'r') as stream:
    try:
        cvdb = yaml.load(stream, Loader=yaml.Loader)
    except yaml.YAMLError as exc:
        print(exc)

# Process the imported YAML; creating the structure required for the document from the source database
processed_cvdb = {}
processed_cvdb['skill_groups'] = cvdb['skill_groups']
processed_cvdb['positions'] = cvdb['positions']
processed_cvdb['elevator_pitch'] = cvdb['elevator_pitch']

processed_cvdb['achievements'] = {}
for position, position_achievements in cvdb['achievements'].iteritems():
    processed_cvdb['achievements'][position] = list()
    for achievement in position_achievements:
        if 'hidden' not in achievement:
            processed_cvdb['achievements'][position].append(achievement)

processed_cvdb['education'] = cvdb['education']

OUTPUT_DOCUMENT_TYPE = "word" # or "html"

if OUTPUT_DOCUMENT_TYPE == "html":

    env = Environment(
        loader=PackageLoader('gencv', 'templates'),
        autoescape=select_autoescape(['html', 'rtf'])
    )

    template = env.get_template('legacy_cv.html')

    # to save the results
    with open("generated_cv.html", "wb") as fh:
        fh.write(template.render(processed_cvdb).encode('utf-8'))

elif OUTPUT_DOCUMENT_TYPE == "word":

    document = Document()

    for style in document.styles:
        print "{} ({})".format(style.name, style.type)

    document.styles['Title'].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.styles['Normal'].font.size = Pt(8)

    # Configure the document properties:
    document.core_properties.title = "Caleb Marchent"
    document.core_properties.author = "Caleb Marchent - Curriculum Vitae"
    document.core_properties.created = datetime.datetime.now()
    document.core_properties.comments = "Generated Automatically\nSource code available at:\nhttps://github.com/calebmarchent/auto_cv.git"

    document.add_heading('Caleb Marchent', 0)

    p = document.add_paragraph('9 Goldfinch Drive, Cottenham, Cambridge, CB24 8XY | 07803 296105 | caleb.marchent@iee.org')
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    document.add_heading('Summary', level=2)

    for para in processed_cvdb['elevator_pitch']:
        p = document.add_paragraph(para)

    document.add_heading('Key Skills', level=2)

    # Find the maximum number of skills in a group
    rows = max(len(skill_group) for skill_group in processed_cvdb['skill_groups'])

    table = document.add_table(rows=1, cols=len(processed_cvdb['skill_groups']))
    col = 0

    # FIXME: Spurious line at start of cell
    # Happens because there has to be cell contrent; there does not appear to be an API to replace the existing text
    # with formatted text

    for skill_group in processed_cvdb['skill_groups']:
        hdr_cells = table.columns[col].cells
        for skill in skill_group:
            hdr_cells[0].add_paragraph(skill, style='ListBullet')
        col += 1

    document.add_heading('Experience', level=2)

    for position in processed_cvdb['positions']:
        p = document.add_paragraph("{}\t{}\t{}".format(position['company_name'],
                                             position['title'],
                                             str(position['start']) + " - " + str(position['finish'])))

        p.paragraph_format.tab_stops.add_tab_stop(Inches(3), WD_TAB_ALIGNMENT.CENTER)
        p.paragraph_format.tab_stops.add_tab_stop(Inches(6), WD_TAB_ALIGNMENT.RIGHT)

        if 'company_summary' in position:
            document.add_paragraph(position['company_summary'])

        for achievement in processed_cvdb['achievements'][position['brief']]:
            document.add_paragraph(achievement['desc'], style='ListBullet')

    document.add_heading('Education', level=2)

    for experience in processed_cvdb['education']:
        p = document.add_paragraph("{}\t{}".format(experience['desc'], experience['date']))
        p.paragraph_format.tab_stops.add_tab_stop(Inches(6), WD_TAB_ALIGNMENT.RIGHT)
        if 'additional_info' in experience:
            p.add_run("\n{}".format(experience['additional_info']))

    document.save('curriculum_vitae.docx')