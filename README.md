# DongerTyper - A small customizable panel for all your text emoticons

ヽ༼ຈل͜ຈ༽ﾉ With this small script you will be able to raise your dongers as efficiently and easily as you want. ヽ༼ຈل͜ຈ༽ﾉ


![DongerTyper](http://i.imgur.com/VVieR7Z.png)

## Install


### For Linux/Mac
There's no install required. I might look into how to make it a standalone executable. For now just clone the repository and execute DongerTyper with Python.

```
python3 /route/to/dongertyper.py
```

**Also be sure that you have dongerlist.txt in the same directory as the python script. If you want to have them separated, you'll have to edit the script.**

### For Windows

(ಥ﹏ಥ) Sorry guys, I don't know how to use this in windows. I guess you'll have to install python3.5 and gtk. I'll research more about it some day, I promise.

## Usage

When you execute it, a small window will appear. You can scroll through it and just choose a text emoticon. It will be automatically copied to your clipboard, ready to paste. The program will close itself when you click a donger.

## Customization

You can add as many text emotes as you want to DongerTyper! Just add them to dongerlist.txt. Each line in dongerlist.txt will be automatically turned into a button ready to be pressed in the program, so you can add anything you want.

If you want to keep the window open constantly, just comment the following line in the code, in the line 43.

```
Gtk.main_quit()
```
