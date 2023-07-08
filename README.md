# timer_app_python

## about
this is timer app(console based). this program does 2 main thing.
- counting the times the computer was on. -> the records will be saved on directory `timer_data` in .csv file
- set timer and play alarm sound when the time is done.

## installation
this program works in windows.

first: download the repository on your machine

second: make exe file by running this lines in cmd:
`pyinstaller --noconfirm --onedir --console --icon "[path to icon]/clock_icon.ico"  "[path to main.py file]/main.py"`

third: well to play sound you have to put the `alarm_sound.mp3` in the main(the folder that .exe file located) folder
Note: you can move the main file whereever you want

fourth: and to auto start the program. first crate a shortcut to the main.exe file. and then put that shortcut in startup folder(open win+R, type: `shell:startup`)

the records should be saved in [the path to folder which main.exe located]/timer_app/records.csv

if you want to change the alarm sound you can just replace the alram_sound.mp3 with another sound(make sure the new sound has the same name as default sound)
