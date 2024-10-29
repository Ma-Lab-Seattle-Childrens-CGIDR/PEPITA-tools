import numpy as np

import dose_response
import util


def test():
    #
    # util
    #

    # util.equalsish




    # util.extract_number



    # util.get_inputs_hashfile

    # util.put_multimap



    # util.Cocktail



    # util.Dose



    # util.Ratio



    # util.Solution



    #
    # dose_response
    #

    # dose_response.do_additive_isobole

    # values from Grabovsky and Tallarida 2004, http://doi.org/10.1124/jpet.104.067264, p. 983
    # except for return value, which has been calculated separately
    assert util.equalsish(
        0.46255,
        dose_response.do_additive_isobole(
            a_i=25,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=1.2,
            p=1.73,
            q=1.92,
        ),
    )
    assert util.equalsish(
        2.06255,
        dose_response.do_additive_isobole(
            a_i=25,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=2.8,
            p=1.73,
            q=1.92,
        ),
    )
    assert util.equalsish(
        4.46255,
        dose_response.do_additive_isobole(
            a_i=25,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=5.2,
            p=1.73,
            q=1.92,
        ),
    )
    assert util.equalsish(
        0.60894,
        dose_response.do_additive_isobole(
            a_i=100,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=2.8,
            p=1.73,
            q=1.92,
        ),
    )
    assert util.equalsish(
        3.00894,
        dose_response.do_additive_isobole(
            a_i=100,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=5.2,
            p=1.73,
            q=1.92,
        ),
    )
    assert util.equalsish(
        2.28538,
        dose_response.do_additive_isobole(
            a_i=400,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=5.2,
            p=1.73,
            q=1.92,
        ),
    )

    # dose_response.do_FIC

    # values as above, with FIC=1 due to the given isoboles being additive
    assert util.equalsish(
        1,
        dose_response.do_FIC(
            a_i=25,
            b_i=0.46255,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=1.2,
            p=1.73,
            q=1.92,
        ),
    )
    assert util.equalsish(
        1,
        dose_response.do_FIC(
            a_i=25,
            b_i=2.06255,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=2.8,
            p=1.73,
            q=1.92,
        ),
    )
    assert util.equalsish(
        1,
        dose_response.do_FIC(
            a_i=25,
            b_i=4.46255,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=5.2,
            p=1.73,
            q=1.92,
        ),
    )
    assert util.equalsish(
        1,
        dose_response.do_FIC(
            a_i=100,
            b_i=0.60894,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=2.8,
            p=1.73,
            q=1.92,
        ),
    )
    assert util.equalsish(
        1,
        dose_response.do_FIC(
            a_i=100,
            b_i=3.00894,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=5.2,
            p=1.73,
            q=1.92,
        ),
    )
    assert util.equalsish(
        1,
        dose_response.do_FIC(
            a_i=400,
            b_i=2.28538,
            A_E50_a=65.8,
            B_E50_b=3.99,
            E_max_a=1.58,
            E_max_b=4.17,
            B_i=5.2,
            p=1.73,
            q=1.92,
        ),
    )

    # dose_response.filter_valid

    assert dose_response.filter_valid([1, 1, 2, 3, 5, 8], minimum=3) == [3, 5, 8]
    assert dose_response.filter_valid([1, 1, 2, 3, 5, 8], tolerance=2) == [1, 3, 5, 8]
    assert dose_response.filter_valid([1, 1, 2, 3, 5, 8], tolerance=3) == [1, 5, 8]
    assert dose_response.filter_valid([1, 1, 2, 3, 5, 8], minimum=3, tolerance=3) == [
        3,
        8,
    ]

    # dose_response.Model

    model = dose_response._get_neo_model()

    assert model.effective_concentration(0.001) < 1
    assert model.get_absolute_E_max() < 50
    assert model.get_condition_E_max() < 50
    assert util.equalsish(1, model.get_pct_survival(xs=0.001))
    assert util.equalsish(0, model.get_pct_survival(xs=2000))
    assert model.get_pct_survival(ys=100) == 1
    assert model.get_pct_survival(ys=0.001) <= 0
    assert util.equalsish(0, model.get_pct_survival(ys=model.get_absolute_E_max()))
    assert model.get_x_units() == "μM"
    assert model.get_ys(0.001) > 99
    assert model.get_ys(2000) < 50

    # get_combo_additive_expectation(pct_inhibition, model_a, model_b, model_combo, plot=True)


#
# main
#

if __name__ == "__main__":
    test()
