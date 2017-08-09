# @Author: Jeff Maggio <jmaggio>
# @Date:   2017-07-30T15:20:58-07:00
# @Email:  jmaggio@planetaryresources.com
# @Project: sam (framing camera simulator)
# @Last modified by:   jmaggio
# @Last modified time: 2017-07-30T16:26:22-07:00
# @Copyright:  #!/usr/bin/env python

################################################################################
# Copyright (c) 2017 Planetary Resources Inc.
# Planetary Resources Proprietary
# NOTICE:
# All information contained herein is, and remains the property of Planetary
# Resources Incorporated, its subsidiaries and its suppliers, if any.  The
# intellectual and technical concepts contained herein are proprietary to
# Planetary Resources Incorporated, its subsidiaries, and its suppliers and
# may be covered by U.S. and Foreign Patents, patents in process, and are
# protected by trade secret or copyright law.  Dissemination of this
# information or reproduction of this material is strictly forbidden unless
# prior written permission is obtained from Planetary Resources Inc.
################################################################################

## Doxygen header
# @author   <your name>
# @brief    <description>

# Standard library imports
################################################################################

# Third party library imports
################################################################################

# Standard PRI imports
################################################################################

# External component imports
################################################################################

# Internal component imports
################################################################################

# Constant definitions
################################################################################

# Utility function definitions
################################################################################

# Public class definitions
################################################################################

# Public function definitions
################################################################################

# Private class definitions
################################################################################

# Private function definitions
################################################################################

# Main function and argument parsing
################################################################################



import numpy as np
import scipy as sp
# from opensimplex import OpenSimplex


class Path(object):
    """
    construct a path through the terrain map for the hyperloop to follows

    MUST DO!!!!
    implement Dikstra's algorithm with a height, deltaChange, sectionLength conditions
        (can't climb mountains, can't turn sharp corners, hyperloop will be made of straight sections)
    3D might be necessary here
    """
    def __init__(self,terrainMap3D,start,end,groundOffset,sectionLength):
        self._terrainMap3D = terrainMap3D
        self._start = start
        self._start = start
        self._end = end
        self._groundOffset = groundOffset

    def recalculate(self):
        pass
        #ADD DIKSTRA HERE
        # self._path =
