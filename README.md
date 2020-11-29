# Main window with menu - QT with PySide generator

This script generates all the boilerplate for a Main window class with menu, using QT and PyDev

## Requirements

This script works using two json configuration files:

- _vars.json_
- _menus.json_

There are two example files in this project. Change them as you want. The explanation of the fields is as follow:

### vars.json
- _$.main_window_class_: Name of the class that will be generated (string)
- _$.window_: Values of the window (object)
- _$.window.title_: Title shown in the main window (string)
- _$.window.width_: Width of the window (integer)
- _$.window.height_: Height of the window (integer)

### menus.json
- _$_: Array with all the main options
- _$[*]_: Object with the main option (the one visible in the menu bar)
- _$[*].text_: Visible text of the main option (string)
- _$[*].options_: Suboptions, nested in the main option (array)
- _$[*].options[*].type_: Type of the option. If this value is "_separator_", adds a separator and ignores the rest of the fields. It it's "_option_", the generator adds an option and uses the rest of the values. No more values are contemplated apart from this two (string)
- _$[*].options[*].text_: Text shown in the suboption (string)
- _$[*].options[*].action_: Name of the method that will be executed as callback of the option. If this methos is "_exit_app_" then adds the code that closes the program.

## Execution
In order to run the program, fill the json files properly and simply type:
```
python generate-menus-class.py
```
This should generate the main class that will be executable
