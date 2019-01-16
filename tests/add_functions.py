from method_versioning.decorator import versioning


@versioning(version=1)
def add(number_list):
    return sum(number_list)
