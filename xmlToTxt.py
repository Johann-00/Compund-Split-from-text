import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('manova_complete.xml')
root = tree.getroot()

# Open a file to write the text
with open('output.txt', 'w', encoding="utf-8") as output_file:
    for elem in root.iter():
        if elem.text:  # Check if there is text
            output_file.write(elem.text.strip() + '\n')
