from approxeng.input.selectbinder import ControllerResource
from time import sleep
from volux.module import VoluxSource
from typing import Any
from threading import Thread


def _noop(*args, **kwargs):
    return


def _prepare():
    return


def _cleanup():
    return


def _joystick_handler(joystick, on_presses):
    # This is an instance of approxeng.input.ButtonPresses
    presses = joystick.check_presses()
    # if presses["square"]:
    #     print("SQUARE pressed since last check")
    # # We can also use attributes directly, and get at the presses object from the controller:
    # if joystick.presses.circle:
    #     print("CIRCLE pressed since last check")
    # # Or we can use the 'x in y' syntax:
    # if "triangle" in presses:
    #     print("TRIANGLE pressed since last check")

    # if we had any presses
    if joystick.has_presses:
        # call on_presses callback with presses
        on_presses(presses)


def _joystick_thread(controller_instance):
    # while controller instance is running (controlled by start/stop methods)
    while controller_instance.running:
        try:
            # connect to joystick
            with ControllerResource() as joystick:
                print("Found a joystick and connected")
                # mark controller as connected on controller instance
                controller_instance.connected = True
                # while joystick is connected and controller instance is running
                while joystick.connected and controller_instance.running:
                    # do joystick stuff
                    _joystick_handler(joystick, controller_instance._on_presses)
                    # sleep until next poll
                    sleep(controller_instance._ms_between_polls)
            # Joystick disconnected...
            print("Connection to joystick lost")
            # mark controller as disconnected on controller instance
            controller_instance.connected = False
        except IOError:
            # No joystick found, wait for a bit before trying again
            print("Unable to find any joysticks")
            sleep(1.0)


# self.joystick = ControllerResource()
# self.joystick.__enter__()

# # HACK: `ControllerResource.__exit__()`'s arguments aren't even used, so
# # ... just pass in some empty strings so we don't get an error about
# # ... missing arguments
# self.joystick.__exit__("", "", "")
# self.joystick = None  # set joystick attrib back to None


class VoluxController(VoluxSource):
    def __init__(self, polling_rate=1000, on_presses=_noop):
        self.connected = False
        self._ms_between_polls = 1 / polling_rate
        self._on_presses = on_presses

        super().__init__(
            prepare=_prepare,
            cleanup=_cleanup,
        )

    def start(self):
        print("starting joystick thread!")
        self.running = True
        self._t_joystick = Thread(target=_joystick_thread, args=(self,))
        self._t_joystick.start()
        return True

    def stop(self):
        print("stopping joystick thread!")
        self.running = False
        self._t_joystick.join()
        return True

    def __enter__(self):
        """Start joystick thread."""
        self.start()
        return self

    def __exit__(
        self, exception_type: Any, exception_value: Any, traceback: Any
    ) -> Any:
        """Stop joystick thread."""
        self.stop()
        # NOTE: WARNING! - don't return anything from this method!
        # ... Exceptions will be suppressed on exit!
