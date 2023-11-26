# Write a function that takes in a string of one or more words, and
# returns the same string, but with all five or more letter words reversed (Just
# like the name of this Kata). Strings passed in will consist of only letters
# and spaces. Spaces will be included only when more than one word is present.
#
# Examples:
#
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(s: str) -> str:
    return " ".join(w[::-1] if len(w) >= 5 else w for w in s.split())


assert spin_words("Welcome") == "emocleW"
assert spin_words("to") == "to"
assert spin_words("CodeWars") == "sraWedoC"
assert spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"