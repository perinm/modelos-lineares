from mmq.MMQ import MMQ
import numpy as np

def test_constructor():
    """
    Teste do construtor
    """
    r = MMQ()

    assert isinstance(r, MMQ)


def test_x_and_values_assertion():
    x = [1, 1, 1]
    y = [1, 1, 1]
    r = MMQ(x, y)

    assert r.x == np.array(x)
    assert r.y == np.array(y)