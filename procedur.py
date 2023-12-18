import subprocess

# funkcijas teksts veiksmgai izvadei
def notify_success(script_name):
    print(f'\033[94mSuccess:\033[0m {script_name} completed successfully')

# teksta izvede ja neizdevas
def notify_failure(script_name):
    print(f'\033[91mFailure:\033[0m {script_name} failed')

# lai izpilditu vaig ja neiet tad var pameginat pilno lokaciju (/usr/bin/python3)
py3 = 'python3'

# izpilda migracijas
print("Running migrate.py")
result = subprocess.run([py3, 'migrate.py'])
if result.returncode == 0:
    notify_success("migrate.py")
else:
    notify_failure("migrate.py")

# izpilda testu
print("Running test.py")
result = subprocess.run([py3, 'test.py'])
if result.returncode == 0:
    notify_success("test.py")
else:
    notify_failure("test.py")

# izpilda skriptu
print("Running skript.py")
result = subprocess.run([py3, 'skript.py'])
if result.returncode == 0:
    notify_success("skript.py")
else:
    notify_failure("skript.py")

# izpilda test1
print("Running test1.py")
result = subprocess.run(['pytest', '-s', 'test1.py'])
if result.returncode == 0:
    notify_success("test1.py")
else:
    notify_failure("test1.py")
