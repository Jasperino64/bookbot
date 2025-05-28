import sys
from stats import word_count, char_count, sort_counts

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    count = word_count(book_text)
    counts = char_count(book_text)
    sorted_counts = sort_counts(counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for c in sorted_counts:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()