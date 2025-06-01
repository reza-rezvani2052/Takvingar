import compileall
import os


def compile_project(path: str):
    """کامپایل کل پروژه به فایل‌های .pyc"""
    print(f"در حال کامپایل فایل‌های .py در مسیر: {path}")
    success = compileall.compile_dir(path, force=True, legacy=False, quiet=1)
    if success:
        print("✅ کامپایل با موفقیت انجام شد.")
    else:
        print("❌ در کامپایل مشکلی پیش آمد.")


def delete_py_files(path: str):
    """حذف فایل‌های .py از کل پروژه"""
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py") and file != os.path.basename(__file__):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"🗑 حذف شد: {file_path}")
                except Exception as e:
                    print(f"⚠️ خطا در حذف {file_path}: {e}")


if __name__ == "__main__":
    # مسیر پروژه
    project_path = os.path.abspath(".")

    # کامپایل پروژه
    compile_project(project_path)

    # حذف فایل‌های .py
    # delete_py_files(project_path)
