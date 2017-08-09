# @Author: Jeff Maggio <jmaggio>
# @Date:   2017-07-30T15:20:58-07:00
# @Email:  jmaggio@planetaryresources.com
# @Project: sam (framing camera simulator)
# @Last modified by:   jmaggio
# @Last modified time: 2017-07-31T09:24:25-07:00
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
import itoc



class Tube(itoc.Path):
    """docstring for Tube."""
    # def __init__(self,terrainMap3D,start,end,groundOffset,diameter,sides,sectionLength):
    #     itoc.Path.__init__(terrainMap3D,start,end,groundOffset)


    def __init__(self,diameter,numSides):
        self._diameter = diameter
        self._numSides = numSides

    def build_tube(self):
        """
        Construct a cylindrical tube around the path

        CONSTUCT a N sided polygon primative around every point
        connect corresponding vertices to form tube sections


        """
        self._primatives = []
        for point in self._path:
            # draw primative around each point

        for poly in self._primatives:
            # connect each primative

class WallFace(object):
    def __init__(self,vertices,normals):
        self._vertices = vertices
        self._normals = normals

class Primative(object):
    def __init__(self,vertices):
        """vertices which actually make up the primative (or maybe just vertex indices)
            edges which
        """
        self._vertices = vertices
        self._edges = []
        for i in range(len(self._vertices)-1)
            self._edges.append( [i,i+1] )







#END
