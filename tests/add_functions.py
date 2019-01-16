from method_versioning.decorator import versioning


@versioning(version=1)
def add(number_list, test_kwarg=False):
    print('number_list', number_list)
    print('test_kwarg', test_kwarg)
    return sum(number_list)
