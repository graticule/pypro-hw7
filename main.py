from stack import Stack


def check_parens(string):
    result = {True: 'Сбалансированно',
              False: 'Несбалансированно'}
    pairs = {'}': '{',
             ']': '[',
             ')': '('}
    check_stack = Stack()
    for i in string:
        if i in pairs:
            if not check_stack.is_empty() and check_stack.peek() == pairs[i]:
                check_stack.pop()
            else:
                return result[False]
        else:
            check_stack.push(i)
    if check_stack.is_empty():
        return result[True]
    else:
        return result[False]


if __name__ == '__main__':
    print(check_parens('(((([{}]))))'))
    print(check_parens('[([])((([[[]]])))]{()}'))
    print(check_parens('{{[()]}}'))
    print(check_parens('}{}'))
    print(check_parens('{{[(])]}}'))
    print(check_parens('[[{())}]'))
