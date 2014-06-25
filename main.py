import roombaSCI
import time

from roombaSCI import RoombaAPI

print "starting ..."
x = RoombaAPI("/dev/ttyO4",115200)
try:
	x.connect()
        x.start()
        x.control()
        time.sleep(1)
	x.spin_left()
        time.sleep(3)
        x.off()
        x.close()
except:
        x.close()
        raise
