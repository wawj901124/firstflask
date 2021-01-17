import os

class GetFileData:
    def __init__(self,file_path):
        self.file_path = file_path
        self.file_list = self.get_file()

    def get_file(self):
        file_list = os.listdir(self.file_path)
        print(file_list)
        return file_list

    def get_image_file(self):
        image_list = []
        for one in self.file_list:
            one_list = one.split('.')
            print(one_list)
            one_list_len = len(one_list)
            if one_list[one_list_len-1] == 'jpg':
                image_list.append(one)

        print(image_list)
        return image_list



if __name__ == "__main__":
    file_path = r"D:\PycharmProjects\firstflask\myimageapps\static\imagefile"
    gfd = GetFileData(file_path=file_path)
    gfd.get_image_file()


