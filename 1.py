ptr = input()
i = int(input())
j = int(input())


def up_letters(ptr):
    '''
    checking for upper elements
    :param ptr: string input
    :return: True if string is upper, False if it is not
    '''
    if ptr.isupper():
        return True
    else:
        return False


out_filter = filter(up_letters, ptr[i - 1:j])
joined_out = ''.join(out_filter)
print(len(joined_out))
