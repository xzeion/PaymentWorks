#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import subway_routes, stops, validate


def test_subway_routes():
    assert subway_routes('routes/badrequest') == []
    assert len(subway_routes('routes')) > 1
    

def test_stops():
    assert stops(None) == []
    assert stops('invlaid route') == []
    assert len(stops('Red')) > 2


def test_validate():
    assert validate(['a','b'],'c') == None
    assert validate(['a','b'],'a') == 'a'
    

