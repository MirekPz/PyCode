import scholarly

i = 0

search_query = scholarly.search_pubs_query('Studia Periegetica')

while not search_query == "":
    print(next(search_query))
    i += 1
    print("Numer kolejny cytowanej pozycji: ", i)

print('*** \nLiczba cytowań: ', i, '***')


"""
print(next(search_query))

print(next(search_query))

print(next(search_query))
"""
