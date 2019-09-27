import pytest
from com.joao.conta_corrente import ContaCorrente

def test_alterarNome():
    conta = ContaCorrente(7,"Wallas")
    conta.alterarNome("Bradesco")
    assert conta.nomeCorrentista == "Bradesco"

def test_alterardeposito():
    conta = ContaCorrente(7,"Wallas")
    conta.deposito(100)
    assert conta.saldo == 100

def test_alterarsaque():
    conta = ContaCorrente(7,"Wallas", 100)
    conta.saque(100)
    assert conta.saldo == 0