See https://stackoverflow.com/questions/15044447/how-do-i-unit-testing-my-gui-program-with-python-and-pyqt

and https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory

I think we should use QTest and unittest because pytest-qt was not working for me.

However, the `pytest` command seems to work on the `unittest` files also!

So we'll continue using `pytest` and will just write some unit tests using the `unittest` library.
