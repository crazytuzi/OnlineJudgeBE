from .DockerConfig import DockersCfg


class DRS:
    minCpuIndex = 0
    dockers = []
    dockerCount = 0

    def __init__(self):
        self.count = len(DockersCfg)
        self.dockers = [{'cpu': 100, 'count': 0}] * self.count
        for i in range(self.dockerCount):
            self.dockers[i][0]['url'] = DockersCfg[i][0]['ip'] + \
                ':' + DockersCfg[i][0]['port']

    def getUrl(self):
        self.dockers[self.minCpuIndex][0]['count'] = self.dockers[self.minCpuIndex][0]['count'] + 1
        self.dockers[self.minCpuIndex][0]['cpu'] = 100
        return self.dockers[self.minCpuIndex][0]['url']

    def getMinCount(self):
        minCount = 100
        for i in range(self.dockerCount):
            if self.dockers[i][0]['count'] < minCount:
                self.minCpuIndex = i
                minCount = self.dockers[i][0]['count']

    def update(self, url, cpu):
        minCpu = 100
        for i in range(self.dockerCount):
            if self.dockers[i][0]['url'] == url:
                self.dockers[i][0]['cpu'] = cpu
                self.dockers[i][0]['count'] = self.dockers[i][0]['count'] - 1
            if self.dockers[i][0]['cpu'] < minCpu:
                self.minCpuIndex = i
                minCpu = self.dockers[i][0]['cpu']
        if minCpu == 100:
            self.getMinCount()
