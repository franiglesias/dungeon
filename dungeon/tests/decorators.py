def expect_event(event_class):
    def assert_event(test):
        def test_with_assertion(self):
            test(self)
            self.assertTrue(self.observer.is_aware_of(event_class))

        return test_with_assertion

    return assert_event


def expect_event_containing(event_class, method, expected):
    def assert_event_with_data(test):
        def test_with_assertion(self):
            test(self)

            last = self.observer.last(event_class)
            if hasattr(last, method):
                self.assertIn(expected, getattr(last, method)())
            else:
                raise AssertionError

        return test_with_assertion

    return assert_event_with_data


def expect_event_equal(event_class, method, expected):
    def assert_event_with_data(test):
        def test_with_assertion(self):
            test(self)

            last = self.observer.last(event_class)
            if hasattr(last, method):
                self.assertEqual(expected, getattr(last, method)())
            else:
                raise AssertionError

        return test_with_assertion

    return assert_event_with_data
