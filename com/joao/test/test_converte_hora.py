import pytest
from com.joao.converte_hora import converteHora

def test_hora_hr_neg():
    assert converteHora(-12, 0) == None


def test_hora_min_neg():
    assert converteHora(0, -8) == None


def test_hr_min_post_extra():
    assert converteHora(0, 70) == None


def test_hr_post_extra():
    assert converteHora(24, 0) == None


def test_hr_menor_doze():
    assert converteHora(10, 0) == '10:00 AM'
    

def test_hr_zerada():
    assert converteHora(0, 0) == '12:00 AM'
    

def test_hr_maior_doze():
    assert converteHora(15, 0) == '03:00 PM'