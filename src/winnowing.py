import hashlib


def generate_fingerprints(
        text,
        k=5
):

    words = text.split()

    shingles = []

    for i in range(

            len(words) - k + 1

    ):

        shingle = " ".join(

            words[i:i + k]

        )

        hash_value = int(

            hashlib.md5(

                shingle.encode()

            ).hexdigest(),

            16

        )

        shingles.append(

            hash_value

        )

    return shingles


def winnowing_similarity(
        text1,
        text2
):

    fp1 = set(

        generate_fingerprints(
            text1
        )

    )

    fp2 = set(

        generate_fingerprints(
            text2
        )

    )

    if not fp1 or not fp2:

        return 0

    similarity = (

        len(

            fp1.intersection(
                fp2
            )

        )

        /

        len(

            fp1.union(
                fp2
            )

        )

    )

    return round(
        similarity * 100,
        2
    )