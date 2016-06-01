import unittest

from chappie import Machine


class MachineTestCase(unittest.TestCase):
    def setUp(self):
        machine = Machine("pending")

        self.state = None
        self.any = False

        def on_confirmed():
            self.state = "Confirmed"

        def on_any():
            self.any = True

        machine.when("confirm", {"pending": "confirmed"})
        machine.when("ignore", {"pending": "ignored"})
        machine.when("reset", {"confirmed": "pending", "ignored": "pending"})

        machine.on("confirmed", on_confirmed)
        machine.on("any", on_any)

        self.state = None
        self.machine = machine

    def test_initial_state(self):
        self.assertEqual("pending", self.machine.state)

    def test_trigger_succeeds(self):
        self.assertTrue(self.machine.trigger("confirm"))
        self.assertEqual("confirmed", self.machine.state)

        self.assertTrue(self.machine.trigger("reset"))
        self.assertEqual("pending", self.machine.state)

        self.assertTrue(self.machine.trigger("ignore"))
        self.assertEqual("ignored", self.machine.state)

    def test_trigger_fails(self):
        self.assertTrue(self.machine.trigger("confirm"))
        self.assertFalse(self.machine.trigger("ignore"))

    def test_trigger_invalid_event(self):
        self.assertFalse(self.machine.trigger("invalid"))

    def test_trigger_callback(self):
        self.machine.trigger("confirm")

        self.assertEqual("Confirmed", self.state)

    def test_trigger_any_callback(self):
        self.machine.trigger("ignore")

        self.assertTrue(self.any)
