import os.path
import argparse
import sys

args = argparse.ArgumentParser(description = 'Score simulator.')
args.add_argument("bin_dir_path", type = str, help = "bin_dir_path")
args.add_argument("traces_dir_path", type = str, help = "traces_dir_path")
args = args.parse_args() 

# check
if not os.path.isdir(args.bin_dir_path):
    print("illegal bin_dir_path!")
    exit(0)

for path,d,filelist in os.walk(args.bin_dir_path):
    for filename in filelist:
        if filename[-5:] != "1core":
            print("illegal trace files!")
            exit(0)

if not os.path.isdir(args.traces_dir_path):
    print("illegal traces_dir_path!")
    exit(0)
    
for path,d,filelist in os.walk(args.traces_dir_path):
    for filename in filelist:
        if filename[-8:] != "trace.xz":
            print("illegal trace files!")
            exit(0)
    
    
bin_dir_path = args.bin_dir_path
trace_file_path = args.traces_dir_path

traces = []
bins=[]
for path,d,filelist in os.walk(trace_file_path):
    for filename in filelist:
        t = os.path.join(path,filename)
        traces.append(t)

for path,d,filelist in os.walk(bin_dir_path):
    for filename in filelist:
        t = os.path.join(path,filename)
        bins.append(t)
        


print("please wait...")
student_num = "tmplog"
log_num = 0

for bin in bins:
    cmd = "./run_champsim.sh " + bin + " 50 100 "
    for trace in traces:
        student_num =os.path.basename(bin) + "_" +os.path.basename(trace)
        trace_cmd = cmd + trace + "> " +student_num
        log_num = log_num + 1
        os.system(trace_cmd)

