import argparse
from .mental_subtraction import mental_subtraction
from .session_setup import session_setup
from .clear_prompt import clear_terminal
from .log_rounds import log_session
import pathlib as pl


def main():
    clear_terminal()
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Run the app with optional parameters."
    )
    parser.add_argument(
        "--task-type",
        type=str,
        default="mental-subtraction",
        help="The kind of task, ie. the mental subtraction task or the negative/neutral speech task",
    )
    parser.add_argument(
        "--time-limit",
        type=int,
        default=300,
        help="Time limit for the session in seconds",
    )
    parser.add_argument(
        "--trial-time",
        type=int,
        default=15,
        help="Number of seconds before each individual trial timesout from a lack of interaction",
    )
    parser.add_argument(
        "--path",
        type=pl.Path,
        default=pl.Path().cwd(),
        help="The path where the session data will be saved",
    )
    args = parser.parse_args()

    participant = session_setup(time_limit=args.time_limit, trial_time=args.trial_time)

    if participant:
        print(f"ID: {participant.id}")

        rounds = mental_subtraction(
            participant, time_limit=args.time_limit, trial_time=args.trial_time
        )

        if rounds:
            log_session(participant, rounds, args.path)


if __name__ == "__main__":
    main()
