import urwid


def check_digital(password_review):
    return any(letter.isdigit() for letter in password_review)


def check_letters(password_review):
    return any(letter.isalpha() for letter in password_review)


def check_upper_letters(password_review):
    return any(letter.isupper() for letter in password_review)


def check_length(password_review):
    return len(password_review) > 12


def check_symbols(password_review):
    return any((not letter.isdigit() and not letter.isalpha()) for letter in password_review)


def check_lower_letters(password_review):
    return any(letter.islower() for letter in password_review)


def main(edit, new_edit):
    funcs_review = [check_length, check_digital, check_letters,
                  check_lower_letters, check_upper_letters, check_symbols]
    score = 0
    for validator in funcs_review:
        if validator(new_edit):
            score += 2
    reply.set_text("Рейтинг пароля: %s" % score)


if __name__ == "__main__":
    ask = urwid.Edit('Введите пароль:')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='middle')
    urwid.connect_signal(ask, 'change', main)
    urwid.MainLoop(menu).run()
