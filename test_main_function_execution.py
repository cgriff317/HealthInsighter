# test_main_function_execution.py
from main import main


def test_main_function_execution():
    app = main()
    assert app is not None, "Main function did not return an app instance"
    assert hasattr(app, 'run_server'), "App instance does not have run_server method"


test_main_function_execution()
