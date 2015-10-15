# _*_ coding: utf-8 _*_
from models import User


def get_email_provider(key):

    email_providers = {
        'mail.ru': [u"Почта Mail.Ru", "https://e.mail.ru/"],
        'bk.ru': [u"Почта Mail.Ru (bk.ru)", "https://e.mail.ru/"],
        'list.ru': [u"Почта Mail.Ru (list.ru)", "https://e.mail.ru/"],
        'inbox.ru': [u"Почта Mail.Ru (inbox.ru)", "https://e.mail.ru/"],
        'yandex.ru': [u"Яндекс.Почта", "https://mail.yandex.ru/"],
        'ya.ru': [u"Яндекс.Почта", "https://mail.yandex.ru/"],
        'yandex.ua': [u"Яндекс.Почта", "https://mail.yandex.ua/"],
        'yandex.by': [u"Яндекс.Почта", "https://mail.yandex.by/"],
        'yandex.kz': [u"Яндекс.Почта", "https://mail.yandex.kz/"],
        'yandex.com': [u"Yandex.Mail", "https://mail.yandex.com/"],
        'gmail.com': [u"Gmail", "https://mail.google.com/"],
        'googlemail.com': [u"Gmail", "https://mail.google.com/"],
        'outlook.com': [u"Outlook.com", "https://mail.live.com/"],
        'hotmail.com': [u"Outlook.com (Hotmail)", "https://mail.live.com/"],
        'live.ru': [u"Outlook.com (live.ru)", "https://mail.live.com/"],
        'live.com': [u"Outlook.com (live.com)", "https://mail.live.com/"],
        'me.com': [u"iCloud Mail", "https://www.icloud.com/"],
        'icloud.com': [u"iCloud Mail", "https://www.icloud.com/"],
        'rambler.ru': [u"Рамблер-Почта", "https://mail.rambler.ru/"],
        'yahoo.com': [u"Yahoo! Mail", "https://mail.yahoo.com/"],
        'ukr.net': [u"Почта ukr.net", "https://mail.ukr.net/"],
        'i.ua':    [u"Почта I.UA", "http://mail.i.ua/"],
        'bigmir.net': [u"Почта Bigmir.net", "http://mail.bigmir.net/"],
        'tut.by': [u"Почта tut.by", "https://mail.tut.by/"],
        'inbox.lv': [u"Inbox.lv", "https://www.inbox.lv/"],
        'mail.kz': [u"Почта mail.kz", "http://mail.kz/"],
    }

    if key in email_providers:
        return email_providers[key]
    return False

