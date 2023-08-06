import time
import random


def typewriter(
    message: str,
    delay: float = 0.05,
    acceleration: float = 0.01,
    reverse: bool = False,
    newline: bool = True,
    suffix: str = "",
    prefix: str = "",
    iterations: int = 1,
    loop_delay: float = 0.5,
    randomness: float = 0.0,
    casing: str = "unchanged",
    random_case: bool = False,
    random_suffix: bool = False,
    repeat_suffix: int = 0,
    clear: bool = False,
    animation: str = "none",
):
    """
    Print a message one character at a time, like a typewriter.

    Args:
        message: The message to print.
        delay: The delay between each character in seconds.
        acceleration: The amount of delay to add for each subsequent character.
        reverse: Whether to print the message in reverse order.
        newline: Whether to print a newline after each message.
        suffix: A string to print after the message.
        prefix: A string to print before the message.
        iterations: The number of times to print the message.
        loop_delay: The delay between each iteration in seconds.
        randomness: The amount of randomness to add to the delay.
        casing: The casing to use for the message. One of "unchanged", "upper", "lower", or "title".
        random_case: Whether to randomly switch the case of each character in the message.
        random_suffix: Whether to add a random suffix after the message.
        repeat_suffix: The number of times to repeat the suffix after the message.
        clear: Whether to clear the console before printing the message.
        animation: The animation to use for the typing effect. One of "none", "wave", "random", "block", "rain".
    """
    if clear:
        print("\033[2J\033[1;1H", end="", flush=True)  # clear the console

    if casing == "upper":
        message = message.upper()
    elif casing == "lower":
        message = message.lower()
    elif casing == "title":
        message = message.title()

    if random_case:
        message = "".join(
            random.choice([c.upper(), c.lower()]) for c in message
        )

    if reverse:
        message = message[::-1]

    for j in range(iterations):
        for i in range(len(message)):
            char = message[i]
            if animation == "wave":
                char = char.upper() if (i // 3) % 2 == 0 else char.lower()
            elif animation == "random":
                char = random.choice([char.upper(), char.lower(), char])
            elif animation == "block":
                char = "\u2588" if char != " " else " "
            elif animation == "rain":
                if char != " ":
                    char = random.choice(["|", "/", "-", "\\"])
            print(prefix + char, end="", flush=True)
            time.sleep(delay + acceleration * i + randomness * (2 * i - len(message)))

        if random_suffix:
            print(random.choice(["!", "?", ".", "..."]), end="")
        elif suffix:
            print(suffix * repeat_suffix, end="")
        if newline:
            print()

        time.sleep(loop_delay)

    if casing == "title":
        message = message.lower()
