# Questions

## How do I use slack?
First you need an invitation, and you can get one
[here](https://pyladies-berlin.herokuapp.com/).
Then you will be able to login using this link:
[pyladiesberlin.slack.com](http://pyladiesberlin.slack.com/).

## What do I need to execute Python?
You just need to install it!

This process will depend in your system:
* `Windows`: Download the installer from [here](https://www.python.org/downloads/).
* `macOS`:
 * Download the installer from [here](https://www.python.org/downloads/).
 * You also can use [brew](https://brew.sh/) to [install it](https://docs.brew.sh/Homebrew-and-Python)
* `Linux`:
 * Use your package manager:
  * Ubuntu: `sudo apt-get install python3`
  * Fedora: `sudo dnf install python3`
  * Arch linux: `sudo pacman -S python`

## What is the difference between Python 2 and Python 3?
Python2 is the devil, and Python3 is the best...
OK, for real now... Python2 is the old version of python,
many things are being improved and changed in Python3.

One of main differences is the `print` function:
* In Python2 you write: `print "Hello World!"`
* In Python3 you write: `print("Hello World!")`

Besides this little example, you have more differences, so be aware
when using one of the other.

## What is a terminal?
A terminal is a different way of go through and use your computer, but
since it was a bit complicated to write everything, we started to use
interfaces with folders, clicks, etc.

Terminals will be different in each platform, so here we will cover
just a few:

**Windows**:
 * cmd: Default terminal for Windows.
 * PowerShell: It is an [improved terminal for windows](https://github.com/powershell/powershell).
   (Comes with [Visual Studio Code](https://code.visualstudio.com/))
   but you can install it without if you want.
 * Git Bash: Comes when you install [Git on Windows](https://git-scm.com/download/win)
**macOS**:
 * Terminal: The normal terminal that comes with macOS.
 * iTerm2: It's an [improved terminal for macOS](https://iterm2.com/),
   including features like splitting windows, search, autocomplete, etc.
**Linux**:
 * Any will work almost the same, so don't worry much about it.

## How do navigate through the Terminal?
There are many commands to achieve everything on the terminal,
but you can concentrate in a few that can get you started:

* Changing directories/folders: `cd`
 * e.g.: `cd Desktop/` will take us to the Desktop directory.
* Listing the files of the current directory `dir` (Powershell, cmd),
  `ls` (Linux, macOS, and Git Bash on Windows):
* When python is in the PATH, you can just type:
  `python my_script.py`

## What is an IDE?
It is an [Integrated Development Environment](https://en.wikipedia.org/wiki/Integrated_development_environment),
this means that it's a nice application that provide you with all the tools
to be able to write and execute code:
* You often will have an Editor, from which you can modify your code,
* A terminal, from where you can execute your code,
* A file manager, to open more files or directories.

## Which IDE can I use to develop a Python application?
  There are many out there, among them (in no particular priority order):
  * [Visual Studio Code](https://code.visualstudio.com/)
  * [PyCharm](https://www.jetbrains.com/pycharm/)
  * [Thonny](https://thonny.org/)
  * [Spyder](https://www.spyder-ide.org/)

## What is Jupyter?

The [Jupyter notebook](https://jupyter.org/) is a web application
that allows you to create document that contain code, visualizations,
documentations, and more!.

The main idea is to get a ready-to-use environment to solve problem
related to simulations, statistical modeling, data analysis, machine
learning, etc.

## What is Anaconda?

[Anaconda](https://www.anaconda.com/) is a distribution of Python and R
that comes with many features focus on scientific programming.

You can think of Anaconda of a "special Python flavor" that comes with
many extra features.

One of the most important things is that Anaconda comes with a command
called `conda` from which you can manage different environments, packages,
and much more.

## What is Pandas?

[Pandas](https://pandas.pydata.org/) is a python module that provide a
way to use labeled data structures to perform high performance analysis.
