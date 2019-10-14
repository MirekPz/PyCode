"""
Przekopiuj zawartość import this do zmiennej.

>>> import this

Policz liczbę wystąpień słowa better.
Usuń z tekstu symbol gwiazdki
Zamień jedno wystąpienie explain na understand
Usuń spacje i połącz wszystkie słowa myślnikiem
Podziel tekst na osobne zdania za pomocą kropki
"""


text = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print("\nTekst oryginalny:\n")
print(text)

print("\nLiczba wystąpień słowa better:", text.count("better"), "\n")

text2 = text.replace("*", "")
print("Tekst bez gwiazdek:", "\n")
print(text2)

print("\nLiczba wystąpień słowa explain:", text.count("explain"), "\n")
text3 = text2.replace("explain", "understand", 1)
print("Zamiana pierwszego 'explain' na 'understand':", "\n")
print(text3, "\n")

print("\nMyślniki zamiast spacji:\n")
text4 = text3.replace(" ", "-")
print(text4)

text5 = text.replace("\n", "")
text6 = text5.split(".")
print("\nOsobne zdania:")
print(text6)
