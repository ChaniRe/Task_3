import markdown
import pdfkit

#Open and read the Markdown file
with open('sample.md', 'r') as f:
    markdown_string = f.read()

#Convert the Markdown text into HTML format
html_string = markdown.markdown(markdown_string)

#Save the converted HTML to a file
with open('sample.html', 'w') as f:
    f.write(html_string)

#Tell Python where the 'wkhtmltopdf' program is installed
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

#Convert the HTML file into a final PDF document
pdfkit.from_file("sample.html", "sample.pdf", configuration=config)
