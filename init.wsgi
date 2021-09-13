activate_this = '/home/bitspan/testing_bitspanindia_com/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
import sys
sys.path.insert(0,"/home/bitspan/")
from testing_bitspanindia_com import app as application
