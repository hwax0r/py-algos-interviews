"""
Created on Sat Aug 28 for Facebook Hacker Cup2021
                            Qualification Round

@author: David Sergeev
"""

# still not solved 9 Sep

VOWEL = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
CONSONANT = {'T': 0, 'R': 0, 'D': 0, 'Y': 0, 'F': 0, 'Q': 0, 'W': 0, 'Z': 0, 'H': 0,
             'G': 0, 'K': 0, 'J': 0, 'N': 0, 'C': 0, 'L': 0, 'M': 0, 'X': 0, 'B': 0,
             'P': 0, 'S': 0, 'V': 0}


def process(idx: int, word: str):
    vowel_amount: int = 0
    consonant_amount: int = 0
    dictionary: dict = {}

    for char in word:
        if char not in dictionary.keys():
            dictionary.update({char: 0})
        dictionary[char] += 1
    result = 0
    # only consonant or vowel
    if len(dictionary) == 1:
        result = 0
    main_chr = [k for k, v in dictionary.items() if v == max(dictionary.values())][0]

    print(f"Case #{idx+1}: {result} {main_chr}")
    print(f"{word} {dictionary}\n")


def main():
    # input
    input_elements: int = int(input())
    input_strings = []
    for x in range(input_elements):
        input_strings.append(input())

    for idx in range(input_elements):
        process(idx, input_strings[idx])


if __name__ == '__main__':
    main()
