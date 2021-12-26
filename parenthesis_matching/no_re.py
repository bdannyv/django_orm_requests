# по заданию необходимо избавиться от частей строки, которын находятся в части, не закрытой скобками. Но в описании
# задания в качестве примера приеведено 'esdfd((esdf)(esdf' -> 'esdfd((esdf)'. Но в данном примере все же есть блок с не
# закрытыми скобками, по-моему для данного задания правильным бы был ответ 'esdfd'. По тому же приницпу работает
# приведенное решение

def process(some_str: str):
    start, stack = 0, []
    for j, el in enumerate(some_str):
        if el == '(':
            stack.append(j)
        elif el == ')':
            if stack:
                stack.pop()
            else:
                # for case with unopened parentheses
                start = j + 1

    return some_str[start:stack[0]] if stack else some_str[start:]


def test():
    io = {
        'esd)fd((esdf)(esdf))': 'fd((esdf)(esdf))',
        'esdfd((esdf)(esdf': 'esdfd',
        'esd)fd((esdf)(esdf': 'fd',
        'esd)fd)((esdf)(esdf': '',
        '(esd)f)d((esdf)(esdf': 'd',
        '((esd)f)d((esdf)(esdf': '((esd)f)d',
    }

    assert all(process(case) == io[case] for case in io)


if __name__ == '__main__':
    test()
