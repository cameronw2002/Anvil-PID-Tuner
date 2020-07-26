# Anvil-PID-Tuner
A simple TVC Model Rocket simulator that allows the user to manually tune his PID controller

This software is not designed to give you 100% accurate PID values, it is only designed to give ballpark values.
Use at your own risk

IMPORTANT INFORMATION: In order to use an engine file, you must change the name of the file to "motor.eng" and place it in the same folder as the exe or the python file. The engine file for the estes F-15 is included in this repositorty
If you come across any other errors, make sure there are no blank lines in the file. If you still have issues, feel free to message me on the BPS discord anytime and I will help you out.
Also, the longer the sim length, the less accurate the results, so don't be supprized if things start to look weird when you are pushing 10 seconds on the sim length. I hope to fix this in the future,
but it is a problem with matplotlib as far as I am aware.

Some information about the sliders (this does not apply to the text boxes):
Kp, Kd, and Inertia are all multiplied by 100, ie: if the slider says Kp = 115, Kp is actually 1.15

When you download the exe, Windows will do everything in its power to make sure that you don't open it.
I promise that there are no malicious things included with the exe file.

The Version number is determined by the size of the update. If the update is only minor, the version goes up by 0.01, 
if the update adds a lot, or fixes major bugs, the version goes up by 0.1

# Virtual Env Option:

Done by prettytrue on the BPS discord

- Python3  (or python 2 with virtualenv installed (`pip install virtualenv`))

Windows:
```
C:/...> cd <this_repo>
C:/...> run.bat
...
```

Unix:
```
$> cd <this_repo>
$> ./run
```
