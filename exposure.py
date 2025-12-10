
# asce7/exposure.py
"""
Helpers to explain/select Exposure Category (B/C/D) and validate sectors.
This module provides text helpers used in the UI to reduce selection errors.
"""

from typing import Dict

EXPOSURE_HELP: Dict[str, str] = {
    'B': (
        "Urban/suburban, wooded, or terrain with numerous closely spaced obstructions. "
        "Upwind distance ≥ 1,500 ft for buildings ≤30 ft tall or ≥ 2,600 ft for taller buildings."
    ),
    'C': (
        "Open terrain with scattered obstructions, such as open country or grasslands. "
        "Extends into adjacent Exposure B for ≥1,500 ft or 10× building height."
    ),
    'D': (
        "Flat, unobstructed areas and water surfaces ≥ 5,000 ft upwind. "
        "Applies within 600 ft inland from coastlines and up to 20× building height."
    ),
}
