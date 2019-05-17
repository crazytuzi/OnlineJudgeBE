from .DockerConfig import DockersCfg


import threading


class DRSalgorithm(object):
    minTimeIndex = 0
    dockers = []
    dockerCount = 0
    _instance_lock = threading.Lock()

    def __init__(self):
        self.dockerCount = len(DockersCfg)
        self.dockers = []
        for i in range(self.dockerCount):
            self.dockers.append({'time': 0})
        for i in range(self.dockerCount):
            self.dockers[i]['url'] = "http://" + DockersCfg[i]['ip'] + \
                ':' + DockersCfg[i]['port'] + "/app/"
        print(self.dockers)

    def __new__(cls, *args, **kwargs):
        if not hasattr(DRSalgorithm, "_instance"):
            with DRSalgorithm._instance_lock:
                if not hasattr(DRSalgorithm, "_instance"):
                    DRSalgorithm._instance = object.__new__(cls)
        return DRSalgorithm._instance

    def getUrl(self):
        return self.dockers[self.minTimeIndex]['url']

    def update(self, url, time):
        minTime = 99
        for i in range(self.dockerCount):
            if self.dockers[i]['url'] == url:
                self.dockers[i]['time'] = time
            if self.dockers[i]['time'] < minTime:
                self.minTimeIndex = i
                minTime = self.dockers[i]['time']
        print(self.dockers)
