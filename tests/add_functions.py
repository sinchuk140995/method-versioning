from method_versioning.decorator import versioning


@versioning(name='add', version=1)
def add_list_items(number_list):
    return sum(number_list)


@versioning(name='add', version=2)
def add_list_items_plus_one(number_list):
    return sum(number_list) + 1
