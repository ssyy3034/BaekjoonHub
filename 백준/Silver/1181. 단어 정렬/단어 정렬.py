words  = int(input())
word_list = set(input().strip() for _ in range(words))

sorted_word_list = sorted(word_list, key=lambda x: (len(x),x))

for pr in range(len(sorted_word_list)):
    print(sorted_word_list[pr])
