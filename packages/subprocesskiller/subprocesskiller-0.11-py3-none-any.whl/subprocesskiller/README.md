# Some functions for killing (sub)processes + children with ctypes - works with "shell=True" 

## pip install subprocesskiller


#### Tested against Windows 10 / Python 3.10 / Anaconda


### Python

```python

from subprocesskiller import get_pro_properties, subprocess_timeout, kill_process_children_parents, kill_subprocs, kill_pid
# Get a dictionary of properties for all running processes
processprops = get_pro_properties()

# Kill all child processes of PID 9348 whose parent process has the executable name "python.exe".
# Don't kill any processes with the name "conhost.exe".
kill_process_children_parents(pid=9348,max_parent_exe='python.exe',dontkill=('Caption', 'conhost.exe'))


# Execute "ping -t 8.8.8.8" in a subprocess with a timeout of 4 seconds.
# If the process doesn't complete within 4 seconds, kill it and all of its child processes.
res = subprocess_timeout(
    "ping -t 8.8.8.8",
    shell=True,
    timeout=4,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE,
)

# You can read the output (stderr/stdout) from a killed process
while g := res.stdout.readline():
    print(g)

# Execute "ping -t 8.8.8.8" in a subprocess.
# Wait for 2 seconds, then kill all running python subprocess and all of its child processes except conhost.exe
subprocess.Popen("ping -t 8.8.8.8", shell=True)
time.sleep(2)
kill_subprocs(dontkill=(("Caption", "conhost.exe"),))


# Kills a pid 
kill_pid(pid=9348)



```
### Command line

This is an example of how to use the Python script from the command line to kill a specific process and all its child processes. In this case, the script is being used to kill a process with PID 7348 that has a parent process with the name "chrome.exe".

To run the script from the command line, navigate to the directory where the script is saved and enter the following command:

```python
.\python.exe .\__init__.py --pid 7348 --max_parent_exe chrome.exe
```

This command specifies the PID of the process to be killed with the --pid flag and the name of the parent process that the process should have with the --max_parent_exe flag. In this case, the parent process name is "chrome.exe".
