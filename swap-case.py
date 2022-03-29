s = 'Python'
for c in s:
    # c += s
    if c.isupper():
        s = c.replace(c.upper(), c.lower())
    else:
        s = c.replace(c.lower(), c.upper())

    print(s, end='')