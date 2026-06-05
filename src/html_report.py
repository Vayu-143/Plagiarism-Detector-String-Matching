def generate_html(report):

    html = f"""

    <html>

    <head>

    <title>
    Plagiarism Report
    </title>

    </head>

    <body>

    <h1>
    Plagiarism Detection Report
    </h1>

    <table border="1">

    """

    for key, value in report.items():

        html += f"""

        <tr>

        <td>{key}</td>

        <td>{value}</td>

        </tr>

        """

    html += """

    </table>

    </body>

    </html>

    """

    with open(
        "outputs/report.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)