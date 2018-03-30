Caleb Marchent
==
caleb.marchent@iee.org

Profile
--
Software Engineer with 20 years experience, predominantly as a hands-on developer leading teams of highly skilled engineers to deliver products using whatever technology is required. Seeks another hands-on technical role, working closely in a team with other engineers to successfully deliver products that satisfy customers.

Holds a rare combination of talents; a broad knowledge of the development, production and support of software, the ability to write code, script systems and use tools while at the same time - create, mentor and manage teams that can do this on a larger scale. Grace under pressure while dealing with demanding customers from around the world and delivering on tight deadlines.

Key Skills
--

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| <li> **Agile:** Certified Scrum Master<br /><li> **Bug Tracking:** JIRA, Bugzilla | right-aligned | $1600 |
|       | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

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