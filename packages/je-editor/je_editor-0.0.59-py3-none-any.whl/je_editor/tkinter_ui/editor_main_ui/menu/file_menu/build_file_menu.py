from tkinter import Menu

from je_editor.tkinter_ui.ui_event.change_font.change_font import change_font, change_font_size
from je_editor.tkinter_ui.ui_event.encoding.set_encoding import set_encoding
from je_editor.tkinter_ui.ui_event.language.set_language import set_language
from je_editor.utils.encoding.encoding_data_module import encoding_list
from je_editor.utils.font.font import get_font
from je_editor.utils.language.language_data_module import language_list


def build_file_menu(editor_instance):
    """
    use to init (read data set file menu)
    :param editor_instance: editor's instance
    :return: None
    """
    # File menu
    editor_instance.file_menu = Menu(editor_instance.menu, tearoff=0)
    # Edit setting menu
    editor_instance.editor_setting_menu = Menu(editor_instance.menu, tearoff=0)
    editor_instance.file_menu.add_command(label="Save File", command=editor_instance.ui_save_file_to_open)
    editor_instance.file_menu.add_command(label="Open File", command=editor_instance.ui_open_file_to_read)
    # Encoding menu
    editor_instance.encoding_menu = Menu(editor_instance.editor_setting_menu, tearoff=0)
    # Language menu
    editor_instance.language_menu = Menu(editor_instance.editor_setting_menu, tearoff=0)
    # Text menu
    editor_instance.text_menu = Menu(editor_instance.editor_setting_menu, tearoff=0)
    editor_instance.text_font_sub_menu = Menu(editor_instance.text_menu, tearoff=0)
    editor_instance.text_size_sub_menu = Menu(editor_instance.text_menu, tearoff=0)
    editor_instance.text_menu.add_cascade(label="Font", menu=editor_instance.text_font_sub_menu)
    editor_instance.text_menu.add_cascade(label="Font Size", menu=editor_instance.text_size_sub_menu)
    editor_instance.font_tuple = get_font(editor_instance.main_window)
    # Encoding menu
    for index, value in enumerate(encoding_list):
        editor_instance.encoding_menu.add_command(
            label=str(value),
            command=lambda choose_encoding=value: set_encoding(editor_instance.exec_manager, choose_encoding)
        )
    # Font menu
    for i in range(len(editor_instance.font_tuple)):
        editor_instance.text_font_sub_menu.add_command(
            label=str(editor_instance.font_tuple[i]),
            command=lambda choose_font=editor_instance.font_tuple[i]:
            change_font(editor_instance.code_editor_textarea, editor_instance.program_run_result_textarea, choose_font)
        )
    # Text size menu
    for i in range(12, 36, 2):
        editor_instance.text_size_sub_menu.add_command(
            label=str(i),
            command=lambda font_size=i: change_font_size(editor_instance.code_editor_textarea,
                                                         editor_instance.program_run_result_textarea,
                                                         font_size)
        )
    # Language menu
    for index, value in enumerate(language_list):
        editor_instance.language_menu.add_command(
            label=str(value),
            command=lambda choose_language=value: set_language(editor_instance.exec_manager, choose_language)
        )
    editor_instance.editor_setting_menu.add_cascade(label="Text", menu=editor_instance.text_menu)
    editor_instance.editor_setting_menu.add_cascade(label="Encoding", menu=editor_instance.encoding_menu)
    editor_instance.editor_setting_menu.add_cascade(label="Language", menu=editor_instance.language_menu)
    editor_instance.file_menu.add_separator()
    editor_instance.file_menu.add_cascade(label="Editor Setting", menu=editor_instance.editor_setting_menu)
