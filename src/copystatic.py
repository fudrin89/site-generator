import os
import shutil


def copy_static(source_dir: str, dest_dir: str):
    """
    Recursively copy everything from source_dir -> dest_dir.
    Deletes dest_dir first to ensure a clean copy.
    """
    # Clean destination
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    # Recreate destination root
    os.mkdir(dest_dir)

    # Walk source directory
    for entry in os.listdir(source_dir):
        src_path = os.path.join(source_dir, entry)
        dst_path = os.path.join(dest_dir, entry)

        if os.path.isfile(src_path):
            print(f"Copy file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            print(f"Copy dir:  {src_path} -> {dst_path}")
            os.mkdir(dst_path)
            copy_static(src_path, dst_path)