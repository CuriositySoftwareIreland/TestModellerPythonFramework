import pytest

import pages.inventory

@pytest.mark.usefixtures("driver")
def test_jadd_to_cart(driver):
    _pagesHome_BBC_News = pages.inventory.Home_BBC_News(driver);

    _pagesHome_BBC_News.GoToUrl();

    _pagesHome_BBC_News.Click_MPs_debate_Johnsons_Brexit_bill_ahead_of_vote();

    _pagesHome_BBC_News.Click_Bailey_named_as_new_Bank_of_England_governor();
