from numpy.distutils.misc_util import Configuration

# Imports
# Standard Library Imports
import json
import os
import warnings


# External Imports
import numpy as np

import seaborn as sns

# Local Imports
from . import absolute, analyze, imageops, pipeline, utils
from .configuration import Configuration


LOG_DIR = f'{Configuration().log_dir}/dose_response'
ABS_MAX = int(Configuration().absolute_max_infection)
ABS_MIN = int(Configuration().absolute_min_infection)

channel_main_infection = int(Configuration().channel_main_infection)
channel_subtr_infection = int(Configuration().channel_subtr_infection)
replacement_delim = Configuration().filename_replacement_delimiter
replacement_brfld = Configuration().filename_replacement_brightfield_infection.split(
    replacement_delim
)
replacement_mask = Configuration().filename_replacement_mask_infection.split(
    replacement_delim
)
replacement_subtr = Configuration().filename_replacement_subtr_infection.split(
    replacement_delim
)


class InfectionImage(analyze.Image):
    channel = channel_main_infection
    channel_subtr = channel_subtr_infection
    particles = False
    replacement_brfld = replacement_brfld
    replacement_mask = replacement_mask
    replacement_subtr = replacement_subtr

    def get_raw_value(self, threshold=0.02):
        if self.value is None:
            fl_img_masked = imageops.apply_mask(self.get_fl_img(), self.get_mask())
            max_value = imageops._get_bit_depth(fl_img_masked)[1]
            total = fl_img_masked.sum(
                dtype=np.uint64, where=(fl_img_masked > max_value * threshold)
            )
            self.value = total if total > 0 else np.nan
        return self.value


def log(results):
    return {key: np.log2(values).tolist() for key, values in results.items()}


def main(
    imagefiles,
    cap=-1,
    chartfile=None,
    checkerboard=False,
    conversions=[],
    debug=0,
    platefile=None,
    plate_control=["B"],
    plate_info=None,
    plate_positive_control=[],
    treatment_platefile=None,
    absolute_chart=False,
    silent=False,
    talk=False,
):
    hashfile = utils.get_inputs_hashfile(
        imagefiles=imagefiles, cap=cap, platefile=platefile, plate_control=plate_control
    )

    if talk:
        sns.set_context("talk")

    if debug == 0 and os.path.exists(hashfile):
        with open(hashfile, "r") as f:  # read cached results
            results = json.load(f)

        for group, relevant_values in results.items():
            if not silent:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", RuntimeWarning)
                    print(group, np.nanmedian(relevant_values), relevant_values)
    else:
        results = quantify_infection(
            imagefiles=imagefiles,
            cap=cap,
            debug=debug,
            platefile=platefile,
            plate_control=plate_control,
            silent=False,
        )
        with open(hashfile, "w") as f:  # cache results for reuse
            json.dump(results, f, ensure_ascii=False)

    if chartfile:
        analyze.chart(log(results), chartfile)

    conversions = dict(conversions)
    drug_conditions = _parse_results(results, conversions)
    control_drugs = [
        utils.Cocktail(utils.Dose(control).drug) for control in plate_control
    ]
    models = {}

    results = {utils.Solution(key, conversions): value for key, value in results.items()}

    # generate plate schematics

    schematic = analyze.get_schematic(platefile, len(imagefiles), flat=False)

    max_result = np.log2(
        max(val for vals_list in results.values() for val in vals_list)
    )

    pipeline.generate_plate_schematic(
        schematic,
        log(results),
        conversions=conversions,
        plate_info=plate_info,
        well_count=96,
        cmap=sns.dark_palette("red", as_cmap=True),
        max_val=max_result,
    )


def quantify_infection(
    imagefiles, cap=-1, debug=0, platefile=None, plate_control=["B"], silent=False
):
    results = {}

    schematic = analyze.get_schematic(platefile, len(imagefiles))
    groups = list(dict.fromkeys(schematic))  # deduplicated copy of `schematic`

    images = [
        InfectionImage(filename, group, debug)
        for filename, group in zip(imagefiles, schematic)
    ]

    for group in groups:
        relevant_values = [
            absolute.get_absolute_value(img) for img in images if img.group == group
        ]
        results[group] = relevant_values
        if not silent:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", RuntimeWarning)
                print(group, np.nanmedian(relevant_values), relevant_values)

    return results


def _key_value_pair(argument, delimiter="="):
    return tuple(argument.split(delimiter))


def _parse_results(results, conversions):
    drug_conditions = {}
    for condition in results:
        solution = utils.Solution(condition, conversions)
        utils.put_multimap(drug_conditions, solution.get_cocktail(), solution)
    return drug_conditions