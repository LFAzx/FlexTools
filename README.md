FlexTools Colored v2.5

<p align="center">
  <b>Python-Based Web Security Scanner & Input Anomaly Detector</b>
</p><p align="center">
  Structured parameter discovery • Multi-stage analysis • SQL-related error fingerprinting • Automated reporting
</p>---

Overview

FlexTools Colored adalah tools berbasis Python yang dirancang untuk membantu proses pengujian keamanan aplikasi web, khususnya pada area input dan parameter HTTP.

Tools ini melakukan analisis terhadap target dengan pendekatan multi-stage. FlexTools membandingkan baseline response dengan response hasil variasi input, kemudian mengumpulkan berbagai sinyal seperti perubahan status HTTP, perubahan panjang response, kemiripan konten, error signature yang berkaitan dengan database, perbedaan logika response, serta anomali waktu respons.

Hasil analisis kemudian dikumpulkan, dievaluasi, dan diberikan confidence score sebelum ditampilkan di terminal dan disimpan secara otomatis ke dalam report.

FlexTools memiliki empat command utama:

- "detector" — analisis mendalam terhadap satu target.
- "scan" — melakukan analisis terhadap satu atau banyak target.
- "discover" — mencari kandidat parameter dari URL, form, dan link.
- "report" — melihat hasil report yang telah dibuat.

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

python main.py detector --help

python main.py scan --help

python main.py discover --help

python main.py report --help

---

Detector

Mode "detector" digunakan untuk melakukan analisis mendalam terhadap satu URL.

Contoh:

python main.py detector --url "http://localhost:8080/index.php?id=1"

Dengan mode agresif:

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --mode aggressive

Custom timeout:

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --timeout 15

Custom report directory:

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --output results

---

Scan

Mode "scan" dapat digunakan untuk satu target maupun banyak target.

Single Target

python main.py scan \
  --url "http://localhost:8080/index.php?id=1"

Multiple Targets

Buat file "targets.txt":

http://localhost:8080/index.php?id=1
http://localhost:8080/product.php?item=10
http://localhost:8080/search.php?q=test

Kemudian jalankan:

python main.py scan \
  --url-file targets.txt

Dengan mode agresif dan beberapa worker:

python main.py scan \
  --url-file targets.txt \
  --mode aggressive \
  --threads 5

---

Scan Profiles

Soft

Mode "soft" digunakan untuk pengujian yang lebih konservatif.

Karakteristik:

- Request lebih sedikit
- Baseline sampling lebih ringan
- Repeated validation lebih sedikit
- Cocok untuk pengujian awal

Contoh:

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --mode soft

---

Aggressive

Mode "aggressive" melakukan sampling dan validasi lebih banyak.

Karakteristik:

- Baseline sampling lebih banyak
- Repeated validation lebih banyak
- Analisis reproducibility lebih mendalam
- Request volume lebih tinggi

Contoh:

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --mode aggressive

---

Analysis Result

FlexTools menampilkan informasi seperti:

╔══ FLEXTOOLS ANALYSIS RESULT ═════════════════════════╗

TARGET  http://localhost:8080/index.php?id=1
MODE    AGGRESSIVE

BASELINE
  status=200
  length=1248
  time=0.021s

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

python main.py discover \
  --url "http://localhost:8080/index.php"

Kemudian lakukan analisis terhadap URL yang memiliki parameter:

python main.py detector \
  --url "http://localhost:8080/index.php?id=1" \
  --mode aggressive

Hasil akan langsung:

1. Ditampilkan di terminal
2. Diberikan confidence score
3. Diberikan severity classification
4. Disimpan sebagai JSON
5. Disimpan sebagai TXT

---

Disclaimer

FlexTools ditujukan untuk security testing, authorized assessments, development environments, dan lab environments.

Gunakan tools ini hanya terhadap sistem yang dimiliki sendiri atau sistem yang telah memberikan izin eksplisit untuk diuji.

---

Author

Mr.Flex

Cybersecurity & Web Security Research

---

<p align="center">
  <b>FLEXTOOLS COLORED v2.5</b>
</p><p align="center">
  Built for structured web security testing and analysis.
</p>
