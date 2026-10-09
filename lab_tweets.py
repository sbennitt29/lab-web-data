# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.
import json
import matplotlib.pyplot as plt

tweets = []
for year in range(2009, 2019):
    filename = 'master_' + str(year) + '.json'

    with open(filename, encoding='utf-8') as f:
        data = json.load(f)

    tweets.extend(data)

print('Total tweets:', len(tweets))

print(tweets[0])

phrases = [
    'Obama',
    'Trump',
    'Mexico',
    'Russia',
    'Fake News',
    'America',
    'freedom',
    'MAGA'
]

counts = {}

for phrase in phrases:
    count = 0

    for tweet in tweets:
        message = tweet.get('full_text', tweet.get('text', ''))

        if phrase.lower() in message.lower():
            count += 1

    counts[phrase] = count

for phrase in phrases:
    print(phrase, counts[phrase])

total = len(tweets)

print('| phrase             | percent of tweets |')
print('| ------------------ | ----------------- |')


for phrase in sorted(phrases):
    percentage = counts[phrase] / total * 100
    print(f'| {phrase.lower():>18} | {percentage:17.2f} |')

names = []
percentages = []

for phrase in sorted(phrases):
    names.append(phrase)
    percentages.append(counts[phrase] / total * 100)

plt.bar(names, percentages)

plt.xlabel('Phrase')
plt.ylabel('Percentage of Tweets')
plt.title('Percentage of Tweets Containing Each Phrase')

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('tweets.png')
plt.show()