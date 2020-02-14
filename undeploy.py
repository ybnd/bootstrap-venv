import os
import shutil

if os.path.isdir('.venv'):
    shutil.rmtree('.venv')
    
    
if os.path.isfile('content'):
    os.remove('content')
