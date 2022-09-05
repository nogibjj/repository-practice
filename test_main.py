from main import login, logout
# use the parameterize mark in pytest to test the login and logout function in main
def test_main():
    assert login() == "Login"
    assert logout() == "Logout"