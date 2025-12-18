"""
🧪 Practice Task: Validate a Username
Task description

Write a function:

def is_valid_username(username: str) -> bool:


That returns True if all of the following are true:

1️⃣ Username length is at least 5 characters
2️⃣ Username contains only letters and digits
3️⃣ Username does not start with a digit

Otherwise, return False.
"""

def is_valid_username(username: str) -> bool:
    if len(username) >= 5 and username.isalnum() and not username[0].isnumeric():
        return True
    else:
        return False


# positive_username
# positive_username_isalnum
# positive_first_character
#
# negative_username
# negative_username_isalnum
# negative_first_character
#
# positive_boundaries_partitioning
# negative_boundaries_partitioning
