import hashlib
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        #с обычным hash не работает, не знаю почему
        #воспользовался https://sky.pro/media/kak-rabotat-s-modulem-hashlib-v-python/
        self.age = int(age)

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hash_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == hash_password:
                self.current_user = user
                #print(f"Пользователь {nickname} успешно вошел.")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)
        #print(f"Пользователь {nickname} зарегистрирован и выполнен вход.")

    def log_out(self):
        if self.current_user is not None:
            self.current_user = None
            print(f"Пользователь {self.current_user} вышел из аккаунта.")
        else:
            print(f"Пользователь {self.current_user} не вошёл в систему.")

    def add(self, *videos):
        for video in videos:
            for existing_video in self.videos:
                if video.title == existing_video.title:
                    continue
            self.videos.append(video)

    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    break

                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now, " ", end="")
                    sleep(1)
                print("Конец видео")
                video.time_now = 0
                break
        else:
            print(f"Видео '{video.title}' не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 5, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
