class Server:
    __amount = 0

    def __new__(cls, *args, **kwargs):
        cls.__amount += 1
        return super().__new__(cls)

    def __init__(self):
        self.ip = Server.__amount
        self.buffer = []    # сюда кидать объекты класса Data - ПРИНЯТЫЕ

    def send_data(self, data):      # data - объект класса Data
        Router.buffer.append(data)

    def get_data(self):
        b = self.buffer.copy()
        self.buffer.clear()
        return b

    def get_ip(self):
        return self.ip


class Router:
    servers = {}
    buffer = []

    def link(self, server):
        self.servers[server.get_ip()] = server  # server - Объект класса Server

    def unlink(self, server):
        self.servers.pop(server.ip)

    def send_data(self):
        for b in self.buffer:
            if self.servers.get(b.ip) is not None:
                self.servers.get(b.ip).buffer.append(b)
        self.buffer.clear()


class Data:
    def __init__(self, data: str, ip):      # ip достается из метода get_ip класса Server
        self.data = data
        self.ip = ip
