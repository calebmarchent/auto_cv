Caleb Marchent
==
{% if contact_info is defined %}
{{ contact_info }}
{% endif %}

Profile
--
{% for para in elevator_pitch %}
{{ para }}

{% endfor %}

Key Skills
--

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| {% for s in skill_groups[0]['items'] %}<li> {{ s }} <br />{% endfor %} |  | |

 


Experience
--
{% for position in positions %}

**{{ position.company_name }}** ({{ position.start }} - {{ position.finish }})
</table>

{% if position.company_summary is defined %}
{{ position.company_summary }}
{% endif %}
{% set achievements_here = achievements[position.brief] %}
{% for achievement in achievements_here %}
* {{ achievement.desc }}
{% endfor %}
{% endfor %}

Education
--
{% for experience in education %}
<table>
    <tr><td>{{ experience.desc }}<td class="date">{{ experience.date }}</td>
</table>
{% endfor %}
<table>
    <tr>
        <td>
MEng. (Hons) Electronic Engineering with Computer Science: 2-1 <br>
University of Wales Swansea <br>
4-year masters course plus one gap year in Fachhochschule Mannheim
        <td class="date">
        1993 - 1998</td>
    </tr>
</table>
</body>