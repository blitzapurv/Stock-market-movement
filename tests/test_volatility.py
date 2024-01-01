from __future__ import absolute_import
import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import volatility


class TestVolatility(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.volatility_period_6_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, 0.1524903845374864, 0.28384513123292787, 0.27472499826423863,
        0.38252018527403447, 0.38119139344971686, 0.3932640765681284,
        0.345017172104509, 0.35502207797108942, 0.26270939140810423,
        0.24341424180238344, 0.12003756515189819, 0.093471666193184894,
        0.069100389420744604, 0.070675428704493393, 0.062386517106180067,
        0.076730224716846165, 0.099142360710378297, 0.10592610770119171,
        0.095343491114294895, 0.094432880117036253, 0.11449523380936444,
        0.19874308222305631, 0.26016821375802046, 0.2507081012898657,
        0.24600361380487154, 0.24486737357919627, 0.20644095495335393,
        0.083562464522411659, 0.089427901528106007, 0.087018108708016018,
        0.059113141553367478, 0.04533882542423192, 0.043745342815681064,
        0.060849166597298179, 0.070157646564281986, 0.076687212024214385,
        0.076789868891622204, 0.079975193196433952, 0.062270973308414995,
        0.065217619381487457, 0.080236726179575529, 0.11968338992681561,
        0.11104995450689067, 0.14933752225515703, 0.15539159036348982,
        0.18969228060158044, 0.18590923547841665, 0.10597103882205337,
        0.10565132353205849, 0.097757896252116783, 0.10432107220772911,
        0.15464388622372643, 0.24770610313421526, 0.1937347685557344,
        0.18639971736694658, 0.17219385405371773, 0.18521003184180665,
        0.19111515274069815, 0.67712758698244713, 0.75084329516417858,
        0.2899490374301914, 0.23434490783501213, 0.23349254824431451,
        0.19491130883035751, 0.17291688690443052, 0.18952455627896306,
        0.14943455591620675, 0.12093538881060768, 0.11352129790844248,
        0.13675111326211081, 0.19911771276113485, 0.19719310858321595,
        0.20301877064572385, 0.17585792951513424, 0.15166114398944808,
        0.12154473460299797, 0.1127687218024727, 0.13396457711138229,
        0.11961401876780703, 0.12471283828508464, 0.11990156860184273,
        0.15070446430502768, 0.37046083687443693, 0.48587580247276602,
        0.48262814317551972, 0.4766783934789619, 0.44934857972966907,
        0.32796411485291727, 0.24385698905210901, 0.22975650992357466,
        0.29279256778033158, 0.2895923424432123, 0.34144133236091717,
        0.37761426331474501, 0.37476224778013606, 0.36994155773453391,
        0.78667112121907068, 0.86300585080251269, 0.23534333044989458,
        0.20968259166195685, 0.22613400310199541, 0.26667264020071202,
        0.19666727318947325, 0.074324483776256126, 0.055897268298958649,
        0.050047074730884822, 0.053240810369060795, 0.076958905307395881,
        0.25066238890997816, 0.3985022148002676, 0.45339018813190163,
        0.40090074005473725, 0.11853669350027883, 0.10192315366136466,
        0.084981565206439555, 0.094696345543641286, 0.10816591739333566,
        0.14787686072786857, 0.094089878168633442, 0.092418384168373155,
        0.087753488657869638, 0.12011498586095044]

        self.volatility_period_8_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, 0.14242985319405954, 0.24169985423921733,
        0.3113338136575341, 0.35823660012175351, 0.2897109786723715,
        0.33920738862680405, 0.30084397674280794, 0.27874472606006989,
        0.14104732116634003, 0.10350850671692319, 0.06808649301377627,
        0.06174397939422651, 0.055043294296986407, 0.055977225305731342,
        0.063756934514425712, 0.084965776367954382, 0.096566525441470791,
        0.11148807968007421, 0.11115393420884391, 0.10616253483420113,
        0.12732666627619157, 0.20137858090346494, 0.22437096030734238,
        0.26314520377982997, 0.23975292286883237, 0.094119224441386942,
        0.092781237738100916, 0.096445271412968908, 0.068309958550182667,
        0.053436187360247279, 0.050255241224061296, 0.050347489184081405,
        0.051256468547238379, 0.069732912097680774, 0.077163466932232569,
        0.080016909130893973, 0.069083593021742828, 0.065739601194198222,
        0.058817456815561914, 0.060853857257781578, 0.068147115460754693,
        0.10291856257863505, 0.13082035431264472, 0.17108073831653245,
        0.17704710115987887, 0.12132604897965137, 0.094112286486332075,
        0.085525186449793872, 0.10638905070274754, 0.11330484467160756,
        0.12192041336088531, 0.15087971223128982, 0.21614349344681355,
        0.19857901026629468, 0.19399819303164684, 0.1818708611384795,
        0.20511592974926141, 0.22512870638934221, 0.3249909324804976,
        0.25715416486495046, 0.25562259799227699, 0.19332500477233347,
        0.16618756076676156, 0.18501467898617538, 0.16520561630664882,
        0.13640762590737562, 0.1282284121401932, 0.13201283568134109,
        0.11105953157811391, 0.11589605525642854, 0.18343547199822768,
        0.19311704180590059, 0.17658236946475381, 0.13926554193674917,
        0.12236363220142392, 0.1235239400745423, 0.12530921417976978,
        0.12816011884378287, 0.12376469343773101, 0.1363460994814035,
        0.13827606997226946, 0.17106893662357836, 0.41897704683504988,
        0.43046502750119209, 0.38435154822328638, 0.3510007201166348,
        0.27101422613079296, 0.20413836250583231, 0.21157867968786048,
        0.22742953561116996, 0.24739832604356007, 0.25462527840422455,
        0.30406177112394239, 0.3814716445475102, 0.42768111395987835,
        0.42847432237222566, 0.27567929241868661, 0.2289390835731577,
        0.21867688679964709, 0.22972338923114549, 0.18365959087967343,
        0.076786556913883058, 0.059003697401793037, 0.052832920168568283,
        0.049505139847874559, 0.051157688941951211, 0.057120316051869298,
        0.083940965662256742, 0.24914260070072689, 0.32979011062763736,
        0.1323096052074898, 0.10480876704059268, 0.085936680527470583,
        0.086629096266763336, 0.083217014518560464, 0.081182983860638047,
        0.073828217218582196, 0.086704492613238301, 0.081142442111067303,
        0.090650588908834859]

        self.volatility_period_10_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, 0.15417809035843458,
        0.2408116896603047, 0.25045642049343686, 0.30298855648830314,
        0.28271934810077803, 0.30019751989944815, 0.15531803130191857,
        0.11220844736986649, 0.074895516632368819, 0.064588551678489051,
        0.052438052372962583, 0.049009961768482831, 0.05333860076049448,
        0.061982060819676429, 0.071085846449511506, 0.094584376755873154,
        0.10922283535084741, 0.12007414225686562, 0.11657088324098044,
        0.11597960977183221, 0.13634800090518195, 0.21566211367290425,
        0.21050418453382061, 0.1025548335663263, 0.1041811347612574,
        0.10414591275448988, 0.075824744175844699, 0.059981588478072154,
        0.056211687126943105, 0.05682230691715013, 0.056793800883131212,
        0.056888695537798205, 0.0547620613726214, 0.068348344590359697,
        0.069404424523249103, 0.071850312728412358, 0.065538294186633275,
        0.05876109463482912, 0.051571185068965152, 0.058338048271236238,
        0.075289596304524004, 0.11326061831246771, 0.14456281738597818,
        0.13184989418600479, 0.10571466044585399, 0.092178120503772679,
        0.090290148369258125, 0.09258525448595116, 0.11796784502651182,
        0.11401260555428137, 0.11748713942752384, 0.15238500510042516,
        0.21846560190322034, 0.20518196327986202, 0.20472687260035038,
        0.20236309821966347, 0.2124558034437691, 0.20628022609509283,
        0.27463453666990251, 0.20551996997796912, 0.17147408459105828,
        0.17970534330383031, 0.16991339139073275, 0.15066791286212405,
        0.14064333770797666, 0.13913782012536724, 0.11980998348323495,
        0.1102096991747443, 0.11004628609875898, 0.11990645094663482,
        0.16908191602784542, 0.15575422107109085, 0.13762855713533648,
        0.13846608743399774, 0.13277770682867118, 0.12888861589990716,
        0.13074380575879921, 0.13964472589084975, 0.13814264807746032,
        0.14421353523639924, 0.14995556537715846, 0.19213160105122412,
        0.37883088187714375, 0.32162673649585843, 0.2506596765354181,
        0.21433145049850072, 0.2210267024430434, 0.19378146428300974,
        0.1856025458775277, 0.20103227506988883, 0.22364031524778469,
        0.25160504803461164, 0.33144950644656002, 0.42572082344622619,
        0.28448686654260275, 0.24665815278320147, 0.23988027396914213,
        0.2335068846511005, 0.17518123479515843, 0.079487247958078391,
        0.060986278450694285, 0.052450777256972343, 0.049087834377186737,
        0.050147935844908974, 0.049494022236588019, 0.052777461547207034,
        0.060753791909360075, 0.088537303234590733, 0.12458655576002062,
        0.10764438999368131, 0.089739789240085133, 0.084219952095353462,
        0.078835298860090011, 0.072477863673140144, 0.062254121762306984,
        0.062903192247182049, 0.064946985330127008, 0.080325571807449661]

    def test_volatility_period_6(self):
        period = 6
        v = volatility.volatility(self.data, period)
        np.testing.assert_array_equal(v, self.volatility_period_6_expected)

    def test_volatility_period_8(self):
        period = 8
        v = volatility.volatility(self.data, period)
        np.testing.assert_array_equal(v, self.volatility_period_8_expected)

    def test_volatility_period_10(self):
        period = 10
        v = volatility.volatility(self.data, period)
        np.testing.assert_array_equal(v, self.volatility_period_10_expected)

    def test_volatility_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            volatility.volatility(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)