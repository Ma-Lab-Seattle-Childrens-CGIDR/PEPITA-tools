"""
Main CLI for pepita-tools
"""

# Imports
# Standard library imports
from __future__ import annotations

import argparse
import json
import os
import re
import warnings

# External imports
import numpy as np

# Local Imports
from .. import analyze, absolute, chart, keyence, imageops

DEFAULT_CONFIG = """
[Main]
absolute_max_infection = 26249
absolute_min_infection = 431
absolute_max_ototox = 26249
absolute_min_ototox = 431
channel_main_ototox = 1
channel_main_infection = 0
channel_subtr_ototox = 0
channel_subtr_infection = 1
filename_replacement_delimiter = |
filename_replacement_brightfield_infection = CH2|CH4
filename_replacement_brightfield_ototox = CH1|CH4
filename_replacement_mask_infection = CH2|mask
filename_replacement_mask_ototox = CH1|mask
filename_replacement_subtr_infection = CH2|CH1
filename_replacement_subtr_ototox = CH1|CH2
log_dir = /path/to/log/dir
"""


def set_arguments(parser):
    parser.add_argument(
        "imagefiles",
        nargs="+",
        help="The absolute or relative filenames where the relevant images can be found.",
    )
    parser.add_argument(
        "-ch",
        "--chartfile",
        help="If supplied, the resulting numbers will be charted at the given filename.",
    )

    parser.add_argument(
        "-p",
        "--platefile",
        help="CSV file containing a schematic of the plate from which the given images were "
        "taken. Row and column headers are optional. The cell values are essentially just "
        "arbitrary labels: results will be grouped and charted according to the supplied "
        "values.",
    )
    parser.add_argument(
        "-pc",
        "--plate-control",
        default=["B"],
        nargs="*",
        help=(
            "Labels to treat as the control condition in the plate schematic. These wells are "
            "used to normalize all values in the plate for more interpretable results. Any number "
            "of values may be passed."
        ),
    )
    parser.add_argument(
        "-pi",
        "--plate-ignore",
        default=[],
        nargs="*",
        help=(
            "Labels to ignore (treat as null/empty) in the plate schematic. Empty cells will "
            'automatically be ignored, but any other null values (e.g. "[empty]") must be '
            "specified here. Any number of values may be passed."
        ),
    )

    parser.add_argument(
        "-g",
        "--group-regex",
        default=".*",
        help=(
            "Pattern to be used to match group names that should be included in the results. "
            "Matched groups will be included, groups that don't match will be ignored. Control "
            "wells will always be included regardless of whether they match."
        ),
    )

    parser.add_argument(
        "-c",
        "--cap",
        default=-1,
        type=int,
        help=(
            "Exclude well values larger than the given integer, expressed as a percentage of "
            "the median control value."
        ),
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="count",
        default=0,
        help=(
            "Indicates intermediate processing images should be output for troubleshooting "
            "purposes. Including this argument once will yield one intermediate image per input "
            "file, twice will yield several intermediate images per input file."
        ),
    )
    parser.add_argument(
        "-s",
        "--silent",
        action="store_true",
        help=(
            "If present, printed output will be suppressed. More convenient for programmatic "
            "execution."
        ),
    )


# region subcommands
def config_file_command(args):
    if args.directory is None:
        directory = os.getcwd()
    else:
        directory = args.directory
    with open(f"{str(directory)}/config.ini", "w") as f:
        f.write(DEFAULT_CONFIG)


def absolute_command(args):
    if args.plate_control is None:
        plate_control = ["B"]
    else:
        plate_control = args.plate_control
    if args.plate_ignore is None:
        plate_ignore = []
    else:
        plate_ignore = args.plate_ignore

    results = {}

    schematic = analyze.get_schematic(
        args.platefile, len(args.imagefiles), plate_ignore
    )
    groups = list(dict.fromkeys(schematic))  # deduplicated copy of `schematic`
    pattern = re.compile(args.group_regex)
    images = [
        analyze.Image(filename, group, args.debug)
        for filename, group in zip(args.imagefiles, schematic)
        if group in plate_control or pattern.search(group)
    ]

    pattern = re.compile(args.group_regex)
    for group in groups:
        if group in plate_control or pattern.search(group):
            relevant_values = [
                absolute.get_absolute_value(img) for img in images if img.group == group
            ]
            results[group] = relevant_values
            if not args.silent:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", RuntimeWarning)
                    print(group, np.nanmedian(relevant_values), relevant_values)

    if args.chartfile:
        analyze.chart(results, args.chartfile)

    return results


def analyze_command(args):
    results = {}

    schematic = analyze.get_schematic(
        args.platefile, len(args.imagefiles), args.plate_ignore
    )
    groups = list(dict.fromkeys(schematic))  # deduplicated copy of `schematic`
    images = analyze.quantify(
        args.imagefiles,
        args.plate_control,
        cap=args.cap,
        debug=args.debug,
        group_regex=args.group_regex,
        schematic=schematic,
    )

    pattern = re.compile(args.group_regex)
    for group in groups:
        if group in args.plate_control or pattern.search(group):
            relevant_values = [
                img.normalized_value for img in images if img.group == group
            ]
            results[group] = relevant_values
            if not args.silent:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", RuntimeWarning)
                    print(group, np.nanmedian(relevant_values), relevant_values)

    if args.chartfile:
        analyze.chart(results, args.chartfile)

    return results


def keyence_command(args):
    for filename in args.filenames:
        metadata = keyence.extract_metadata(filename)
        print(filename, json.dumps(metadata, indent=2))

def imageops_command(args):
    for bf_filename in args.imagefiles:
        fl_filename = bf_filename.replace("CH4", "CH1")
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            bf_img = imageops.read(bf_filename, np.uint16)
            fl_img = None if not args.particles else imageops.read(fl_filename, np.uint16, 1)
        imageops.get_fish_mask(
            bf_img,
            fl_img,
            particles=args.particles,
            silent=args.debug < 1,
            verbose=args.debug > 1,
            v_file_prefix="imageops",
            mask_filename=bf_filename.replace("CH4", "mask"),
        )

def chart_command(args):
    if args.chart_type == "boxplot":
        # boxplot([int(x) for x in sys.argv[2:]])
        chart.boxplot()

# endregion subcommands


def create_parser():
    # region toplevel parser
    top_parser = argparse.ArgumentParser(prog="PEPITA-tools")
    top_parser.add_argument(
        "--config",
        required=False,
        default="./config.ini",
        help="Path to config file, if not provided will look for config.ini in current"
        "directory",
    )
    subparsers = top_parser.add_subparsers(help="subcommand help", required=True)
    # endregion toplevel parser

    # region config-file parser
    # Create the parse for the "config-file" command
    config_file_parser = subparsers.add_parser(
        "config-file", help="create a default config file"
    )
    config_file_parser.add_argument(
        "-d",
        "--directory",
        required=False,
        default=None,
        type=str,
        help="Directory to place default config file, current directory is used if not provided",
    )
    config_file_parser.set_defaults(func=config_file_command)
    # endregion config-file parser

    # region absolute parser
    # Create the parser for the absolute script
    absolute_parser = subparsers.add_parser(
        "absolute",
        help="Analyzer for images of whole zebrafish with stained neuromasts, for the "
        "purposes of measuring hair cell damage in absolute terms. Reports values in "
        "arbitrary units not relative to any other value.",
    )
    set_arguments(absolute_parser)
    absolute_parser.set_defaults(func=absolute_command)
    # endregion absolute parser

    # region analyze parser
    # Create the parser for the Analyze Script
    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyzer for images of whole zebrafish with stained "
        "neuromasts, for the purposes of measuring hair cell damage."
        " Reports values relative to control.",
    )
    set_arguments(analyze_parser)
    analyze_parser.set_defaults(func=analyze_command)
    # endregion analyze parser

    # region keyence
    # Create the Parser for the keyence script
    keyence_parser = subparsers.add_parser(
        "keyence", help="Print the metadata from keyence files"
    )
    keyence_parser.add_argument(
        "filenames", nargs="+", help="Files to get metadata from"
    )
    keyence_parser.set_defaults(func=keyence_command)

    # Create the parser for the imageops command
    imageops_parser = subparsers.add_parser(
        "imageops", help = "Utility for operating on images of whole zebrafish with stained neuromasts, "
            "for the purposes of measuring hair cell damage."
    )
    imageops_parser.add_argument(
        "imagefiles",
        nargs="+",
        help="The absolute or relative filenames where the relevant images can be found.",
    )
    imageops_parser.add_argument(
        "-p",
        "--particles",
        action="store_true",
        help=(
            "If present, the resulting mask will obscure everything except the bright particles "
            "on the fish in the given images. Otherwise the whole fish will be shown."
        ),
    )
    imageops_parser.add_argument(
        "-d",
        "--debug",
        action="count",
        default=1,
        help=(
            "Indicates intermediate processing images should be output for troubleshooting "
            "purposes. Including this argument once will yield one intermediate image per input "
            "file, twice will yield several intermediate images per input file."
        ),
    )
    imageops_parser.set_defaults(func=imageops_command)
    # endregion keyence

    # region chart parser
    # Create the parser for the chart subcommand
    chart_parser = subparsers.add_parser(
        "chart", help = "Create a boxplot"
    )
    chart_parser.add_argument("chart_type", required=True, type=str,
                              help="Desired type of chart e.g boxplot")
    chart_parser.set_defaults(func=chart_command)
    # endregion chart parser

    # region dose_response parser
    # Create the parser for the dose_response script
    
    # endregion dose_response parser

    return top_parser


def pepita():
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)
