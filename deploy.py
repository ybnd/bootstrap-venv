import sys
import shutil
import subprocess

print(f"Running '{__file__}' with {sys.executable}\n")

# Create a virtual environment in .venv
subprocess.check_call(['python', '-m', 'venv', '.venv'])

# Copy activate_this.py to .venv/bin
# shutil.copy('activate_this.py', '.venv/bin')

# Install requirements.txt
subprocess.check_call(['.venv/bin/python', '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.check_call(['.venv/bin/python', '-m', 'pip', 'install', '-r', 'requirements.txt'])

# Run some code with this new environment
subprocess.check_call(['.venv/bin/python', 'generate.py'])
