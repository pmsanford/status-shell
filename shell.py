#!/usr/bin/python
import argparse
import status_values
import json
cmds_available = False
try:
	import shellcmds
	cmds_available = True
except:
	pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--command")
	args = parser.parse_args()

	healthreport = {'health': status_values.healthy}

	if cmds_available:
		for cmd in shellcmds.command_list:
			cmd.run(args.command, healthreport)
	
	print(json.dumps(healthreport))