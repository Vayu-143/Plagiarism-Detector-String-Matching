import matplotlib.pyplot as plt
import os

def generate_chart(score):

    os.makedirs(
        "static",
        exist_ok=True
    )

    labels = [
        "Matched",
        "Unique"
    ]

    values = [
        score,
        100 - score
    ]

    plt.figure(figsize=(5,5))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title(
        "Plagiarism Distribution"
    )

    plt.savefig(
        "static/similarity_chart.png"
    )

    plt.close()