# Python-Package-Checker-and-Installer
A simple script that I wrote to be used at the beginning of Python Scripts to Verify that they have all of the necessary packages needed to run the script installed. 

## Setup
---
#### Install the latest version of Python

Visit https://www.python.org/downloads/ and install the latest version of Python. As of writing, this is Python 3.11.2 
![download-installer](https://github.com/jaredbergenthal/Simple-Defang-Tool/blob/main/images/download-installer.png)

Once the executable is downloaded, run the installer selecting the express “Install Now” option.


![install-python](https://github.com/jaredbergenthal/Simple-Defang-Tool/blob/main/images/install-python.png)

After the setup is complete, you’ll need to ensure that pyperclip, a module that handles plain text copy and paste functions, is installed. On a windows machine, input windows + r to open the “run” prompt, and input “cmd” and hit okay.


![run-cmd](https://github.com/jaredbergenthal/Simple-Defang-Tool/blob/main/images/run-cmd.png)

#### install pyperclip
This will open your windows command prompt. From here, input 
`pip install pyperclip`
and hit enter to install the pyperclip.


![install-pyperclip](https://github.com/jaredbergenthal/Simple-Defang-Tool/blob/main/images/install-pyperclip.png)


#### Install the defanging tool

Go to https://github.com/jaredbergenthal/Simple-Defang-Tool, and from here select the green “Code” button, select download zip, download, and extract the tool. After the file is extracted, simply double click the file entitled “main.py” to run it.

![main-prompt](https://github.com/jaredbergenthal/Simple-Defang-Tool/blob/main/images/main-prompt.png)
From here, input the URL/ip you wish to defang. If you would like to include another URL/ip, simply click enter once then type the next one. When finished, click enter twice to run the program.

```sh
<ip> [Enter]
```
(Additional as needed:
```sh
<ip> [Enter]
```
)
```sh
[Enter]
```

![defanged-example](https://github.com/jaredbergenthal/Simple-Defang-Tool/blob/main/images/Test%20case%203.png)

The new, defanged url is now copied to your clipboard and ready for you to analyze. 

---

Here is an example of Malicious IP addresses and Links being found on GreyNoise
![defanged-example1](https://github.com/jaredbergenthal/Simple-Defang-Tool/blob/2d7abcfef6aa0e96a9cf855afc16fb3745cb160c/images/Test%20case%201.png)
