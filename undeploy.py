import os
import shutil

# Remove virtual environment
if os.path.isdir('.venv'):
    shutil.rmtree('.venv')
    
# Remove generated file
if os.path.isfile('content'):
    os.remove('content')
