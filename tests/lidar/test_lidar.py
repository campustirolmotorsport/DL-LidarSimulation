from src.lidar.lidar import Lidar


def testLaserHitObject():
    lidar = Lidar()
    laser = lidar._ray((0, 0, 0), 0)
    point = (1, 0)
    assert laser.onLine(point)


def testLaserNoHit():
    lidar = Lidar()
    laser = lidar._ray((0, 0, 0), 0)
    point = (-1, -1)
    assert not laser.onLine(point)


def testLaserOutOfRange():
    lidar = Lidar()
    laser = lidar._ray((0, 0, 0), 0)
    point = (5, 0)
    assert not laser.onLine(point)
