import os
import re
import config


def replace_strings_in_file(file_path, translations):
    """替换文件中的字符串"""

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for original, translated in sorted(translations.items(), key=lambda x: -len(x[0])):
        pattern = re.escape(original)
        content = re.sub(pattern, translated, content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated: {file_path}")


def process_files_in_directory(folder_path, translations):
    """遍历目录及其子目录，并处理文件"""
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                replace_strings_in_file(file_path, translations)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")


if __name__ == "__main__":
    # 要替换的文件包
    folder_path = r'D:\zh\vehicles\zh_cn\vehicles'

    translations = config.translations

    process_files_in_directory(folder_path, translations)
