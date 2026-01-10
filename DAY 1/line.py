from textblob import TextBlob

line = TextBlob("I AM HAPPY")

print(f"Polarity:{line.sentiment.polarity}")

p=line.sentiment.polarity

if p == -1.0:
    print("Negative Sentence")

elif p == 1.0:
    print("Positive Sentence0")

else :
    print("Nutral Sentence")