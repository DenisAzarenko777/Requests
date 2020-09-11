import requests
import urllib

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        response = requests.get("...", params={"path": "C:\Users\denaz\PycharmProjects\untitled\gif"})
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('C:\Users\denaz\PycharmProjects\untitled\gif')
    result = uploader.upload()