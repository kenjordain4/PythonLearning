import re
from collections import Counter

def most_common_words(file,m):
    with open(file,'r',encoding='utf-8') as f:
        words_data=f.read()
        regex_pattern=r'\b[A-Za-z]+\b'
        words=re.findall(regex_pattern,words_data)
        word_counts=Counter(words)
        most_common_words= word_counts.most_common(m)
        return most_common_words
print(most_common_words("obama's speech.txt",5))


def clean_text(file):

        regex_pattern=r'[^A-Za-z0-9]+'
        matches=re.sub(regex_pattern,' ',file)
        return matches.lower()
def remove_support_words(cleaned_text):

    words=cleaned_text.split()
    with open('stopwords.txt','r',encoding='utf-8') as f:
        stopwords_text=f.read()
        filtered_word=[word for word in words if word not in stopwords_text]
        return' '.join(filtered_word)

def check_similarities(file1,file2):
    with open(file1,'r',encoding='utf-8') as f:
        text1=f.read()
    with open(file2,'r',encoding='utf-8') as f:
        text2=f.read()
    #cleaned_text

    text1_cleaned=clean_text(text1)
    text2_cleaned=clean_text(text2)

    #remove_support words

    text1_filtered=remove_support_words(text1_cleaned)
    text2_filtered=remove_support_words(text2_cleaned)

    #check_similarities

    words1=set(text1_filtered.split())
    words2=set(text2_filtered.split())

    intersection = words1.intersection(words2)
    union = words1.union(words2)
    similarity = len(intersection)/len(union) if union else 0
    return similarity

print(check_similarities("michelle_speech.txt","melina_speech.txt"))


#--------------------------------------------------------------------------------
#repeated_words(file) reads a text file and identifies the most frequently occurring words.
#It extracts all alphabetical words using regular expressions,
# counts their occurrences,
# and returns the top 10 most repeated words along with their frequencies.

def repeated_words(file):
    with open(file,'r',encoding='utf-8') as f:
        text1=f.read()
        regex_pattern=r'\b[A-Za-z]+\b'
        words=re.findall(regex_pattern,text1)
        words_count=Counter(words)
        most_repeated_words=words_count.most_common(10)
        return most_repeated_words

#find_the_number_of_lines(file) analyzes a text file and counts how many lines mention specific programming languages.
#It checks each line for references to Python,
# JavaScript, and Java (excluding JavaScript), prints the results,
# and returns the counts as a tuple.
def find_the_number_of_lines(file):
    with open(file,'r',encoding='utf-8') as f:
        text1=f.read()
        line_count1=0
        line_count2=0
        line_count3=0
        for line in text1.split('\n'):
            if 'python'in line or 'Python' in line:
                line_count1+=1
            if 'JavaScript' in line or 'javascript'in line or 'Javascript' in line:
                line_count2+=1
            if 'Java'in line and not 'JavaScript' in line:
                line_count3+=1
        print('Number of lines in file containing python or Python:',line_count1)
        print('Number of lines in file containing JavaScript, javascript or Javascript:',line_count2)
        print('Number of lines in file containing Java and not JavaScript:',line_count3)

        return line_count1,line_count2,line_count3

print(find_the_number_of_lines("hacker_news"))