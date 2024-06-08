def bubble_sort(_list):
    for i in range(len(_list)):
        for j in range(len(_list) - 1):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
    return _list