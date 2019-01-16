def versioning(version, name=''):

    def versioning_decorator(function):

        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

        setattr(wrapper, 'mv_name', name if name else function.__name__)
        setattr(wrapper, 'mv_version', version)

        return wrapper

    return versioning_decorator
