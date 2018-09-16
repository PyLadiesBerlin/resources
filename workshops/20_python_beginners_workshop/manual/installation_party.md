# Installation Party

We'll ask you to do two installations: 
1. Python interpreter so that you can run your code.
2. Pycharm - a powerful editor[^1] to make your programming efforts easier.

## Table of Contents
* [Installing Python](#installing-python-3)
* [Installing PyCharm](#installing-pycharm)

## Installing Python 3
Choose your operating system and follow the instructions:
* [Windows](#windows)
* [Linux](#linux)
* [Mac OS](#mac-os)

### Windows 

You can go with official Python release but we do not recommend it. Primarily, because it supports only 32-bit OS architecture. 

Instead, we recommend that you go with Anaconda distribution of Python, specifically tailored for data analysis. 
1. Go to [Anaconda download page](https://www.anaconda.com/download/).
1. Choose the Python 3.X version. At the time of writing it is version 3.6.
1. Also, choose the 64-bit installer if you have a 64-bit operating system, otherwise go with the 32-bit installer. If you are wondering whether you should choose a 64-bit or a 32-bit installer, see our [Shall I choose a 32-bit or a 64-bit installer?](os_architecture.md) page.
1. Download and run the installer.
1. When prompted where to install Anaconda, copy the suggested location aside (we'll need it later on) OR change it to something that you will easily find afterwards (like `C:\Anaconda3`).

Once you have your Anaconda installed, there is one trick that will make your life easier. Follow these steps:

6. Press "Windows" key and search for "Edit the system environment variables".
1. In the "User variables" section (top one) 
  * press "New...". 
  * Variable name: `PYTHON3`. 
  * Variable value: `[Anaconda_dir];[Anaconda_dir]\Scripts;[Anaconda_dir]\Library\bin;` replacing `[Anaconda_dir]` with the directory you copied aside in step 5.`. 
  * Press "OK". You just created a new User variable `PYTHON3`. 
8. Do you have a `Path` User variable?
  * If not, press "New...". In the window that just showed set Variable name: `Path`. Variable value: `%PYTHON3%`. Press "OK". 
  * If yes, press "Edit..". In the window that just showed press "New" (that will make the last row of the table editable) and paste `%PYTHON3%` there. 
  
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
then something went wrong. Try again or search for support on our Slack channel.

### Linux

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vehicula auctor viverra. Sed dapibus efficitur quam quis scelerisque. Nam efficitur ornare nisi. Vivamus placerat mi id maximus pellentesque. Aliquam ultricies sapien porta ante lobortis, non feugiat turpis vulputate. Vestibulum porttitor augue tortor, id volutpat leo condimentum eu. Curabitur id facilisis velit. Aliquam erat volutpat. Nullam varius iaculis quam, sit amet sagittis magna. Sed non fringilla orci. Donec fermentum lorem ipsum, placerat dictum lacus dapibus et. Aenean molestie lorem ut erat efficitur fringilla. Nunc viverra, orci eu eleifend vestibulum, turpis nibh lacinia lacus, ac ultrices turpis neque sed mauris. Maecenas mattis nibh vel suscipit pellentesque. Aenean eu mauris rhoncus nisi iaculis malesuada eget et tortor.

Quisque convallis diam ac ultrices sodales. Nulla facilisi. Etiam vitae metus facilisis, elementum arcu in, laoreet enim. Nullam ut leo id libero dapibus consequat. Quisque felis augue, faucibus non nunc ut, interdum venenatis neque. Vivamus volutpat magna orci, nec viverra ligula efficitur sed. Sed vel magna convallis, fringilla tellus nec, eleifend ante.

Maecenas nec est tempor, egestas justo faucibus, pulvinar odio. Aenean vulputate odio ut eros hendrerit pretium. Sed a velit eget turpis ornare auctor vitae nec lectus. Proin fringilla velit arcu, sit amet volutpat risus auctor eget. Fusce hendrerit iaculis vehicula. Phasellus ac turpis non velit rhoncus egestas non a augue. Nullam id erat aliquam quam placerat congue sit amet sed dolor.

Pellentesque vestibulum, dui eu feugiat maximus, dui massa dignissim neque, ac consectetur lacus mi sit amet elit. Maecenas a urna non odio sodales consectetur ut id nulla. Suspendisse sit amet pellentesque quam. Duis tempor purus sed metus varius efficitur. Proin interdum dolor in lacus lobortis lacinia ac ac lectus. Sed at porttitor sapien. Praesent efficitur semper porta. In blandit fringilla sodales. Vestibulum blandit posuere risus. Morbi pharetra hendrerit tristique. Praesent sed consequat turpis, condimentum pulvinar lectus.

Quisque facilisis sapien hendrerit, porttitor ante eu, posuere dui. Donec commodo, mauris sit amet dictum accumsan, tortor diam lobortis urna, ac interdum tortor justo vitae est. Sed molestie, metus ut condimentum consequat, urna odio feugiat velit, id facilisis lectus urna eget sem. Integer et mauris vitae lectus suscipit dignissim nec ac sapien. Mauris ligula nunc, ultricies non ullamcorper scelerisque, aliquam et diam. Sed a orci dolor. Suspendisse potenti. Nulla bibendum metus nec ipsum tempus, sit amet fringilla urna dignissim. Quisque porta tristique nibh vitae molestie. Suspendisse volutpat enim a sapien tempor, eget sodales ante mattis.

### Mac OS

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vehicula auctor viverra. Sed dapibus efficitur quam quis scelerisque. Nam efficitur ornare nisi. Vivamus placerat mi id maximus pellentesque. Aliquam ultricies sapien porta ante lobortis, non feugiat turpis vulputate. Vestibulum porttitor augue tortor, id volutpat leo condimentum eu. Curabitur id facilisis velit. Aliquam erat volutpat. Nullam varius iaculis quam, sit amet sagittis magna. Sed non fringilla orci. Donec fermentum lorem ipsum, placerat dictum lacus dapibus et. Aenean molestie lorem ut erat efficitur fringilla. Nunc viverra, orci eu eleifend vestibulum, turpis nibh lacinia lacus, ac ultrices turpis neque sed mauris. Maecenas mattis nibh vel suscipit pellentesque. Aenean eu mauris rhoncus nisi iaculis malesuada eget et tortor.

Quisque convallis diam ac ultrices sodales. Nulla facilisi. Etiam vitae metus facilisis, elementum arcu in, laoreet enim. Nullam ut leo id libero dapibus consequat. Quisque felis augue, faucibus non nunc ut, interdum venenatis neque. Vivamus volutpat magna orci, nec viverra ligula efficitur sed. Sed vel magna convallis, fringilla tellus nec, eleifend ante.

Maecenas nec est tempor, egestas justo faucibus, pulvinar odio. Aenean vulputate odio ut eros hendrerit pretium. Sed a velit eget turpis ornare auctor vitae nec lectus. Proin fringilla velit arcu, sit amet volutpat risus auctor eget. Fusce hendrerit iaculis vehicula. Phasellus ac turpis non velit rhoncus egestas non a augue. Nullam id erat aliquam quam placerat congue sit amet sed dolor.

Pellentesque vestibulum, dui eu feugiat maximus, dui massa dignissim neque, ac consectetur lacus mi sit amet elit. Maecenas a urna non odio sodales consectetur ut id nulla. Suspendisse sit amet pellentesque quam. Duis tempor purus sed metus varius efficitur. Proin interdum dolor in lacus lobortis lacinia ac ac lectus. Sed at porttitor sapien. Praesent efficitur semper porta. In blandit fringilla sodales. Vestibulum blandit posuere risus. Morbi pharetra hendrerit tristique. Praesent sed consequat turpis, condimentum pulvinar lectus.

Quisque facilisis sapien hendrerit, porttitor ante eu, posuere dui. Donec commodo, mauris sit amet dictum accumsan, tortor diam lobortis urna, ac interdum tortor justo vitae est. Sed molestie, metus ut condimentum consequat, urna odio feugiat velit, id facilisis lectus urna eget sem. Integer et mauris vitae lectus suscipit dignissim nec ac sapien. Mauris ligula nunc, ultricies non ullamcorper scelerisque, aliquam et diam. Sed a orci dolor. Suspendisse potenti. Nulla bibendum metus nec ipsum tempus, sit amet fringilla urna dignissim. Quisque porta tristique nibh vitae molestie. Suspendisse volutpat enim a sapien tempor, eget sodales ante mattis.

## Installing PyCharm

From the [download page of PyCharm](https://www.jetbrains.com/pycharm/download/) download the **Community** edition for your OS. Run the installer. After you're done with the installer run PyCharm. If everything went well you should see something like this:



[^1]: PyCharm is actually an [Integrated Development Enviroment (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment)) rather than a simple editor.
