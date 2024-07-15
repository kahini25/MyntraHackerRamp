from collections import Counter
import matplotlib.pyplot as plt

# Sample data: a list of hashtags extracted from posts
hashtags = [
    "#fashion", "#style", "#ootd", "#fashion", "#style",
    "#fashionista", "#summerfashion","bohostyle", "#fashion", "#fashionista",
    "#vintagefashion", "#streetstyle", "#style", "#fashionblogger", "bohostyle",
    "#fallfashion", "#fashionweek", "#sustainablefashion", "#style", "bohostyle",
]

# Count the frequency of each hashtag
hashtag_counts = Counter(hashtags)

# Identify the most common hashtags
common_hashtags = hashtag_counts.most_common(10)  # Top 10 hashtags

# Visualize the top 10 common hashtags
labels, counts = zip(*common_hashtags)
plt.bar(labels, counts)
plt.xlabel('Hashtags')
plt.ylabel('Frequency')
plt.title('Top 10 Common Hashtags on Instagram')
plt.xticks(rotation=45)
plt.show()