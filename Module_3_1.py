calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    global calls
    calls += 1
    a = (len(string), string.upper(), string.lower())
    return a


def is_contains(string, list_to_search):
    global calls
    calls += 1
    list_to_search = str(list_to_search).lower()
    string = str(string.lower())
    return True if string in list_to_search else False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

