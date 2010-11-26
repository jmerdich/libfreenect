#!/usr/bin/env python
import freenect
import cv
import numpy as np


cv.NamedWindow('Depth')    
while 1:
    depth, timestamp = freenect.sync_get_depth_np()
    cv.ShowImage('Depth', depth.astype(np.uint8))
    cv.WaitKey(10)