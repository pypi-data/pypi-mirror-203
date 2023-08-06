#!/usr/bin/env python3
"""! @brief LorettOrbital Python 3 library for orbital calculations and planning"""
##
# @mainpage LorettOrbital
#
# @section LorettOrbital Description
# An example Python program demonstrating how to use Doxygen style comments for
# generating source code documentation with Doxygen.
#
# @section scheduler Notes
# Contains several classes that provide TLE processing, calculation of flight schedules by parameters, etc.
#

from . import scheduler
from . import exceptions

__version__= scheduler.__version__
# Global Constants
## Elements of the lorettOrbital
__all__ = ["scheduler", "exceptions", "__version__"]
