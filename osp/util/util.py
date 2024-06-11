import time
import subprocess
import os


def poller(interval, timeout):
    """
    Returns a poller for givent interval and timeout
    """
    start = 0
    while (start + interval) <= timeout:
        time.sleep(interval)
        start += interval
        yield True


def run_command(cmd: str) -> tuple:
    """
    Runs a command and returns stdout and stderr
    """
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = p.communicate()
    return stdout, stderr, p.returncode


def oc_create(path: str, namespace: str) -> tuple:
    """
    Runs `oc create -f $path -n $namespace` and returns stdout and stderr
    """
    print(os.getcwd())
    return run_command(f"oc create -f {path} -n {namespace}")


def oc_apply(path: str, namespace: str) -> bool:
    """
    Runs `oc apply -f $path` and returns stdout and stderr
    """
    return run_command(f"oc apply -f {path} -n {namespace}")


def oc_delete(path: str, namespace: str) -> bool:
    """
    Runs `oc delete -f $path` and returns stdout and stderr
    """
    return run_command(f"oc delete -f {path} -n {namespace}")
