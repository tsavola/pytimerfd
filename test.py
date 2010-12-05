import asyncore

import timerfd
import timerfd.async

class TestDispatcher(timerfd.async.dispatcher):

	def handle_expire(self, count):
		print(self, "handle_expire", count)

	def handle_close(self):
		print(self, "handle_close")
		self.close()

	def handle_error(self):
		print(self, "handle_error")
		self.close()

def main():
	dispatcher = TestDispatcher(timerfd.CLOCK_MONOTONIC)
	dispatcher.settime(0, timerfd.itimerspec(0.5, 1))

	print(dispatcher.gettime())

	asyncore.loop()

if __name__ == "__main__":
	main()
