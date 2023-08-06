import argparse
import contextlib
import sys
from textwrap import dedent
from typing import Any, List, NoReturn, Optional, Tuple

from scalene.scalene_arguments import ScaleneArguments
from scalene.scalene_version import scalene_version, scalene_date

scalene_gui_url = "https://plasma-umass.org/scalene-gui/"


class RichArgParser(argparse.ArgumentParser):
    def __init__(self, *args: Any, **kwargs: Any):
        from rich.console import Console

        self.console = Console()
        super().__init__(*args, **kwargs)

    def _print_message(self, message: Optional[str], file: Any = None) -> None:
        if message:
            self.console.print(message)


class StopJupyterExecution(Exception):
    """NOP exception to enable clean exits from within Jupyter notebooks."""

    def _render_traceback_(self) -> None:
        pass


class ScaleneParseArgs:
    @staticmethod
    def clean_exit(code: object = 0) -> NoReturn:
        """Replacement for sys.exit that exits cleanly from within Jupyter notebooks."""
        raise StopJupyterExecution

    @staticmethod
    def parse_args() -> Tuple[argparse.Namespace, List[str]]:
        # In IPython, intercept exit cleanly (because sys.exit triggers a backtrace).
        with contextlib.suppress(BaseException):
            from IPython import get_ipython

            if get_ipython():
                sys.exit = ScaleneParseArgs.clean_exit
                sys._exit = ScaleneParseArgs.clean_exit  # type: ignore
        defaults = ScaleneArguments()

        # If any of the individual profiling metrics were specified,
        # disable the unspecified ones (set as None).
        if args.cpu or args.gpu or args.memory:
            if not args.memory:
                args.memory = False
            if not args.gpu:
                args.gpu = False
        else:
            # Nothing specified; use defaults.
            args.cpu = defaults.cpu
            args.gpu = defaults.gpu
            args.memory = defaults.memory

        args.cpu = True  # Always true

        in_jupyter_notebook = len(sys.argv) >= 1 and re.match(
            r"ipython-input-([0-9]+)-.*", sys.argv[0]
        )
        # If the user did not enter any commands (just `scalene` or `python3 -m scalene`),
        # print the usage information and bail.
        if not in_jupyter_notebook and (len(sys.argv) + len(left) == 1):
            parser.print_help(sys.stderr)
            sys.exit(-1)
        if args.version:
            print(f"Scalene version {scalene_version} ({scalene_date})")
            sys.exit(-1)
        return args, left
