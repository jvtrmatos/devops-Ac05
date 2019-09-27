import pytest
from com.joao.calcula_parcela import valorPagamento

def test_calcula_parcela():
	assert valorPagamento(50, 0) == 50
	
def test_dias_de_atraso():
	assert valorPagamento(50, 2) == 52.5
	
def test_dias():
	assert valorPagamento(-1, 0) == None