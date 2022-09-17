class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        for item in self.apps:
            if hasattr(item, 'name'):
                if item.name == app.name:
                    return
            elif hasattr(item, 'memory_max'):
                if item.memory_max == app.memory_max:
                    return
        self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = 'ВКонтакте'


class AppYouTube:
    def __init__(self, memory_max=1024):
        self.memory_max = memory_max
        self.name = 'YouTube'


class AppPhone:
    def __init__(self, phone_list: dict):
        self.name = 'Phone'
        self.phone_list = phone_list
