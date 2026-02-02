# Insider Threat Detection Lab

A hands-on Python project exploring **rule-based detection**, **risk scoring**, **anomaly detection**, and **time-based alerts** for insider threat analysis.

Python-based insider threat detection framework with AI/ML and time-sequence anaysis.

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






