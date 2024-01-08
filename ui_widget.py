# -*- coding: utf-8 -*-

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(700, 591)
        self.horizontalLayout_2 = QHBoxLayout(Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rec_widget_ = QTabWidget(Widget)
        self.rec_widget_.setObjectName(u"rec_widget_")
        self.rec_id_tab_ = QWidget()
        self.rec_id_tab_.setObjectName(u"rec_id_tab_")
        self.verticalLayout_4 = QVBoxLayout(self.rec_id_tab_)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.id_h_layout_ = QHBoxLayout()
        self.id_h_layout_.setObjectName(u"id_h_layout_")
        self.id_label_ = QLabel(self.rec_id_tab_)
        self.id_label_.setObjectName(u"id_label_")
        self.id_label_.setWordWrap(True)

        self.id_h_layout_.addWidget(self.id_label_)

        self.id_spin_box_ = QSpinBox(self.rec_id_tab_)
        self.id_spin_box_.setObjectName(u"id_spin_box_")

        self.id_h_layout_.addWidget(self.id_spin_box_)

        self.id_h_spacer_ = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.id_h_layout_.addItem(self.id_h_spacer_)


        self.verticalLayout_4.addLayout(self.id_h_layout_)

        self.id_artist_h_layout_ = QHBoxLayout()
        self.id_artist_h_layout_.setObjectName(u"id_artist_h_layout_")
        self.preffered_v_layout_ = QVBoxLayout()
        self.preffered_v_layout_.setObjectName(u"preffered_v_layout_")
        self.preffered_label_ = QLabel(self.rec_id_tab_)
        self.preffered_label_.setObjectName(u"preffered_label_")
        self.preffered_label_.setAlignment(Qt.AlignCenter)
        self.preffered_label_.setWordWrap(True)

        self.preffered_v_layout_.addWidget(self.preffered_label_)

        self.preffered_list_widget_ = QListWidget(self.rec_id_tab_)
        self.preffered_list_widget_.setObjectName(u"preffered_list_widget_")

        self.preffered_v_layout_.addWidget(self.preffered_list_widget_)


        self.id_artist_h_layout_.addLayout(self.preffered_v_layout_)

        self.rec_button_v_layout_ = QVBoxLayout()
        self.rec_button_v_layout_.setObjectName(u"rec_button_v_layout_")
        self.rec_button_v_spacer_ = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.rec_button_v_layout_.addItem(self.rec_button_v_spacer_)

        self.rec_push_button_ = QPushButton(self.rec_id_tab_)
        self.rec_push_button_.setObjectName(u"rec_push_button_")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rec_push_button_.sizePolicy().hasHeightForWidth())
        self.rec_push_button_.setSizePolicy(sizePolicy)

        self.rec_button_v_layout_.addWidget(self.rec_push_button_)

        self.rec_button_v_spacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.rec_button_v_layout_.addItem(self.rec_button_v_spacer_2)


        self.id_artist_h_layout_.addLayout(self.rec_button_v_layout_)

        self.rec_artist_v_layout_ = QVBoxLayout()
        self.rec_artist_v_layout_.setObjectName(u"rec_artist_v_layout_")
        self.rec_artist_label_ = QLabel(self.rec_id_tab_)
        self.rec_artist_label_.setObjectName(u"rec_artist_label_")
        self.rec_artist_label_.setScaledContents(True)
        self.rec_artist_label_.setAlignment(Qt.AlignCenter)
        self.rec_artist_label_.setWordWrap(True)

        self.rec_artist_v_layout_.addWidget(self.rec_artist_label_)

        self.rec_artist_list_widget_ = QListWidget(self.rec_id_tab_)
        self.rec_artist_list_widget_.setObjectName(u"rec_artist_list_widget_")

        self.rec_artist_v_layout_.addWidget(self.rec_artist_list_widget_)


        self.id_artist_h_layout_.addLayout(self.rec_artist_v_layout_)


        self.verticalLayout_4.addLayout(self.id_artist_h_layout_)

        self.rec_widget_.addTab(self.rec_id_tab_, "")
        self.rec_artist_tab_ = QWidget()
        self.rec_artist_tab_.setObjectName(u"rec_artist_tab_")
        self.verticalLayout_5 = QVBoxLayout(self.rec_artist_tab_)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.artist_h_layout_ = QHBoxLayout()
        self.artist_h_layout_.setObjectName(u"artist_h_layout_")
        self.artist_label_ = QLabel(self.rec_artist_tab_)
        self.artist_label_.setObjectName(u"artist_label_")

        self.artist_h_layout_.addWidget(self.artist_label_)

        self.artist_line_edit_ = QLineEdit(self.rec_artist_tab_)
        self.artist_line_edit_.setObjectName(u"artist_line_edit_")

        self.artist_h_layout_.addWidget(self.artist_line_edit_)

        self.artist_h_spacer_ = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.artist_h_layout_.addItem(self.artist_h_spacer_)

        self.search_push_button = QPushButton(self.rec_artist_tab_)
        self.search_push_button.setObjectName(u"search_push_button")

        self.artist_h_layout_.addWidget(self.search_push_button)


        self.verticalLayout_5.addLayout(self.artist_h_layout_)

        self.artist_list_widget_ = QListWidget(self.rec_artist_tab_)
        self.artist_list_widget_.setObjectName(u"artist_list_widget_")

        self.verticalLayout_5.addWidget(self.artist_list_widget_)

        self.rec_widget_.addTab(self.rec_artist_tab_, "")

        self.horizontalLayout_2.addWidget(self.rec_widget_)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430 \u043c\u0443\u0437\u044b\u043a\u0430\u043b\u044c\u043d\u044b\u0445 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.id_label_.setText(QCoreApplication.translate("Widget", u"ID \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.preffered_label_.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u0435\u0434\u043f\u043e\u0447\u0438\u0442\u0430\u0435\u043c\u044b\u0435 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0438", None))
        self.rec_push_button_.setText(QCoreApplication.translate("Widget", u"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u0442\u044c", None))
        self.rec_artist_label_.setText(QCoreApplication.translate("Widget", u"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u044b\u0435 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0438", None))
        self.rec_widget_.setTabText(self.rec_widget_.indexOf(self.rec_id_tab_), QCoreApplication.translate("Widget", u"\u041f\u043e \u043f\u0440\u0435\u0434\u043f\u043e\u0447\u0442\u0435\u043d\u0438\u044f\u043c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.artist_label_.setText(QCoreApplication.translate("Widget", u"\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c:", None))
        self.search_push_button.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0439\u0442\u0438 \u043f\u043e\u0445\u043e\u0436\u0438\u0445 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.rec_widget_.setTabText(self.rec_widget_.indexOf(self.rec_artist_tab_), QCoreApplication.translate("Widget", u"\u041f\u043e \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044e", None))
    # retranslateUi
        