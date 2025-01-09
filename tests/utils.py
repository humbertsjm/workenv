import string
import random

def get_random_string_from_length(length: int=1) -> str:
    alphabet = string.ascii_letters
    return ''.join([random.choice(alphabet) for x in range(length)])


if __name__ == "__main__":
    pass
