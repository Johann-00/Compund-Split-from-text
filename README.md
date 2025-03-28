## About the Project

This program is designed to take in any text, split all compound words in it and count the first and second words
This project was created for the Staatsexamensarbeit of Jessica Schmidt.
It was created using ChatGPT.
For processing natural language we used spaCy: https://spacy.io/

## How to use

* use a txt file or convert a xml file using xmlToTxt.py file in the project
* use preFilter.py (open it and change the input_file variable) to filter out all nouns in the text
* use the [MOP Compound Splitter (MCS)](https://www.ims.uni-stuttgart.de/forschung/ressourcen/werkzeuge/mcs/) tool to split all compund words
* use the filter.py to create 2 files containing sorted counts of first words and second words

## Authors

* Johann Eckhardt
* in cooperation with Jessica Schmidt
