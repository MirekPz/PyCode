"""
W dowolny sposób ponumeruj wierzchołki grafu miasteczka.
Korzystając z dowolnej metody reprezentacji grafu zapisać istniejące połączenia pomiędzy budynkami.
Wyświetl wszystkie krawędzie parami, podzielone za pomocą ---
"""

lista_obiektow = ['dom', 'szkoła', 'kościół', 'bar', 'szpital', 'kino', 'teatr']

# połączenia:
graph = [
    ['0', '1', '1', '1', '0', '0', '0'],
    ['1', '0', '0', '0', '1', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '0'],
    ['0', '1', '0', '1', '0', '1', '1'],
    ['0', '0', '1', '0', '0', '0', '1'],
    ['0', '0', '0', '0', '1', '1', '0'],
]

for row in range(7):
    print(lista_obiektow[row], ":")
    for col in range(7):
        if graph[row][col] == '1':
            print(lista_obiektow[row], "<--->", lista_obiektow[col])
