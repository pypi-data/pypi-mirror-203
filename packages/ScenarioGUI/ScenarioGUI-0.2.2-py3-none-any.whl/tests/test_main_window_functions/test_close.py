import os
from functools import partial

import PySide6.QtCore as QtC
import PySide6.QtWidgets as QtW

import ScenarioGUI.global_settings as globs
from ScenarioGUI.gui_classes.gui_combine_window import MainWindow

from ..gui_structure_for_tests import GUI
from ..result_creating_class_for_tests import ResultsClass, data_2_results
from ..test_translations.translation_class import Translations


def test_close(qtbot):
    """
    test if the close dialog works correctly

    Parameters
    ----------
    qtbot: qtbot
        bot for the GUI
    """

    # init gui window
    main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
    main_window.delete_backup()
    main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
    main_window.add_scenario()
    main_window.gui_structure.float_b.set_value(2.1)
    # set filenames
    filename_1 = f"test_1.{globs.FILE_EXTENSION}"
    # delete files if they already exists
    if os.path.exists(main_window.default_path.joinpath(filename_1)):  # pragma: no cover
        os.remove(main_window.default_path.joinpath(filename_1))

    def close():
        # handle dialog now
        if isinstance(main_window.dialog, QtW.QMessageBox):
            main_window.dialog.close()

    def cancel():
        # handle dialog now
        if isinstance(main_window.dialog, QtW.QMessageBox):
            main_window.dialog.buttons()[2].click()

    def exit_window():
        # handle dialog now
        if isinstance(main_window.dialog, QtW.QMessageBox):
            main_window.dialog.buttons()[1].click()

    def save():
        # handle dialog now
        if isinstance(main_window.dialog, QtW.QMessageBox):
            main_window.dialog.buttons()[0].click()

    QtC.QTimer.singleShot(500, close)
    main_window.close()

    QtC.QTimer.singleShot(500, cancel)
    main_window.close()

    QtC.QTimer.singleShot(500, save)
    
    def get_save_file_name(*args, **kwargs):
        """getSaveFileName proxy"""
        return kwargs["return_value"]
    
    QtW.QFileDialog.getSaveFileName = partial(get_save_file_name, return_value=(f"{filename_1}", f"{main_window.filename_default[1]}"))
    main_window.close()

    QtC.QTimer.singleShot(500, exit_window)
    main_window.close()
    main_window.delete_backup()
