#prime.py
def check_prime(number):
    for div in range(2, int(number * 0.5) + 1):
        if number % div == 0:
            return False
    return True
