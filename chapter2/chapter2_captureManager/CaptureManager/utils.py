import cv2
import numpy
import scipy.interpolate

def createCurveFunc(points):
    """Return a function derived from control points."""
    if points is None:
        return None
    numPoints = len(points)
    if numPoints < 2:
        return None
    xs, ys = zip(*points)
    #kaz notes: the * (asterisk) is called a "splatter" operator, which takes a list and turns them into arguments. "So if uniqueCrossTabs was [ [ 1, 2 ], [ 3, 4 ] ], then itertools.chain(*uniqueCrossTabs) is the same as saying itertools.chain([ 1, 2 ], [ 3, 4 ])"
    #reference:
    #https://stackoverflow.com/questions/5239856/foggy-on-asterisk-in-python
    #https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean
    if numPoints < 4:
        kind = 'linear'
        # 'quadratic' is not implemented.
    else:
        kind = 'cubic'
    return scipy.interpolate.interp1d(xs, ys, kind, bounds_error = False)
    
def createLookupArray(func, length = 256):
    """Return a lookup for whole-number inputs to a function.
    
    The lookup values are clamped to [0, length - 1].
    
    """
    if func is None:
        return None
    lookupArray = numpy.empty(length)
    i = 0
    while i  < length:
        func_i = func(i)
        lookupArray[i] = min(max(0, func_i), length - 1)
        i += 1
    return lookupArray
    
def applyLookupArray(lookupArray, src, dst):
    """Map a source to a destination using a lookup."""
    if lookupArray is None:
        return
    dst[:] = lookupArray[src]

def createCompositeFunc(func0, func1):
    """Return a composite of two functions."""
    if func0 is None:
        return func1
    if func1 is None:
        return func0
    return lambda x: func0(func1(x))

def createFlatView(array):
    """Return a 1D view of an array of any dimensionality."""
    flatView = array.view()
    flatView.shape = array.size
    return flatView