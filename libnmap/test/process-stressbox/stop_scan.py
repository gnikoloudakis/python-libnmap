#!/usr/bin/env python

from time import sleep

from libnmap.process import NmapProcess

nmap_proc = NmapProcess(targets="scanme.nmap.org", options="-sV")
nmap_proc.run_background()
while nmap_proc.is_running():
    nmaptask = nmap_proc.current_task
    if nmaptask:
        print(
            "Task {0} ({1}): ETC: {2} DONE: {3}%".format(
                nmaptask.name, nmaptask.status, nmaptask.etc, nmaptask.progress
            )
        )
    sleep(3)
    nmap_proc.stop()

print("rc: {0} output: {1}".format(nmap_proc.rc, nmap_proc.summary))
print(nmap_proc.stdout)
print(nmap_proc.stderr)
