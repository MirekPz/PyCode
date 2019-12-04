import scholarly

search_query = scholarly.search_pubs_query('Studia Periegetica')

i = 0

while not search_query == "":
    try:
        x = next(search_query)
    except Exception as e:
        print("Koniec wyszukiwania", e)
        break
    print(x)
    i += 1
    print("Numer kolejny cytowanej pozycji: ", i)

print('*** \nLiczba cytowań: ', i, '***')


"""
print(next(search_query))

print(next(search_query))

print(next(search_query))
"""
