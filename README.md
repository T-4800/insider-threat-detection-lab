# Insider Threat Detection Lab

Python-based insider threat detection framework with AI/ML and time-sequence anaysis.

## Portfolio Summary

This project showcases a hands-on approach to **insider threat detection** using Python, rule-based analysis, and ML/AI-inspired techniques.  

It demonstrates the ability to:  
- Detect **failed logins** and **unauthorized file downloads** with rule-based logic  
- Compute **user risk scores** and categorize medium- and high-risk users  
- Identify **anomalous behavior** using distance-based methods  
- Generate **time-based alerts** for suspicious sequences of user activity  
- Organize a Python project professionally with clean folder structure (`src/`, `data/`, `docs/`)  
- Use **version control** effectively and document workflows clearly for reproducibility  

This repository reflects the combination of **security expertise** and **data-driven analysis**, illustrating skills in **Python programming, data parsing, anomaly detection, and explainable ML features**. It’s designed as a **portfolio-ready lab** demonstrating the practical application of insider threat detection principles.

## Repo Structure

- **src/** : Python scripts for detection logic  
- **data/** : Logs and CSVs (not tracked in GitHub)  
- **requirements.txt** : Environment setup  
- **.gitignore** : Files/folders excluded from GitHub  

## Scripts

1. **rule_based_detection.py**  
   Detects failed logins and restricted file downloads.

2. **csv_risk_scoring.py**  
   Computes risk scores from user activity CSVs.

3. **anomaly_detection.py**  
   Identifies unusual user behavior using distance-based methods.

4. **time_based_detection.py**  
   Generates alerts when suspicious sequences occur within a time window.

## Usage

```bash
# Clone the repo
git clone https://github.com/T-4800/insider-threat-detection-lab.git
cd insider-threat-detection-lab

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run a detection script
python3 src/rule_based_detection.py

## Sample Output

Failed login summary:
asmith: 3
kjones: 3

Restricted file policy violations:
ALERT: jdoe downloaded a restricted file after successful login
ALERT: kjones downloaded a restricted file after successful login

## Sample Output

### Failed login summary:

asmith: 3
kjones: 3


