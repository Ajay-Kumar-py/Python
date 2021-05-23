import re
## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwashe ajay54@gmail.com hjjgh  abhi32@gmail.com jkggkgjb'

## Here re.findall() returns a list of all the found email strings

emails = re.findall(r'[\w\.]+@abc[\w\.]+', str)  ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email string
    print(email)