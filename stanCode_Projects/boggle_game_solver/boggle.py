"""
File: boggle.py
Name: Jim Chiu
----------------------------------------
This program create a 4x4 square tray with 16 alphabets on it, allowing user to input each alphabet.
Then the program will find all vocabularies which are composed of adjacent alphabets and print all of them.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary_set = set()
words_count = 0


def main():
    """
    This program create a 4x4 square tray with 16 alphabets on it, allowing user to input each alphabet.
    Then the program will find all vocabularies which are composed of adjacent alphabets and print all of them.
    """
    global words_count
    global dictionary_set
    word = [[], [], [], []]
    for i in range(len(word)):
        line = input(f'{i + 1} row of letters: ')
        word[i] = line.lower().split()
        # cases of illegal input
        if len(word[i]) != 4:
            print('Illegal input')
            return
        for j in word[i]:
            if not j.isalpha() or len(j) > 1:
                print('Illegal input')
                return
    read_dictionary(word)
    boggle(word)
    print(f'There are {words_count} words in total.')


def boggle(word):
    """
    :param word: the nested list of the alphabets of the boggle
    :return: None
    """
    found_list = []
    for i in range(4):
        for j in range(4):
            boggle_helper(word, [(i, j)], word[i][j], i, j, found_list)


def boggle_helper(word, used_position, current_word, x, y, found_list):
    """
    :param word: the nested list of the alphabets of the boggle
    :param used_position: the (x, y) coordinates which have been used
    :param current_word: the current word that the program is processing
    :param x: the x coordinate of the boggle
    :param y: the y coordinate of the boggle
    :param found_list: the list which is made up of vocabularies we found
    :return: None
    """
    global dictionary_set
    global words_count
    if current_word in dictionary_set and current_word not in found_list:
        print(f'Found \"{current_word}\"')
        found_list.append(current_word)
        # for a word which is start from other word, such as room and roomy
        dictionary_set.remove(current_word)
        if has_prefix(current_word):
            boggle_helper(word, used_position, current_word, x, y, found_list)
        words_count += 1
    else:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 4 > x + i >= 0 and 4 > y + j >= 0 and (x + i, y + j) not in used_position:
                    if has_prefix(current_word + word[x + i][y + j]):
                        new_x = x + i
                        new_y = y + j
                        used_position.append((new_x, new_y))
                        boggle_helper(word, used_position, current_word + word[new_x][new_y], new_x, new_y, found_list)
                        used_position.pop()


def read_dictionary(word):
    """
    This function creates a global dictionary list by importing a dictionary file
    :return: None
    """
    global dictionary_set
    with open(FILE, 'r') as f:
        line = f.readline()
        while line is not None and line != '':
            line = line.strip()
            # add words which are longer than 4
            if len(line) >= 4:
                # add words only consist of the alphabets of the boggle
                for i in range(4):
                    for j in range(4):
                        if word[i][j] in line:
                            dictionary_set.add(line)
                            break
                    if line in dictionary_set:
                        break
            line = f.readline()


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    global dictionary_set
    for word in dictionary_set:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
