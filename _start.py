import sys
import subprocess
from PySide6 import QtWidgets
from main_window import MainWindow
import os
import atexit

app = QtWidgets.QApplication(sys.argv)

exe_dir_path = os.path.dirname(sys.argv[0])
# Dedicated data directory
mongodb_data_path = os.path.join(exe_dir_path, "mongodb-data")

# Unique port
mongodb_port = "PORT"

mongodb_binaries_path = os.path.abspath(os.path.join(exe_dir_path, "mongodb_binary", "bin"))
mongod_path = os.path.join(mongodb_binaries_path, "mongod")
mongorestore_path = os.path.join(mongodb_binaries_path, "mongorestore")
mongo_backup_path = os.path.join(exe_dir_path, "mongo_backup")



if not os.path.exists(mongodb_data_path):
    try:
        os.makedirs(mongodb_data_path)
    except OSError as e:
        print(f"Error creating data directory: {e}")


flag_file_path = os.path.join(exe_dir_path, "mongorestore_done.txt")



mongod = subprocess.Popen([mongod_path, "--dbpath", mongodb_data_path, "--port", f"{mongodb_port}"], cwd=mongodb_binaries_path)


window = MainWindow()

window.show()
app.exec()

def kill():
    mongod.terminate()

atexit.register(kill)
