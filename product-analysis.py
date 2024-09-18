# Task 1: Keyword Highlighter
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

# Defining a function to iterate through the words in an individual review in search of keywords to highlight
def highlight_keyword(string):
    split_string = string.split(" ")
    for word in split_string:
        for keyword in keywords:
            if keyword in word.lower():
                split_string[split_string.index(word)] = word.upper()
    return " ".join(split_string)

# Iterating through the list of reviews and applying the 'highlight_keyword()' function to each
print("The list of reviews with highlighted keywords:\n")

for review in reviews:
    new_review = highlight_keyword(review)
    print(new_review)

# Task 2: Sentiment Tally
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Defining a function to iterate through the reviews and tally the occurences of positive and negative words
def tally_sentiments(strings):
    positive_tally = 0
    negative_tally = 0
    for string in strings:
        for word in positive_words:
            if word in string.lower():
                positive_tally += string.lower().count(word)
        for word in negative_words:
            if word in string.lower():
                negative_tally += string.lower().count(word)
    return positive_tally, negative_tally

positive_count, negative_count = tally_sentiments(reviews)

print(f"\nThe list of reviews contains {positive_count} positive words and {negative_count} negative words.")

# Task 3: Review Summary

# Defining a function to split a review into a list of characters and loop through this list until it locates a space or period to establish a coherent cutoff point
def summarize(string):
    chars = list(string)
    cutoff_num = 30
    if len(chars) > cutoff_num:
        while True:
            cutoff_char = chars[cutoff_num - 1]
            if cutoff_num == len(chars):
                return string
            elif cutoff_char == ".":
                break
            elif cutoff_char.isspace():
                break
            else:
                cutoff_num += 1
        shortened_string = chars[:cutoff_num - 1]
        shortened_string.append("...")
        return "".join(shortened_string)
    else:
        return string

# Iterating through the list of reviews and applying the 'summarize()' function to create a summary of each
print("\nThe list of reviews summarized:\n")

for review in reviews:
    summary = summarize(review.strip())
    print(summary)