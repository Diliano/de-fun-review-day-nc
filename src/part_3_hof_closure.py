def generate_multiples(multiple):
    def generate_list_of_multiples(list_length):
        return [multiple * i for i in range(1, list_length + 1)]
    return generate_list_of_multiples


def capitaliser(func):
    def decorated_func():
        func_output = func()
        if isinstance(func_output, str):
            return func_output.upper()
        else:
            return func_output

    return decorated_func


# Advanced Challenge - Come back later!
def secure_func():
    # implement me
    pass
