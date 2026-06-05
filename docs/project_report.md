# Plagiarism Detector Pro

## Project Overview

Plagiarism Detector Pro is a web-based plagiarism detection system developed using Python and Flask. The system compares a submitted document against one or more source documents and calculates similarity scores using multiple string matching and document similarity algorithms.

The application provides a user-friendly interface for uploading files, generating plagiarism reports, visualizing similarity scores, and maintaining scan history.

---

# Objectives

* Detect plagiarism between submitted and source documents.
* Compare multiple plagiarism detection algorithms.
* Generate detailed plagiarism reports.
* Visualize similarity results using charts and graphs.
* Maintain user authentication and scan history.

---

# Technologies Used

## Backend

* Python 3
* Flask
* SQLite

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Chart.js

## Database

* SQLite Database

---

# System Architecture

User → Login/Register → Upload Documents → Preprocessing → Similarity Algorithms → Score Aggregation → Report Generation → Visualization

---

# Features

## User Authentication

* User Registration
* User Login
* Session Management
* Logout

## Plagiarism Detection

The system compares a submitted document against uploaded source documents using:

### TF-IDF

Measures similarity using term frequency and inverse document frequency.

### Jaccard Similarity

Measures overlap between unique words.

### Fingerprinting

Creates document fingerprints and compares matching patterns.

### Winnowing

Uses fingerprint selection techniques for plagiarism detection.

### MinHash

Estimates document similarity using hashing techniques.

---

# Similarity Score Calculation

The final plagiarism score is computed as:

Final Score =
(TF-IDF + Jaccard + Fingerprint + Winnowing + MinHash) / 5

This provides a balanced plagiarism estimation.

---

# Modules

## app.py

Main Flask application.

Responsibilities:

* Routing
* Session handling
* File uploads
* Result rendering

## database.py

Handles:

* Database creation
* User registration
* User login
* Scan history storage

## preprocess.py

Handles:

* Text cleaning
* Sentence splitting
* Normalization

## multi_compare.py

Compares submitted document against all source files.

## sentence_similarity.py

Generates sentence-level similarity heatmaps.

## chart.py

Generates plagiarism distribution charts.

## pdf_report.py

Generates PDF plagiarism reports.

---

# Database Design

## Users Table

| Field    | Type    |
| -------- | ------- |
| id       | INTEGER |
| username | TEXT    |
| email    | TEXT    |
| password | TEXT    |

## Scans Table

| Field          | Type    |
| -------------- | ------- |
| id             | INTEGER |
| user_id        | INTEGER |
| scan_date      | TEXT    |
| submitted_file | TEXT    |
| matched_file   | TEXT    |
| score          | REAL    |

---

# Workflow

1. User registers an account.
2. User logs in.
3. User uploads:

   * Submitted document
   * Source document(s)
4. System preprocesses text.
5. Multiple algorithms calculate similarity.
6. Final score is generated.
7. Risk level is determined:

   * LOW
   * MEDIUM
   * HIGH
8. Results are displayed.
9. PDF report is generated.
10. Scan history is stored.

---

# Output Screens

## Login Page

Allows authenticated access.

## Registration Page

Creates new users with username and email.

## Upload Page

Upload submission and source files.

## Result Dashboard

Displays:

* Final Score
* Best Match
* Risk Level
* Algorithm Scores
* Benchmark Chart
* Similarity Visualization
* Sentence Heatmap
* Source Ranking

## History Page

Displays previous plagiarism scans.

---

# Advantages

* Multiple plagiarism detection algorithms.
* User authentication system.
* Interactive dashboard.
* PDF report generation.
* Scan history management.
* Easy to use interface.

---

# Limitations

* Supports text documents only.
* Uses SQLite for storage.
* Does not compare documents from online sources.

---

# Future Enhancements

* PDF and DOCX support.
* AI-powered plagiarism detection.
* Online source checking.
* Export reports in Excel format.
* User profile management.
* Cloud deployment.
* Real-time plagiarism checking.

---

# Conclusion

Plagiarism Detector Pro successfully combines multiple document similarity algorithms into a single web application. The system provides accurate plagiarism analysis, detailed visualizations, report generation, and user management functionalities. The project demonstrates practical implementation of string matching, document comparison, data visualization, and web development concepts using Python and Flask.
