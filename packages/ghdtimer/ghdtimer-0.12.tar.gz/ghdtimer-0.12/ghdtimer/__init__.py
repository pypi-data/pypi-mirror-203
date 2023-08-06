from typing import Literal

import time

class Timer:
    """A Simple tick-tock based timer.

    Raises:
        ValueError: If the timer has not been started and tock() is called.

    Examples:
        >>> my_timer = Timer(mode="ms")
        >>> my_timer.tick()
        >>> do_something()
        >>> my_timer.tock()
        Took 50 ms
    """
    def __init__(self, mode:Literal['sec', 'ms', 'ns'] ="ms", decimals:int =2):
        """Create an instance of the Timer, call tick() before doing something and tock() after finishing it.

        Args:
            mode (Literal['sec', 'ms', 'ns'], optional): The mode of the timer. Defaults to "ms".
            decimals (int): Number of decimals to print. Defaults to 2
        """
        self.__start_time = None
        self.__decimals = decimals
        self.__mode = mode
        
    def tick(self):
        """Start or restart the timer
        """
        self.__start_time = time.perf_counter_ns()
        
    def tock(self, print_time:bool =True, message:str ="Took "):
        """Stop the timer, print the elapsed time and return the elapsed time.

        Args:
            print_time (bool): Whether to print the elapsed time. Defaults to True.

        Returns:
            int: The elapsed time.

        Raises:
            ValueError: If the timer has not been started.
        
        Examples:
            >>> my_timer = Timer()
            >>> my_timer.tick()
            >>> my_timer.tock()
            1.23456789012345e+09
        
        """
        if self.__start_time is not None:
            elapsed_time = time.perf_counter_ns() - self.__start_time

            # Convert to the desired mode
            if self.__mode == "sec":
                elapsed_time /= 1e9
            elif self.__mode == "ms":
                elapsed_time /= 1e6

            self.__start_time = time.perf_counter_ns()
            if print_time:
                print(f"{message}{round(elapsed_time, self.__decimals)} {self.__mode}")
            return elapsed_time
        else:
            raise ValueError("Timer must be started before it can be stopped")