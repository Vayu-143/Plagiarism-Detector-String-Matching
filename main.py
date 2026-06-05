from colorama import Fore, init

from src.multi_compare import compare_against_sources

from src.preprocess import (
    clean_text,
    split_sentences
)

from src.sentence_similarity import (
    sentence_heatmap
)

from src.report import (
    save_txt,
    save_json,
    save_csv
)

from src.html_report import (
    generate_html
)

from src.pdf_report import (
    generate_pdf
)

init(autoreset=True)


def main():

    print(
        Fore.CYAN +
        "\nStarting Plagiarism Detection System..."
    )

    # --------------------------------------------------
    # Read Submitted File
    # --------------------------------------------------

    try:

        with open(
                "documents/submitted.txt",
                "r",
                encoding="utf-8"
        ) as file:

            submitted_text = file.read()

    except FileNotFoundError:

        print(
            Fore.RED +
            "documents/submitted.txt not found."
        )

        return

    # --------------------------------------------------
    # Compare Against All Source Files
    # --------------------------------------------------

    results = compare_against_sources(
        submitted_text,
        "sources"
    )

    if len(results) == 0:

        print(
            Fore.RED +
            "No source documents found."
        )

        return

    # --------------------------------------------------
    # Best Match
    # --------------------------------------------------

    best_match = results[0]

    # --------------------------------------------------
    # Sentence Similarity Heatmap
    # --------------------------------------------------

    source_file_path = (
        f"sources/{best_match['file']}"
    )

    with open(
            source_file_path,
            "r",
            encoding="utf-8"
    ) as file:

        source_text = file.read()

    submitted_sentences = split_sentences(
        clean_text(submitted_text)
    )

    source_sentences = split_sentences(
        clean_text(source_text)
    )

    heatmap = sentence_heatmap(
        submitted_sentences,
        source_sentences
    )

    # --------------------------------------------------
    # Build Report
    # --------------------------------------------------

    report = {

        "Submitted File":
            "submitted.txt",

        "Best Matching File":
            best_match["file"],

        "TF-IDF Similarity (%)":
            best_match["tfidf"],

        "Jaccard Similarity (%)":
            best_match["jaccard"],

        "Fingerprint Similarity (%)":
            best_match["fingerprint"],

        "Final Similarity Score (%)":
            best_match["final_score"],

        "Sentence Heatmap":
            heatmap,

        "All Source Results":
            results
    }

    # --------------------------------------------------
    # Save Reports
    # --------------------------------------------------

    save_txt(report)

    save_json(report)

    save_csv(report)

    generate_html(report)

    generate_pdf(report)

    # --------------------------------------------------
    # Terminal Dashboard
    # --------------------------------------------------

    print(
        Fore.GREEN +
        "\n" +
        "=" * 70
    )

    print(
        "PLAGIARISM DETECTION REPORT"
    )

    print(
        "=" * 70
    )

    print(
        Fore.YELLOW +
        f"\nBest Matching File : "
        f"{best_match['file']}"
    )

    print(
        f"TF-IDF Similarity  : "
        f"{best_match['tfidf']}%"
    )

    print(
        f"Jaccard Similarity : "
        f"{best_match['jaccard']}%"
    )

    print(
        f"Fingerprint Score  : "
        f"{best_match['fingerprint']}%"
    )

    print(
        Fore.RED +
        f"\nFINAL SCORE : "
        f"{best_match['final_score']}%"
    )

    # --------------------------------------------------
    # Source Ranking
    # --------------------------------------------------

    print(
        Fore.CYAN +
        "\nSOURCE DOCUMENT RANKING"
    )

    print("-" * 70)

    for rank, item in enumerate(
            results,
            start=1
    ):

        print(

            f"{rank}. "

            f"{item['file']} "

            f"-> "

            f"{item['final_score']}%"

        )

    # --------------------------------------------------
    # Sentence Heatmap
    # --------------------------------------------------

    print(
        Fore.MAGENTA +
        "\nSENTENCE HEATMAP"
    )

    print("-" * 70)

    for idx, item in enumerate(
            heatmap,
            start=1
    ):

        sentence = item[0]
        score = item[1]

        print(
            f"{idx}. "
            f"{score}% "
            f"-> "
            f"{sentence[:80]}"
        )

    # --------------------------------------------------
    # Generated Files
    # --------------------------------------------------

    print(
        Fore.GREEN +
        "\nGenerated Reports"
    )

    print("-" * 70)

    print(
        "TXT  : outputs/report.txt"
    )

    print(
        "JSON : outputs/report.json"
    )

    print(
        "CSV  : outputs/report.csv"
    )

    print(
        "HTML : outputs/report.html"
    )

    print(
        "PDF  : reports/plagiarism_report.pdf"
    )

    print(
        Fore.GREEN +
        "\nAnalysis Completed Successfully."
    )


if __name__ == "__main__":
    main()