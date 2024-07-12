def is_mail_valid(s):
    is_valid = False
    i = -1
    while s[i] != '.':
        i += -1
    ind_dot = len(s) + i
    if (s[ind_dot:len(s)] == '.ru' or s[ind_dot:len(s)] == '.com' or s[ind_dot:len(s)] == '.net') and '@' in s:
        is_valid = True
    return is_valid


def send_email(message, recipient,*, sender="university.help@gmail.com"):

    if str(recipient).lower() == str(sender).lower():
        print('Нельзя отправить письмо самому себе!')
        return
    if is_mail_valid(recipient) and is_mail_valid(sender):
        if str(sender).lower() != 'urban.info@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            return
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
            return
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


