import random


def minhash_similarity(
        text1,
        text2,
        num_hashes=100
):

    set1 = set(
        text1.split()
    )

    set2 = set(
        text2.split()
    )

    union = list(

        set1.union(
            set2
        )

    )

    signatures1 = []

    signatures2 = []

    for _ in range(
            num_hashes
    ):

        random.shuffle(
            union
        )

        min1 = min(

            [
                union.index(x)
                for x in set1
            ]

        )

        min2 = min(

            [
                union.index(x)
                for x in set2
            ]

        )

        signatures1.append(
            min1
        )

        signatures2.append(
            min2
        )

    matches = sum(

        1

        for a, b in zip(
            signatures1,
            signatures2
        )

        if a == b

    )

    return round(

        (
            matches
            /
            num_hashes
        )
        * 100,

        2

    )