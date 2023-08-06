import json
import os
from pathlib import Path
from threading import Lock

from je_editor.utils.editor_content.editor_content_data import editor_content_data_dict
from je_editor.utils.exception.exceptions import JEditorContentFileException
from je_editor.utils.json_format.json_process import reformat_json
from je_editor.utils.project.create_project import check_project_is_exist, check_project_content_is_exist
from je_editor.utils.project.create_project import create_project


def read_output_content():
    """
    read the editor content
    """
    lock = Lock()
    try:
        lock.acquire()
        cwd = os.getcwd()
        if check_project_is_exist() and check_project_content_is_exist():
            file_path = Path(cwd + "/.je_editor/je_editor_content.json")
            if file_path.exists() and file_path.is_file():
                with open(cwd + "/.je_editor/je_editor_content.json", "r+") as read_file:
                    return read_file.read()
    except JEditorContentFileException:
        raise JEditorContentFileException
    finally:
        lock.release()


def write_output_content():
    """
    write the editor content
    """
    lock = Lock()
    try:
        lock.acquire()
        cwd = os.getcwd()
        if check_project_is_exist():
            with open(cwd + "/.je_editor/je_editor_content.json", "w+") as file_to_write:
                file_to_write.write(reformat_json(json.dumps(editor_content_data_dict)))
        else:
            create_project()
            with open(cwd + "/.je_editor/je_editor_content.json", "w+") as file_to_write:
                file_to_write.write(reformat_json(json.dumps(editor_content_data_dict)))
    except JEditorContentFileException:
        raise JEditorContentFileException
    finally:
        lock.release()


def save_content_and_quit():
    """
    set content data and write
    """
    write_output_content()


def open_content_and_start():
    """
    read data and set content
    """
    temp_content = read_output_content()
    if temp_content is not None:
        return json.loads(temp_content)
