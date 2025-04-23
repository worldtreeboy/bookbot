from stats import get_book_text, get_book_string, get_report
import sys

def main(): 
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exits with code 1 to indicate an error
    # s = get_book_text(sys.argv[1]) 
    #split_string = s.split()
    s2 = get_book_string(sys.argv[1]) 
   
    get_report(s2)
 
     
if __name__ == "__main__": 
    main()
    
