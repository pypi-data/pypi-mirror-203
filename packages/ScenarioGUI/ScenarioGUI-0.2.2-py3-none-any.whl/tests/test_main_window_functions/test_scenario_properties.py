import PySide6.QtWidgets as QtW

from ScenarioGUI.gui_classes.gui_combine_window import MainWindow

from ..gui_structure_for_tests import GUI
from ..result_creating_class_for_tests import ResultsClass, data_2_results
from ..test_translations.translation_class import Translations


def test_gui_scenario_properties(qtbot):
    """
    test if gui scenario properties like adding and deleting are working correctly.

    Parameters
    ----------
    qtbot: qtbot
        bot for the GUI
    """
    # init gui window
    main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
    main_window.delete_backup()
    main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
    # check if at start no scenario exists
    assert len(main_window.list_ds) == 0
    assert main_window.list_widget_scenario.count() == 0
    # check if saving of a scenario if an empty list create one
    main_window.save_scenario()
    assert len(main_window.list_ds) == 1
    assert main_window.list_widget_scenario.count() == 1
    # check if adding a scenario is adding one
    for i in range(10):
        main_window.save_scenario()
        main_window.add_scenario()
        assert len(main_window.list_ds) == 2 + i
        assert main_window.list_widget_scenario.count() == 2 + i
    # check if deleting a scenario is removing a scenario
    for i in range(10):
        main_window.delete_scenario()
        assert len(main_window.list_ds) == 10 - i
        assert main_window.list_widget_scenario.count() == 10 - i
    # check if deleting the last scenario is ignored so at least one exists
    main_window.delete_scenario()
    assert len(main_window.list_ds) == 1
    assert main_window.list_widget_scenario.count() == 1
    main_window.delete_backup()
