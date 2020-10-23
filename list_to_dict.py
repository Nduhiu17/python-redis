def list_to_dict():
    """Python function that coverts a list to a dict"""
    lst = ['a', 1, 'b', 2, 'c', 3]

    res_dict = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}

    print(res_dict)


def list_to_dict2():
    lst = ['a', 1, 'b', 2, 'c', 3]
    it = iter(lst)
    res_dict = dict(zip(it, it))
    print(res_dict)


if __name__ == '__main__':
    list_to_dict()
    list_to_dict2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
