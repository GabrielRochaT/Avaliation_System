import os
import psutil

def is_file_open(file_path):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            p = psutil.Process(proc.pid)
            for f in p.open_files():
                if f.path == file_path:
                    return True
        except (psutil.NoSuchProcess, psutil.ZombieProcess, psutil.AccessDenied):
            pass
    
    return False

def open_archive(archive_name):
    if os.path.exists(archive_name):
        os.system(f"start notepad {archive_name}")
    else:
        print(f"O arquivo '{archive_name}' não existe.")
