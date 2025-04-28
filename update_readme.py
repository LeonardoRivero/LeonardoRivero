from datetime import datetime

start_year = 2021
current_year = datetime.now().year
years_programming = current_year - start_year

with open("README_template.md", "r", encoding="utf-8") as template_file:
    content = template_file.read()

content = content.replace("{{years_programming}}", str(years_programming))

with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(content)
