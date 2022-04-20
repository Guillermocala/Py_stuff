import re

# (?!...) if ... doesn't match, the whole pattern will fail
practice = re.compile(r".*[.](?!bat$).*$")

print(practice.search("archivo.bat"))