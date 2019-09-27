import pytest
from com.joao.converte_hora import converteHora

def test_converte_hora():
	assert converteHora(-3, 48) == None
	
def test_converte_manha():
	assert converteHora(8, 10) == "08:10 AM"
	
def test_converte_tarde():
	assert converteHora(21, 20) == "09:20 PM"
	
def test_converte_hora():
	assert converteHora(10, 63) == None