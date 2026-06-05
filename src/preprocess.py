import re


def clean_text(text):

    text = text.lower()

    text = re.sub(
        r'[^a-zA-Z0-9\s.]',
        ' ',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()


def split_sentences(text):

    return [
        sentence.strip()
        for sentence in text.split(".")
        if sentence.strip()
    ]