import random
import string


def random_user_id(x):
    characters=string.ascii_letters+string.digits
    return "".join(random.choice(characters) for _ in range(x))


