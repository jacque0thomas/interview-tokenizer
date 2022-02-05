'''
CAEN Round 3 
Python Project
Inputs:     CL file location of text file with words
Outputs:    Summary information*; alphabetic dictionary file*
*See original specs for more detail
'''

import io



# INPUT:    Text file name on the command line
# OUTPUT:   Summary to command line
#           Alphabetized output of words and their length, to command line or file
def main():
    print("Hello! I'm here to assist you with:")
    print("1. Reading a text file,")
    print("2. Providing some summary details,")
    print("And 3. Outputting an alphabetized list of the words used with")
    print("their lengths.")
    print("**********************************")
    print("Are you ready? Y/N")
    # input loop, waiting for y or n
    # if n, quit
    
    print("So, let's begin!")
    print("First, I'll need the file name that I'll be reading:")
    # input loop with basic error catching
    # errors to catch: file not found, folder not found,
    print("Thanks!")
    
    # reads in file
    # error catching: empty file, no words found
    print("Here is some summary information of the words in that file:")
    print("There are NUMBER words in the file.")
    print("There are NUMBER unique words in the file.")
    print("The third most frequent word in the file is WORD.")

  
  

if __name__=="__main__":
    main()