def update_counts(line, counts_dict):
    """helper function: updates the count of a dictionsary 
                        of words, sentences, and characters
    inputs:
        > line
            >> current line (str) of file being processed
        > counts_dict
            >> dictionary holding counts of words, sentences, and characters
    """
    # update sentence count (only by periods)
    counts_dict['sentences'] += line.count('.')
    # update word count
    counts_dict['words'] += len(line.split())
    # update characters count (include spaces)
    counts_dict['characters'] += len(line)
    
def create_report(file_path='misc/test_text.txt'):
    """function: take file name and return the
                 number of sentences, words, and characters
    inputs:
        > file_name
            >> path to file in question
    """
    # set counting dictionary (track sentences, words, characters) 
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
  
    # open the file (not making it a string, yet)
    with open(file=file_path, mode='r') as txt_file:
        # go through each line 
        for line in txt_file:
            # call helper function to update dictionary 
            update_counts(line, counts_dict)
            
    # return dictionary with counts of sentences, words, and characters
    return counts_dict
  

# if this file is called ("python test.py")
if __name__ == '__main__':
    # print default report
    print(create_report())
