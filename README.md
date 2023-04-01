# Python-Package-Checker-and-Installer
A simple script that I wrote to be used at the beginning of Python Scripts to Verify that they have all of the necessary packages needed to run the script installed. 

## Setup
---
#### Install the latest version of Python

Visit https://www.python.org/downloads/ and install the latest version of Python. As of writing, this is Python 3.11.2 
![download-installer](https://github.com/jaredbergenthal/Simple-Defang-Tool/blob/main/images/download-installer.png)

Once the executable is downloaded, run the installer selecting the express “Install Now” option.


![install-python](https://github.com/jaredbergenthal/Simple-Defang-Tool/blob/main/images/install-python.png)

After the setup is complete, ensure that python is correctly installed. You can do this from the command prompt by openin the command prompt and typing 
```sh
python --version
```


![run-cmd](https://github.com/jaredbergenthal/Simple-Defang-Tool/blob/main/images/run-cmd.png)




#### Python-Package-Checker-and-Installer

Go to https://github.com/jaredbergenthal/Python-Package-Checker-and-Installer, and from here select the green “Code” button, select download zip, download, and extract the tool. After the file is extracted, you can take this code and add it to any program you wish to share with others but don't want to worry about telling them which packages need to be downloaded. This tool simply takes all the hassle out of sharing Python scripts. 


Below is a screenshot of some code that I wanted to share with a friend. As can be seen the Python Package PyperClip hasn't been installed and once the code was run an error message showing that the Module requests wasn't found was displayed.

![error message](https://github.com/jaredbergenthal/Python-Package-Checker-and-Installer/blob/main/images/Error%20Message.jpg)

In order to get the code to work I added the Python-Package-Checker-and-Installer code to the beginning of the script. In order to make the program check all of the packages needed one simply needs to add the names of the packages to the pythonPackageList as higlighted in the screenshot below. 
![editing the script](https://github.com/jaredbergenthal/Python-Package-Checker-and-Installer/blob/main/images/highlighted%20list.jpg)
Once all the packages are added to the list the program can be executed. As shown below it correctly installed the Pyperclip module and the code was successfully run. 
![editing the script](https://github.com/jaredbergenthal/Python-Package-Checker-and-Installer/blob/main/images/packages%20Installed.jpg)
Now the code can be successfully shared with anyone and you don't have to worry about telling them which packages to download! 
