'''
CAEN Round 3 
Python Project
Inputs:     CL file location of text file with words
Outputs:    Summary information*; alphabetic dictionary*
*See original specs for more detail, attached.
'''

import os, argparse

# list of common non-alpha characters
NONALPHA = "1234567890!@#$%^&*()-_=+\\\'\"[]\{\};:,./<>?`~"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# COMMAND LINE FUNCTIONS

# Retrieve command line arguments
def parse_arguments():
    # Create the parser and add arguments
    parser = argparse.ArgumentParser()
    
    # file is required 
    parser.add_argument(dest='filename', type=str, help="Name of the file to parse and summarize")

    # to help less technical users
    parser.add_argument('-v', default=False, action="store_true", required=False, help="Verbose. Provides additional output as the program executes.")
    
    # retreive arguments
    args = parser.parse_args()
    
    return args.filename, args.v

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ASSERT FUNCTIONS

# Quits program if the file does not exist
def assert_file_exists(filename):
    if not os.path.exists(filename): 
        print("File name \"" + filename + "\"does not exist from this directory.")
        print("Please ensure your filename is correct relative to the current working directory.")
        print("Your current working directory: " + os.getcwd())
        quit()

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
    print("{")
    for item in sorted_list:
        print("\t" + item + ": " + str(len(item)))
    print("}")

# Prints summary statistics according to specs
def print_summary(word_count, uniq_word_count, third_frequent):
    print("There are " + str(word_count) + " words in the file.")
    print("There are " + str(uniq_word_count) + " unique words in the file.")
    print("The third most frequent word in the file is \"" + third_frequent + ".\"")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ASSEMBLES 

# reads the file, creates stats, outputs stats
def assemble_file_stats(filename):
    
    # basic error checking 
    assert_file_exists(filename)
    
    word_count = 0
    word_freq = {}
    
    # reads line and retrieves data
    with open(filename) as f:
        for line in f:
            for word in line.split():
                word = word.strip(NONALPHA).lower()
                
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
    
    print_summary(word_count, len(word_freq), sorted_words_by_freq[3][0])
    
    print_psuedo_len_dict(sorted_words_by_abc)


# main
def main(): 
    
    # retrieves the command line arguments
    filename, verbose = parse_arguments()
    
    # reads the file, creates stats, outputs stats
    assemble_file_stats(filename)


# stub for main
if __name__=="__main__":
    main()