import subprocess

start = 1002548
end = 1102095

with open("raw_data_hanoi", "a") as file:
	for sbd in range(start,end):
		command = 'curl -F "sobaodanh=0' + str(sbd) + '" https://diemthi.vnexpress.net/index/detail/sbd/0' + str(sbd) + '/year/2023'
		result = subprocess.check_output(command)

		file.write(str(result) + "\n")