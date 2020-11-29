import json

text = ""

def load_json(json_path):
    with open(json_path) as file:
        json_info = json.load(file)

    return json_info

def tab(tab_no = 0):
    global text

    for i in range(0, tab_no):
        text += "    "

def ln(txt = "", tab_no = 0):
    global text

    tab(tab_no)
    text += txt + "\n"

def add_options_menu(menus_info):
    for menu_info in menus_info:
        menu_name = "menu_" + menu_info['text'].lower().replace(" ", "")

        ln(menu_name + " = self.menubar.addMenu('" + menu_info['text'] + "')", 2)
        ln()

        options = menu_info['options']

        for option in options:
            if option['type'] == 'option':
                action_name = option['action'] + "_action"

                ln(action_name + " = " + menu_name + ".addAction('" + option['text'] + "')", 2)
                ln(action_name + ".triggered.connect(self." + option['action'] + ")", 2)

            elif option['type'] == 'separator':
                ln(menu_name + ".addSeparator()", 2)

            ln()

def add_options_callbacks(menus_info):
    for menu_info in menus_info:
        options = menu_info['options']
        options = filter(lambda x: x['type'] == 'option', options)

        for option in options:
            ln("def " + option['action'] + "(self):", 1)
            ln("print('" + option['text'] + "')", 2)

            if option['action'] == "exit_app":
                ln("QtCore.QCoreApplication.instance().quit()", 2)

            ln()

def add_last_section(class_name):
    ln("if __name__ == '__main__':")
    ln("app = QtWidgets.QApplication(sys.argv)", 1)
    ln("main_window = " + class_name + "()", 1)
    ln("main_window.show()", 1)
    ln()
    ln("sys.exit(app.exec_())", 1)

def generate_class_text(vars):
    class_name = vars['main_window_class']

    ln("import sys")
    ln("from PySide2 import QtCore, QtWidgets")
    ln()
    ln("class " + class_name + "(QtWidgets.QMainWindow):")
    ln("def __init__(self):", 1)
    ln("super(" + class_name + ", self).__init__()", 2)
    ln()
    ln("self.setWindowTitle('" + vars['window']['title'] + "')", 2)
    ln("self.resize(" + str(vars['window']['width']) + ", " + str(vars['window']['height']) + ")", 2)
    ln()
    ln("self.menubar = self.menuBar()", 2)
    ln("self.load_options_menu()", 2)
    ln()
    ln("def load_options_menu(self):", 1)

    menus_info = load_json('menus.json')

    add_options_menu(menus_info)
    add_options_callbacks(menus_info)
    add_last_section(class_name)

vars = load_json('vars.json')

generate_class_text(vars)

class_name = vars['main_window_class'] + '.py'

with open(class_name, 'w') as file:
    file.write(text)
