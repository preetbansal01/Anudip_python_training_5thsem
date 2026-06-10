reviews = [
    "excellent movie", 
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# 1. Count sentiments
def count_sentiments(reviews):
    excellent = good = poor = average = 0
    for review in reviews :
        if reviews.startswith(excellent):
            excellent += 1

        elif reviews.startswith(good):
            good += 1
        
        elif reviews.startswith(poor):
            poor += 1

        elif reviews.startswith(average):
            average += 1

        return excellent , poor ,good ,average
    
# 2. Most common word
def most_common_word (reviews):
    for review in reviews :
        word_count = {}

    for review in reviews:
        words = review.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    return max(word_count, key=word_count.get)

# 3. Longest review
def longest_review(reviews):
    return max(reviews, key=len)


# 4. Reviews containing a keyword
def reviews_with_keyword(reviews, keyword):
    return [review for review in reviews if keyword.lower() in review.lower()]


# Driver Code
excellent, good, average, poor = count_sentiments(reviews)

print("Excellent Reviews:", excellent)
print("Good Reviews:", good)
print("Average Reviews:", average)
print("Poor Reviews:", poor)

print("\nMost Common Word:", most_common_word(reviews))

print("\nLongest Review:", longest_review(reviews))

keyword = "excellent"
print(f"\nReviews containing '{keyword}':")
for review in reviews_with_keyword(reviews, keyword):
    print(review)
    
