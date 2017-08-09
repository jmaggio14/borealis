# @Author: Jeff Maggio <jmaggio>
# @Date:   2017-07-30T15:27:23-07:00
# @Email:  jmaggio@planetaryresources.com
# @Project: sam (framing camera simulator)
# @Last modified by:   jmaggio
# @Last modified time: 2017-07-30T17:41:01-07:00
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


from opensimplex import OpenSimplex
import numpy as np
import random
import sys

def terrain_map2D(octaves=10, startFreq=1, persistance=2, lacunarity=2,
                    size=(256,256), seed=0, maxValue=1.0):
    """
    generates a coherent noise map

    """
    #building noise generator, scaled from 0 -1
    noiseGen = lambda nx,ny : (OpenSimplex(seed).noise2d(nx,ny) / 2.0) + 0.5

    terrainMap = np.zeros(size)
    freq = startFreq
    amp = 1
    #looping through number of frequency additions
    for i in range(octaves):
        # modifying amplititude of every new frequency
        amp = float(amp) / persistance
        #modifying frequency
        freq = freq * lacunarity
        #looping through every pixel in 2 space
        for r in range(size[0]):
            for c in range(size[1]):
                nx = float(c) / size[1]
                ny = float(r) / size[0]
                terrainMap[r,c] = terrainMap[r,c] + ( amp * noiseGen(freq * nx,freq * ny) )

    #normalizing
    terrainMap = terrainMap - np.min(terrainMap)
    terrainMap = terrainMap / np.max(terrainMap)
    return terrainMap


def convert_2D_to_3D(map2D,maxHeight,numValues):
    ##UNTESTED
    """converts a 2D terrrain map to 3D coordinates"""
    #UNIT TESTS
    if isinstance(numValues,int) == False:
        print("var 'numValues' must be int")
        sys.exit()


    # scaling to maxHeight
    scaled2D = map2D * maxHeight
    # quantizing to numValues
    quantizationFactor = maxHeight // numValues
    scaled2D = scaled2D // quantizationFactor
    values3D = scaled2D * quantizationFactor

    # zipping into vertices
    vertices = []
    xCords,yCords = np.indices( map2D.shape )
    for x in xCords:
        for y in yCords:
            vertices.append( [ x,y,values3D[x,y] ] )
    return vertices





if __name__ == "__main__":
    import cv2
    # import sam
    testMap2D = terrain_map2D() * 255
    cv2.imwrite("test.png",testMap2D)


    #testing 2D --> 3D
    testMap3D = convert_2D_to_3D(testMap2D,255,128)
    print(testMap3D)
    # cv2.waitKey(2213)


#END
