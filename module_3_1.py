calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    tuple_ = len(string), string.upper(), string.lower()
    count_calls()
    return tuple_
def is_contains(string, list_to_search):
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string.lower() in list_to_search:
        return 'True'
    else:
        return 'False'
print(string_info('Copybara'))
print(string_info('Armagedon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)