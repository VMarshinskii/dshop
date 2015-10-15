# _*_ coding: utf-8 _*_
from models import User


def get_email_provider(key):

    email_providers = {
        'mail.ru': [u"Почта Mail.Ru", u"https://e.mail.ru/"],
        'bk.ru': [u"Почта Mail.Ru (bk.ru)", u"https://e.mail.ru/"],
        'list.ru': [u"Почта Mail.Ru (list.ru)", u"https://e.mail.ru/"],
        'inbox.ru': [u"Почта Mail.Ru (inbox.ru)", u"https://e.mail.ru/"],
        'yandex.ru': [u"Яндекс.Почта", u"https://mail.yandex.ru/"],
        'ya.ru': [u"Яндекс.Почта", u"https://mail.yandex.ru/"],
        'yandex.ua': [u"Яндекс.Почта", u"https://mail.yandex.ua/"],
        'yandex.by': [u"Яндекс.Почта", u"https://mail.yandex.by/"],
        'yandex.kz': [u"Яндекс.Почта", u"https://mail.yandex.kz/"],
        'yandex.com': [u"Yandex.Mail", u"https://mail.yandex.com/"],
        'gmail.com': [u"Gmail", u"https://mail.google.com/"],
        'googlemail.com': [u"Gmail", u"https://mail.google.com/"],
        'outlook.com': [u"Outlook.com", u"https://mail.live.com/"],
        'hotmail.com': [u"Outlook.com (Hotmail)", u"https://mail.live.com/"],
        'live.ru': [u"Outlook.com (live.ru)", u"https://mail.live.com/"],
        'live.com': [u"Outlook.com (live.com)", u"https://mail.live.com/"],
        'me.com': [u"iCloud Mail", u"https://www.icloud.com/"],
        'icloud.com': [u"iCloud Mail", u"https://www.icloud.com/"],
        'rambler.ru': [u"Рамблер-Почта", u"https://mail.rambler.ru/"],
        'yahoo.com': [u"Yahoo! Mail", u"https://mail.yahoo.com/"],
        'ukr.net': [u"Почта ukr.net", u"https://mail.ukr.net/"],
        'i.ua':    [u"Почта I.UA", u"http://mail.i.ua/"],
        'bigmir.net': [u"Почта Bigmir.net", u"http://mail.bigmir.net/"],
        'tut.by': [u"Почта tut.by", u"https://mail.tut.by/"],
        'inbox.lv': [u"Inbox.lv", u"https://www.inbox.lv/"],
        'mail.kz': [u"Почта mail.kz", u"http://mail.kz/"],
    }

    if key in email_providers:
        return email_providers[key]
    return False

