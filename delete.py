import os


def delete_non_jbeam_files(folder_path):
    """删除所有非 .jbeam 文件"""
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if not filename.endswith('.jbeam'):
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")


if __name__ == "__main__":
    # 解压出来备份的地方
    folder_path = r'D:\zh\vehicles\vehicles'

    delete_non_jbeam_files(folder_path)
