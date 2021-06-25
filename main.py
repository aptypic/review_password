user_input = input()
score = 0


def check_digital(user_input):
    return any(letter.isdigit() for letter in user_input)


def check_letters(user_input):
    return any(letter.isalpha() for letter in user_input)


def check_upper_letters(user_input):
    return any(letter.isupper() for letter in user_input)


def check_length(user_input):
    if len(user_input) > 12:
        return True


def check_symbols(user_input):
    return any((letter.isdigit() == False and letter.isalpha() == False) for letter in user_input)


def check_lower_letters(user_input):
    return any(letter.islower() for letter in user_input)


funcs_dict = [check_length(user_input), check_digital(user_input), check_letters(user_input),
              check_lower_letters(user_input), check_upper_letters(user_input), check_symbols(user_input)]


def main(score):
    for func in funcs_dict:
        if func:
            score += 2
    return score


if __name__ == "__main__":
    print("Рейтинг пароля:", main(score))
