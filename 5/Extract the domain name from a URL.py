# Write a function that when given a URL as a string, parses out just
# the domain name and returns it as a string. For example:
#
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"
import re


def domain_name(url: str) -> str:
    pattern = r'^(?:http[s]?:\/\/)?(?:www\.)?([a-zA-Z0-9-]+)\.'
    match = re.match(pattern, url)
    return match.group(1)


def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"
assert domain_name("http://www.google.com") == "google"

