import subprocess
import threading

class Video:

    def __run_video__(self):
        bashCommand = "raspivid -t 999999 -n -h 720 -w 1280 -fps 25 -b 2000000  -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=0.0.0.0 port=8554"
        subprocess.check_output(['bash','-c', bashCommand])

    def start_streaming(self):
        t1 = threading.Thread(target=self.__run_video__, args=[])
        t1.start()