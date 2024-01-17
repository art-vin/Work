test_lst = [
    [1, 2, 3],
    [4, 5, 6],
    [None, 8, 9],
    [10, 11, 12],
    [13, None, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, None],
]

end_lst = [
    [
        item2 if item2 is not None else 0
        for item2 in item
    ]
    for item in test_lst
]
print(end_lst)