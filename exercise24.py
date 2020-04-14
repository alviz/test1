
def print_field(size):
    for _ in range(size):
        print(' ' + '--- ' * size)
        print('|' + '   |' * size)
    print(' ' + '--- ' * size)


if __name__=="__main__":
    print_field(10)
#
# a = '---'.join('    ')
# b = '   '.join('||||')
# print('\n'.join((a, b, a, b, a, b, a)))