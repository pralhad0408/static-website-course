import os
import shutil

def copy_static_to_public(src: str, dst: str) -> None:
    if os.path.exists(dst):
        shutil.rmtree(dst)

    os.mkdir(dst)

    copy_directory(src, dst)

def copy_directory(src: str, dst: str) -> None:
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            print(f"Creating directory: {dst_path}")
            os.mkdir(dst_path)
            copy_directory(src_path, dst_path)

def main():
    copy_static_to_public("static", "public")

if __name__ == "__main__":
    main()