import re

email = 'purple alice-b@google.com monkey dishwasher'

# get only one characters within the set of chars using []
vowels = r"[aeiou]"
lowercase_letters = r"[a-z]"
uppercase_letters = r"[A-Z]"
all_letters = r"[A-z]"
numbers = r"[0-9]"


# repeat_once_or_more = r"+"
# repetion_zero_or_more = r"*"
# repetion_zero_or_once = r"?"
# exclude = r"^"
# group = r"()"


# ============================= search() ==========================
match1 = re.search(r'\w+@\w+', email)
if match1:
    print(match1.group())    # b@google


match2 = re.search(r'[\w.-]+@[\w.-]+', email)
if match2:
    print(match2.group())   # alice-b@google.com


match3 = re.search(r"([\w.-]+)@([\w.-]+)", email)
if match3:
    print("line 33 ", match3.group())
    print("line 34 ",match3.group(1))  # the first ()
    print("line 35 ",match3.group(2))  # the 2nd ()
    # alice-b@google.com
    # alice-b
    # google.com


# =========================== findall() =================================
text = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
emails = re.findall(r'[\w.-]+@[\w.-]+', text)
print("line 44 ", emails)

findall_groups = re.findall(r'([\w.-]+)@([\w.-]+)', text)
print("line 47 ", findall_groups)
# line 47  [('alice', 'google.com'), ('bob', 'abc.com')]