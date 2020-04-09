#######################  exercise 6 (String Palindrome)
# BEST
string = input('Input string:')
if string == string[::-1]:
    print('Palindrome')
else:
    print('NON Palindrome')

# --- my
# string = input('Input string:')
# for index in range(0,int(len(string)/2)):
#     if string[index] != string[-1-index]:
#         print('Non palindrome')
#         exit()
#
# print('Palindrome')
