def jaccard_similarity(text1, text2):

    s1 = set(text1.split())
    s2 = set(text2.split())

    intersection = len(
        s1.intersection(s2)
    )

    union = len(
        s1.union(s2)
    )

    if union == 0:
        return 0

    return round(
        (intersection / union) * 100,
        2
    )