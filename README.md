# AutoPyUIC
Tool to automatically convert .ui made with Qt Designer files to .py with pyuic5.

# Requirements
You only need `watchdog` module to use this.
```
pip install -r requirements.txt
```

# Usage
```
python main.py [directory]
```
Directory must be specified. To monitor current directory, set it to `/`.

If you want to activate recursive mode (which also monitors subfolders), add the `-r` argument.
```
python main.py [directory] -r
```
