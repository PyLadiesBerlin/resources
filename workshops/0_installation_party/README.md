# Getting started - setting up your machine

Our goal is to get you set up with the base things you will need to participate in our other workshops.

🔊 In short you will learn the following:

- How to [install Python](#installing-python)
- How to [set up a virtual environment](#setting-up-virtual-environments)
- [Install an IDE](#setting-up-a-code-editor-ide), what it is and why we use one
- [Install Git](#installing-git) and [connect to GitHub](#getting-started---setting-up-your-machine) so you can start pushing and pulling code
- [Put it all together and clone this repository](#putting-it-all-together)

🚨 Before you continue you will need the following:

- a free [github account](https://github.com/signup) *requires an email and name*
- a computer on which you have permission to install new software

## Installing Python

First!
Check if you already have python installed by writing the following in a terminal:

```sh
python --version
```

Linux and macOS users might be familiar with terminals, if you are using windows you
can try executing `cmd` from your applications, it should open a black window
where you can write.

If you see the following output then you already have python installed and don’t need to do anything:

```sh
Python 3.x.x
```

Other wise follow [these](https://tutorial.djangogirls.org/en/installation/#python) instructions.

> **Note**
> If the version is below 3.8.x then you will need to upgrade the version.
> You can read about managing multiple python versions [here](https://github.com/pyenv/pyenv#simple-python-version-management-pyenv).


## Setting up Virtual environments

Virtual environments are isolated spaces on your computer where you can run your code and install libraries without affecting the rest of your machine's setup. We recommend setting up [python venv](https://docs.python.org/3/library/venv.html). You will see that there are many ways to create these, and even with different options, the idea of using `venv` is because it's included with Python already.

Convention is to create a new one for each project to help avoid conflicts with other installations. Virtual environments are easy to delete and rebuild in case of errors. [Read more](https://realpython.com/python-virtual-environments-a-primer/).

## Setting up a Code editor (IDE)

There are many code editors and IDEs (Integrated Development Environment), which one you choose to use for viewing, editing, updating, running and debugging your code is up to you.
We recommend using [Visual Studio Code (VSC)](https://code.visualstudio.com) because it is popular among professional programmers, offers multiple languages support and is free to use. [Read more](https://realpython.com/python-ides-code-editors-guide/).

In case you prefer to install another IDE, it's totally fine, and at the end
will depend of your taste.

## Installing Git

Git is a version control system which allows us to track changes in computer files. Files saved in Git can be "rewound" to find previous versions, which can be very useful when debugging!

First!
Check if you already have git installed, open your terminal and run:

```sh
git --version
```

If you see the following output then you already have git installed and don’t need to do anything:

```sh
git version 2.x.x
```

Otherwise follow [these instructions](https://github.com/git-guides/install-git).

## Connecting with GitHub

[GitHub](https//github.com) is a website and hosting service for our projects, connected with git. You will need to [sign up](https://github.com/join) for an account, if you have not already. We will use it to store our code. It also allows us to collaborate with others and can be used to showcase your work.

Setting up ssh. When you connect your local machine to GitHub it is easiest to set it up with a ssh connection. This is a security key that will sit on your machine and GitHub will check for it when you want to pull or push code between your local machine and the GitHub server. If you don't set this up you will be required to log in via the terminal each time you want to interact with the server.

## Putting it all together

Once you have all these things set up (please ask coaches if you are at a setup event or reach out on slack if you need support) we have a small challenge for you to test the setup has been done correctly, this will also ensure you are ready for future PyLadies workshops *(though note some of them may require more than this base setup to be completed before attending)*.

### Your challenge

- Use GitHub to fork this repository
- Clone your fork to local machine using Git

  ```sh
  git clone git@github.com:YOUR_USERNAME/resources
  ```
  replacing `YOUR_USERNAME` by your Github username.
- Open the code in your code editor (for further steps you *can* use the terminal in your IDE)
- Create a virtual environment for this project with Python's `venv`

Linux & Mac OS
```sh
# create your virtual environment
python -m venv venv
# activate it
source venv/bin/activate

```

Windows
```sh
# create your virtual environment
python -m venv venv
# activate it on `cmd`
venv\Scripts\activate
# OR activate it on `PowerShell`
. .\venv\Scripts\activate.ps1
```
- Update the code in [test_script.py](README.md) with your name/nickname/twitter handle
- Run the script with Python using the following command

```sh
# you need run this from within this directory
cd workshops/0_installation_party/
python test_script.py
```
- Confirm the output contains your given name
- Add your changes using git

```sh
git add test_script.py
```

- Commit your change using git

```sh
git commit -m 'updated with my name'
```
- Push your change using git

```sh
git push
```
- Confirm that your changes are visible on GitHub *(on your fork)*
- Celebrate - you are now finished with the set up! 🎉

## Further reading and resources

- [Git and GitHub Tutorial For Beginners | Full Course [2021] [NEW]](https://www.youtube.com/watch?v=3fUbBnN_H2c)
- [Introduction to Version Control and Git](http://tutorials.codebar.io/version-control/introduction/tutorial.html) by [CodeBar](https://codebar.io/)
