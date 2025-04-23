def get_book_text(input):
    with open(input) as f: 
       file_contents = f.read() 
    return file_contents

def get_book_string(input): 
    with open(input) as f: 
       file_contents = f.read() 
    return str(file_contents)

def get_report(s2):
    myDict = {} 
    for string in s2:
        string = string.lower()
        if string not in myDict: 
            myDict[string] = 1 
        else: 
            myDict[string] += 1 
     
    sorted_dict = dict(sorted(myDict.items(), key = lambda x:x[1], reverse=True)) 
    
    for key,value in sorted_dict.items():
        if key.isalpha(): 
             print(f"{key}: {value}")
    
