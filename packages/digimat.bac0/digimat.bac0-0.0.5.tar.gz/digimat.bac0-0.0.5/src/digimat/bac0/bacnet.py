import functools
import BAC0

# import time
import logging
import logging.handlers

from prettytable import PrettyTable


class BACBag(object):
    def __init__(self, device, key=None):
        self._device=device
        self._points=[]
        self._pointsByName={}
        self._pointsIndexByName={}
        if key:
            self.add(key)

    def __repr__(self):
        return '<%s[%s](%d points)>' % (self.__class__.__name__, self.device.name,
            len(self._points))

    @property
    def logger(self):
        return self._device.logger

    @property
    def device(self):
        return self._device

    def points(self, key=None, objectType=None, outOfService=False):
        items=[]
        if key:
            key=key.lower()
        if key=='*':
            key=None
        for point in self._points:
            if not outOfService and point.bacnet_properties['outOfService']:
                continue
            if objectType and objectType!=point.properties.type:
                continue
            if key:
                if key not in point.properties.name.lower() and \
                        key not in point.properties.description.lower():
                    continue
            items.append(point)
        return items

    def point(self, name):
        try:
            return self._pointsByName[name]
        except:
            pass
        try:
            return self._points[int(name)]
        except:
            pass

    def __getitem__(self, key):
        return self.point(key)

    def count(self):
        return len(self._points)

    def __len__(self):
        return self.count()

    def add(self, key):
        if key:
            if type(key)==list:
                points=key
            else:
                points=self.device.points(key)
            if points:
                for point in points:
                    if not self.point(point.properties.name):
                        self._pointsByName[point.properties.name]=point
                        self._pointsIndexByName[point.properties.name]=len(self._points)
                        self._points.append(point)

    def cov(self, key=None):
        points=self.points(key)
        if points:
            for point in points:
                if not point.cov_registered:
                    point.subscribe_cov()

    def properties(self, index):
        point=self.point(index)
        if point:
            return point.properties

    def dump(self, key=None):
        points=self.points(key)
        if points:
            t=PrettyTable()
            t.field_names=['#', 'name', 'type', 'value', 'COV', 'unit', 'description']
            t.align['#']='l'
            t.align['name']='l'
            t.align['type']='l'
            t.align['value']='r'
            t.align['unit']='l'
            t.align['description']='l'
            for point in points:
                index=self._pointsIndexByName[point.properties.name]
                cov=''
                if point.cov_registered:
                    cov='X'
                t.add_row([index, point.properties.name, point.properties.type, point.value, cov, point.units, point.properties.description])
            print(t)

    def __iter__(self):
        return iter(self._points)


class BACDevice(object):
    def __init__(self, parent, ip, did):
        self._parent=parent
        self._did=did
        self._ip=ip
        self.logger.info('Creating device %s:%d' % (ip, did))
        self._device=BAC0.device(ip, did, parent.bac0)

    def __repr__(self):
        return '<%s:%d(%s:%s, %s, %d points)>' % (self.__class__.__name__, self._did,
            self.vendorName, self.modelName, self.systemStatus,
            len(self._device.points))

    @property
    def logger(self):
        return self._parent.logger

    @property
    def bac0(self):
        return self._parent.bac0

    @property
    def properties(self):
        return self._device.bacnet_properties

    @property
    def name(self):
        return self.properties['objectName']

    @property
    def did(self):
        return self._did

    @property
    def ip(self):
        return self._ip

    @property
    def systemStatus(self):
        return self.properties['systemStatus']

    @property
    def vendorName(self):
        return self.properties['vendorName']

    @property
    def vendorIdentifier(self):
        return self.properties['vendorIdentifier']

    @property
    def modelName(self):
        return self.properties['modelName']

    @property
    def description(self):
        return self.properties['description']

    def count(self, key=None, objectType=None, outOfService=False):
        return len(self.points(key, objectType, outOfService))

    @functools.cache
    def points(self, key=None, objectType=None, outOfService=False):
        items=[]
        if key:
            key=key.lower()
        if key=='*':
            key=None
        for point in self._device.points:
            if not outOfService and point.bacnet_properties['outOfService']:
                continue
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

    def dump(self, points=None, outOfService=False):
        if type(points) is not list:
            points=self.points(points, outOfService=outOfService)
        if points:
            t=PrettyTable()
            t.field_names=['name', 'type', 'value', 'COV', 'unit', 'description']
            t.align['name']='l'
            t.align['type']='l'
            t.align['value']='r'
            t.align['unit']='l'
            t.align['description']='l'
            for point in points:
                cov=''
                if point.cov_registered:
                    cov='X'
                t.add_row([point.properties.name, point.properties.type, point.value, cov, point.units, point.properties.description])
            print(t)

    def bag(self, key=None):
        return BACBag(self, key)

    def __iter__(self):
        return iter(self._device.points)


class BAC(object):
    def __init__(self, network, ipRouter=None, logServer='localhost', logLevel=logging.DEBUG):
        logger=logging.getLogger("BAC(%s)" % network)
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

    def __repr__(self):
        return '<%s:%s(%d devices)>' % (self.__class__.__name__, self._network, len(self._devices))

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
            return self._devices[int(did)]
        except:
            pass

    def devices(self, key=None):
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
        devices=self.devices()
        if devices:
            t=PrettyTable()
            t.field_names=['name', 'id', 'ip', 'vendor', 'model', ' status', 'description', 'points']
            t.align['*']='l'
            t.align['name']='l'
            t.align['vendor']='l'
            t.align['model']='l'
            t.align['description']='l'
            for device in devices:
                t.add_row([device.name, device.did, device.ip,
                           device.vendorName, device.modelName, device.systemStatus,
                           device.description,
                           device.count()])
            print(t)

    def __iter__(self):
        return iter(self._devices)


if __name__=='__main__':
    pass
