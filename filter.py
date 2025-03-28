import spacy
from collections import Counter


nlp = spacy.load("de_core_news_sm")


# filter for only split words (have a "·" in the word) in text
def split_words_into_two_lists(file_path):
    # Initialize two lists to store words before and after the "·" symbol
    words_before_dot = []
    words_after_dot = []
    all_words = []
    
    # Open the file and read line by line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split each line into words
            words = line.split()
            # Check each word for the split symbol
            for word in words:
                # Remove leading and trailing symbols
                word = word.lstrip('„‚')
                word = word.rstrip('“‘.,')
                if '|' in word:
                    # Split the word by the split symbol
                    parts = word.split('|')
                    # Add the parts to their respective lists
                    words_before_dot.append(parts[0])
                    words_after_dot.append(parts[1])
    
    return words_before_dot, words_after_dot, all_words

# count which word appears how often and write to file
def word_count(word_list, output_file_name):
    word_counts = Counter(word_list)
    sorted_word_counts = word_counts.most_common()
    
    # Write the results to a file
    with open(output_file_name, 'w', encoding="utf-8") as output_file:
        for word, count in sorted_word_counts:
            output_file.write(f"{word}: {count}\n")

    return sorted_word_counts

# filter for words that spacy accepts as nouns
def nouns_only(word_array):
    nouns = []

    for word in word_array:
        doc = nlp(word)
        if(doc):
            token = doc[0]
            if(token.tag_ == 'NN'):
                nouns.append(token.text)


    return nouns


file_path = 'ManovaNounsOnly.txt.kmax2.lemmaSplit' 
words_before, words_after, all_words = split_words_into_two_lists(file_path)
nouns_erstglieder = nouns_only(words_before)
nouns_zweitglieder = nouns_only(words_after)

word_count(nouns_erstglieder, 'ManovaErstglieder.txt')
word_count(nouns_zweitglieder, 'ManovaZweitglieder.txt')
print("All Complete!")
