import os 
import subprocess 
import re

def detect_keylogger():
    # Get the list of running processes
    processes = subprocess.check_output(['ps', '-eo', 'pid,args'], shell=False).decode('utf-8').split('\n')

    # Check if any processes match known keyloggers
    keyloggers = ['logkeys', 'lkl', 'ubkey', 'thc-vlogger', 'thc-vlogger-bruteforce', 'cron', 'nohup', 'busybox']
    for process in processes:
        for keylogger in keyloggers:
            if re.search(keylogger, process, re.IGNORECASE):
                print('Keylogger detected: ' + process)
                return True

    # Check for any suspicious files in the home folder
    home_folder = os.environ['HOME']
    suspicious_files = ['.logs', '.klog', '.xlog', '.vlog', '.ssh/authorized_keys', '.ssh/config', '.ssh/id_rsa', '.ssh/id_rsa.pub', '.ssh/known_hosts','.logkeys']
    for file in os.listdir(home_folder):
        for suspicious_file in suspicious_files:
            if re.search(suspicious_file, file, re.IGNORECASE):
                print('Suspicious file found: ' + os.path.join(home_folder, file))
                return True

    # No keyloggers detected
    print('No keyloggers detected.')
    return False

if __name__ == '__main__':
    detect_keylogger()

