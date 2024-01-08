from typing import Optional

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot

from ui_widget import Ui_Widget
from rec_sys import RecommendationSystem

class Widget(QWidget):
    def __init__(self,
                 parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.m_ui = Ui_Widget()
        self.m_ui.setupUi(self)

        self.m_ui.id_spin_box_.setRange(1, 17493)
        self.m_ui.id_spin_box_.valueChanged.connect(self.ChangePrefferedArtists)

        self.m_ui.rec_push_button_.clicked.connect(self.RecommendArtistsForUser)
        self.m_ui.search_push_button.clicked.connect(self.RecommendSimilarArtists)

        self.m_rec_sys_ = RecommendationSystem()

        artists = self.m_rec_sys_.GetPrefferedArtistTitles(self.m_ui.id_spin_box_.value())
        self.m_ui.preffered_list_widget_.addItems(artists)

    @Slot(int)
    def ChangePrefferedArtists(self, user_id: int) -> None:
        self.m_ui.rec_artist_list_widget_.clear()

        artists = self.m_rec_sys_.GetPrefferedArtistTitles(user_id)
        self.m_ui.preffered_list_widget_.clear()
        self.m_ui.preffered_list_widget_.addItems(artists)

    @Slot()
    def RecommendArtistsForUser(self) -> None:
        self.m_ui.rec_artist_list_widget_.clear()
        artists = self.m_rec_sys_.GetRecommendedArtistTitles(self.m_ui.id_spin_box_.value())
        self.m_ui.rec_artist_list_widget_.addItems(artists)

    @Slot()
    def RecommendSimilarArtists(self) -> None:
        self.m_ui.artist_list_widget_.clear()
        artists = self.m_rec_sys_.GetSimilarArtists(self.m_ui.artist_line_edit_.text())
        self.m_ui.artist_list_widget_.addItems(artists)

