print("Введите пароль: pbwDWnd2")
user_input = input()
score = 0


def check_digital(user_input):
    return any(letter.isdigit() for letter in user_input)


def check_length(user_input):
    if len(user_input) < 12:
        return True


def check_letters(user_input):
    return any(letter.isalpha() for letter in user_input)


def main(score):
    if check_letters(user_input):
        print("Есть буквы")
        score += 2
    else:
        print("Нет букв")
    if check_digital(user_input):
        print("Есть цифры")
        score += 2
    else:
        print("Нет цифр")
    if check_length(user_input):
        print("Короткий")
    else:
        print("Длинный")
        score += 2
    return score


if __name__ == "__main__":
    print("Рейтинг пароля:", main(score))
