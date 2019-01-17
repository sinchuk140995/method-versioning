from method_versioning.decorator import versioning


@versioning(name='multiply', version=1)
def multiply_by_two(number):
    return number * 2


@versioning(name='multiply', version=2)
def multiply_by_two_plus_one(number):
    return number * 2 + 1
