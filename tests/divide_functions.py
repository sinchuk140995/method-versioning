from method_versioning.decorator import versioning


@versioning(name='divide', version=1)
def divide_by_two(number):
    return number / 2


@versioning(name='divide', version=2)
def divide_by_two_plus_one(number):
    return number / 2 + 1
