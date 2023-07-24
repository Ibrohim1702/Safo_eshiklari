from collections import OrderedDict


def basketFormat(data):
    return OrderedDict({
        "product":data.product.name_uz,
        "quantity":data.quantity,
    })


def format_cnt(data):
    return {
        "id": data.id,
        "name": data.name,
        "phone": data.phone,
    }


def format_ctg(data):
    return {
        "id": data.id,
        "name": data.name,
        "key": data.key,
        "is_menu": data.is_menu,
    }