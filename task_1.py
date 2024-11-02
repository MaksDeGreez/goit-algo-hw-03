import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir")
    parser.add_argument("destination_dir", default="dist", nargs="?")
    return parser.parse_args()

def recursive_copy_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for item in os.listdir(source_dir):
        source_item_path = os.path.join(source_dir, item)

        if os.path.isdir(source_item_path):
            recursive_copy_files(source_item_path, destination_dir)
        elif os.path.isfile(source_item_path):
            file_extension = os.path.splitext(item)[1][1:].lower()
            extension_dir = os.path.join(destination_dir, file_extension)

            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)

            shutil.copy2(source_item_path, extension_dir)
            print(f"Copying {item} to {extension_dir}")

def main():
    args = parse_arguments()
    recursive_copy_files(args.source_dir, args.destination_dir)

if __name__ == "__main__":
    main()
