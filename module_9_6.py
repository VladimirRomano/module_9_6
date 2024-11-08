def all_variants(text):
    t = len(text)
    for k in range(1, t + 1):
        for d in range(t - k + 1):
            v = k + d
            yield text[d:v]


a = all_variants("abc")
for i in a:
    print(i)