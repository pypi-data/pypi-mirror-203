import ctypes.wintypes
import os
import subprocess
import time
import comtypes.client
from flatten_any_dict_iterable_or_whatsoever import fla_tu
from ordered_set import OrderedSet
from subprocess_alive import is_process_alive
from hackyargparser import add_sysargv


Psapi = ctypes.WinDLL("Psapi.dll")
EnumProcesses = Psapi.EnumProcesses
EnumProcesses.restype = ctypes.wintypes.BOOL
GetProcessImageFileName = Psapi.GetProcessImageFileNameA
GetProcessImageFileName.restype = ctypes.wintypes.DWORD

Kernel32 = ctypes.WinDLL("kernel32.dll")
OpenProcess = Kernel32.OpenProcess
OpenProcess.restype = ctypes.wintypes.HANDLE
TerminateProcess = Kernel32.TerminateProcess
TerminateProcess.restype = ctypes.wintypes.BOOL
CloseHandle = Kernel32.CloseHandle

TerminateProcess = Kernel32.TerminateProcess
TerminateProcess.restype = ctypes.wintypes.BOOL
GetExitCodeThread = Kernel32.GetExitCodeThread
GetExitCodeThread.restype = ctypes.wintypes.BOOL
GetExitCodeThread.argtypes = [ctypes.wintypes.HANDLE, ctypes.wintypes.LPDWORD]
PROCESS_TERMINATE = 0x0001
PROCESS_QUERY_INFORMATION = 0x0400


def kill_pid(pid: int) -> list:
    r"""
    Terminates a process with the given process ID (pid) and returns a list of tuples containing the terminated process ID
    and its full path.

    Args:
        pid (int): The process ID of the process to be terminated.

    Returns:
        list: A list of tuples containing the terminated process ID and its full path.

    Raises:
        None.

    Example:
        >>> kill_pid(1234)
        [(1234, 'C:\\Windows\\System32\\notepad.exe')]
    """
    killp = []
    try:
        pidx = int(pid)
        hProcess = OpenProcess(
            PROCESS_TERMINATE | PROCESS_QUERY_INFORMATION, False, pidx
        )
        ImageFileName = (ctypes.c_char * 260)()
        if GetProcessImageFileName(hProcess, ImageFileName, 260) > 0:
            fullp = ImageFileName.value.decode("utf-8", "ignore")
            killp.append((pid, fullp))
            Kernel32.TerminateProcess(hProcess, 1)
        try:
            Kernel32.CloseHandle(hProcess)
        except Exception:
            pass
    except Exception as fe:
        print(fe)
    return killp


def get_process_instances() -> tuple:
    r"""Get instances of all currently running processes using WMI.

    Returns:
        Tuple: A tuple containing the WMI object and the process instances.
    """
    WMI = comtypes.client.CoGetObject("winmgmts:")
    processes = WMI.InstancesOf("Win32_Process")
    return WMI, processes


def get_pro_properties() -> dict:
    r"""
    Retrieves system information about running processes and returns a dictionary containing the information.

    Returns:
        A dictionary containing process information for each running process and its parent process (if applicable). The dictionary has the following keys:
        - ProcessId: The process ID
        - ParentProcessId: The ID of the process's parent process (if applicable)
        - All properties listed in the `allprops` list (see code for full list) with their respective values
        - is_parent: A boolean value indicating whether the process is a parent process or not.

        If an error occurs while retrieving the value for a particular property, its value in the dictionary will be `None`.

    Raises:
        None

    """
    allprops = [
        "CreationClassName",
        "Caption",
        "CommandLine",
        "CreationDate",
        "CSCreationClassName",
        "CSName",
        "Description",
        "ExecutablePath",
        "ExecutionState",
        "Handle",
        "HandleCount",
        "InstallDate",
        "KernelModeTime",
        "MaximumWorkingSetSize",
        "MinimumWorkingSetSize",
        "Name",
        "OSCreationClassName",
        "OSName",
        "OtherOperationCount",
        "OtherTransferCount",
        "PageFaults",
        "PageFileUsage",
        "ParentProcessId",
        "PeakPageFileUsage",
        "PeakVirtualSize",
        "PeakWorkingSetSize",
        "Priority",
        "PrivatePageCount",
        "ProcessId",
        "QuotaNonPagedPoolUsage",
        "QuotaPagedPoolUsage",
        "QuotaPeakNonPagedPoolUsage",
        "QuotaPeakPagedPoolUsage",
        "ReadOperationCount",
        "ReadTransferCount",
        "SessionId",
        "Status",
        "TerminationDate",
        "ThreadCount",
        "UserModeTime",
        "VirtualSize",
        "WindowsVersion",
        "WorkingSetSize",
        "WriteOperationCount",
        "WriteTransferCount",
    ]
    allinfos = {}
    WMI, processes = get_process_instances()
    for process in processes:
        pid = process.Properties_("ProcessID").Value
        parent = process.Properties_("ParentProcessId").Value
        allinfos.setdefault(pid, {})
        allinfos.setdefault(parent, {})
        for pro in allprops:
            try:
                allinfos[pid].setdefault(pro, process.Properties_(pro).Value)
                allinfos[pid].setdefault("is_parent", False)
            except Exception:
                allinfos[pid].setdefault(pro, None)
                allinfos[pid].setdefault("is_parent", False)
                continue
        for pro in allprops:
            try:
                allinfos[parent].setdefault(pro, process.Properties_(pro).Value)
                allinfos[parent]["is_parent"] = True
            except Exception:
                allinfos[parent].setdefault(pro, None)
                allinfos[parent]["is_parent"] = True
                continue

    return allinfos


def kill_subprocs(dontkill: tuple = (("Caption", "conhost.exe"),)) -> list:
    r"""
    Kills all child processes of the current process except for those specified in the `dontkill` tuple, and returns a list of the PIDs of the killed processes.

    Args:
        dontkill: A tuple containing tuples of process properties and their respective values. Processes matching any of the properties specified in `dontkill` will not be killed. The default value is (("Caption", "conhost.exe"),), which will prevent the killing of any conhost.exe processes.

    Returns:
        A list of the PIDs of the killed processes.

    Raises:
        None

    """
    killedpids = []
    pr = get_pro_properties()

    mypid = os.getpid()
    chi = [(key, item) for key, item in pr.items() if item["ParentProcessId"] == mypid]
    oldlen = -1
    chilen = len(chi)
    while oldlen != chilen:
        oldlen = chilen
        for c in chi:
            othpo = [
                (key, item)
                for key, item in pr.items()
                if item["ParentProcessId"] == c[0]
            ]
            if othpo:
                for oo in othpo:
                    if oo not in chi:
                        chi.extend(othpo)
        chilen = len(chi)

    nottokill = list(
        set(
            [
                q[0]
                for q in [
                    [x[0] if x[1][y[0]] == y[1] else -1 for y in dontkill] for x in chi
                ]
                if q[0] != -1
            ]
        )
    )
    tokill = [x for x in chi if x[0] not in nottokill]
    tokill = sorted(tokill, key=lambda x: x[1]["is_parent"])
    for pi in tokill:
        killedpids.extend(kill_pid(pi[0]))

    return killedpids


def subprocess_timeout(*args, **kwargs):
    r"""
    Runs a subprocess with the specified command and arguments, and returns a `subprocess.Popen` object. If a `timeout` value is provided, the function will wait for the subprocess to complete, but will kill it and its child processes if it takes longer than the specified timeout.

    Args:
        *args: Positional arguments to be passed to `subprocess.Popen`.
        **kwargs: Keyword arguments to be passed to `subprocess.Popen`.
        timeout: Optional. The maximum amount of time (in seconds) to wait for the subprocess to complete. If the subprocess does not complete within this time, it will be terminated along with its child processes. Default value is -1 (no timeout).

    Returns:
        A `subprocess.Popen` object representing the subprocess.

    Raises:
        None

    """
    timeout = -1
    if "timeout" in kwargs:
        timeout = kwargs["timeout"]
        del kwargs["timeout"]
    p = subprocess.Popen(*args, **kwargs)

    if timeout > -1:
        finaltimeout = time.time() + timeout
        while is_process_alive(p.pid):
            if time.time() > finaltimeout:
                kill_subprocs(dontkill=(("Caption", "conhost.exe"),))
                break
            time.sleep(0.005)
    return p


def kill_process_children_parents(
    pid: int, max_parent_exe: str | None = None, dontkill: tuple = ()
) -> list:
    r"""
    Kill a process and all its child processes.

    Args:
    pid (int): The process ID to be killed.
    max_parent_exe (str|None, optional): The maximum parent process exe name to kill (for now, the maximum is one level up). Defaults to None.
    dontkill (tuple, optional): A tuple containing key-value pairs of process properties that should not be killed. Defaults to ().

    Returns:
    list: A list of killed process IDs.
    """
    try:
        max_parent_exe = max_parent_exe.strip().lower()
    except Exception:
        pass
    pr = get_pro_properties()
    mypid = pid

    WMI = comtypes.client.CoGetObject("winmgmts:")
    processes = WMI.InstancesOf("Win32_Process")
    subprocess_pids = {}

    for process in processes:
        pid = process.Properties_("ProcessID").Value
        parent = process.Properties_("ParentProcessId").Value
        subprocess_pids.setdefault(parent, []).append(pid)
        subprocess_pids.setdefault(pid, [])

    susu = list(fla_tu(subprocess_pids))
    allsubis = []

    def get_all_chi(i):
        for q in subprocess_pids[i]:
            allsubis.append(q)
            get_all_chi(q)

    get_all_chi(mypid)
    allsubis.append(mypid)
    if max_parent_exe:
        for x in susu:
            if mypid == x[0]:
                if (pr[x[1][0]]["Caption"]).strip().lower() == max_parent_exe:
                    get_all_chi(x[1][0])
                    allsubis.append(x[1][0])

    anni = []
    for su in allsubis:
        anni.append(tuple(pr[su].items()))
    anni = OrderedSet(anni)
    allkilled = []
    for a in anni:
        diza = dict(a)
        if dontkill:
            for do in dontkill:
                if diza[do[0]] == do[1]:
                    continue
        allkilled.append(kill_pid(diza["ProcessId"]))
    return allkilled


@add_sysargv
def kill_process(
    pid: int | None = None,
    max_parent_exe: str | None = None,
    dontkill: tuple | None = None,
) -> None:
    r"""
    Kill a process and all of its child processes and parents.

    Args:
        pid (int | None): The process ID to kill.
        max_parent_exe (str | None): The maximum parent executable to kill up to. If specified,
            only child processes and parents whose highest-level parent has this executable name
            will be killed. (for now, the maximum is one level up)
        dontkill (tuple | None): A tuple of process properties (represented as (key, value) pairs)
            that should not be killed. Processes whose properties match any of these values will be
            skipped.

    Returns:
        None.
    """
    if not pid:
        return
    print(
        repr(
            kill_process_children_parents(
                pid=pid, max_parent_exe=max_parent_exe, dontkill=dontkill
            )
        )
    )


if __name__ == "__main__":
    kill_process()
