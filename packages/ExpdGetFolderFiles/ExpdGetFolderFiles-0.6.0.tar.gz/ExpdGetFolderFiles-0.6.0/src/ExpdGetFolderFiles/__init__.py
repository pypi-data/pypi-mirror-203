from os import path, walk
from loguru import logger


class GetFileList:
    def __init__(self, path, exts=None):
        self.file_path = path
        self.file_exts = exts.split(",") if exts is not None else []

    @property
    def files(self):
        file_list = []
        for root, dirs, files in walk(self.file_path):
            if len(self.file_exts) > 0:
                for ext in self.file_exts:
                    [file_list.append(path.join(root, name)) for name in files if str(name).lower().endswith(str(ext).lower())]
            else:
                [file_list.append(path.join(root, name)) for name in files]
        logger.debug(f"Local folder total files: [{len(file_list)}]")
        return file_list


if __name__ == "__main__":
    files = GetFileList(path=r"C:\temp", exts="Html").files
    print(files)
