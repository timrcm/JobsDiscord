from os import listdir

with open('./content/quotes.txt', 'r') as f:
    usable_quotes = sum(1 for _ in f.readlines()) // 2

usable_windows = len(listdir('./content/windows')) // 2

quotes = []
windows = []