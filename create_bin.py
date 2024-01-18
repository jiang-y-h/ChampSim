import subprocess
import itertools
import sys

def run_build_champsim(param1_options, param2_options, param3_options, param4_options):
    forbidden_combination = ("ip_stride", "ip_stride")
    for params in itertools.product(param1_options, param2_options, param3_options, param4_options):
        # Run the build_champsim.sh script with the provided parameters
        
        if params[1:3] == forbidden_combination:
            print(f"Skipped forbidden combination: {params}")
            continue
        
        cmd = "./build_champsim.sh " + " ".join(params)
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Check the exit status of the subprocess
        if result.returncode == 0:
            print(f"Build successful for parameters: {params}")
            print(result.stdout.decode())
        else:
            print(f"Build failed for parameters: {params}")
            print(result.stderr.decode())

if __name__ == "__main__":
    # Define different choices for each parameter
    param1_options = ["no"]
    param2_options = ["ghb","pangloss"]
    param3_options = ["no"]
    param4_options = ["ship","drrip"]

    # Run the build_champsim.sh script for each combination
    run_build_champsim(param1_options, param2_options, param3_options, param4_options)
