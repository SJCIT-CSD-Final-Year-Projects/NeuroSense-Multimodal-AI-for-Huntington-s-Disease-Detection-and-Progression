"""NeuroSense — AI-Powered Huntington's Disease Detection Platform.

A multi-modal clinical decision support framework integrating
structural MRI, genetic biomarkers (CAG repeat count), and UHDRS
clinical scores for early HD detection and progression forecasting.

Version: 1.0.0
"""

from __future__ import annotations

import sys
from pathlib import Path

__version__ = "1.0.0"
__author__ = "Suraj"

# Extend neurosense package path to include neurosense/backend
# This ensures both `import neurosense.api` and `import neurosense.backend.api` work seamlessly!
_backend_dir = str(Path(__file__).resolve().parent / "backend")
if _backend_dir not in __path__:
    __path__.append(_backend_dir)

