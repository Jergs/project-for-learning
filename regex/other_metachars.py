import re

pattern = r"(.+) \1"
# \d - digits
# \s - spaces
# \w - words
# uppercase (\D) - opposite
# \A - beginning of string
# \Z - ending of string
# \b - boundary between words
# \B matches the empty string anywhere else

match = re.match(pattern, "word word")
if match:
    print("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print("Match 2")

match = re.match(pattern, "abc cde")
if match:
    print("Match 3")

