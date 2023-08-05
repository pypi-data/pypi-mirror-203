# SPDX-FileCopyrightText: 2023 German Aerospace Center <fame@dlr.de>
#
# SPDX-License-Identifier: Apache-2.0

import argparse
import copy
from enum import Enum, auto
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple

from fameio.source.logs import LOG_LEVELS

ERR_NEGATIVE_INT = "Given value `{}` is not a non-negative int."


class Options(Enum):
    """Specifies command line configuration options"""

    FILE = auto()
    LOG_LEVEL = auto()
    LOG_FILE = auto()
    OUTPUT = auto()
    AGENT_LIST = auto()
    SINGLE_AGENT_EXPORT = auto()
    MEMORY_SAVING = auto()
    RESOLVE_COMPLEX_FIELD = auto()
    TIME = auto()
    TIME_MERGING = auto()


class TimeOptions(Enum):
    """Specifies options for conversion of time in output"""

    INT = auto()
    UTC = auto()
    FAME = auto()


class ResolveOptions(Enum):
    """Specifies options for resolving complex fields in output files"""

    IGNORE = auto()
    SPLIT = auto()
    MERGE = auto()


class MergingOptions(Enum):
    """Specifies options for merging TimeSteps"""

    FOCAL_POINT = auto()
    STEPS_BEFORE = auto()
    STEPS_AFTER = auto()


def arg_handling_make_config(args: List[str], defaults: Dict) -> Tuple[str, Dict]:
    """Handles command line arguments and returns `input_file` and `run_config` for make_config script"""
    parser = argparse.ArgumentParser()

    add_file_argument(parser, "provide path to configuration file")
    add_log_level_argument(parser, defaults[Options.LOG_LEVEL])
    add_logfile_argument(parser)
    add_output_argument(parser, defaults[Options.OUTPUT], "provide file-path for the file to generate")

    args = parser.parse_args(args)
    run_config = {
        Options.LOG_LEVEL: args.log,
        Options.LOG_FILE: args.logfile,
        Options.OUTPUT: args.output,
    }
    return args.file, run_config


def arg_handling_convert_results(args: List[str], defaults: Dict) -> Tuple[str, Dict]:
    """Handles command line arguments and returns `input_file` and `run_config` for convert_results script"""
    parser = argparse.ArgumentParser()

    add_file_argument(parser, "provide path to protobuf file")
    add_log_level_argument(parser, defaults[Options.LOG_LEVEL])
    add_logfile_argument(parser)
    add_output_argument(
        parser,
        defaults[Options.OUTPUT],
        "provide path to folder to store output .csv files",
    )
    add_select_agents_argument(parser)
    add_single_export_argument(parser, defaults[Options.SINGLE_AGENT_EXPORT])
    add_memory_saving_argument(parser, defaults[Options.MEMORY_SAVING])
    add_resolve_complex_argument(parser, defaults[Options.RESOLVE_COMPLEX_FIELD])
    add_time_argument(parser, defaults[Options.TIME])
    add_merge_time_parser(parser)

    args = parser.parse_args(args)

    run_config = {
        Options.LOG_LEVEL: args.log,
        Options.LOG_FILE: args.logfile,
        Options.OUTPUT: args.output,
        Options.AGENT_LIST: args.agents,
        Options.SINGLE_AGENT_EXPORT: args.single_export,
        Options.MEMORY_SAVING: args.memory_saving,
        Options.RESOLVE_COMPLEX_FIELD: ResolveOptions[args.complex_column],
        Options.TIME: args.time,
        Options.TIME_MERGING: get_merging_args(args),
    }
    return args.file, run_config


def add_file_argument(parser: argparse.ArgumentParser, help_text: str) -> None:
    """Adds required 'file' argument to the provided `parser` with the provided `help_text`"""
    parser.add_argument("-f", "--file", type=Path, required=True, help=help_text)


def add_select_agents_argument(parser: argparse.ArgumentParser) -> None:
    """Adds optional repeatable string argument 'agent' to given `parser`"""
    help_text = "Provide list of agents to extract (default=None)"
    parser.add_argument("-a", "--agents", nargs="*", type=str, help=help_text)


def add_logfile_argument(parser: argparse.ArgumentParser) -> None:
    """Adds optional argument 'logfile' to given `parser`"""
    help_text = "provide logging file (default=None)"
    parser.add_argument("-lf", "--logfile", type=Path, help=help_text)


def add_output_argument(parser: argparse.ArgumentParser, default_value, help_text: str) -> None:
    """Adds optional argument 'output' to given `parser` using the given `help_text` and `default_value`"""
    parser.add_argument("-o", "--output", type=Path, default=default_value, help=help_text)


def add_log_level_argument(parser: argparse.ArgumentParser, default_value: str) -> None:
    """Adds optional argument 'log' to given `parser`"""
    help_text = "choose logging level (default: {})".format(default_value)
    parser.add_argument(
        "-l",
        "--log",
        default=default_value,
        choices=list(LOG_LEVELS.keys()),
        type=str.lower,
        help=help_text,
    )


def add_single_export_argument(parser: argparse.ArgumentParser, default_value: bool) -> None:
    """Adds optional repeatable string argument 'agent' to given `parser`"""
    help_text = "Enable export of single agents (default=False)"
    parser.add_argument(
        "-se",
        "--single-export",
        default=default_value,
        action="store_true",
        help=help_text,
    )


def add_memory_saving_argument(parser: argparse.ArgumentParser, default_value: bool) -> None:
    """Adds optional bool argument to given `parser` to enable memory saving mode"""
    help_text = "Reduces memory usage profile at the cost of runtime (default=False)"
    parser.add_argument(
        "-m",
        "--memory-saving",
        default=default_value,
        action="store_true",
        help=help_text,
    )


def add_resolve_complex_argument(parser, default_value: str):
    """Instructs given `parser` how to deal with complex field outputs"""
    help_text = f"How to deal with complex index columns? (default={default_value})"
    parser.add_argument(
        "-cc",
        "--complex-column",
        default=default_value,
        choices=[e.name for e in ResolveOptions],
        help=help_text,
        type=str.upper,
    )


def add_time_argument(parser: argparse.ArgumentParser, default_value: str) -> None:
    """Adds optional argument to given `parser` to define conversion of TimeSteps"""
    help_text = "Apply conversion of time steps to given format (default=UTC)"
    parser.add_argument(
        "-t", "--time", default=default_value, choices=[e.name for e in TimeOptions], help=help_text, type=str.upper
    )


def add_merge_time_parser(parser: argparse.ArgumentParser) -> None:
    """Adds subparser for merging of TimeSteps to given `parser`"""
    subparser = parser.add_subparsers(dest="time_merging", required=False, help="Optional merging of TimeSteps")
    group_parser = subparser.add_parser("merge-times")
    add_focal_point_argument(group_parser)
    add_steps_before_argument(group_parser)
    add_steps_after_argument(group_parser)


def add_focal_point_argument(parser: argparse.ArgumentParser) -> None:
    """Adds `focal-point` argument to given `parser`"""
    help_text = "TimeStep on which `steps_before` earlier and `steps_after` later TimeSteps are merged on"
    parser.add_argument("-fp", "--focal-point", required=True, type=int, help=help_text)


def add_steps_before_argument(parser: argparse.ArgumentParser) -> None:
    """Adds `steps-before` argument to given `parser`"""
    help_text = "Range of TimeSteps before the `focal-point` they get merged to"
    parser.add_argument("-sb", "--steps-before", required=True, type=non_negative_int, help=help_text)


def non_negative_int(value: Any) -> int:
    """
    Casts a given ´value` to int and checks it for non-negativity

    Args:
        value: to check and parse

    Returns:
        `value` parsed to int if it is a non-negative integer

    Raises:
        TypeError: if `value` is None
        ValueError: if `value` cannot be parsed to int
        argparse.ArgumentTypeError: if `value` is a negative int

    """
    value = int(value)
    if value < 0:
        raise argparse.ArgumentTypeError(ERR_NEGATIVE_INT.format(value))
    return value


def add_steps_after_argument(parser: argparse.ArgumentParser) -> None:
    """Adds `steps-after` argument to given `parser`"""
    help_text = "Range of TimeSteps after the `focal-point` they get merged to"
    parser.add_argument("-sa", "--steps-after", required=True, type=non_negative_int, help=help_text)


def get_merging_args(args: argparse.Namespace) -> Dict[MergingOptions, int]:
    """Returns a dictionary of GroupingOptions with their values if `time_merging` entry exists"""
    merging_args = {}
    if "time_merging" in args:
        merging_args[MergingOptions.FOCAL_POINT] = args.focal_point
        merging_args[MergingOptions.STEPS_BEFORE] = args.steps_before
        merging_args[MergingOptions.STEPS_AFTER] = args.steps_after
    return merging_args


def update_default_config(config: Optional[dict], default: dict) -> dict:
    """Returns `default` config with updated fields received from `config`"""
    result = copy.deepcopy(default)
    if config:
        for name, option in config.items():
            result[name] = option
    return result
