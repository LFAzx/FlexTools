# FlexTools Colored v2.5
Author: Mr.Flex

Defensive web security testing suite focused on structured input anomaly detection and reporting.

## Colored CLI
The CLI uses ANSI colors automatically when supported by the terminal.

Commands:
- `python main.py --help`
- `python main.py detector --help`
- `python main.py scan --help`
- `python main.py discover --help`
- `python main.py report --help`

The analysis pipeline covers target parsing, baseline sampling, response comparison, SQL-related error signatures, boolean differential signals, length/status/timing anomalies, DBMS-related error fingerprinting, scoring, terminal output, and JSON/TXT reporting.

No database enumeration, credential extraction, or data extraction functionality is included.
