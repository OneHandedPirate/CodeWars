# An anagram is a word, a phrase, or a sentence formed from another by
# rearranging its letters. An example of this is "angel", which is an anagram of "glean".
#
# Write a function that receives an array of words, and returns the total number
# of distinct pairs of anagramic words inside it.
#
# Some examples:
#
# There are 2 anagrams in the array ["dell", "ledl", "abc", "cba"]
# There are 7 anagrams in the array ["dell", "ledl", "abc", "cba", "bca", "bac"]


def anagram_counter(words: list[str]) -> int:
    count = 0
    for i in range(len(words) - 1):
        count += len([w for w in words[i + 1:] if sorted(words[i]) == sorted(w)])
    return count
