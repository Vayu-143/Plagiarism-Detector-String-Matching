# Project Architecture

## Plagiarism Detector Pro – System Architecture

```text
┌─────────────────────────────┐
│          USER               │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│      Flask Web Interface    │
│  (Login, Register, Upload)  │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│       Authentication        │
│   User Login & Registration │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│      File Upload Module     │
│ Submitted & Source Files    │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│     Text Preprocessing      │
│ • Text Cleaning             │
│ • Tokenization              │
│ • Sentence Splitting        │
│ • Normalization             │
└─────────────┬───────────────┘
              │
              ▼
┌────────────────────────────────────────┐
│      Similarity Detection Engine       │
├────────────────────────────────────────┤
│ TF-IDF Similarity                      │
│ Jaccard Similarity                     │
│ Fingerprinting Algorithm               │
│ Winnowing Algorithm                    │
│ MinHash Algorithm                      │
└─────────────┬──────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│    Score Aggregation Layer  │
│ Calculates Final Score      │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│      Risk Assessment        │
│ LOW / MEDIUM / HIGH         │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│        Visualization Module         │
├─────────────────────────────────────┤
│ Similarity Chart                    │
│ Algorithm Benchmark Chart           │
│ Sentence Similarity Heatmap         │
│ Source Ranking Table                │
└─────────────┬───────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│      Report Generation      │
│ HTML Report                 │
│ PDF Report                  │
│ CSV / JSON Export           │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│      SQLite Database        │
├─────────────────────────────┤
│ Users                       │
│ Scan History                │
│ Report Metadata             │
└─────────────────────────────┘
```

---

# Architectural Layers

## Presentation Layer

Responsible for user interaction.

Components:

* Login Page
* Registration Page
* Upload Dashboard
* Detection Result Dashboard
* History Page

Technologies:

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Chart.js

---

## Application Layer

Controls application flow.

Components:

* Flask Routes
* Session Management
* Request Handling
* File Management

Files:

* app.py

---

## Business Logic Layer

Performs plagiarism detection.

Modules:

* preprocess.py
* multi_compare.py
* sentence_similarity.py

Algorithms:

* TF-IDF
* Jaccard
* Fingerprinting
* Winnowing
* MinHash

---

## Data Layer

Stores application data.

Database:

* SQLite

Tables:

### Users

| Field    | Type    |
| -------- | ------- |
| id       | INTEGER |
| username | TEXT    |
| email    | TEXT    |
| password | TEXT    |

### Scans

| Field          | Type    |
| -------------- | ------- |
| id             | INTEGER |
| user_id        | INTEGER |
| scan_date      | TEXT    |
| submitted_file | TEXT    |
| matched_file   | TEXT    |
| score          | REAL    |

---

# Data Flow

1. User logs into the system.
2. User uploads a submission file.
3. User uploads one or more source documents.
4. Text preprocessing is applied.
5. Similarity algorithms calculate scores.
6. Final plagiarism score is generated.
7. Risk level is determined.
8. Results are visualized.
9. Report is generated.
10. Scan history is stored in SQLite.

---

# Final Score Formula

Final Score =

(TF-IDF + Jaccard + Fingerprint + Winnowing + MinHash) / 5

This ensures balanced evaluation across multiple plagiarism detection techniques.
