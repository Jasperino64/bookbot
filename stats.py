def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    
    return counts

def sort_counts(counts):
    sorted_counts = []
    for c, count in counts.items():
        sorted_counts.append({
            'char': c,
            'num': count
        })
    sorted_counts.sort(key=lambda x: x['num'], reverse=True)
    return sorted_counts