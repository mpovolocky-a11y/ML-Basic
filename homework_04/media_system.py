from abc import ABC, abstractmethod
from datetime import datetime

# --- Базовый уровень: Хранилище (Задание 3) ---

class Storage(ABC):
    """Абстрактный класс для логики хранения"""
    @abstractmethod
    def save(self, file_obj): pass

    @abstractmethod
    def delete(self, file_obj): pass

class LocalStorage(Storage):
    def save(self, file_obj): print(f"Сохранение {file_obj.name} на жесткий диск...")
    def delete(self, file_obj): print(f"Удаление {file_obj.name} с диска...")

class S3Storage(Storage):
    def save(self, file_obj): print(f"Загрузка {file_obj.name} в облако S3 (AWS)...")
    def delete(self, file_obj): print(f"Удаление {file_obj.name} из S3...")

# --- Средний уровень: Базовый медиа-файл (Задание 1) ---

class MediaFile(ABC):
    def __init__(self, name, size, owner, storage: Storage):
        self.name = name
        self.size = size  # в байтах
        self.owner = owner
        self.created_at = datetime.now()
        self.storage = storage  # Инъекция зависимости (способ хранения)

    def save(self):
        self.storage.save(self)

    def delete(self):
        self.storage.delete(self)

    @abstractmethod
    def get_info(self):
        """Метод для получения специфичных метаданных"""
        pass

# --- Уровень реализации: Конкретные типы (Задание 1) ---

class AudioFile(MediaFile):
    def __init__(self, bitrate, duration, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bitrate = bitrate
        self.duration = duration

    def get_info(self):
        return f"Аудио: {self.name}, Длительность: {self.duration} сек, Битрейт: {self.bitrate}kbps"

class VideoFile(MediaFile):
    def __init__(self, resolution, fps, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = resolution
        self.fps = fps

    def get_info(self):
        return f"Видео: {self.name}, Разрешение: {self.resolution}, FPS: {self.fps}"

    def extract_features(self):
        """Пример действия (Задание 2)"""
        print(f"Извлечение признаков (лиц/объектов) из видео {self.name}...")

class PhotoFile(MediaFile):
    def __init__(self, camera_model, has_gps, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.camera_model = camera_model
        self.has_gps = has_gps

    def get_info(self):
        return f"Фото: {self.name}, Камера: {self.camera_model}"

    def convert_to_png(self):
        """Пример действия (Задание 2)"""
        print(f"Конвертация {self.name} в формат PNG...")

# --- Пример использования (Задание 2) ---

if __name__ == "__main__":
    # Выбираем способ хранения (можем легко поменять на S3Storage())
    my_disk = LocalStorage()
    cloud = S3Storage()

    # Создаем файлы
    track = AudioFile(name="song.mp3", size=5000, owner="Mihail", 
                      storage=my_disk, bitrate=320, duration=180)
    
    movie = VideoFile(name="avatar.mp4", size=1500000, owner="Admin", 
                      storage=cloud, resolution="4K", fps=60)

    # Действия
    print(track.get_info())
    track.save()

    print(movie.get_info())
    movie.extract_features()
    movie.save()

#     Ответы на вопросы (Задание 4)
# 1. Много ли кода придется переписать при добавлении новых типов файлов?
# Почти ничего.
# Нам нужно будет просто создать новый класс (например, DocumentFile),
# унаследовать его от MediaFile и прописать его уникальные свойства.
# Остальной код (логика сохранения, удаления, работа в списках) останется прежним.
# Это соблюдение принципа Open-Closed (программа открыта для расширения, но закрыта для изменения).

# 2. Много ли кода менять при добавлении новых способов хранения?
# Минимум. 
# Мы просто создаем новый класс, наследуемый от Storage (например, DropboxStorage).
# Благодаря тому, что мы передаем объект хранилища в конструктор медиа-файла (self.storage = storage),
# нам не нужно лезть внутрь классов AudioFile или VideoFile, чтобы научить их работать с новым облаком.