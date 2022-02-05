'''
CAEN Round 3 
Python Project
Inputs:     CL file location of text file with words
Outputs:    Summary information*; alphabetic dictionary*
*See original specs for more detail, attached.
'''

import os, argparse
from string import strip

# list of common non-alpha characters
NONALPHA = "1234567890!@#$%^&*()-_=+\\\'\"[]\{\};:,./<>?`~"



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


# quits program if the file does not exist
def assert_file_exists(filename):
    if not os.path.exists(filename): 
        print("File name \"" + filename + "\"does not exist from this directory.")
        print("Please ensure your filename is correct relative to the current working directory.")
        print("Your current working directory: " + os.getcwd())
        quit()
        
        
# prints summary statistics according to specs
def print_summary(word_count):
    print("")



# in: file 
def assemble_file_stats(filename):
    
    # basic error checking 
    assert_file_exists(filename)
    
    word_count = 0
    words = {}
    # reads line and retrieves data
    with open(filename) as f:
        for line in f:
            for word in line.split().strip(NONALPHA):
                print(word)
                
    # checking if the input was garbage
    if word_count == 0:
        print("No words found in " + filename + ".")
        print("Please use a text file that contains words.")
                

                
        
    

# main
def main(): 
    
    # retrieves the command line arguments
    filename, verbose = parse_arguments()
    
    # the main part of the program
    assemble_file_stats(filename)
    
    print(filename)
    print(verbose)

# stub for main
if __name__=="__main__":
    main()