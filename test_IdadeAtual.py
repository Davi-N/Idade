from IdadeAtual import IdadeAtual
def test_IdadeAtualVazio():
    assert IdadeAtual("","") == False

def test_IdadeAtualDataVazio():
    assert IdadeAtual("a","") == None
    
def test_IdadeAtualFormatoErrado():
    assert IdadeAtual("teste","30-06-2001") == None

def test_IdadeAtualDiaErrado():
    assert IdadeAtual("t","50/03/2011") == None

def test_IdadeAtualNomeVazio():
    assert IdadeAtual("","10/05/2000") == False
def test_IdadeAtualAnoMaior():
    assert IdadeAtual("t","30/03/2050") == False

def test_IdadeAtualAnoMaior():
    assert IdadeAtual("t","30/03/2010") == 10
