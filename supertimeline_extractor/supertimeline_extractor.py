#######################
# @author: RaffaDNDM
# @date:   2022-05-16
#######################

import os

#Filter file
FILTER_FILE = 'filter_windows.txt'

#Dump folder
DUMP_FOLDER = 'Dump'

#Format of a machine
FORMAT_MACHINE = '.vmdk'

#Format of the Supertimeline files
FORMAT_DUMP = '.dump'

folder = [x for x in os.listdir('.') if os.path.isdir(x) and x!=DUMP_FOLDER]
print(folder)

machines = [x for x in os.listdir(folder[0]) if x.endswith('flat'+FORMAT_MACHINE)]
destination = DUMP_FOLDER+'/'+folder[0]
os.mkdir(destination)

for x in machines:
	print(folder[0]+'/'+x)
	dump_file = x[:-len(FORMAT_MACHINE)]+'.dump'
	print(destination+'/'+dump_file)
	command = f"log2timeline.py -f {FILTER_FILE} '{destination}/{dump_file}' '{folder[0]}/{x}'"
	print(command)
	#os.system(command)
    