import finlogic as fl


def test_db_info():
    db_info = fl.database_info()
    assert db_info["First Financial Statement"] == "2009-01-31"
    assert db_info["Accounting Rows"] > 20_000_000


def test_search_company():
    # Search for petrobras
    search_result = fl.search_company("petrobras")
    """
        co_name                            cvm_id  fiscal_id
    0   PETROBRAS DISTRIBUIDORA S/A         24295  34.274.233/0001-02
    1   PETROLEO BRASILEIRO S.A. PETROBRAS   9512  33.000.167/0001-01
    """
    # Check the results
    assert set(search_result["cvm_id"]) == {9512, 24295}
