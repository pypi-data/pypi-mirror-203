from je_editor.utils.editor_content.editor_content_data import editor_content_data_dict


def set_language(exec_manager, language):
    """
    :param exec_manager: which exec manager change program language
    :param language: set exec manager program language
    """
    if isinstance(language, list):
        exec_manager.program_language = language[0]
    else:
        exec_manager.program_language = language
    editor_content_data_dict["language"] = language
