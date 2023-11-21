# Complete the solution so that it returns the number of times the search_text
# is found within the full_text.
#
# search_substr( full_text, search_text, allow_overlap = True )
# so that overlapping solutions are (not) counted. If the searchText is empty,
# it should return 0. Usage examples:
#
# search_substr('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
# search_substr('aaabbbcccc', 'bbb') # should return 1
# search_substr( 'aaa', 'aa' ) # should return 2
# search_substr( 'aaa', '' ) # should return 0
# search_substr( 'aaa', 'aa', False ) # should return 1

def search_substr(full_text: str, search_text: str, allow_overlap=True) -> int:
    if not search_text:
        return 0

    if allow_overlap:
        count = 0
        for i in range(len(full_text) - len(search_text) + 1):
            if full_text[i:i + len(search_text)] == search_text:
                count += 1
        return count
    else:
        return full_text.count(search_text)


assert search_substr('aaa', 'aa', False) == 1
assert search_substr('aa_bb_cc_dd_bb_e', 'bb') == 2
assert search_substr('aaacccbbbcccc', 'cc') == 5
assert search_substr('aaabbbaaa', 'bb',False) == 1
