from pylab import *
import numpy

analyze_value = array([
	25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975,
	1025, 1075, 1125, 1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975,
	2025, 2075, 2125, 2175, 2225, 2275, 2325, 2375, 2425, 2475, 2525, 2575, 2625, 2675, 2725, 2775, 2825, 2875, 2925, 2975,
	3025, 3075, 3125, 3175, 3225, 3275, 3325, 3375, 3425, 3475, 3525, 3575, 3625, 3675, 3725, 3775, 3825, 3875, 3925, 3975,
	4025, 4075, 4125, 4175, 4225, 4275, 4325, 4375, 4425, 4475, 4525, 4575, 4625, 4675, 4725, 4775, 4825, 4875, 4925, 4975,
	5025, 5075, 5125, 5175, 5225, 5275, 5325, 5375, 5425, 5475, 5525, 5575, 5625, 5675, 5725, 5775, 5825, 5875, 5925, 5975,
	6025, 6075, 6125, 6175, 6225, 6275, 6325, 6375, 6425, 6475, 6525, 6575, 6625, 6675, 6725, 6775, 6825, 6875, 6925, 6975,
	7025, 7075, 7125, 7175, 7225, 7275, 7325, 7375, 7425, 7475, 7525, 7575, 7625, 7675, 7725, 7775, 7825, 7875, 7925, 7975,
	8025, 8075, 8125, 8175, 8225, 8275, 8325, 8375, 8425, 8475, 8525, 8575, 8625, 8675, 8725, 8775, 8825, 8875, 8925, 8975,
	9025, 9075, 9125, 9175, 9225, 9275, 9325, 9375, 9425, 9475, 9525, 9575, 9625, 9675, 9725, 9775, 9825, 9875, 9925, 9975,
	10025, 10075, 10125, 10175, 10225, 10275, 10325, 10375, 10425, 10475, 10525, 10575, 10625, 10675, 10725, 10775, 10825, 10875, 10925, 10975,
	11025, 11075, 11125, 11175, 11225, 11275, 11325, 11375, 11425, 11475, 11525, 11575, 11625, 11675, 11725, 11775, 11825, 11875, 11925, 11975,
	12025, 12075, 12125, 12175, 12225, 12275, 12325, 12375, 12425, 12475, 12525, 12575, 12625, 12675, 12725, 12775, 12825, 12875, 12925, 12975,
	13025, 13075, 13125, 13175, 13225, 13275, 13325, 13375, 13425, 13475, 13525, 13575, 13625, 13675, 13725, 13775, 13825, 13875, 13925, 13975,
	14025, 14075, 14125, 14175, 14225, 14275, 14325, 14375, 14425, 14475, 14525, 14575, 14625, 14675, 14725, 14775, 14825, 14875, 14925, 14975,
	15025, 15075, 15125, 15175, 15225, 15275, 15325, 15375, 15425, 15475, 15525, 15575, 15625, 15675, 15725, 15775, 15825, 15875, 15925, 15975,
	16025, 16075, 16125, 16175, 16225, 16275, 16325, 16375, 16425, 16475, 16525, 16575, 16625, 16675, 16725, 16775, 16825, 16875, 16925, 16975,
	17025, 17075, 17125, 17175, 17225, 17275, 17325, 17375, 17425, 17475, 17525, 17575, 17625, 17675, 17725, 17775, 17825, 17875, 17925, 17975,
	18025, 18075, 18125, 18175, 18225, 18275, 18325, 18375, 18425, 18475, 18525, 18575, 18625, 18675, 18725, 18775, 18825, 18875, 18925, 18975,
	19025, 19075, 19125, 19175, 19225, 19275, 19325, 19375, 19425, 19475, 19525, 19575, 19625, 19675, 19725, 19775, 19825, 19875, 19925, 19975,
	20025, 20075, 20125, 20175, 20225, 20275, 20325, 20375, 20425, 20475, 20525, 20575, 20625, 20675, 20725, 20775, 20825, 20875, 20925, 20975,
	21025, 21075, 21125, 21175, 21225, 21275, 21325, 21375, 21425, 21475, 21525, 21575, 21625, 21675, 21725, 21775, 21825, 21875, 21925, 21975,
	22025, 22075, 22125, 22175, 22225, 22275, 22325, 22375, 22425, 22475, 22525, 22575, 22625, 22675, 22725, 22775, 22825, 22875, 22925, 22975,
	23025, 23075, 23125, 23175, 23225, 23275, 23325, 23375, 23425, 23475, 23525, 23575, 23625, 23675, 23725, 23775, 23825, 23875, 23925, 23975,
	24025, 24075, 24125, 24175, 24225, 24275, 24325, 24375, 24425, 24475, 24525, 24575])
analyze_score = array([
	[93192, 93502, 0, 0], [92958, 93051, 0, 0], [92816, 92909, 92854, 0], [92428, 92183, 90320, 0], [92153, 91949, 57787, 0],
	[91777, 92369, 92379, 0], [91253, 91456, 91062, 0], [91058, 90917, 97947, 0], [90731, 90743, 90586, 0], [90439, 90560, 89820, 0],
	[90212, 90540, 90831, 89978], [89356, 89599, 90034, 89849], [88800, 89238, 89986, 91985], [88539, 89135, 89050, 97111], [88235, 88641, 95195, 112333],
	[88031, 87723, 88691, 0], [87434, 87685, 87357, 0], [87138, 88104, 90844, 0], [86915, 86847, 86473, 0], [86500, 86294, 85131, 0],
	[86341, 86006, 83604, 83933], [85301, 85745, 85973, 84479], [84081, 84553, 88380, 86748], [83638, 83842, 85824, 90658], [83387, 83290, 87410, 95129],
	[83119, 83123, 89164, 146235], [82674, 82990, 83391, 157450], [82298, 82216, 83380, 158298], [81960, 81848, 83468, 0], [81622, 81734, 83013, 0],
	[81389, 81285, 84005, 0], [80971, 81011, 80880, 80928], [80385, 80535, 80264, 80659], [79932, 79850, 79908, 80047], [79642, 79526, 79652, 80292],
	[79271, 79296, 80206, 80266], [78957, 79189, 79878, 80326], [78589, 78736, 78867, 85619], [78257, 78119, 77669, 93026], [77913, 78041, 77848, 0],
	[77695, 77535, 74764, 0], [77266, 77525, 78081, 76749], [74948, 75580, 76203, 76664], [74146, 73882, 74078, 75546], [73751, 73557, 72489, 73924],
	[73432, 73694, 71221, 71653], [73067, 72888, 72018, 71210], [72593, 73092, 74036, 68631], [72368, 72417, 74373, 70553], [72104, 72569, 72923, 70898],
	[71760, 71707, 72415, 60828], [71529, 71225, 71073, 70864], [70861, 71107, 71291, 71172], [70395, 70852, 70505, 71063], [70076, 70091, 69820, 70611],
	[69718, 69590, 68601, 68573], [69429, 69441, 68522, 68510], [68976, 69247, 69376, 69299], [68674, 68388, 68784, 64683], [68447, 68296, 68629, 0],
	[68117, 67620, 66194, 0], [67838, 68004, 67399, 63548], [67322, 67288, 67299, 67848], [66546, 66213, 65610, 66948], [66172, 65849, 64897, 65950],
	[65785, 65501, 65326, 64122], [65625, 65102, 63420, 62625], [65233, 65170, 65192, 62215], [64924, 64771, 63219, 62483], [64707, 64620, 64860, 63523],
	[64437, 64175, 62491, 62618], [64182, 63886, 60347, 62561], [63824, 63773, 63706, 63721], [63273, 62852, 60521, 62987], [63101, 62429, 60123, 63673],
	[62905, 61632, 59452, 60430], [62768, 62633, 54448, 61470], [62630, 62154, 62548, 60467], [62368, 60647, 55010, 54807], [62130, 61288, 48024, 46062],
	[62223, 61218, 59442, 32249], [62408, 62124, 58950, 32874], [62268, 62395, 63133, 65713], [59173, 58787, 57941, 61145], [58162, 56723, 52995, 51757],
	[58182, 56260, 52881, 50990], [57944, 57037, 47369, 47677], [57927, 57903, 55620, 48900], [57648, 57599, 57783, 46402], [57424, 57807, 57077, 41158],
	[57167, 56709, 56665, 49475], [56924, 56819, 55897, 50926], [56638, 56670, 55908, 54404], [55968, 55713, 55599, 55094], [55617, 55990, 55396, 55717],
	[55288, 55270, 54651, 54823], [54932, 55168, 54671, 55405], [54760, 54468, 54118, 55032], [54242, 54667, 55520, 54902], [53890, 54326, 57352, 59161],
	[53597, 53877, 53727, 54258], [53273, 53359, 53327, 0], [53033, 53535, 50984, 50763], [52393, 52316, 52464, 52632], [51629, 51733, 51523, 52055],
	[51147, 50879, 50722, 51181], [50887, 50973, 50265, 49870], [50577, 50434, 49529, 49309], [50225, 49812, 49957, 48577], [49915, 49887, 49613, 47993],
	[49612, 49493, 50553, 48182], [49275, 49127, 47584, 48978], [49070, 48639, 45581, 49643], [48593, 48525, 48846, 50739], [48048, 47499, 45008, 49253],
	[47940, 47671, 46880, 49735], [47690, 46635, 45915, 49199], [47513, 47191, 43977, 50728], [47309, 47048, 47624, 51349], [47014, 45352, 41818, 50408],
	[46864, 45194, 36513, 9858], [46780, 46280, 43476, 26], [46925, 46795, 43163, 0], [46914, 46925, 47016, 47948], [45651, 45164, 43947, 45159],
	[45429, 43909, 39047, 35182], [45454, 45425, 43595, 35333], [45476, 45208, 40732, 33211], [45479, 45173, 43794, 34067], [45263, 45458, 45441, 32475],
	[45181, 45211, 48526, 31409], [44820, 44708, 43711, 30784], [44531, 44011, 36200, 34864], [44352, 44349, 43365, 45248], [43752, 43348, 41758, 44177],
	[43415, 42297, 36979, 40608], [43237, 42710, 40908, 37989], [42975, 42470, 34641, 39025], [42741, 42399, 41598, 39479], [42454, 41483, 40751, 38204],
	[42104, 40745, 30982, 46319], [41903, 41345, 37902, 0], [41827, 41556, 39245, 0], [41781, 41800, 40847, 45703], [41619, 41048, 40824, 42611],
	[41454, 40682, 35717, 34603], [41647, 40791, 38482, 33009], [41598, 40415, 33919, 30388], [41586, 40567, 31360, 31582], [41439, 41290, 41140, 33368],
	[41380, 40484, 35939, 36536], [41259, 40917, 37274, 37087], [41147, 41010, 40031, 38076], [41081, 40581, 39858, 40340], [41067, 40765, 40400, 43148],
	[41283, 39818, 31177, 34823], [41420, 40343, 31312, 20886], [41326, 40960, 37967, 16855], [41325, 40441, 34300, 16897], [41747, 41077, 38729, 18344],
	[42378, 41164, 33843, 11810], [42991, 41881, 37741, 1189], [44567, 43380, 43142, 0], [46174, 43907, 39977, 0], [48668, 49172, 52265, 54600],
	[43899, 43036, 42362, 45081], [42572, 40168, 33331, 31747], [42627, 39691, 33586, 28459], [42918, 41823, 28412, 28134], [43106, 43230, 40753, 30834],
	[42570, 42724, 42071, 13604], [42413, 42168, 33810, 13910], [42290, 42615, 40799, 17097], [42116, 42630, 40549, 18583], [41939, 41830, 40897, 38905],
	[41262, 41494, 41594, 41579], [40831, 41024, 41445, 41933], [40482, 40491, 40655, 41653], [40161, 40081, 40801, 42291], [39862, 40124, 40608, 41057],
	[39431, 39080, 37972, 41340], [39100, 38513, 36039, 20892], [38799, 38684, 37185, 476], [38470, 38564, 37581, 259], [38288, 37966, 37315, 34865],
	[37676, 37758, 37605, 37746], [36887, 36671, 36390, 36492], [36497, 36637, 36301, 36537], [36166, 36371, 36087, 36431], [35897, 35807, 36066, 36151],
	[35469, 35192, 34507, 35742], [35056, 34981, 33928, 37137], [34843, 34817, 34609, 34790], [34438, 34125, 33998, 36373], [34168, 34339, 32918, 36635],
	[33797, 33729, 33368, 35437], [33425, 33268, 32096, 36059], [33095, 32638, 31928, 35384], [32847, 32351, 30288, 35068], [32562, 32500, 31070, 36552],
	[32257, 31927, 31722, 37978], [31947, 31011, 25759, 45684], [31706, 30928, 25300, 61841], [31710, 31216, 30289, 0], [31538, 31565, 29461, 0],
	[31257, 31281, 31746, 32319], [29670, 29460, 28874, 29450], [29369, 29208, 27419, 24742], [29230, 28803, 28268, 25385], [29036, 28707, 26360, 23130],
	[28936, 28855, 28136, 23947], [28557, 28572, 30140, 19546], [28375, 28581, 31050, 22342], [28010, 27400, 27084, 23674], [27762, 27224, 22342, 24104],
	[27486, 27351, 27174, 27943], [26792, 26750, 25892, 28057], [26388, 25834, 22857, 25282], [26138, 26408, 26193, 24971], [25793, 25558, 23700, 25973],
	[25635, 25650, 25918, 25879], [25259, 24691, 23511, 23823], [25008, 23937, 16500, 5951], [24792, 24321, 21969, 804], [24574, 24546, 22844, 469],
	[24456, 24413, 23673, 23781], [23912, 23596, 23390, 24392], [23511, 22534, 17932, 16554], [23434, 22867, 21122, 16569], [23383, 22473, 16934, 15762],
	[23243, 22562, 17710, 16553], [23148, 23094, 22527, 17106], [22848, 22319, 16621, 14356], [22616, 22164, 18347, 13264], [22420, 22134, 20610, 13428],
	[22142, 21859, 21083, 15017], [22124, 21631, 21332, 22772], [21918, 20727, 15578, 12900], [21963, 21233, 16761, 7884], [21917, 21567, 18986, 6342],
	[21840, 21087, 15491, 5756], [21979, 21346, 18489, 6231], [22332, 21668, 16274, 4338], [22690, 22079, 18935, 919], [23346, 23161, 22910, 76],
	[23958, 23188, 22918, 0], [24715, 24825, 25998, 28055], [22438, 20708, 17723, 19505], [22277, 20763, 13867, 11526], [22256, 21383, 19466, 11099],
	[22384, 21943, 16373, 12076], [22624, 22439, 21050, 12706], [22376, 22239, 21346, 2114], [22124, 21559, 18605, 1867], [22011, 22292, 21311, 3101],
	[21879, 21709, 18997, 5211], [21563, 21738, 20727, 19045], [20881, 20712, 20123, 20248], [20521, 20110, 19790, 21237], [20281, 20130, 19600, 21060],
	[19951, 19707, 15343, 22129], [19746, 19555, 19369, 21612], [19281, 18611, 17108, 16507], [19015, 18498, 11681, 9642], [18781, 18538, 17283, 522],
	[18512, 18322, 18820, 271], [18410, 18163, 17387, 16683], [17650, 17395, 16911, 19458], [17012, 16464, 12874, 15093], [16907, 16659, 15755, 13739],
	[16635, 16364, 14259, 14498], [16462, 16738, 16072, 15199], [16147, 16195, 16660, 14320], [15878, 15612, 13250, 17518], [15674, 15709, 14282, 18763],
	[15445, 14712, 13831, 18634], [15403, 15441, 15422, 20149], [14983, 14965, 14820, 15431], [14551, 14299, 12827, 9319], [14361, 13956, 12204, 7328],
	[14351, 13942, 11386, 4780], [14301, 13546, 9493, 5430], [14206, 13745, 14234, 3620], [14257, 13783, 12435, 1096], [14356, 13395, 12516, 0],
	[14787, 14257, 14047, 0], [15094, 14195, 12926, 0], [15031, 15050, 15495, 14959], [13783, 13117, 11425, 11324], [13548, 13069, 9884, 8879],
	[13370, 13126, 11136, 8263], [13307, 13526, 10742, 9307], [13450, 13130, 12510, 11297], [13092, 13228, 10864, 3285], [12926, 13153, 9359, 4957],
	[12707, 12153, 11389, 6149], [12488, 12205, 11588, 6305], [12328, 12002, 13955, 14485], [11977, 11635, 11224, 10754], [11790, 11879, 11317, 5071],
	[11502, 11963, 11900, 10106], [11315, 11867, 12371, 1671], [11056, 10854, 10443, 1360], [11004, 10888, 9255, 902], [10984, 10333, 7774, 489],
	[10793, 10912, 11286, 207], [10795, 10656, 10077, 0], [11235, 11403, 10580, 8376], [11536, 11810, 11709, 12731], [11307, 10470, 4110, 4868],
	[11283, 10723, 8666, 2062], [11089, 10961, 7389, 1836], [11060, 10788, 6461, 2196], [10834, 11257, 11356, 1578], [10815, 11184, 8013, 1036],
	[10848, 10828, 11544, 629], [10915, 10415, 11164, 324], [11114, 11173, 12166, 10255], [12061, 10404, 8582, 6248], [12803, 11076, 2020, 1518],
	[13502, 12609, 3556, 630], [14207, 12098, 8678, 439], [15571, 13578, 3610, 202], [19888, 18517, 17707, 70], [24484, 25774, 25415, 11],
	[27960, 27218, 34952, 0], [30963, 29558, 37019, 0], [36258, 27828, 54378, 0], [46259, 49450, 58436, 57378], [36526, 37925, 36986, 34592],
	[32695, 27848, 15226, 1467], [32782, 28024, 8977, 1183], [32407, 30444, 850, 850], [31690, 30819, 27386, 474], [32094, 28349, 23710, 288],
	[32939, 32139, 25912, 33], [33829, 35633, 40373, 0], [33382, 34225, 40927, 0], [32564, 32855, 30653, 35285], [32117, 32163, 33114, 38771],
	[32045, 34206, 33405, 38473], [31749, 34171, 35831, 37025], [31371, 33128, 54287, 12595], [30946, 31289, 32620, 0], [30115, 27244, 23697, 0],
	[30037, 29837, 24476, 0], [29865, 30715, 29916, 0], [29205, 28867, 50437, 0], [29161, 30133, 35442, 35589], [28146, 26239, 27060, 22145],
	[26993, 26404, 27819, 21782], [26803, 26669, 27704, 25034], [26304, 26809, 26903, 24374], [26059, 27507, 27145, 27551], [25562, 26325, 26322, 27914],
	[24838, 26020, 29691, 40427], [24786, 24926, 28735, 51785], [24480, 23582, 23514, 51616], [23992, 24228, 23572, 0], [23708, 21801, 23960, 24608],
	[24228, 23685, 21536, 26244], [23522, 23318, 19851, 15709], [23310, 23440, 22700, 18998], [22884, 24440, 20467, 18430], [22275, 23647, 24141, 18005],
	[22604, 23423, 26851, 0], [21875, 21728, 22709, 0], [21304, 22165, 22263, 0], [21505, 19433, 19998, 0], [20645, 20190, 19464, 24303],
	[17663, 18664, 11237, 12867], [17254, 15936, 10477, 13216], [17144, 14916, 10368, 9249], [17570, 17276, 8162, 6629], [18088, 18444, 16280, 7030],
	[17947, 17215, 17878, 25], [17687, 19090, 24519, 0], [17619, 15997, 9551, 0], [17406, 19213, 1592, 0], [17194, 16343, 20762, 30143],
	[17570, 15002, 14260, 11862], [16873, 17529, 15214, 20824], [16234, 15484, 16176, 2939], [16089, 17784, 10078, 11548], [15983, 15741, 14959, 0],
	[15292, 16830, 20912, 0], [15283, 12822, 5618, 0], [15270, 15212, 7861, 0], [15016, 15273, 13637, 0], [14647, 14732, 15635, 7549],
	[15270, 14756, 12405, 14482], [14802, 15608, 5556, 5150], [14194, 15417, 14239, 4628], [14149, 12756, 13894, 4447], [13812, 14041, 7226, 4165],
	[13179, 13516, 15848, 2888], [12767, 13120, 0, 0], [12371, 12126, 6864, 0], [12178, 10991, 3380, 0], [12199, 12154, 6670, 3855],
	[12741, 14149, 18310, 19847], [13553, 14290, 10164, 10164], [13259, 11965, 6379, 660], [12868, 9936, 2982, 296], [12710, 11990, 639, 100],
	[13832, 13347, 9752, 0], [14600, 15222, 7439, 0], [14381, 12078, 7886, 0], [16801, 20035, 26273, 0], [17064, 15543, 0, 0],
	[20775, 20557, 23470, 30587], [19998, 17780, 13761, 9858], [19599, 17769, 5399, 668], [19953, 17246, 14089, 317], [20186, 19048, 85, 85],
	[23528, 23926, 18212, 0], [23206, 24968, 30365, 0], [23047, 21326, 15411, 0], [23328, 26222, 22858, 0], [22751, 23247, 0, 0],
	[21957, 21162, 19672, 19814], [20952, 18522, 0, 0], [21035, 18627, 0, 0], [20789, 19818, 20488, 0], [20388, 23074, 12041, 0],
	[20314, 19448, 23605, 0], [19544, 18237, 14275, 0], [19112, 16239, 11943, 0], [18892, 17847, 13705, 0], [18443, 18093, 0, 0],
	[17996, 16238, 20967, 26858], [16989, 15846, 15038, 16227], [15570, 15074, 0, 0], [15329, 15906, 14212, 0], [15300, 9536, 7935, 0],
	[14766, 12419, 9483, 0], [14788, 16261, 18361, 0], [14059, 12657, 11212, 0], [13927, 14390, 9578, 0], [13572, 12419, 7029, 0],
	[13518, 14511, 0, 0], [12586, 10620, 10422, 14464], [12097, 11857, 4797, 2672], [11683, 9919, 6120, 4517], [11480, 10698, 12716, 0],
	[10740, 13018, 0, 0], [11188, 11054, 6271, 0], [10218, 9641, 2779, 0], [10297, 10276, 3338, 0], [12617, 13012, 12245, 0],
	[12741, 10393, 20003, 0], [10645, 9760, 10313, 9533], [9547, 9514, 995, 995], [8926, 7603, 5862, 633], [8677, 6938, 5667, 368],
	[8628, 8090, 4438, 129], [11936, 11914, 11660, 2], [12057, 11012, 0, 0], [11863, 12716, 13624, 0], [11559, 12200, 11566, 0],
	[10989, 10234, 0, 0], [10734, 10408, 12736, 12520], [9973, 9140, 8378, 8290], [9560, 9130, 0, 0], [9145, 8401, 7441, 0],
	[8880, 10133, 7090, 0], [8566, 7764, 8840, 0], [8144, 8717, 0, 0], [7766, 8487, 0, 0], [7449, 7554, 8919, 0],
	[7239, 6758, 9383, 0], [7214, 6791, 8817, 0], [5418, 5285, 5423, 4859], [4585, 5552, 0, 0], [4405, 3999, 6276, 0],
	[3939, 4282, 2182, 0], [3607, 3466, 1540, 0], [3249, 2515, 1675, 0], [3103, 3103, 1093, 0], [2547, 2310, 974, 0],
	[2290, 2331, 422, 0], [2497, 3572, 3753, 3496], [3024, 3085, 3477, 3477], [2676, 2720, 0, 0], [2357, 2360, 2364, 0],
	[2069, 2063, 0, 0], [1801, 1815, 1635, 0], [1410, 1410, 1410, 0], [1150, 1150, 1150, 0], [738, 906, 906, 0],
	[284, 365, 0, 0], [69, 39, 0, 0]])

close("all")
figure("Speed2048 - analyze test2", figsize=(16,9))

plot(analyze_value, analyze_score, label="score")
legend(loc="upper right")
xlabel("Board value")
ylabel("Score")
grid()

tight_layout()
show()
