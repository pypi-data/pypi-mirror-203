from je_assert_lib.utils.assert_fail import assert_fail_message


def assert_callable_equal_value(callable1, callable2, when_failure_print_message: str = None):
    if (callable1() == callable2) is False:
        assert_fail_message(when_failure_print_message)


def assert_callable_not_equal_value(callable1, callable2, when_failure_print_message: str = None):
    if (callable1() == callable2) is True:
        assert_fail_message(when_failure_print_message)
