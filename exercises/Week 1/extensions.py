#identifies the file extension

def main():

    file_name = input("File name: ").strip().lower()

    media_types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }

    if "." in file_name:
        ext = file_name.rsplit(".", 1)[-1]
        print(media_types.get(ext, "application/octet-stream"))
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
