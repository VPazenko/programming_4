def doubler(number):
    return number * 2

def tripler(number):
    return number * 3


def func_to_list(list_sample, func):
    '''
    function applies the arg-function to a given data set and returns list of values
    '''
    new_list = [func(elem) for elem in list_sample]
    return new_list


def func_to_list_mod(list_sample, *func):
    '''
    function applies all n arg-functions to a given data set and returns a list of n lists
    '''
    new_list = [[f(elem) for elem in list_sample] for f in func]
    return new_list


if __name__ == '__main__':
    function = doubler
    function2 = tripler
    list_ = [1, 2, 3, 4, 5]
    new = func_to_list(list_, function)
    print(new)

    new = func_to_list_mod(list_, function, function2)
    print(new)
