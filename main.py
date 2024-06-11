import json
import pdfkit
import requests

with open('data.txt', 'r') as file:
    file_details = file.read()

details = json.loads(file_details)

all_links_list = details.values()

HTML_links_list = []
for values in all_links_list:
    for value in values:
        if ".html" in value:
            HTML_links_list.append(value)


for i in range(len(HTML_links_list)):
    url = HTML_links_list[i]
    path = f"Output{i}"
    pdfkit.from_url(url,path)
    print(f"PDF generated Output{i}.pdf")