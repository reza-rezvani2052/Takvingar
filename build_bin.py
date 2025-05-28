import shutil
import subprocess
from pathlib import Path

# تنظیم مسیر فایل‌ها
BASE_DIR = Path(__file__).resolve().parent
MAIN_SCRIPT = BASE_DIR / "main.py"
ICON_PATH = BASE_DIR / "RC" / "app-icon.ico"
# ...
SPLASH_PATH = BASE_DIR / "RC" / "splash.png"
FONTS_DIR = BASE_DIR / "RC" / "fonts"

# نام اجرایی (پوشه خروجی هم همین خواهد بود در حالت --onedir)
APP_NAME = "Takvingar"

# حذف build و dist اگر وجود دارند
for folder in ["build", "dist"]:
    folder_path = BASE_DIR / folder
    if folder_path.exists():
        shutil.rmtree(folder_path)

# ماژول‌هایی که می‌خواهیم حذف کنیم
excluded_modules = ["PyQt5", "PyQt6", "PyQt5.sip", "PyQt6.sip", ]

# لیست ماژول‌های hidden-import
hidden_imports = [
    "bcrypt", "shiboken6", "PySide6",
    "jalali_core", "jdatetime",
]

# ساخت دستور pyinstaller
cmd = [
    "pyinstaller",
    "--noconfirm",
    "--windowed",  # TODO: در انتشار نهایی این گزینه فعال باشد
    "--onedir",
    # "--onefile",
    f"--icon={ICON_PATH}",
    f"--name={APP_NAME}",
]

# اضافه کردن hidden-import ها به دستور
for hidden_import in hidden_imports:
    cmd.append(f"--hidden-import={hidden_import}")

# اضافه کردن exclude-module به دستور
for module in excluded_modules:
    cmd.append(f"--exclude-module={module}")

cmd.append(f"--paths={str(Path(BASE_DIR).joinpath('.venv', 'Lib', 'site-packages'))}")

cmd.append(str(MAIN_SCRIPT))

# اجرای دستور
result = subprocess.run(cmd, text=True)
# with open("build-log.txt", "w", encoding="utf-8") as log_file:
#     result = subprocess.run(cmd, text=True, stdout=log_file, stderr=subprocess.STDOUT)

print("_" * 110)

# بررسی موفقیت و کپی فایل‌ها در صورت موفق بودن
if result.returncode == 0:
    print("✅ The executable file was successfully built.")
    # ...
    output_dir = BASE_DIR / "dist" / APP_NAME

    # کپی splash.png
    if SPLASH_PATH.exists():
        shutil.copy(SPLASH_PATH, output_dir / "_internal" / SPLASH_PATH.name)
        print(f"📄 Copied splash.png to {output_dir}")

    # کپی پوشه fonts
    if FONTS_DIR.exists():
        dest_fonts = output_dir / "_internal" / "fonts"
        shutil.copytree(FONTS_DIR, dest_fonts, dirs_exist_ok=True)
        print(f"📁 Copied fonts directory to {dest_fonts}")

else:
    print("❌ Error occurred while building the executable file.")
