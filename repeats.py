from os import listdir

with open('./content/quotes.txt', 'r') as f:
    usable_quotes = sum(1 for _ in f.readlines()) // 2

with open('./content/responses.txt', 'r') as f:
    usable_responses = sum(1 for _ in f.readlines()) // 2

usable_memes = len(listdir('./content/memes')) // 2
usable_reactions = len(listdir('./content/reactions')) // 2
usable_windows = len(listdir('./content/windows')) // 2

memes = []
reactions = []
responses = []
quotes = []
windows = []
