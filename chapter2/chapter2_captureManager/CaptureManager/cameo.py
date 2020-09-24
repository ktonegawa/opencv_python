import cv2
import filters
from managers import WindowManager, CaptureManager

class Cameo(object):
    
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
        #kaz notes: enter a random color filter here
        #self._curveFilter = filters.BGRPortraCurveFilter()
        self._curveFilter = filters.BGRVelviaCurveFilter()
        #kaz note end
    
    def run(self):
        '''Run the main loop.'''
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            
            # TODO: Filter the frame (Chapter 3).
            
            #kaz notes: enter a random effect filter (blur, sharpen, colorize) here
            #filters.strokeEdges(frame, frame)
            #filters.recolorCMV(frame, frame)
            self._curveFilter.apply(frame, frame)
            #kaz note end
            
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
    
    def onKeypress(self, keycode):
        '''Handle a keypress.
        
        space   -> Take a screenshot
        tab     -> Start/stop recording a screencast.
        escape  -> Quit.
        
        '''
        if keycode == 32: # space
            self._captureManager.writeImage('C:\\Users\\Desktop02\\Documents\\OpenCV_pythonFiles\\chapter2_captureManager\\CaptureManager\\screenshotTest02.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('C:\\Users\\Desktop02\\Documents\\OpenCV_pythonFiles\\chapter2_captureManager\\CaptureManager\\screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

if __name__ == '__main__':
    Cameo().run()