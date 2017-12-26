def get_number_guesser(answer):
    last_guess = None

    def guess(n):
        nonlocal last_guess
        if n == last_guess:
            print('already guessed that!')

        last_guess = n

        return n == answer
