"""
script for a status bar logger class
"""
from __future__ import annotations

from logging import Handler
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QStatusBar

import ScenarioGUI.global_settings as globs
from ScenarioGUI.utils import set_default_font

if TYPE_CHECKING:
    from logging import LogRecord

    from PySide6.QtWidgets import QWidget


class StatusBar(Handler):
    """
    Class to create a status bar logger. To display messages in the GUI Status Bar
    """

    def __init__(self, parent: QWidget):
        """
        Init status bar.

        Parameters
        ----------
        parent: QtW.QWidget
            parent to create QStatusBar in
        """
        super().__init__()
        self.widget: QStatusBar = QStatusBar(parent)
        set_default_font(self.widget)
        self.level_2_color: dict[str, str] = {
            "DEBUG": f"{globs.WHITE}",
            "INFO": f"{globs.WHITE}",
            "ERROR": "rgb(255,0,0)",
            "CRITICAL": "rgb(255,0,0)",
            "WARNING": f"{globs.WARNING}",
        }

    def emit(self, record: LogRecord) -> None:
        """
        Display record in statusbar.

        Parameters
        ----------
        record: logging.LogRecord
            record to be displayed

        Returns
        -------
        None

        """
        message = self.format(record)
        self.widget.setStyleSheet(f"color: {self.level_2_color[record.levelname]};")
        self.widget.showMessage(message, 10_000)
