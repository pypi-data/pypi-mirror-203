# Python Web I/O
 Generate a webpage as a GUI for a Python script, and serve from anywhere.

## Usage
```
$ export FLASK_SECRET_KEY="someSecureSecretKey"
$ python_web_io .\example.py
```
* Create a `.envrc` file, setting `FLASK_SECRET_KEY` as per [`python_web_io/.envrc.example`](https://github.com/Cutwell/python-web-io/blob/main/python_web_io/.envrc.example).
* Try running the [`example.py`](https://github.com/Cutwell/python-web-io/blob/main/python_web_io/example.py) script using `python_web_io example.py`.

## Config
|Argument|||
|:---:|:---:|:---:|
|`"example.py"`|Required|Specify the file path for the app Python script / entrypoint.|
|`--title "Python Web I/O"`|Optional|Set a title for the browser tab / website title.|
|`--icon "🎯"`|Optional|Set an emoji icon for the browser tab / website icon.|
|`--debug`|Optional|Run the Flask server with debug output enabled.|

## License
MIT
