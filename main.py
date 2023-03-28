######################################## PACKAGE INSTALLER
import importlib
pythonPackageList = [""] #HERE YOU ADD THE PYTHON PACKAGE NAMES for example "requests"

def installed_packageChecker(package_name):
    try:
        importlib.import_module(package_name)
        print(f"The Python Package [{package_name}]: is already installed")
    except ImportError:
        import subprocess
        subprocess.check_call(['pip', 'install', package_name])
        print(f"The Python Package [{package_name}]: has been installed")

# Usage
for i in pythonPackageList:
    installed_packageChecker(i)
##############################################################End of Package installer
