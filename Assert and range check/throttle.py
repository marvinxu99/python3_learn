# https://rednafi.github.io/reflections/apply-constraints-with-assert-in-python.html
#
def throttle(current_iter: int, throttle_after: int = -1) -> None:
    # Return early if 'throttle_after=-1'.
    if throttle_after == -1:
        print("No throttling.")
        return

    # Ensure 'current_iter' is a positive integer.
    assert (
        isinstance(current_iter, int) and current_iter >= 0
    ), "Value of 'current_iter' must be a positive integer."

    # Ensure 'throttle_after' is a non-zero positive integer.
    assert isinstance(throttle_after, int) and throttle_after > 0, (
        "Value of 'throttle_after' must be either -1 or an "
        " integer greater than 0."
    )

    # Do the throttling.
    if current_iter > throttle_after:
        print(f"Thottling after {throttle_after} iterations.")
        return


# src.py
def throttle2(current_iter: int, throttle_after: int = -1) -> None:
    """
    The value of 'throttle_after' must be -1 or an integer
    greater than 0. Here, -1 means no throttling, and 'n'
    means that the function will throttle some operation
    after 'n' iterations.

    The `current_iter` parameter denotes the current iteration
    of some operation. When 'current_iter > throttle_after' this
    function will throttle the operation.
    """

    # Return early if 'throttle_after=-1'.
    if throttle_after == -1:
        print("No throttling.")
        return

    # Ensure 'current_iter' is a positive integer.
    if not (isinstance(current_iter, int) and current_iter >= 0):
        raise ValueError(
            "Value of 'current_iter' must be a" " positive integer."
        )

    # Ensure 'throttle_after' is a non-zero positive integer.
    if not (isinstance(throttle_after, int) and throttle_after > 0):
        raise ValueError(
            "Value of 'throttle_after' must be either -1 or an"
            " integer greater than 0."
        )

    # Do the throttling.
    if current_iter > throttle_after:
        print(f"Thottling after {throttle_after} iteration(s).")
        return


if __name__ == "__main__":
    # Prints 'Throttling after 1 iteration(s).'
    throttle(current_iter=2, throttle_after=1)
