#!/usr/bin/python3

import argparse
import itertools
import string
import time

parser = argparse.ArgumentParser(description='Password checker --> Find out if your password is readily available in the RockYou list or if it can be brute forced. \n Warning this program will brute force a string. This may take time and compute power.')

parser.add_argument('-p',
                    '--password',
                    help="Password you'd like to test",
                    type=str,
                    required=True)

args = parser.parse_args()

def guess_common_passwords(password):
    with open('rockyou_passwords.txt', 'r', encoding='utf-8') as passwords:
        data = passwords.read().splitlines()

    for i, match in enumerate(data):
        if match == password:
            return f'The password is {match} (Attempt #{i})'


    return 0


def brute_force(password, min_length=4, max_length=9):
    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    for password_length in range(min_length, max_length):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return f'The password is {guess} (Attempts #{attempts})'
            print(guess, attempts)


def get_password(password):
    common = guess_common_passwords(password)
    return brute_force(password) if common == 0 else common


if __name__ == '__main__':
    start_time = time.time()
    print(get_password(args.password))
    print(round(time.time() - start_time, 2), 's')