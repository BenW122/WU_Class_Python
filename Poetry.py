import requests
from collections import Counter

r = requests.get("http://gutenberg.org/files/11/11-0.txt")
x = r.text

ignore = {"the","and","to","a","of","she","said","in","was","you","I","as","that","with","at","her","had","all"}
wordcount = Counter(x.split())
print(wordcount.most_common(20))



file = open("alice.txt","r")

from collection import Counter
cnt = Counter(file.read().split())

for word in file:
	word = word.lower()
	cnt[word.lower()] += 1
print(cnt.most_common(10))