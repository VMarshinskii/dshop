# coding=utf-8
from models import Product

SORTED_PRODUCT_OPTION = {
    'default': 'по умолчанию',
    'ascending_prices': 'по возростанию цены',
    'descending_prices': 'по убыванию цены',
    'by_popularity': 'по популярности',
    'by_newest': 'по новинкам',
    'by_sale': 'по скидкам',
}

def sorted_product(products, field):
    if field in SORTED_PRODUCT_OPTION.keys():
        if field == 'ascending_prices':
            return sorted(products, key=lambda product: product.get_price())
        if field == 'descending_prices':
            return sorted(products, key=lambda product: product.get_price(), reverse=True)
        if field == 'by_popularity':
            return sorted(products, key=lambda product: product.popularity, reverse=True)
        if field == 'by_newest':
            return sorted(products, key=lambda product: product.date)
        if field == 'by_sale':
            return sorted(products, key=lambda product: product.sale_status, reverse=True)
    return products
