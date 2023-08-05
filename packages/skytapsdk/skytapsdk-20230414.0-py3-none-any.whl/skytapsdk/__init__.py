"""
Python SDK for accessing Skytap APIs
"""

from .course_manager import CourseManager
from .skytap import Skytap

__all__ = [
    "Skytap",
    "CourseManager",
]
