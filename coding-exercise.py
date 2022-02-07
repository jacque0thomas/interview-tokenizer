'''
Jacque Thomas
CAEN Interview Process February 2021
Word Parser/Summary Exercise
Requirements: 
    Python 3
    Libraries: os, argparse
    Arguments: FILENAME (position 1, name relative to cwd)
Optional:
    Arguments: --freq (will optionally print the dictionary with values
                       of frequency, rather than word length)
Outputs: 
    Printed summary of data, as specified.
    Printed dictionary of (word, length) 
                       or (word, frequency) if using the flag --freq]
'''

import os, argparse


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GLOBALS

# list of common non-alpha characters
NONALPHA = "1234567890!@#$%^&*()-_=+\\\'\"[]\{\};:,./<>?`~"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# COMMAND LINE FUNCTIONS

# Retrieve command line arguments
def parse_arguments():
    # Create the parser and add arguments
    parser = argparse.ArgumentParser()
    
    # file is required 
    parser.add_argument(dest='filename', type=str, 
                        help="Name of the file to parse and summarize")

    parser.add_argument('--freq', default=False, action="store_true", 
                        required=False, 
                        help="Will optionally print the dictionary with values of frequency, rather than word length.")

    # retreive arguments
    args = parser.parse_args()
    
    return args.filename, args.freq


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ASSERT FUNCTIONS

# Quits program if the file does not exist
def assert_file_exists(filename):
    if not os.path.exists(filename): 
        print("File name \"" + filename + "\"does not exist from this directory.")
        print("Please ensure your filename is correct relative to the current working directory.")
        print("Your current working directory: " + os.getcwd())
        quit()

# Quits program if no words were found
def assert_words(word_count, filename):
    if word_count == 0:
        print("No words found in " + filename)
        print("Please use a text file that contains words.")
        quit()
        
        
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# OUTPUT FUNCTIONS

# A sorted dictionary is useless to python
# but can be useful to users. 
def print_psuedo_len_dict(sorted_list):
    print("lengths = {")
    for item in sorted_list:
        print("\t" + item + ": " + str(len(item)))
    print("}")
    
# In the case that the "length" requested in the output dictionay is frequency,
# this function will output the frequency dictionary 
def print_freq_dict(sorted_list, word_freq):
    print("frequencies = {")
    for item in sorted_list:
        print("\t" + item + ": " + str(word_freq[item]))
    print("}")

# Prints summary statistics according to specs
def print_summary(word_count, uniq_word_count, third_frequent):
    print("There are " + str(word_count) + " words in the file.")
    print("There are " + str(uniq_word_count) + " unique words in the file.")
    print("The third most frequent word in the file is \"" + third_frequent + ".\"")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ENGINES 

# reads the file, creates stats, outputs stats
def assemble_file_stats(filename, freq):
    
    # basic error checking 
    assert_file_exists(filename)
    
    word_count = 0
    word_freq = {}
    
    # reads line and retrieves data
    with open(filename) as f:
        for line in f:
            for word in line.split():
                word = word.strip(NONALPHA).lower()
                
                # remove tokens that were only symbols
                if len(word) != 0:
                    word_count += 1
                    
                    if word in word_freq:
                        word_freq[word] = word_freq[word] + 1
                    else:
                        word_freq[word] = 1
                        
    # asserting that the input was readable
    assert_words(word_count, filename)
        
    # sorting for frequency and alphabetically
    sorted_words_by_freq = sorted(word_freq.items(), key=lambda x:x[1], reverse=True)
    sorted_words_by_abc = sorted(word_freq.keys())
    
    # Asserting that there are more than 2 words to print
    third_freq = sorted_words_by_freq[2][0] if len(sorted_words_by_freq) > 2 else "N/a. Not enough words"
    
    # Printing summary and required dictionary
    print_summary(word_count, len(word_freq), third_freq)
    if freq:
        print_freq_dict(sorted_words_by_abc, word_freq)
    else:
        print_psuedo_len_dict(sorted_words_by_abc)


# main
def main(): 
    
    # retrieves the command line arguments
    filename, freq = parse_arguments()
    
    # reads the file, creates stats, outputs stats
    assemble_file_stats(filename, freq)


# stub for main
if __name__=="__main__":
    main()