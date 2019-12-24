import pytest


import pages.Create_New_Customer_Account


@pytest.mark.usefixtures("driver")
def test_gotourl(driver):
    
    _pagesCreate_New_Customer_Account = pages.Create_New_Customer_Account.Create_New_Customer_Account(driver);
    _pagesCreate_New_Customer_Account.GoToUrl();


    _pagesCreate_New_Customer_Account.Enter_First_Name("sit");

    _pagesCreate_New_Customer_Account.Enter_Last_Name("Schumm");

    _pagesCreate_New_Customer_Account.Enter_Email("james.walker@curiosity.software");

    _pagesCreate_New_Customer_Account.Enter_Password("HQR5pwprpK");

    _pagesCreate_New_Customer_Account.Click_Create_an_Account();


@pytest.mark.usefixtures("driver")
def test_GoToUrlPositiveFirstNamePositiveLastNamePositiveEmailNegativePasswordError2(driver):
    
    _pagesCreate_New_Customer_Account = pages.Create_New_Customer_Account.Create_New_Customer_Account(driver);
    _pagesCreate_New_Customer_Account.GoToUrl();


    _pagesCreate_New_Customer_Account.Enter_First_Name("et");

    _pagesCreate_New_Customer_Account.Enter_Last_Name("Wunsch");

    _pagesCreate_New_Customer_Account.Enter_Email("james.walker@curiosity.software");

    _pagesCreate_New_Customer_Account.Enter_Password("#!_ @");


@pytest.mark.usefixtures("driver")
def test_GoToUrlPositiveFirstNamePositiveLastNameNegativeEmailError3(driver):
    
    _pagesCreate_New_Customer_Account = pages.Create_New_Customer_Account.Create_New_Customer_Account(driver);
    _pagesCreate_New_Customer_Account.GoToUrl();


    _pagesCreate_New_Customer_Account.Enter_First_Name("sed");

    _pagesCreate_New_Customer_Account.Enter_Last_Name("Kling");

    _pagesCreate_New_Customer_Account.Enter_Email("james.walker");


@pytest.mark.usefixtures("driver")
def test_GoToUrlPositiveFirstNameNegativeLastNameError4(driver):
    
    _pagesCreate_New_Customer_Account = pages.Create_New_Customer_Account.Create_New_Customer_Account(driver);
    _pagesCreate_New_Customer_Account.GoToUrl();


    _pagesCreate_New_Customer_Account.Enter_First_Name("pariatur");

    _pagesCreate_New_Customer_Account.Enter_Last_Name("");


@pytest.mark.usefixtures("driver")
def test_GoToUrlPositiveFirstNameNegativeLastNameError5(driver):
    
    _pagesCreate_New_Customer_Account = pages.Create_New_Customer_Account.Create_New_Customer_Account(driver);
    _pagesCreate_New_Customer_Account.GoToUrl();


    _pagesCreate_New_Customer_Account.Enter_First_Name("sit");

    _pagesCreate_New_Customer_Account.Enter_Last_Name("#!_ @");


@pytest.mark.usefixtures("driver")
def test_GoToUrlNegativeFirstNameError6(driver):
    
    _pagesCreate_New_Customer_Account = pages.Create_New_Customer_Account.Create_New_Customer_Account(driver);
    _pagesCreate_New_Customer_Account.GoToUrl();


    _pagesCreate_New_Customer_Account.Enter_First_Name("389348");


