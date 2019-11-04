"""
Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.
"""

mixed_list = [13, 'string', 2.45, [1, 2, 3], ('a', 'b'), False, True]
for i in mixed_list:
    try:
        10/i
        print(i, " ----- wynik: ", 10/i)
    except Exception as ex:
        print("Błąd", " =====> ", i, " =====> ", ex)




