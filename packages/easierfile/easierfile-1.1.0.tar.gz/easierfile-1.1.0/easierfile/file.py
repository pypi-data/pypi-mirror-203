import os

class File:
    def __init__(self, file_path):
        self.__m_file_path = file_path
        self.__m_file_full_name = os.path.basename(self.__m_file_path)
        self.__m_file_name, self.__m_file_extension = os.path.splitext(self.__m_file_full_name)
        self.__m_dir_path = os.path.dirname(self.__m_file_path)

        if os.path.exists(self.__m_dir_path) == False:  # If the directory of the file path does not exist, it will be created.
            os.mkdir(self.__m_dir_path)
        try:  # If the file does not exist, it will be created.
            self.__m_file = open(self.__m_file_path, "x")
        except FileExistsError:
            pass  # Indicates that the file exists and no further exception handling is required.
        else:
            self.__m_file.close()

    @property
    def content(self):
        self.__m_file = open(self.__m_file_path, "r")
        self.__m_content = self.__m_file.read()
        self.__m_file.close()
        return self.__m_content

    @property
    def full_name(self):
        return self.__m_file_full_name

    @property
    def name(self):
        return self.__m_file_name

    @property
    def ext(self):
        return self.__m_file_extension.split(".")[-1]

    def rewrite(self,content):
        self.__m_file = open(self.__m_file_path, "w")
        self.__m_file.write(content)
        self.__m_file.close()

    def append(self,content):
        self.__m_file = open(self.__m_file_path, "a")
        self.__m_file.write(content)
        self.__m_file.close()

    def delete(self):
        if os.path.exists(self.__m_file_path):
            os.remove(self.__m_file_path)