# Move the first letter of each word to the end of it, then add "ay" to the
# end of the word. Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text: str) -> str:
    return " ".join((w[1:] + w[0] + 'ay' if w.isalpha() else w for w in text.split(' ')))


assert pig_it('Pig latin is cool') == "igPay atinlay siay oolcay"
assert pig_it('Hello world !') == "elloHay orldway !"
