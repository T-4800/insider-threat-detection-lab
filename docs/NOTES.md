# Notes on Insider Threat Detection Lab

## Design Decisions
- All Python scripts live in `src/`
- Logs and CSVs in `data/` (excluded from GitHub)
- Scripts are modular for future ML/AI integration

## Observations
- Users with multiple failed logins and restricted file downloads get flagged as high-risk
- Time-based alerts detect sequences like downloading sensitive files shortly after login

## Future Improvements
- Add ML-based anomaly detection
- Integrate a scoring dashboard
- Implement user behavior simulation for testing
