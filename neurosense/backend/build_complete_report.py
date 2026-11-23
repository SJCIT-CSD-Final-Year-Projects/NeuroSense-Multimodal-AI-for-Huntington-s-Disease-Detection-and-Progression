# Script to assemble the entire NeuroSense project report (Chapters 1 through 10, Bibliography, Appendices)
import os

# Resolve paths relative to this script's directory
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
md_path = os.path.join(_SCRIPT_DIR, 'report/NeuroSense_Project_Report.md')
print(f"Target report path: {md_path}")
