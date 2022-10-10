STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


# def print_word_freq(file):
#     """Read in `file` and print out the frequency of words in that file."""
import string
with open ("praise_song_for_the_day.txt", "r") as f:
    text = f.read()
    text = text.lower()
    words = text.split()
    table =str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in words]
    # print (stripped)

    resultwords  = [word for word in stripped if word not in STOP_WORDS]
    # result = ' '.join(resultwords)
    # print(resultwords)

count_we = str(resultwords.count("we"))
count_each = str(resultwords.count("each"))
count_or = str(resultwords.count("or"))
count_need = str(resultwords.count("need"))
count_love = str(resultwords.count("love"))
count_about = str(resultwords.count("about"))
count_praise = str(resultwords.count("praise"))
count_song = str(resultwords.count("song"))
count_day = str(resultwords.count("day"))
count_our = str(resultwords.count("our"))


print ("we |", count_we, int(count_we) * '*')
print ("each |", count_each, int(count_each) * '*')
print ("or |", count_or, int(count_or) * '*')
print ("need |", count_need, int(count_need) * '*')
print ("love |", count_love, int(count_love) * '*')
print ("about |", count_about, int(count_about) * '*')
print ("praise |", count_praise, int(count_praise) * '*')
print ("song |", count_song, int(count_song) * '*')
print ("day |", count_day, int(count_day) * '*')
print ("our |", count_our, int(count_our) * '*')

# def word_counter(w):
#     str(resultwords.count(w))

# print(word_counter("each"))



# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
