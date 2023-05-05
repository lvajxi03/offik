#!/usr/bin/env python3

from offik.core.ctypes import Direction, Orientation


def test_direction_1():
    v = Direction.EAST
    v = v.rotate_left()
    assert (v == Direction.NORTH)


def test_direction_2():
    v = Direction.SOUTH
    v = v.rotate_right()
    assert (v == Direction.WEST)


def test_direction_3():
    v = Direction.EAST
    v = v.rotate_left()
    assert(v == Direction.NORTH)


def test_direction_4():
    v = Direction.WEST
    v = v.rotate_right()
    assert(v == Direction.NORTH)


def test_direction_5():
    v = Direction.WEST
    v = v.rotate_right()
    v = v.rotate_right()
    assert(v == Direction.EAST)


def test_direction_6():
    v = Direction.EAST
    v = v.rotate_left()
    v = v.rotate_left()
    assert(v == Direction.WEST)


def test_orientation_1():
    o = Orientation.HORIZONTAL
    o = o.change()
    assert(o == Orientation.VERTICAL)


def test_orientation_2():
    o = Orientation.VERTICAL
    o = o.change()
    assert(o == Orientation.HORIZONTAL)


def test_orientation_3():
    o = Orientation.HORIZONTAL
    o = o.change()
    o = o.change()
    assert(o == Orientation.HORIZONTAL)


def test_orientation_4():
    o = Orientation.VERTICAL
    o = o.change()
    o = o.change()
    assert(o == Orientation.VERTICAL)
