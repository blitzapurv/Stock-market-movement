from __future__ import absolute_import
import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import hull_moving_average


class TestHullMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.hma_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, 811.69349206349204, 814.12269841269847, 814.7884126984128,
        812.54301587301563, 812.76507936507926, 815.84714285714279,
        817.38571428571413, 813.18317460317473, 808.87650793650789,
        800.66285714285698, 792.19317460317461, 780.45333333333326,
        773.55539682539677, 766.2136507936508, 761.45111111111135,
        765.67015873015896, 779.60444444444454, 789.36746031746031,
        788.32793650793667, 782.25698412698432, 781.09047619047612,
        783.47984126984136, 781.29365079365073, 781.73365079365067,
        781.5338095238094, 778.5084126984126, 764.47793650793665,
        760.38761904761907, 769.34603174603183, 792.08984126984149,
        812.3779365079364, 816.01476190476194, 799.37571428571437,
        782.61063492063511, 779.18682539682538, 792.12841269841238,
        807.45666666666659, 819.50285714285701, 823.32126984126955,
        824.20666666666659, 827.10682539682546, 833.52063492063496,
        832.59650793650769, 826.18523809523811, 823.40587301587311,
        822.29301587301597, 814.53809523809525, 805.10174603174619,
        800.19238095238109, 804.06031746031749, 808.92031746031751,
        813.08206349206341, 808.62460317460318, 803.11682539682533,
        799.81793650793634, 800.30349206349183, 800.65809523809514,
        802.1258730158728, 802.99793650793652, 806.68492063492067,
        810.57539682539698, 808.63238095238091, 810.03047619047595,
        814.20158730158721, 812.31285714285741, 804.47984126984136,
        796.12682539682555, 793.56253968253952, 796.62619047619046,
        795.28952380952387, 790.46730158730145, 791.72126984126987,
        791.73015873015868, 796.58841269841275, 804.44523809523798,
        810.22777777777776, 806.01158730158716, 796.22888888888883,
        788.649523809524, 787.49365079365089, 791.48174603174596,
        794.16841269841245, 793.41873015872989, 792.65873015873012,
        794.41380952380962, 796.79888888888911, 799.19206349206388,
        801.93349206349228, 805.00666666666655, 804.73412698412687,
        804.90761904761928, 806.26936507936523, 808.18873015872998,
        809.21285714285705, 808.80190476190501, 806.85888888888883,
        805.96285714285693, 801.63365079365076, 797.94587301587296,
        797.31587301587331, 799.16349206349207, 796.2311111111112,
        779.59984126984125, 761.98936507936514, 752.09698412698401,
        751.06063492063493, 754.41619047619054, 755.39523809523814,
        755.67142857142869, 754.42920634920654, 753.15571428571423,
        744.10952380952369, 735.09650793650792, 728.31825396825388,
        727.54174603174613, 727.11126984126986, 721.96650793650804,
        711.58444444444456, 704.96015873015892, 702.35476190476186,
        705.01380952380953]

        self.hma_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, 814.87485185185187, 813.36083333333352,
        813.55231481481485, 815.52453703703713, 816.60727777777777,
        813.98846296296279, 810.63998148148141, 802.97816666666677,
        794.1872222222222, 782.91662962962971, 774.48968518518529,
        766.42933333333337, 760.50948148148143, 763.24012962962979,
        774.202388888889, 784.22724074074085, 787.44496296296302,
        785.29031481481491, 783.6895370370371, 783.7029444444446,
        781.14409259259253, 781.8435740740739, 781.75061111111097,
        778.72283333333326, 767.65135185185193, 762.56981481481489,
        767.40042592592602, 784.3859444444447, 804.96877777777797,
        813.94570370370366, 805.61705555555579, 791.71831481481502,
        783.63575925925932, 788.7425925925927, 800.89879629629615,
        814.41779629629616, 822.57618518518518, 826.01870370370352,
        829.13720370370356, 833.73727777777776, 833.25348148148157,
        828.76670370370357, 826.15944444444449, 823.14057407407392,
        815.59246296296305, 807.42929629629634, 801.63170370370381,
        802.28418518518538, 805.72983333333332, 810.31735185185187,
        808.87588888888888, 805.00875925925936, 801.68362962962965,
        800.02007407407393, 799.71653703703703, 801.08372222222215,
        802.32698148148131, 805.70177777777769, 809.56007407407412,
        808.71794444444447, 810.6441111111111, 814.02403703703703,
        812.15257407407398, 806.73107407407406, 799.33396296296314,
        794.71192592592604, 795.253462962963, 793.69187037037045,
        790.56812962962977, 791.91151851851839, 790.98842592592609,
        794.78342592592605, 802.43051851851851, 807.94801851851844,
        806.9679259259259, 800.01377777777782, 792.35214814814833,
        788.40029629629623, 789.58801851851831, 791.8107407407407,
        792.51031481481459, 793.013222222222, 794.36855555555542,
        796.08503703703707, 798.46237037037065, 801.42464814814832,
        804.52703703703719, 805.00503703703714, 805.58818518518513,
        806.73112962962966, 807.91777777777781, 809.11981481481473,
        809.15120370370369, 807.68392592592591, 806.69788888888888,
        802.65225925925915, 798.90994444444448, 797.67529629629632,
        798.04609259259269, 795.81775925925933, 782.72083333333342,
        767.09688888888877, 755.16894444444449, 749.3611111111112,
        750.40946296296295, 751.94831481481481, 753.80949999999996,
        754.11581481481483, 753.11190740740756, 745.79924074074097,
        737.47272222222216, 730.18538888888872, 726.73574074074077,
        725.42294444444451, 721.21061111111112, 713.11685185185195,
        706.6011666666667, 702.21687037037054, 702.67659259259256]

        self.hma_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 815.32591919191918,
        816.12421212121228, 814.75205050505053, 812.61346464646465,
        806.92502020202016, 799.51380808080796, 789.05283838383832,
        780.03197979797972, 770.46478787878777, 763.25721212121198,
        761.58636363636344, 767.63827272727269, 775.77882828282827,
        781.8372626262626, 784.24756565656571, 785.22970707070715,
        785.18085858585857, 783.0120808080809, 782.54077777777786,
        781.85660606060594, 779.98356565656559, 772.14741414141406,
        767.10270707070697, 766.90434343434356, 776.80352525252545,
        791.87784848484864, 804.56147474747468, 806.02061616161609,
        800.17926262626258, 792.75338383838391, 791.47886868686874,
        796.00545454545443, 805.8371717171716, 815.15221212121196,
        822.61240404040382, 828.08223232323223, 833.26813131313122,
        834.26621212121211, 832.05248484848471, 829.48733333333337,
        826.34853535353557, 819.84758585858583, 812.29935353535359,
        805.71183838383843, 803.18005050505053, 803.32984848484841,
        806.45084848484851, 806.91360606060607, 805.94520202020215,
        803.5248181818182, 801.79042424242425, 800.13414141414125,
        800.31101010101008, 800.98313131313125, 803.67286868686858,
        806.94001010100999, 808.04006060606059, 810.06931313131315,
        812.73437373737363, 812.65314141414137, 809.27161616161618,
        803.78738383838379, 798.82522222222212, 796.3195252525253,
        793.77120202020194, 791.12181818181818, 791.15825252525258,
        790.53879797979789, 792.94096969696966, 798.02382828282828,
        803.94456565656583, 805.53484848484857, 802.95450505050519,
        797.65067676767683, 792.79690909090914, 790.60606060606062,
        790.43761616161612, 790.83787878787859, 791.72852525252495,
        793.3122626262624, 795.02549494949506, 797.12912121212105,
        799.79068686868698, 802.83097979798004, 804.30681818181836,
        805.59772727272741, 806.70973737373754, 807.88142424242449,
        808.77309090909091, 809.22807070707074, 808.56136363636358,
        807.74880808080832, 804.7325454545454, 801.46482828282808,
        799.03266666666661, 798.22172727272743, 796.06696969696986,
        787.46221212121225, 775.40901010101027, 763.10101010101005,
        754.05883838383841, 749.79986868686865, 748.77178787878802,
        750.07509090909082, 751.28872727272721, 752.02005050505034,
        747.90270707070704, 741.89556565656574, 734.59636363636366,
        729.5704545454546, 725.75333333333344, 721.78834343434357,
        715.49432323232338, 709.65518181818186, 704.43677777777759,
        702.50812121212118]

    def test_hma_period_6(self):
        period = 6
        hma = hull_moving_average.hull_moving_average(self.data, period)
        np.testing.assert_array_equal(hma, self.hma_period_6_expected)

    def test_hma_period_8(self):
        period = 8
        hma = hull_moving_average.hull_moving_average(self.data, period)
        np.testing.assert_array_equal(hma, self.hma_period_8_expected)

    def test_hma_period_10(self):
        period = 10
        hma = hull_moving_average.hull_moving_average(self.data, period)
        np.testing.assert_array_equal(hma, self.hma_period_10_expected)

    def test_hull_moving_average_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            hull_moving_average.hull_moving_average(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
