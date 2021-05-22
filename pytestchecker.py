import check_test_widget

import primeno as pm

def test_add():
    result = pm.add(3,5)
    assert result == 8

if __name__=="__main__":
    check_test_widget.main("test_add")

