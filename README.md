FlexTools

<p align="center">
  <b>Python-Based Web Security Scanner & Input Anomaly Detector</b>
</p><p align="center">
  Structured parameter discovery • Multi-stage analysis • SQL-related error fingerprinting • Automated reporting
  <strong>Python-Based Web Security Scanner & Input Anomaly Detector</strong>
</p><p align="center">
  Parameter Discovery • Multi-Stage Analysis • SQL-Related Error Detection • Automated Reporting
>>>>>>> 40d6e45 (docs: improve README and installation guide)
</p>---

Overview

<<<<<<< HEAD
FlexTools Colored adalah tools berbasis Python yang dirancang untuk membantu proses pengujian keamanan aplikasi web, khususnya pada area input dan parameter HTTP.

Tools ini melakukan analisis terhadap target dengan pendekatan multi-stage. FlexTools membandingkan baseline response dengan response hasil variasi input, kemudian mengumpulkan berbagai sinyal seperti perubahan status HTTP, perubahan panjang response, kemiripan konten, error signature yang berkaitan dengan database, perbedaan logika response, serta anomali waktu respons.

Hasil analisis kemudian dikumpulkan, dievaluasi, dan diberikan confidence score sebelum ditampilkan di terminal dan disimpan secara otomatis ke dalam report.

FlexTools memiliki empat command utama:

- "detector" — analisis mendalam terhadap satu target.
- "scan" — melakukan analisis terhadap satu atau banyak target.
- "discover" — mencari kandidat parameter dari URL, form, dan link.
- "report" — melihat hasil report yang telah dibuat.

FlexTools Colored is a Python-based web security testing tool designed to analyze web application input parameters and identify suspicious response behavior.

The tool uses a structured multi-stage detection pipeline to compare normal application responses with responses generated during controlled input testing. Multiple signals are collected and evaluated, including:

- HTTP status changes
- Response length differences
- Content similarity changes
- SQL-related error signatures
- Boolean response differences
- Response timing anomalies
- Database-related error fingerprints

The collected signals are then aggregated and scored to produce a confidence level and severity classification.

FlexTools automatically displays the analysis results in the terminal and saves reports in both JSON and TXT formats.
>>>>>>> 40d6e45 (docs: improve README and installation guide)

---

Features

Multi-Stage Detection Pipeline

FlexTools menggunakan beberapa tahap analisis:

1. Target validation
2. URL normalization
3. Query parameter mapping
4. Baseline HTTP status collection
5. Baseline response length sampling
6. Baseline response timing sampling
7. SQL-related error signature analysis
8. Boolean differential analysis
9. Content similarity comparison
10. Response length anomaly detection
11. HTTP status anomaly detection
12. Timing consistency analysis
13. DBMS-related error fingerprinting
14. Signal aggregation
15. Signal deduplication
16. Confidence scoring
17. Severity classification
18. Terminal result presentation
19. Automatic JSON reporting
20. Automatic TXT reporting

---

Parameter Discovery

Command "discover" digunakan untuk mencari kandidat parameter dari sebuah halaman.

FlexTools dapat mengidentifikasi parameter dari:

- Existing URL query parameters
- HTML "<input>" fields
- HTML "<select>" fields
- HTML "<textarea>" fields
- Links yang memiliki query parameter

Contoh:

python main.py discover --url "http://localhost:8080/index.php"

Contoh output:

╔══ PARAMETER DISCOVERY ═══════════════════════════════╗

TARGET  http://localhost:8080/index.php

FOUND   5 candidate parameters

[url]
  • id
  • page

[forms]
  • username
  • search

[links]
  • category
=======
- Multi-stage web input analysis
- Automatic query parameter detection
- HTML form parameter discovery
- Link parameter discovery
- Baseline response collection
- HTTP status analysis
- Response length analysis
- Content similarity comparison
- SQL-related error signature detection
- Boolean differential analysis
- Response timing analysis
- Database-related error fingerprinting
- Confidence scoring
- Severity classification
- Colored terminal output
- Single target scanning
- Multi-target scanning
- Soft and aggressive scan profiles
- Automatic JSON reporting
- Automatic TXT reporting

---

Detection Pipeline

FlexTools performs analysis through multiple stages:

[01] Target validation
        │
        ▼
[02] URL normalization
        │
        ▼
[03] Query parameter identification
        │
        ▼
[04] Baseline HTTP response collection
        │
        ▼
[05] Response length sampling
        │
        ▼
[06] Response timing sampling
        │
        ▼
[07] SQL-related error signature analysis
        │
        ▼
[08] Boolean differential analysis
        │
        ▼
[09] Content similarity comparison
        │
        ▼
[10] Response length anomaly analysis
        │
        ▼
[11] HTTP status anomaly analysis
        │
        ▼
[12] Timing anomaly analysis
        │
        ▼
[13] Database-related error fingerprinting
        │
        ▼
[14] Signal aggregation
        │
        ▼
[15] Confidence scoring
        │
        ▼
[16] Severity classification
        │
        ▼
[17] Terminal output
        │
        ▼
[18] JSON and TXT reporting
>>>>>>> 40d6e45 (docs: improve README and installation guide)

---

Installation

Requirements

Sebelum menjalankan FlexTools, pastikan sistem memiliki:

- Python 3.8 atau lebih baru
- Git
- pip

Untuk pengguna Termux:

pkg update && pkg upgrade
pkg install python git

---

Clone Repository

Clone repository FlexTools:

git clone https://github.com/LFAzx/FlexTools.git

Masuk ke directory project:

cd FlexTools

---

Install Dependencies

Install seluruh dependency Python:

pip install -r requirements.txt

Jika menggunakan "pip3":

pip3 install -r requirements.txt

---

Verify Installation

Jalankan:

python main.py --help

Jika instalasi berhasil, FlexTools akan menampilkan menu utama beserta command yang tersedia.

---

Commands

1. Help

Untuk melihat seluruh command:

python main.py --help

Untuk melihat bantuan command tertentu:

Before installing FlexTools, make sure the following software is available:

- Python 3.8 or newer
- Git
- pip

Check your Python installation:

python --version

Check Git:

git --version

---

Installation on Termux

Update your packages:

pkg update && pkg upgrade -y

Install Python and Git:

pkg install python git -y

Clone the repository:

git clone https://github.com/LFAzx/FlexTools.git

Enter the project directory:

cd FlexTools

Install the required Python dependencies:

pip install -r requirements.txt

Verify the installation:

python main.py --help

If everything is installed correctly, FlexTools should display its command interface.

---

Installation on Linux

Install Python, pip, and Git using your package manager.

For Debian or Ubuntu:

sudo apt update
sudo apt install python3 python3-pip git

Clone the repository:

git clone https://github.com/LFAzx/FlexTools.git

Enter the project directory:

cd FlexTools

Install dependencies:

pip3 install -r requirements.txt

Run FlexTools:

python3 main.py --help

---

Usage

Display the main help menu:

python main.py --help

Available commands:

detector    Run deep analysis against one target
scan        Scan one or multiple targets
discover    Discover candidate parameters
report      List generated reports

For command-specific help:
>>>>>>> 40d6e45 (docs: improve README and installation guide)

python main.py detector --help

python main.py scan --help

python main.py discover --help

python main.py report --help

---

<<<<<<< HEAD
Detector

Mode "detector" digunakan untuk melakukan analisis mendalam terhadap satu URL.

Contoh:

python main.py detector --url "http://localhost:8080/index.php?id=1"

Dengan mode agresif:

Parameter Discovery

The "discover" command inspects a target page and searches for possible input parameters.

FlexTools can collect candidate parameters from:

- Existing URL query parameters
- HTML input fields
- HTML select fields
- HTML textarea fields
- Links containing query parameters

Example:

python main.py discover --url "http://localhost:8080/index.php"

Example output:

╔══ PARAMETER DISCOVERY ═══════════════════════════════╗

TARGET
http://localhost:8080/index.php

FOUND
5 candidate parameters

[url]
• id
• page

[forms]
• username
• search

[links]
• category

---

Detector Mode

The "detector" command performs a deeper multi-stage analysis against a single target.

Example:

python main.py detector \
  --url "http://localhost:8080/index.php?id=1"

Using aggressive mode:
>>>>>>> 40d6e45 (docs: improve README and installation guide)

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --mode aggressive

Custom timeout:

Using a custom timeout:
>>>>>>> 40d6e45 (docs: improve README and installation guide)

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --timeout 15

<<<<<<< HEAD
Custom report directory:

Saving reports to a custom directory:
>>>>>>> 40d6e45 (docs: improve README and installation guide)

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --output results

---

<<<<<<< HEAD
Scan

Mode "scan" dapat digunakan untuk satu target maupun banyak target.

Single Target

Scan Mode

The "scan" command can analyze a single target or multiple targets from a text file.

Scan a Single Target
>>>>>>> 40d6e45 (docs: improve README and installation guide)

python main.py scan \
  --url "http://localhost:8080/index.php?id=1"


Multiple Targets

Buat file "targets.txt":

Scan Multiple Targets

Create a file named:

targets.txt

Example:
>>>>>>> 40d6e45 (docs: improve README and installation guide)

http://localhost:8080/index.php?id=1
http://localhost:8080/product.php?item=10
http://localhost:8080/search.php?q=test

<<<<<<< HEAD
Kemudian jalankan:

Run the scanner:
>>>>>>> 40d6e45 (docs: improve README and installation guide)

python main.py scan \
  --url-file targets.txt

Dengan mode agresif dan beberapa worker:

Use multiple workers:

python main.py scan \
  --url-file targets.txt \
  --threads 5

Use aggressive mode:
>>>>>>> 40d6e45 (docs: improve README and installation guide)

python main.py scan \
  --url-file targets.txt \
  --mode aggressive \
  --threads 5

---

Scan Profiles

Soft

<<<<<<< HEAD
Mode "soft" digunakan untuk pengujian yang lebih konservatif.

Karakteristik:

- Request lebih sedikit
- Baseline sampling lebih ringan
- Repeated validation lebih sedikit
- Cocok untuk pengujian awal

Contoh:

The "soft" profile is designed for lower request volume and lighter analysis.

Characteristics:

- Fewer repeated measurements
- Lower request volume
- Faster execution
- Suitable for initial testing

Example:
>>>>>>> 40d6e45 (docs: improve README and installation guide)

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --mode soft

---

Aggressive

<<<<<<< HEAD
Mode "aggressive" melakukan sampling dan validasi lebih banyak.

Karakteristik:

- Baseline sampling lebih banyak
- Repeated validation lebih banyak
- Analisis reproducibility lebih mendalam
- Request volume lebih tinggi

Contoh:

The "aggressive" profile performs additional repeated analysis.

Characteristics:

- More baseline sampling
- More repeated validation
- Higher request volume
- Deeper reproducibility checking

Example:
>>>>>>> 40d6e45 (docs: improve README and installation guide)

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --mode aggressive

---

<<<<<<< HEAD
Analysis Result

FlexTools menampilkan informasi seperti:

╔══ FLEXTOOLS ANALYSIS RESULT ═════════════════════════╗

TARGET  http://localhost:8080/index.php?id=1
MODE    AGGRESSIVE

BASELINE
  status=200
  length=1248
  time=0.021s

Analysis Results

After analysis, FlexTools displays the detected signals and confidence score.

Example:

╔══ FLEXTOOLS ANALYSIS RESULT ═════════════════════════╗

TARGET
http://localhost:8080/index.php?id=1

MODE
AGGRESSIVE

BASELINE
status=200
length=1248
time=0.021s
>>>>>>> 40d6e45 (docs: improve README and installation guide)

[+] PARAMETER: id | HIGH | 85/100

    [POSITIVE] SQL-related error signature
        └─ Database-related error pattern detected

    [POSITIVE] Boolean differential
        └─ Significant response difference observed

    [POSITIVE] Response anomaly
        └─ Response characteristics differ from baseline

DBMS FINGERPRINT

  MySQL, MariaDB

╚══════════════════════════════════════════════════════╝

Confidence score dan severity dihasilkan berdasarkan kombinasi sinyal yang ditemukan, bukan hanya satu indikator tunggal.

MySQL, MariaDB

╚══════════════════════════════════════════════════════╝

A parameter is evaluated using multiple signals rather than relying on a single response difference.

The confidence score represents the combined strength and consistency of the detected indicators.
>>>>>>> 40d6e45 (docs: improve README and installation guide)

---

Reporting

Setelah proses "detector" atau "scan" selesai, FlexTools akan menyimpan hasil secara otomatis.

Format report:

reports/
├── report_2026xxxx_xxxxxx.json
└── report_2026xxxx_xxxxxx.txt

Untuk melihat daftar report:

python main.py report --list

Untuk menggunakan directory lain:

python main.py report --list --dir results

FlexTools automatically saves analysis results after scanning.

By default, reports are stored inside:

reports/

Example:

reports/
├── report_20260829_132713.json
└── report_20260829_132713.txt

To list generated reports:

python main.py report --list

To check a custom report directory:

python main.py report \
  --list \
  --dir results
>>>>>>> 40d6e45 (docs: improve README and installation guide)

---

Project Structure

FlexTools/
│
├── main.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── core/
│   ├── baseline.py
│   ├── colors.py
│   ├── config.py
│   ├── http_client.py
│   ├── models.py
│   ├── normalizer.py
│   └── scoring.py
│
├── scanner/
│   ├── discovery.py
│   ├── engine.py
│   ├── target_loader.py
│   └── url_parser.py
│
├── detector/
│   ├── boolean_based.py
│   ├── error_based.py
│   ├── fingerprint.py
│   ├── length_analysis.py
│   ├── status_analysis.py
│   └── timing_analysis.py
│
└── reporting/
    ├── colored_help.py
    ├── report_manager.py
    └── terminal.py

---

<<<<<<< HEAD
Colored CLI

FlexTools menggunakan ANSI terminal colors untuk meningkatkan keterbacaan output.

Bagian yang diberi visual highlighting meliputi:

- Header
- Command
- CLI options
- Target URL
- Scan profile
- Detection stages
- Severity
- Positive signals
- Baseline information
- Report status

Terminal dengan dukungan ANSI seperti Termux, Linux terminal, dan sebagian besar terminal modern akan menampilkan warna secara otomatis.

Module Overview

"core/"

Contains the main utility components.

- HTTP request handling
- Baseline collection
- Configuration profiles
- Response normalization
- Data models
- Confidence scoring
- Terminal color support

"scanner/"

Handles target processing and parameter discovery.

- URL parsing
- Target loading
- Parameter discovery
- Scan orchestration

"detector/"

Contains the analysis modules.

- Error signature analysis
- Boolean differential analysis
- Response length analysis
- HTTP status analysis
- Timing analysis
- Database-related error fingerprinting

"reporting/"

Handles result presentation and report generation.

- Colored terminal output
- JSON reports
- TXT reports
- Colored help interface
>>>>>>> 40d6e45 (docs: improve README and installation guide)

---

Typical Workflow

Alur penggunaan yang direkomendasikan:

Target Web Application
        │
        ▼
Parameter Discovery
        │
        ▼
Target & Parameter Identification
        │
        ▼
Baseline Collection
        │
        ▼
Multi-Stage Analysis
        │
        ├── Error Analysis
        ├── Boolean Differential
        ├── Length Analysis
        ├── Status Analysis
        ├── Timing Analysis
        └── DBMS Fingerprinting
        │
        ▼
Signal Aggregation
        │
        ▼
Confidence Scoring
        │
        ▼
Terminal Output
        │
        ▼
JSON + TXT Reporting

---

Example Workflow

Discover parameter terlebih dahulu:

A typical testing workflow looks like this:

Web Application
      │
      ▼
Parameter Discovery
      │
      ▼
Target Selection
      │
      ▼
Baseline Collection
      │
      ▼
Multi-Stage Analysis
      │
      ├── Error Analysis
      ├── Boolean Analysis
      ├── Length Analysis
      ├── Status Analysis
      ├── Timing Analysis
      └── DBMS Fingerprinting
      │
      ▼
Signal Aggregation
      │
      ▼
Confidence Scoring
      │
      ▼
Terminal Output
      │
      ▼
JSON + TXT Reports

---

Quick Start

Clone the repository:

git clone https://github.com/LFAzx/FlexTools.git
cd FlexTools

Install dependencies:

pip install -r requirements.txt

Check the available commands:

python main.py --help

Discover candidate parameters:
>>>>>>> 40d6e45 (docs: improve README and installation guide)

python main.py discover \
  --url "http://localhost:8080/index.php"

Kemudian lakukan analisis terhadap URL yang memiliki parameter:

Analyze a parameterized target:
>>>>>>> 40d6e45 (docs: improve README and installation guide)

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --mode aggressive

Hasil akan langsung:

1. Ditampilkan di terminal
2. Diberikan confidence score
3. Diberikan severity classification
4. Disimpan sebagai JSON
5. Disimpan sebagai TXT


>>>>>>> 40d6e45 (docs: improve README and installation guide)
---

Disclaimer

FlexTools ditujukan untuk security testing, authorized assessments, development environments, dan lab environments.

Gunakan tools ini hanya terhadap sistem yang dimiliki sendiri atau sistem yang telah memberikan izin eksplisit untuk diuji.

FlexTools is intended for:

- Authorized security testing
- Local development environments
- Security research
- Educational environments
- Controlled laboratory testing

Only test systems that you own or systems for which you have explicit authorization.

Automated results should always be manually reviewed and validated.
>>>>>>> 40d6e45 (docs: improve README and installation guide)

---

Author

Mr.RezWithLove

Cybersecurity & Web Security Research

---

<p align="center">
  <b>FLEXTOOLS COLORED v2.5</b>

---

<p align="center">
  <strong>FLEXTOOLS COLORED v2.5</strong>
>>>>>>> 40d6e45 (docs: improve README and installation guide)
</p><p align="center">
  Built for structured web security testing and analysis.
</p>
