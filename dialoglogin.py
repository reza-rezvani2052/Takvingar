import re
import logging
from datetime import datetime
import jdatetime  # تاریخ شمسی

from UI.ui_dialoglogin import Ui_DialogLogin
from dialogpopup import DialogPopup
from dialogdraggable import DialogDraggable

# import DB.users
from DB.users import (add_user_to_db, get_pass_hint, get_all_username,
                      check_password, set_user_last_login)
from DB.settings import update_settings
from definitions import Direction, user_info

from PySide6.QtCore import Qt, QPoint, QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import QStackedWidget, QWidget, QCompleter
from PySide6.QtGui import QKeyEvent, QCloseEvent


class DialogLogin(DialogDraggable):
    def __init__(self, show_login_page=True, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogLogin()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)

        # popup dialog
        self.popup = None

        self.list_usernames = get_all_username()
        completer = QCompleter(self.list_usernames)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)  # مطابقت جزئی، نه فقط ابتدای رشته
        self.ui.ledUsername.setCompleter(completer)

        self._is_user_registered_successfully = False

        # جلوگیری از حملات بروت فورث و هک شدن پسورد
        self.failed_attempts = 0  # شمارنده تلاش‌های ناموفق ورود به برنامه - پسورد اشتباه

        # ...
        if show_login_page:
            self.ui.stackedWidgetMain.setCurrentWidget(self.ui.pageLogin)
        else:
            self.ui.stackedWidgetMain.setCurrentWidget(self.ui.pageRegistration)
        # ...

        self.connect_signals_to_slots()

    # ------------------------------------------------------------------------

    def connect_signals_to_slots(self):
        self.ui.btnClose.clicked.connect(self.btnClose_clicked)
        self.ui.btnLogIn.clicked.connect(self.btnLogIn_clicked)
        self.ui.btnPasswordHint.clicked.connect(self.btnPasswordHint_clicked)

        self.ui.btnRegister.clicked.connect(self.btnRegister_clicked)
        self.ui.btnGoToLoginPage.clicked.connect(self.btnGoToLoginPage_clicked)
        self.ui.btnCancelRegistrationPage.clicked.connect(self.btnClose_clicked)

    def btnClose_clicked(self):
        self.close()

    def btnLogIn_clicked(self):
        if self.failed_attempts >= 3:
            self.popup = DialogPopup(
                    "تعداد تلاش های ورود به برنامه بیش از حد مجاز است" + "\n" +
                    "جهت یادآوری کلمه عبور از دکمه 'یادآوری کلمه عبور' استفاده کنید "
                    , duration=6000, parent=self
                    )
            self.popup.show()
            self.ui.ledUsername.setEnabled(False)
            self.ui.ledPassword.setEnabled(False)
            self.ui.btnLogIn.setEnabled(False)
            return

        username = self.ui.ledUsername.text().strip()
        password = self.ui.ledPassword.text()
        ret = check_password(username, password)
        if not ret:
            self.failed_attempts += 1
            remaining = 3 - self.failed_attempts

            self.popup = DialogPopup(
                    "نام کاربری یا کلمه عبور نادرست است" + "\n" +
                    "تعداد تلاش باقی مانده:" + "\n"
                                               f" {remaining} "
                    , duration=2500, parent=self
                    )
            self.popup.show()

        else:
            user_info.username = username

            # set user last login
            now_jalali = jdatetime.datetime.fromgregorian(datetime=datetime.now())
            last_login = f"{now_jalali.strftime('%Y-%m-%d_%H-%M-%S')}"
            set_user_last_login(user_info.username, last_login)

            self.animateAndAccept()

    def btnPasswordHint_clicked(self):
        username = self.ui.ledUsername.text().strip()
        if not username:
            DialogPopup(
                    "لطفاً نام کاربری را وارد کنید"
                    , duration=2500, parent=self
                    ).show()
            self.ui.ledUsername.setFocus()
            return

        ret = get_pass_hint(username).strip()
        if not ret:
            ret = "چیزی یافت نشد"

        self.popup = DialogPopup(ret, duration=2500, parent=self)
        self.popup.show()

    # ------------------------------------------------------------------------

    def btnGoToLoginPage_clicked(self):
        if self.ui.stackedWidgetMain.currentWidget() != self.ui.pageLogin:
            self.animateStackedWidgetPages(
                    self.ui.stackedWidgetMain, self.ui.pageLogin
                    )

    def btnRegister_clicked(self):
        if not self.validate_registration():  # پیام های خطای احتمالی در همان تابع نمایش داده میشود
            return
        # ...
        username = self.ui.ledUsernameRegistrationPage.text().strip()
        password = self.ui.ledPasswordRegistrationPage.text()
        pass_hint = self.ui.ledPasswordHint.text().strip()

        success, message = \
            self.register_user(username, password, pass_hint, access_level=1)
        if success:
            self._is_user_registered_successfully = True
            self.write_settings()

            self.btnGoToLoginPage_clicked()  # animate and go to Login Page!
            self.ui.ledUsername.setText(username)
            self.ui.ledPassword.setFocus()
        else:
            DialogPopup(
                    "ثبت کاربر با خطا مواجه شده است." + "\n" + message
                    , duration=3500, parent=self
                    ).show()

    def validate_registration(self):
        username = self.ui.ledUsernameRegistrationPage.text().strip()
        password = self.ui.ledPasswordRegistrationPage.text()
        password_again = self.ui.ledPasswordAgainRegistrationPage.text()
        reminder = self.ui.ledPasswordHint.text().strip()

        # بررسی تکمیل بودن فیلدها
        if not username:
            DialogPopup("لطفاً نام کاربری را وارد کنید", duration=2500, parent=self).show()
            self.ui.ledUsernameRegistrationPage.setFocus()
            return False

        if not password:
            DialogPopup("لطفاً کلمه عبور را وارد کنید", duration=2500, parent=self).show()
            self.ui.ledPasswordRegistrationPage.setFocus()
            return False

        if not password_again:
            DialogPopup("لطفاً تکرار کلمه عبور را وارد کنید", duration=2500, parent=self).show()
            self.ui.ledPasswordAgainRegistrationPage.setFocus()
            return False

        if not reminder:
            DialogPopup("لطفاً یادآوری کلمه عبور را وارد کنید", duration=2500, parent=self).show()
            self.ui.ledPasswordHint.setFocus()
            return False

        # بررسی معتبر بودن نام کاربری (حداقل 4 حرف شامل حروف انگلیسی، عدد، زیرخط)
        if not re.fullmatch(r"[A-Za-z0-9_]{4,}", username):
            DialogPopup(
                    "نام کاربری باید حداقل ۴ حرف و شامل حروف، عدد یا زیرخط (_) باشد", duration=3500,
                    parent=self
                    ).show()
            self.ui.ledUsernameRegistrationPage.setFocus()
            return False

        # بررسی تطابق کلمه عبور و تکرار آن
        if password != password_again:
            DialogPopup("کلمه عبور و تکرار آن یکسان نیستند", duration=2500, parent=self).show()
            self.ui.ledPasswordAgainRegistrationPage.setFocus()
            return False

        # بررسی اینکه هیچ بخش معنادار (۴ کاراکتر یا بیشتر) از رمز داخل یادآوری نباشد
        for i in range(len(password) - 3):
            substring = password[i:i + 4].lower()
            if substring in reminder.lower():
                DialogPopup(
                        "عبارت یادآوری نباید شامل بخش‌هایی از کلمه عبور باشد",
                        duration=2500, parent=self
                        ).show()
                self.ui.ledPasswordHint.setFocus()
                return False

        # اگر همه چیز درست بود
        return True

    @staticmethod
    def register_user(username, password, pass_hint, access_level) -> tuple[bool, str]:
        return add_user_to_db(username, password, pass_hint, access_level)

    # ------------------------------------------------------------------------

    def keyPressEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Escape:
            self.btnClose_clicked()
        else:
            super().keyPressEvent(e)

    # ------------------------------------------------------------------------

    def closeEvent(self, event: QCloseEvent):
        # _ = event  # به جای Q_UNUSED(event)
        # ...
        self.write_settings()
        super().closeEvent(event)

    def write_settings(self):
        new_settings = {
            "HasLoginFormShownBefore": True,
            "IsUserRegisteredSuccessfully":
                len(self.list_usernames) > 0  # یعنی قبلا یک یوزر ثیت شده
                or
                self._is_user_registered_successfully
            }

        # تغییر و ذخیره تنظیمات
        if not update_settings(new_settings):
            logging.debug("Failed to update settings(dialoglogin.py -> write_settings()")
        else:
            logging.info("Successfully updated settings(dialoglogin.py -> write_settings())")

    # ------------------------------------------------------------------------

    def animateAndAccept(self):
        self.anim = QPropertyAnimation(self, b"windowOpacity")  # ذخیره به عنوان attribute
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        self.anim.setDuration(800)

        # اتصال مستقیم بدون Qt.QueuedConnection
        self.anim.finished.connect(self._on_animation_finished)

        self.anim.start()

    def _on_animation_finished(self):
        self.accept()
        self.anim.deleteLater()  # حذف انیمیشن با استفاده از reference مستقیم
        self.anim = None  # جلوگیری از circular reference

    def animateStackedWidgetPages(
            self, stacked_widget: QStackedWidget, page: QWidget,
            direction: Direction = Direction.LeftToRight
            ) -> None:
        # 1. ابتدا صفحه را مخفی کرده و موقعیت اولیه را تنظیم کنید
        page.show()  # اطمینان از visibility
        page.raise_()  # اطمینان از قرارگیری در بالای stacked widget

        # 2. موقعیت پایانی را از geometry واقعی ویجت بگیرید
        pos_end = page.pos()

        # 3. تنظیم موقعیت اولیه بر اساس جهت
        pos_start = QPoint(pos_end)

        if direction == Direction.TopToBottom:
            pos_start.setY(pos_end.y() - 35)  # حرکت از بالا
        elif direction == Direction.BottomToTop:
            pos_start.setY(pos_end.y() + 35)  # حرکت از پایین
        elif direction == Direction.RightToLeft:
            pos_start.setX(pos_end.x() + 50)  # حرکت از راست
        elif direction == Direction.LeftToRight:
            pos_start.setX(pos_end.x() - 15)  # حرکت از چپ

        # 4. اعمال موقعیت اولیه قبل از شروع انیمیشن
        page.move(pos_start)
        stacked_widget.setCurrentWidget(page)

        # 5. ایجاد و تنظیم انیمیشن
        animation = QPropertyAnimation(page, b"pos")
        animation.setDuration(700)  # مدت زمان بهینه‌تر
        animation.setStartValue(pos_start)
        animation.setEndValue(pos_end)
        animation.setEasingCurve(QEasingCurve.OutQuint)  # منحنی نرم‌تر

        # 6. مدیریت حذف خودکار انیمیشن
        animation.finished.connect(
                lambda: (
                    animation.deleteLater(),
                    # logging.debug("Animation completed and deleted")  # برای دیباگ
                    )
                )

        animation.start()

    # ------------------------------------------------------------------------
