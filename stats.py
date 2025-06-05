def get_num_words(text):
    """
    Counts the number of words in a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def get_num_chars(text):
    """
    Counts the number of times each character appears in a given text.
    
    Args:
        text (str): The text to analyze.
        
    Returns:
        a dictionary where the keys are the characters and the values are the number of times the character appears
    """
    char_counts = {}
    text = text.lower()

    for char in text: 
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def get_sorted_char_count(char_dict):
    """
    Takes the dictionary of characters and their counts and returns a sorted list of dictionaries
    
    Args:
        dict: the dictionary output from get_num_chars()
        
    Returns:
        a sorted list of dictionaries made from the inputted argument
    """
    char_list = []

    for char, count in char_dict.items():
        char_list.append({'char': char, 'num': count})
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list