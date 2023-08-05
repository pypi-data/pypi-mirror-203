import functools
import BAC0

# import time
import logging
import logging.handlers

from prettytable import PrettyTable


class BACDevice(object):
    def __init__(self, bacnet, ip, did):
        self._bacnet=bacnet
        self._did=did
        self._ip=ip
        self.logger.info('Creating device %s:%d' % (ip, did))
        self._device=BAC0.device(ip, did, bacnet.bac0)

    @property
    def bacnet(self):
        return self._bacnet

    @property
    def logger(self):
        return self.bacnet.logger

    @property
    def bac0(self):
        return self.bacnet.bac0

    @property
    def properties(self):
        return self._device.bacnet_properties

    @property
    def name(self):
        return self.properties['objectName']

    @property
    def description(self):
        return self.properties['description']

    @functools.cache
    def points(self, key=None, objectType=None):
        items=[]
        if key:
            key=key.lower()
        for point in self._device.points:
            if objectType and objectType!=point.properties.type:
                continue
            if key:
                if key not in point.properties.name.lower() and \
                        key not in point.properties.description.lower():
                    continue
            items.append(point)
        return items

    def ai(self, key=None):
        return self.points(key, objectType='analogInput')

    def ao(self, key=None):
        return self.points(key, objectType='analogOuput')

    def bi(self, key=None):
        return self.points(key, objectType='binaryInput')

    def bo(self, key=None):
        return self.points(key, objectType='binaryOutput')

    def bv(self, key=None):
        return self.points(key, objectType='binaryValue')

    def av(self, key=None):
        return self.points(key, objectType='analogValue')

    def __getitem__(self, key):
        try:
            return self.points(key)[0]
        except:
            pass

    def dump(self, points=None):
        if type(points) is not list:
            points=self.points(points)
        if points:
            t=PrettyTable()
            t.field_names=['name', 'type', 'value', 'unit', 'description']
            t.align['name']='l'
            t.align['type']='l'
            t.align['value']='l'
            t.align['unit']='l'
            t.align['description']='l'
            for point in points:
                t.add_row([point.properties.name, point.properties.type, point.value, point.units, point.properties.description])
            print(t)


class BAC(object):
    def __init__(self, network, ipRouter=None, logServer='localhost', logLevel=logging.DEBUG):
        logger=logging.getLogger("BACNET(%s)" % network)
        logger.setLevel(logLevel)
        socketHandler = logging.handlers.SocketHandler(logServer, logging.handlers.DEFAULT_TCP_LOGGING_PORT)
        logger.addHandler(socketHandler)
        self._logger=logger

        self._network=network
        self._bac0=None

        if ipRouter:
            self.logger.info('Starting BAC0 with network %s@%s' % (self._network, ipRouter))
            self._bac0=BAC0.lite(ip=network, bbmdAddress=ipRouter, bbmdTTL=900)
        else:
            self.logger.info('Starting BAC0 with network %s' % self._network)
            self._bac0=BAC0.lite(ip=self._network)

        if self._bac0:
            self.logger.info('Using BAC0 v%s' % BAC0.version)
            self.logger.info('BAC0:%s' % self._bac0)

        self._devices={}

        # self.open()

    @property
    def logger(self):
        return self._logger

    @property
    def bac0(self):
        return self._bac0

    def open(self):
        if self._bac0:
            self.whois()

    def close(self):
        if self._bac0:
            self._bac0.disconnect()

    def device(self, did):
        try:
            return self._devices[did]
        except:
            pass

    def devices(self):
        return self._devices.values()

    def whois(self, autoDeclare=False):
        if self._bac0:
            items=self._bac0.whois()
            if items and autoDeclare:
                for item in items:
                    self.declare(item[0], item[1])
            return items

    def discover(self):
        return self.whois(True)

    def declare(self, ip, did):
        if not self.device(did):
            device=BACDevice(self, ip, did)
            self._devices[did]=device
            return device

    def __getitem__(self, key):
        return self.device(key)

    def dump(self):
        pass

    def table(self):
        pass


if __name__=='__main__':
    pass
