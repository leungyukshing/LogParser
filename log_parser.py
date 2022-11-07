import sys
import json
import requests
log_file = sys.argv[1]
server_address = "http://127.0.0.1:12202/gelf"
print("parsing log_file: " + log_file)

test_line = '[FINE   ] [2022-11-04 14:50:45] [dslabs.paxos.PaxosServer] server1: handleP1aMessage: got p1a Ballot(0, server2), curr latest bn: null'

def parse_line(line):
	arr = line.split(' ')
	print(line)
	arr = [s for s in arr if s != '']
	level = ''.join(arr[0:2]).lstrip('[').rstrip(']')
	timestamp = ' '.join(arr[2:4]).lstrip('[').rstrip(']')
	server = arr[5].rstrip(':')
	msg = ' '.join(arr[6:])
	#print(level)
	#print(timestamp)
	#print(server)
	#print(msg)

	tmp = {}
	tmp['level'] = level
	tmp['timestamp'] = timestamp
	tmp['server'] = server
	tmp['message'] = msg

	return tmp

lines = []
with open(log_file) as f:
	for line in f:
		if line.startswith('[') is False:
			continue
		tmp = parse_line(line)
		# tmpStr = json.dumps(dict)
		lines.append(tmp)

for s in lines:
	r = requests.post(server_address, json = s)
	#print(r.status_code)

print('done!')