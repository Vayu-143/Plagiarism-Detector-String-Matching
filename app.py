from flask import (
    Flask,
    render_template,
    request,
    send_file,
    redirect,
    session
)

import os

from datetime import datetime

from src.multi_compare import (
    compare_against_sources
)

from src.preprocess import (
    clean_text,
    split_sentences
)

from src.sentence_similarity import (
    sentence_heatmap
)

from src.chart import (
    generate_chart
)

from src.database import (
    create_database,
    register_user,
    login_user,
    save_scan,
    get_user_scans
)

app = Flask(__name__)

app.secret_key = "plagiarism_detector_secret"


# ==================================================
# HOME
# ==================================================

@app.route("/")
def home():

    if "user_id" not in session:

        return redirect("/login")

    return render_template(
        "index.html"
    )


# ==================================================
# REGISTER
# ==================================================

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        success = register_user(
            username,
            email,
            password
        )

        if success:

            return redirect(
                "/login"
            )

        return "User already exists"

    return render_template(
        "register.html"
    )
# ==================================================
# LOGIN
# ==================================================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        username = request.form[
            "username"
        ]

        password = request.form[
            "password"
        ]

        user = login_user(
            username,
            password
        )

        if user:

            session[
                "user_id"
            ] = user[0]

            session[
                "username"
            ] = user[1]

            return redirect("/")

        return "Invalid Login"

    return render_template(
        "login.html"
    )


# ==================================================
# LOGOUT
# ==================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# ==================================================
# DETECT
# ==================================================

@app.route(
    "/detect",
    methods=["POST"]
)
def detect():

    if "user_id" not in session:

        return redirect(
            "/login"
        )

    uploaded_file = request.files.get(
        "submitted_file"
    )

    if not uploaded_file:

        return "No submitted file uploaded."

    submitted_text = (
        uploaded_file
        .read()
        .decode("utf-8")
    )

    upload_folder = (
        "uploads/sources"
    )

    os.makedirs(
        upload_folder,
        exist_ok=True
    )

    # ----------------------------------
    # Clear Old Files
    # ----------------------------------

    for old_file in os.listdir(
            upload_folder
    ):

        old_path = os.path.join(
            upload_folder,
            old_file
        )

        if os.path.isfile(
                old_path
        ):
            os.remove(
                old_path
            )

    # ----------------------------------
    # Upload Source Files
    # ----------------------------------

    source_files = request.files.getlist(
        "source_files"
    )

    for file in source_files:

        if file.filename:

            file.save(

                os.path.join(
                    upload_folder,
                    file.filename
                )

            )

    # ----------------------------------
    # Compare Documents
    # ----------------------------------

    results = compare_against_sources(

        submitted_text,

        upload_folder

    )

    if len(results) == 0:

     return "No source files found."

    best_match = results[0]

    # ----------------------------------
    # Algorithm Scores
    # ----------------------------------

    algorithm_scores = {

        "tfidf": best_match["tfidf"],
        "jaccard": best_match["jaccard"],
        "fingerprint": best_match["fingerprint"],
        "winnowing": best_match["winnowing"],
        "minhash": best_match["minhash"]

    }

    # ----------------------------------
    # Save Scan
    # ----------------------------------

    save_scan(

        session["user_id"],

        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        uploaded_file.filename,

        best_match["file"],

        best_match["final_score"]

    )
    # ----------------------------------
    # Read Best Match
    # ----------------------------------

    source_file_path = os.path.join(

        upload_folder,

        best_match["file"]

    )

    with open(
            source_file_path,
            "r",
            encoding="utf-8"
    ) as file:

        source_text = file.read()

    # ----------------------------------
    # Heatmap
    # ----------------------------------

    submitted_sentences = (
        split_sentences(
            clean_text(
                submitted_text
            )
        )
    )

    source_sentences = (
        split_sentences(
            clean_text(
                source_text
            )
        )
    )

    heatmap = sentence_heatmap(

        submitted_sentences,

        source_sentences

    )

    # ----------------------------------
    # Risk
    # ----------------------------------

    score = best_match[
        "final_score"
    ]

    if score >= 70:

        risk = "HIGH"

        risk_class = "high"

    elif score >= 40:

        risk = "MEDIUM"

        risk_class = "medium"

    else:

        risk = "LOW"

        risk_class = "low"

    # ----------------------------------
    # Pie Chart
    # ----------------------------------

    generate_chart(score)

    # ----------------------------------
    # Render
    # ----------------------------------

    return render_template(

    "result.html",

    best_match=best_match,

    results=results,

    heatmap=heatmap,

    risk=risk,

    risk_class=risk_class,

    algorithm_scores=algorithm_scores

)


# ==================================================
# HISTORY
# ==================================================

@app.route("/history")
def history():

    if "user_id" not in session:

        return redirect(
            "/login"
        )

    scans = get_user_scans(

        session["user_id"]

    )

    return render_template(

        "history.html",

        scans=scans

    )


# ==================================================
# DOWNLOAD PDF
# ==================================================

@app.route("/download")
def download_pdf():

    pdf_path = (
        "reports/plagiarism_report.pdf"
    )

    if not os.path.exists(
            pdf_path
    ):

        return (
            "PDF report not found."
        )

    return send_file(

        pdf_path,

        as_attachment=True

    )


# ==================================================
# RUN APP
# ==================================================

if __name__ == "__main__":

    create_database()

    os.makedirs(
        "uploads/sources",
        exist_ok=True
    )

    app.run(
        debug=True
    )