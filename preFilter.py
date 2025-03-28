import spacy

def filter_nouns_large_file(input_file, nouns_output_file):
    # Load the spaCy language model
    nlp = spacy.load("de_core_news_sm")
    
    # Open input and output files
    with open(input_file, 'r', encoding='utf-8') as file, \
         open(nouns_output_file, 'w', encoding='utf-8') as nouns_file:
        
        # Process the file line by line
        for line in file:
            # Skip empty lines
            if line.strip():
                # Process the line with spaCy
                doc = nlp(line)
                
                # Collect nouns from the line
                nouns = [token.text for token in doc if token.tag_ == 'NN']
                
                # Write nouns to the output file
                if nouns:  # Only write if there are nouns in the line
                    nouns_file.write(" ".join(nouns) + "\n")


input_file = 'Manova_complete.txt'
nouns_output_file = 'nouns.txt'

filter_nouns_large_file(input_file, nouns_output_file)
print("Processing complete. Check the nouns output file.")
