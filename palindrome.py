def reverse(a):
    a = a[::-1]
    return a

def palindrome(strx):
    rev = reverse(strx)
    if strx==rev:
        return True
    else:
        return False

string1 = 'dad'
string2 = 'malayalam'
string3 = 'hello'

print(palindrome(string1))
print(palindrome(string2))
print(palindrome(string3))
