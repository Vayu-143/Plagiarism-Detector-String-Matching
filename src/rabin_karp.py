def rabin_karp(text, pattern):

    d = 256
    q = 101

    n = len(text)
    m = len(pattern)

    if m > n:
        return []

    p = 0
    t = 0

    h = 1

    matches = []

    for _ in range(m - 1):

        h = (h * d) % q

    for i in range(m):

        p = (d * p + ord(pattern[i])) % q

        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):

        if p == t:

            if text[i:i+m] == pattern:

                matches.append(i)

        if i < n - m:

            t = (

                d *

                (t - ord(text[i]) * h)

                + ord(text[i+m])

            ) % q

            if t < 0:
                t += q

    return matches