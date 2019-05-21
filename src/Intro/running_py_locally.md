<!---
{"next":"Intro/jupyter_notebooks.md","title":"Running Python Locally"}
-->


# Running Python Locally

Before we get into writing our code, we will have to install a few programs and tools. It may take about a half hr to pull off but ultimately a properly established development environment will pay off in spades as we navigate the rest of our day.

## Installing Python 3

Instructions vary slightly depending on what kind of machine you're using. Click the link below that applies to you:

[Installation Instructions: Mac](#installation-instructions-mac)

[Installation Instructions: Linux](#installation-instructions-linux)

[Installation Instructions: Windows](#installation-instructions-windows)


## Installation Instructions: Mac

Macs usually come with Python 2 already installed. We're going to run through some installation steps to make sure you've got the latest and greatest that Python has to offer.

### 1. Open up your terminal.

You can do this by pressing command+space bar and typing "terminal," or by locating the application and clicking on the icon.


### 2. Install XCode with the following command.

```bash
xcode-select --install
```

This may take a few minutes. Once it's done, you can run the following command to make sure it's installed properly.

```bash
xcode-select -p
```

Your output should look something like this:

> /Applications/Xcode.app/Contents/Developer

### 3. Install `Homebrew` by running the following command.

> **Pro tip:** Do not try to type this in. Copy and paste to make sure everything is correct. Do this by selecting the text with your cursor and pressing command+C. Then, go to your terminal and press command+V.

```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Once this command runs, type `brew doctor` on your terminal prompt. If you get the output `Your system is ready to brew`, you are ready to move on to the next step.


### 4. Add PATH environment variable.

This is a bit confusing, but basically we're setting the path up so Homebrew knows where to install something.

```bash
open ~/.profile
```

The file should open up. Ask your instructor for help if it didn't. Copy and paste the following line at the bottom of this file:

> export PATH=/usr/local/bin:/usr/local/sbin:$PATH

Save the changes and close the file.


### 5. Install Python 3 (finally!).

Homebrew, by default, gets the latest stable version of whatever you're trying to install.

```bash
brew install python
```

### 6. Create an alias for `python3`.

```bash
open ~/.bashrc
```

At the bottom of that file, copy and paste the following lines:

```bash
alias python=python3
alias pip=pip3
```

Learn more about aliases [here](https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3).


### 7. Restart your Terminal.

Right click (control+click on most Macs) on the Terminal icon in your application tray. Select `Quit` from the menu to make sure Terminal is fully stopped. Then, open it again (see Step 1).

> **Pro tip:** Your settings won't be updated until Terminal is fully stopped and restarted. If you simply minimize the program, you will not see any updates!

### 8. Check version.

```bash
python --version
```

You will get something like this. As long as it starts with a 3, you're good to go!

> Python 3.6.5

Now let's check `pip`, the package installer.

```bash
pip --version
```

> pip 10.0.1 from /usr/local/lib/python3.6/site-packages/pip (python 3.6)

You want `pip` to be pointing to the Python 3.x version. If either `python` or `pip` are still pointing to version 2, please alert your instructor.


You are now in a development environment!

## Installation Instructions: Linux

> **Pro tip:** The instructions are for Ubuntu. If you have another version of Linux, please follow these [suggested directions](http://docs.python-guide.org/en/latest/starting/install3/linux/).

### 1. Open your terminal.

Either:

* Click Ubuntu icon (upper-left corner) to open Dash. Then, type "terminal" and select Terminal from the results.

Or:

* Hit the keyboard shortcut `Ctrl - Alt + T`.


### 2. Check to see if Python 3 exists.

Some distributions of Linux come with Python 3 already installed. How nice! To check if you have Python 3 already, run the following command:

```bash
python3 --version
```

If it gives you a version, you're good to go! Otherwise, move to Step 3.


### 3. Install Python 3.6.

```bash
sudo apt-get update
sudo apt-get install python3.6
```

Check again for the Python 3 version.

```bash
python3 --version
```

This time, things should be all good.

If you are still unable to get Python 3, please alert your instructor now.

---

## Installation Instructions: Windows

> **Pro tip:** If you have Windows XP, you need to be downgraded from Python 3.6 to 3.4. Please ask your instructor for help if you plan on using Windows XP.

### 1. Download the Python installer.

Visit [python.org](https://www.python.org/downloads/release/python-365/) and download the web-based installer for Windows. You'll find this under a "Files" section at the bottom of the page.

If you have 64-bit Windows, use the link that contains `64`. If you have 32-bit Windows, download the one without `64`. If you have no idea what you have, [click here to learn how to find out](#windows-64-bit-or-32-bit).


### 2. Run the installer.

* Make sure both `Add Python 3.6 to PATH` and `Install for all users` are checked.
* Click `Install Now`.


### 3. Disable length limit.

After the initial installation is finished, there will be an additional option that says something about a max character limit. **You want this!** Provide permission for this setting to be changed.

### 4. Open your terminal.

```text
    * Click *Start*.
    * Open *Windows System* menu.
    * Select *Command Prompt*.
```

### 5. Run the `py` command.

```bash
py
```

You should get a message telling you what version of Python you're using as well as opening an in-terminal REPL. If you did, great! Skip to the next step.

If you instead received an error message like the one below, something went wrong and Python didn't install correctly.

```bash
'py' is not recognized as an internal or external command,
operable program or batch file.
```

In this case, ask your instructor for assistance.

## Windows 64-Bit or 32-Bit

> **Pro tip:** These directions are for Windows 7 and Windows Vista operating systems. If you have Windows 10, you most likely have a 64-bit machine, but if you want to be extra sure, [check here](https://support.microsoft.com/en-us/help/13443/windows-which-operating-system).

1. Open "System" by clicking the "Start" button.

2. Right click "Computer."

3. Click "Properties."

4. Under "System," you can view the system type.

This will give you a bunch of stats about your machine, including whether it is 32-bit or 64-bit.

5. Return to [Installation Instructions: Windows](#installation-instructions-windows).


## 🚗 Parking Lot

* [Official OSX Installation Instructions](http://docs.python-guide.org/en/latest/starting/install3/osx/)
* [Official Windows Installation Instructions](https://docs.python.org/3/using/windows.html)
* [Windows-Specific Modules](https://docs.python.org/3/library/windows.html#mswin-specific-services)
