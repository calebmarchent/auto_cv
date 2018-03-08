Automatic CV Generator
==

I want and automatic CV generator so that I can keep the underlying information in a source controlled YAML database; while
also being able to tag specific versions distributed and select specific achievements that demonstate my ability to so a
given role.


Notes on thought process and hence design
--
The original concept was to use Jinja2 templates; to create a LaTex document and from that to create PDF.
I rapidly fell back to HTML rendering for the first prototype; this worked quite smoothly.
In most cases people want word documents; so I added docx generation; this time using docx-python library in a similar
method to that I have used for automatic report generation in many of my previous roles.

