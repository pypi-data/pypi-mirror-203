import os


class FileCache:
    def __init__(self):
        self.cache = dict()

    class fileinfo:
        def __init__(self, path):
            self.exist = os.path.exists(path)
            if self.exist:
                self.mtime = os.stat(path).st_mtime
            else:
                self.mtime = 0

    def update_info(self, path):
        self.cache[path] = self.fileinfo(path)

    def get_info(self, path):
        # if path not in self.cache:
        #    self.update_info(path)
        # return self.cache[path]

        try:
            return self.cache[path]
        except KeyError:
            self.update_info(path)
            return self.cache[path]


fcache = FileCache()
