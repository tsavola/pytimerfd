__all__ = [
	"dispatcher",
]

import asyncore

import timerfd

class dispatcher(asyncore.file_dispatcher):

	def __init__(self, clock_id, flags=0, map=None):
		fd = timerfd.create(clock_id, flags)
		asyncore.file_dispatcher.__init__(self, fd, map)

	def settime(self, flags, new_value):
		return timerfd.settime(self.socket.fileno(), flags, new_value)

	def gettime(self):
		return timerfd.gettime(self.socket.fileno())

	def handle_expire(self, count):
		self.log_info("unhandled expire event", "warning")

	def handle_read(self):
		buf = self.recv(timerfd.bufsize)
		if buf:
			count = timerfd.unpack(buf)
			self.handle_expire(count)
		else:
			self.close()

	def writable(self):
		return False
