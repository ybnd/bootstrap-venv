import sys
from faker import Faker

print(f"\n\nRunning '{__file__}' with {sys.executable}\n")

# Generate some text using a module we've just installed
fake = Faker()

with open('content', 'w+') as f:
    f.write(fake.text())
