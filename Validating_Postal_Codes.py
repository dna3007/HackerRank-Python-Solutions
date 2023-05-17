"""
A valid postal code P have to fulfill both below requirements:

P must be a number in the range from 100000 to 999999 inclusive.
P must not contain more than one alternating repetitive digit pair.
P Alternating repetitive digits are digits which repeat immediately after the next digit. In other words,
an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
"""
import re

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(?=([\d])([\d])(\1))"

P = input()

print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

"""
r'(\d)(?=\d\1)'
 regular expression pattern matches any digit that has the same digit immediately following it, 
without capturing the second digit. Here is a breakdown of the pattern:

\d matches any digit (0-9). () specifies a capturing group, which captures the digit matched by \d so that it can be 
referenced later. (?=\d\1) is a positive lookahead assertion that checks if the next character after the digit that 
was matched by \d is also a digit \d that is the same digit matched earlier \1. In other words, this lookahead 
assertion matches any digit that is followed by the same digit as itself. So, the overall match will capture the 
first digit in any pair of adjacent digits that are the same."""
