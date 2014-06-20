from bottle import route, run
import roombaSCI
import time

from roombaSCI import RoombaAPI

x = RoombaAPI("/dev/ttyO4",115200)
try:
	x.connect()
        x.start()
        x.control()
except:
        x.close()
        raise

@route('/left')
def turn_left():
	x.spin_left()
	print "turning left"

@route('/right')
def turn_right():
	x.spin_right()
	print "turning right"

@route('/stop')
def stop():
	x.off()
	x.close()


run(host='localhost', port=8080, debug=True)

