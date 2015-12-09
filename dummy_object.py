class DummyObject:
	def __init__(self):
		self.name = 'dummy'

	def run(self, command, healthreport):
		if command == self.name:
			healthreport['dummy'] = 'Dummy Object'