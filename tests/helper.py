from random import choices, randint
import string


def gen_rand_str(len_from, len_to):
    return "".join(choices(string.ascii_lowercase + string.digits + "_", k=randint(len_from, len_to)))

def gen_rand_email():
    return f"test_{gen_rand_str(2, 19)}@example.com"