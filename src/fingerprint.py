def generate_ngrams(
        text,
        n=5
):

    words = text.split()

    return set(

        tuple(words[i:i+n])

        for i in range(
            len(words)-n+1
        )

    )


def fingerprint_similarity(
        text1,
        text2
):

    fp1 = generate_ngrams(text1)

    fp2 = generate_ngrams(text2)

    if not fp1:
        return 0

    common = fp1.intersection(fp2)

    return round(

        len(common) /

        len(fp1) * 100,

        2

    )