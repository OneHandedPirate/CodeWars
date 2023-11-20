# The word i18n is a common abbreviation of internationalization in the developer
# community, used instead of typing the whole word and trying to spell it correctly.
# Similarly, a11y is an abbreviation of accessibility.
#
# Write a function that takes a string and turns any and all "words" (see below)
# within that string of length 4 or greater into an abbreviation, following these rules:
#
# A "word" is a sequence of alphabetical characters. By this definition, any
# other character like a space or hyphen (eg. "elephant-ride") will split up a
# series of letters into two words (eg. "elephant" and "ride").
# The abbreviated version of the word should have the first letter, then the number
# of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").


def abbreviate(s: str) -> str:
    def abbr_word(w: str) -> str:
        if len(w) < 4:
            return w
        return w[0] + str(len(w) - 2) + w[-1]

    word, res = "", ""

    for char in s:
        if char.isalpha():
            word += char
        else:
            res += abbr_word(word) + char
            word = ""
    res += abbr_word(word)
    return res


assert abbreviate("internationalization") == "i18n"
assert abbreviate("Accessibility") == "A11y"
assert abbreviate("elephant-ride") == "e6t-r2e"
assert abbreviate("elephant-rides are really fun!") == "e6t-r3s are r4y fun!"

