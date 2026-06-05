from difflib import SequenceMatcher


def sentence_heatmap(
        submitted_sentences,
        source_sentences
):

    results = []

    for submitted in submitted_sentences:

        best_score = 0

        for source in source_sentences:

            score = SequenceMatcher(

                None,

                submitted,

                source

            ).ratio()

            best_score = max(
                best_score,
                score
            )

        results.append(

            (
                submitted,
                round(
                    best_score * 100,
                    2
                )
            )

        )

    return results