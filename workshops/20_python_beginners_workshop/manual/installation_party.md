# Installation Party

We ask you to install two things:
1. Python 3 interpreter, so that you can run your code.
2. Pycharm - a powerful editor[^1] to make your programming efforts easier.

## Table of Contents
* [Installing Python 3](#installing-python-3)
* [Installing PyCharm](#installing-pycharm)

## Installing Python 3
Choose your operating system and follow the instructions:
* [Windows](#windows)
* [Linux](#linux) on an example of Ubuntu
* [Mac OS X](#mac-os-x)

### Windows 

You can go with official Python release but we do not recommend it. Primarily, because it supports only 32-bit OS architecture. 

Instead, we recommend that you go with Anaconda distribution of Python, specifically tailored for data analysis. 
1. Go to [Anaconda download page](https://www.anaconda.com/download/).
1. Choose the Python 3.X version. At the time of writing it is version 3.6.
1. Also, choose the 64-bit installer if you have a 64-bit operating system, otherwise go with the 32-bit installer. If you are not sure which is right for you, see our [Shall I choose a 32-bit or a 64-bit installer?](os_architecture.md) page.
1. Download and run the installer. 
  * When prompted where to install Anaconda, copy the suggested location aside (we'll need it later on) OR change it to something that you will easily find afterwards (like `C:\Anaconda3`).

Once you have your Anaconda installed, there is one trick that will make your life easier. Follow these steps:

6. Press "Windows" key and search for "Edit the system environment variables".
1. In the "User variables" section (top one) 
  * press "New...". 
  * Variable name: `PYTHON3`. 
  * Variable value: `[Anaconda_dir];[Anaconda_dir]\Scripts;[Anaconda_dir]\Library\bin;` replacing `[Anaconda_dir]` with the directory you copied aside in step 5. 
  * Press "OK". You just created a new User variable `PYTHON3`. 
8. Do you have a `Path` User variable?
  * If not, press "New...". In the window that just showed set Variable name: `Path`. Variable value: `%PYTHON3%`. Press "OK". 
  * If yes, press "Edit..". In the window that just showed press "New" (that will make the last row of the table editable) and paste `%PYTHON3%` there. 
  
In the end it should look something like this:
![Python Environment Variable](images/environment_variables.png "Python environment variables")
  
Now, if everything worked fine you should be able to access Python from any location. Test it:
1. Press "Windows" key, type "cmd" (that should find a command prompt) and press Enter. 
2. type `python` and press enter
3. If everything went well you'll see something like that:
```
C:\Users\youruser>python
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Type `quit()` to exit Python interpreter, and `exit` to shut down the command prompt window.

4. If you see this:
```
C:\Users\youruser>python
'python' is not recognized as an internal or external command,
operable program or batch file.
```
then something went wrong. Try again or search for support on our Slack.

### Linux

Ubuntu (at least as of 16.04 LTE) ships with both Python 3 and Python 2 pre-installed. To make sure our versions are up-to-date run:
```
sudo apt-get update
sudo apt-get upgrade
```
typing in your password and agreeing when necessary.

Once the process is complete, we can check the version of Python 3 that is installed in the system by typing:

```
python3 -V
```

You will receive output in the terminal window that will let you know the version number. The version number may vary, but it will look similar to this:

```
Python 3.6.5
```

To manage software packages for Python, let’s install pip:

```
sudo apt-get install -y python3-pip
```

A tool for use with Python, pip installs and manages programming packages we may want to use in our development projects. You can install Python packages by typing:

```
pip3 install package_name
```

Here, `package_name` can refer to any Python package or library, such as Django for web development or NumPy for scientific computing. So if you would like to install NumPy, you can do so with the command `pip3 install numpy`.


### Mac OS X

Although Mac OS X comes with Python pre-installed, it is a wrong version of Python (2.7) and we need to install a new one (3.X, currently 3.6 or 3.7). 

1. Install Xcode. It is required to install Homebrew and Python. Download it from the App store. 

## Installing PyCharm

PyCharm is an [Integrated Development Enviroment (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment)) for Python that allows you to write, run and debug code, easily intergrate your projects with remote repositories, and many more.

Below are instructions for various operating systems. If you are running on Windows or you OS is not listed then follow the instructions in the [Direct download section](#direct-download).

### Ubuntu

In "Ubuntu Software" search for "PyCharm CE". If available install it. If not, follow the instructions in the [Direct download section](#direct-download).

### Mac OS X

In "App Store" search for "PyCharm CE" or "PyCharm Community Edition". If available install it from there.

If not, follow the instructions in the [Direct download section](#direct-download).

### Direct download 

If running on Ubuntu or Mac OS check for PyCharm community edition in . If available, it is okay to install it from the store.

From the [download page of PyCharm](https://www.jetbrains.com/pycharm/download/) download the **Community** edition for your OS. Run the installer. 
