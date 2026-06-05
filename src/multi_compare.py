import os

from src.preprocess import clean_text

from src.tfidf_similarity import (
    tfidf_cosine_similarity
)

from src.jaccard import (
    jaccard_similarity
)

from src.fingerprint import (
    fingerprint_similarity
)

from src.winnowing import (
    winnowing_similarity
)

from src.minhash import (
    minhash_similarity
)


def compare_against_sources(
        submitted_text,
        source_folder
):

    results = []

    submitted_clean = clean_text(
        submitted_text
    )

    for filename in os.listdir(
            source_folder
    ):

        if not filename.endswith(
                ".txt"
        ):
            continue

        file_path = os.path.join(
            source_folder,
            filename
        )

        with open(
                file_path,
                "r",
                encoding="utf-8"
        ) as file:

            source_text = file.read()

        source_clean = clean_text(
            source_text
        )

        # -------------------------
        # Similarity Algorithms
        # -------------------------

        tfidf_score = (
            tfidf_cosine_similarity(
                submitted_clean,
                source_clean
            )
        )

        jaccard_score = (
            jaccard_similarity(
                submitted_clean,
                source_clean
            )
        )

        fingerprint_score = (
            fingerprint_similarity(
                submitted_clean,
                source_clean
            )
        )

        winnowing_score = (
            winnowing_similarity(
                submitted_clean,
                source_clean
            )
        )

        minhash_score = (
            minhash_similarity(
                submitted_clean,
                source_clean
            )
        )

        # -------------------------
        # Final Score
        # -------------------------

        final_score = round(

            (

                tfidf_score +

                jaccard_score +

                fingerprint_score +

                winnowing_score +

                minhash_score

            ) / 5,

            2

        )

        results.append({

            "file": filename,

            "tfidf": tfidf_score,

            "jaccard": jaccard_score,

            "fingerprint": fingerprint_score,

            "winnowing": winnowing_score,

            "minhash": minhash_score,

            "final_score": final_score

        })

    results.sort(

        key=lambda x:
        x["final_score"],

        reverse=True

    )

    return results