import json
import csv


def save_txt(report):

    with open(

            "outputs/plagiarism_report.txt",

            "w",

            encoding="utf-8"

    ) as file:

        for key, value in report.items():

            file.write(

                f"{key}: {value}\n"

            )


def save_json(report):

    with open(

            "outputs/plagiarism_report.json",

            "w",

            encoding="utf-8"

    ) as file:

        json.dump(

            report,

            file,

            indent=4

        )


def save_csv(report):

    with open(

            "outputs/plagiarism_report.csv",

            "w",

            newline="",

            encoding="utf-8"

    ) as file:

        writer = csv.writer(file)

        writer.writerow(

            ["Metric", "Value"]

        )

        for k, v in report.items():

            writer.writerow(

                [k, str(v)]

            )