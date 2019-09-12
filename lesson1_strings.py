import six

def check_arg(arg1, arg2):
    if not isinstance(arg1, str) or not isinstance(arg2, str):
        return 0
    elif arg1 == arg2:
        return 1
    elif arg1 != arg2 and len(arg1) > len(arg2):
        return 2
    elif arg1 != arg2 and arg2 == 'learn':
        return 3

print(check_arg(12, 43))
print(check_arg('12', '12'))
print(check_arg('123', '12'))
print(check_arg('12', 'learn'))