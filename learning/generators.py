def generator():
    company_name = "Mate academy"

    for letter in company_name:
        yield letter


g = generator()
print(next(g))
print(next(g))
print(next(g))
