def task1(seq1, seq2, *args):
    for x in seq1, seq2:
        if not isinstance(x, (list, tuple, set, dict)):
            exit(1)
    return (sorted(set(seq1) & set(seq2)))


def task2(seq1, seq2):
    for x in seq1, seq2:
        if not isinstance(x, (list, tuple)):
            exit(1)
    if isinstance(seq2, (tuple)):
        seq2 = list(seq2)
    x = 0
    mydict = {}
    while x < int(len(seq1)):
        if x + 1 > int(len(seq2)):
            seq2.append(None)
        mydict.update({seq1[x]: seq2[x]})
        x = x + 1
    return(mydict)


def task3(seq):
    x = 0
    result = []
    while x < len(seq):
        if isinstance(seq[x], str):
           exit(1)
        if isinstance(seq[x], int):
            result.append(seq[x])
        else:
            result=result+list(seq[x])
        x=x+1
    return(sorted(result))


#task2((), [1, 2, 3])

task1([1, 2, 3], [2, 3, 4])
task1(['foo', True, 42], (True, 42, 'baz'))
task1((99, 22, 11, 44), {'test', 99, 22.0})
task1({1, 2, 3}, {6, 5, 4})
task2(['a', 'b', 'c', 'd', 'e'], [1, 2, 3])
task2(['a', 'b', 'c'], [1, 2, 3])
task2(['a', 'b', 'c', 'd', 'e'], (1, 2, 3))
task3([1, 2, 3, (4, 5), [6, 7], {8, 9}])
task3(set())
task3((set(), (1, ), [42], 1, 99, []))

9
#task3([1, 2, 3, (4, 5), [6, 7], {8, 9}])
