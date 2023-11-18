import random
min_num = 0
max_num = 2
def generate_single_random(min_num, max_num):
    random_number = random.randint(min_num, max_num)
    return random_number
print(generate_single_random(min_num, max_num))