import metadict

import piig as g


# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-statements
def haas_names(dst):
    dst.NAME = "HAAS NGC"
    dst.ORIGIN = [0, 0, 0]

    dst.NO_SKIP = "M78"
    dst.MUST_SKIP = "M79"
    dst.FEED_FAST = 650.0
    dst.FEED_SLOW = 50.0
    dst.PROBE_FAST = 50.0
    dst.PROBE_SLOW = 10.0

    dst.PROBE_H = g.Fixed[3](addr=2001)

    dst.PROBE_ON = "G65 P9832"
    dst.NO_LOOKAHEAD = ["G103 P1", "G04 P1", "G04 P1", "G04 P1"]

    # MACHINE GEN BELOW
    dst.NULL = g.FixedFloat(addr=0)
    dst.MACRO_ARGUMENTS = g.Fixed[33](addr=1)
    # 34 .. 99 - ..
    dst.GP_SAVED1 = g.Fixed[100](addr=100)
    # 200 .. 499 - ..
    dst.GP_SAVED2 = g.Fixed[50](addr=500)
    dst.PROBE_CALIBRATION1 = g.Fixed[6](addr=550)
    dst.PROBE_R = g.Fixed[3](addr=556)
    dst.PROBE_CALIBRATION2 = g.Fixed[22](addr=559)
    dst.GP_SAVED3 = g.Fixed[119](addr=581)
    # 700 .. 799 - ..
    dst.GP_SAVED4 = g.Fixed[200](addr=800)
    dst.INPUTS = g.Fixed[64](addr=1000)
    dst.MAX_LOADS_XYZAB = g.Fixed[5](addr=1064)
    # 1069 .. 1079 - ..
    dst.RAW_ANALOG = g.Fixed[10](addr=1080)
    dst.FILTERED_ANALOG = g.Fixed[8](addr=1090)
    dst.SPINDLE_LOAD = g.FixedFloat(addr=1098)
    # 1099 .. 1263 - ..
    dst.MAX_LOADS_CTUVW = g.Fixed[5](addr=1264)
    # 1269 .. 1600 - ..
    dst.TOOL_TBL_FLUTES = g.ToolTable[200](addr=1601)
    dst.TOOL_TBL_VIBRATION = g.ToolTable[200](addr=1801)
    dst.TOOL_TBL_OFFSETS = g.ToolTable[200](addr=2001)
    dst.TOOL_TBL_WEAR = g.ToolTable[200](addr=2201)
    dst.TOOL_TBL_DROFFSET = g.ToolTable[200](addr=2401)
    dst.TOOL_TBL_DRWEAR = g.ToolTable[200](addr=2601)
    # 2801 .. 2999 - ..
    dst.ALARM = g.FixedInt(addr=3000)
    dst.T_MS = g.FixedTime(addr=3001)
    dst.T_HR = g.FixedTime(addr=3002)
    dst.SINGLE_BLOCK_OFF = g.FixedInt(addr=3003)
    dst.FEED_HOLD_OFF = g.FixedInt(addr=3004)
    # 3005 .. 3005 - ..
    dst.STOP_WITH_MESSAGE = g.FixedInt(addr=3006)
    # 3007 .. 3010 - ..
    dst.YEAR_MONTH_DAY = g.FixedTime(addr=3011)
    dst.HOUR_MINUTE_SECOND = g.FixedTime(addr=3012)
    # 3013 .. 3019 - ..
    dst.POWER_ON_TIME = g.FixedTime(addr=3020)
    dst.CYCLE_START_TIME = g.FixedTime(addr=3021)
    dst.FEED_TIMER = g.FixedTime(addr=3022)
    dst.CUR_PART_TIMER = g.FixedTime(addr=3023)
    dst.LAST_COMPLETE_PART_TIMER = g.FixedTime(addr=3024)
    dst.LAST_PART_TIMER = g.FixedTime(addr=3025)
    dst.TOOL_IN_SPIDLE = g.FixedInt(addr=3026)
    dst.SPINDLE_RPM = g.FixedInt(addr=3027)
    dst.PALLET_LOADED = g.FixedInt(addr=3028)
    # 3029 .. 3029 - ..
    dst.SINGLE_BLOCK = g.FixedInt(addr=3030)
    dst.AGAP = g.FixedFloat(addr=3031)
    dst.BLOCK_DELETE = g.FixedInt(addr=3032)
    dst.OPT_STOP = g.FixedInt(addr=3033)
    # 3034 .. 3195 - ..
    dst.TIMER_CELL_SAFE = g.FixedTime(addr=3196)
    # 3197 .. 3200 - ..
    dst.TOOL_TBL_DIAMETER = g.ToolTable[200](addr=3201)
    dst.TOOL_TBL_COOLANT_POSITION = g.ToolTable[200](addr=3401)
    # 3601 .. 3900 - ..
    dst.M30_COUNT1 = g.FixedInt(addr=3901)
    dst.M30_COUNT2 = g.FixedInt(addr=3902)
    # 3903 .. 4000 - ..
    dst.LAST_BLOCK_G = g.Fixed[21](addr=4001)
    # 4022 .. 4100 - ..
    dst.LAST_BLOCK_ADDRESS = g.Fixed[26](addr=4101)
    # 4127 .. 5000 - ..
    dst.LAST_TARGET_POS = g.CWCPos[20](addr=5001)
    dst.MACHINE_POS = g.MachinePos[20](addr=5021)
    dst.WORK_POS = g.CWCPos[20](addr=5041)
    dst.SKIP_POS = g.CWCPos[20](addr=5061)
    dst.TOOL_OFFSET = g.Fixed[20](addr=5081)
    # 5101 .. 5200 - ..
    dst.G52 = g.WorkOffsetTable(addr=5201)
    dst.G54 = g.WorkOffsetTable(addr=5221)
    dst.G55 = g.WorkOffsetTable(addr=5241)
    dst.G56 = g.WorkOffsetTable(addr=5261)
    dst.G57 = g.WorkOffsetTable(addr=5281)
    dst.G58 = g.WorkOffsetTable(addr=5301)
    dst.G59 = g.WorkOffsetTable(addr=5321)
    # 5341 .. 5400 - ..
    dst.TOOL_TBL_FEED_TIMERS = g.ToolTable[100](addr=5401)
    dst.TOOL_TBL_TOTAL_TIMERS = g.ToolTable[100](addr=5501)
    dst.TOOL_TBL_LIFE_LIMITS = g.ToolTable[100](addr=5601)
    dst.TOOL_TBL_LIFE_COUNTERS = g.ToolTable[100](addr=5701)
    dst.TOOL_TBL_LIFE_MAX_LOADS = g.ToolTable[100](addr=5801)
    dst.TOOL_TBL_LIFE_LOAD_LIMITS = g.ToolTable[100](addr=5901)
    # 6001 .. 6197 - ..
    dst.NGC_CF = g.FixedInt(addr=6198)
    # 6199 .. 7000 - ..
    dst.G154_P1 = g.WorkOffsetTable(addr=7001)
    dst.G154_P2 = g.WorkOffsetTable(addr=7021)
    dst.G154_P3 = g.WorkOffsetTable(addr=7041)
    dst.G154_P4 = g.WorkOffsetTable(addr=7061)
    dst.G154_P5 = g.WorkOffsetTable(addr=7081)
    dst.G154_P6 = g.WorkOffsetTable(addr=7101)
    dst.G154_P7 = g.WorkOffsetTable(addr=7121)
    dst.G154_P8 = g.WorkOffsetTable(addr=7141)
    dst.G154_P9 = g.WorkOffsetTable(addr=7161)
    dst.G154_P10 = g.WorkOffsetTable(addr=7181)
    dst.G154_P11 = g.WorkOffsetTable(addr=7201)
    dst.G154_P12 = g.WorkOffsetTable(addr=7221)
    dst.G154_P13 = g.WorkOffsetTable(addr=7241)
    dst.G154_P14 = g.WorkOffsetTable(addr=7261)
    dst.G154_P15 = g.WorkOffsetTable(addr=7281)
    dst.G154_P16 = g.WorkOffsetTable(addr=7301)
    dst.G154_P17 = g.WorkOffsetTable(addr=7321)
    dst.G154_P18 = g.WorkOffsetTable(addr=7341)
    dst.G154_P19 = g.WorkOffsetTable(addr=7361)
    dst.G154_P20 = g.WorkOffsetTable(addr=7381)
    # 7401 .. 7500 - ..
    # 7501 .. 7600 PALLET_PRIORITY ..
    # 7601 .. 7700 PALLET_STATUS ..
    # 7701 .. 7800 PALLET_PROGRAM ..
    # 7801 .. 7900 PALLET_USAGE ..
    # 7901 .. 8499 - ..
    dst.ATM_ID = g.FixedInt(addr=8500)
    dst.ATM_PERCENT = g.FixedPercent(addr=8501)
    dst.ATM_TOTAL_AVL_USAGE = g.FixedInt(addr=8502)
    dst.ATM_TOTAL_AVL_HOLE_COUNT = g.FixedInt(addr=8503)
    dst.ATM_TOTAL_AVL_FEED_TIME = g.FixedSecs(addr=8504)
    dst.ATM_TOTAL_AVL_TOTAL_TIME = g.FixedSecs(addr=8505)
    # 8506 .. 8509 - ..
    dst.ATM_NEXT_TOOL_NUMBER = g.FixedInt(addr=8510)
    dst.ATM_NEXT_TOOL_LIFE = g.FixedPercent(addr=8511)
    dst.ATM_NEXT_TOOL_AVL_USAGE = g.FixedInt(addr=8512)
    dst.ATM_NEXT_TOOL_HOLE_COUNT = g.FixedInt(addr=8513)
    dst.ATM_NEXT_TOOL_FEED_TIME = g.FixedSecs(addr=8514)
    dst.ATM_NEXT_TOOL_TOTAL_TIME = g.FixedSecs(addr=8515)
    # 8516 .. 8549 - ..
    dst.TOOL_ID = g.FixedInt(addr=8550)
    dst.TOOL_FLUTES = g.FixedInt(addr=8551)
    dst.TOOL_MAX_VIBRATION = g.FixedFloat(addr=8552)
    dst.TOOL_LENGTH_OFFSETS = g.FixedFloat(addr=8553)
    dst.TOOL_LENGTH_WEAR = g.FixedFloat(addr=8554)
    dst.TOOL_DIAMETER_OFFSETS = g.FixedFloat(addr=8555)
    dst.TOOL_DIAMETER_WEAR = g.FixedFloat(addr=8556)
    dst.TOOL_ACTUAL_DIAMETER = g.FixedFloat(addr=8557)
    dst.TOOL_COOLANT_POSITION = g.FixedInt(addr=8558)
    dst.TOOL_FEED_TIMER = g.FixedSecs(addr=8559)
    dst.TOOL_TOTAL_TIMER = g.FixedSecs(addr=8560)
    dst.TOOL_LIFE_LIMIT = g.FixedFloat(addr=8561)
    dst.TOOL_LIFE_COUNTER = g.FixedFloat(addr=8562)
    dst.TOOL_LIFE_MAX_LOAD = g.FixedFloat(addr=8563)
    dst.TOOL_LIFE_LOAD_LIMIT = g.FixedFloat(addr=8564)
    # 8565 .. 8999 - ..
    dst.THERMAL_COMP_ACC = g.FixedFloat(addr=9000)
    # 9001 .. 9015 - ..
    dst.THERMAL_SPINDLE_COMP_ACC = g.FixedFloat(addr=9016)
    # 9017 .. 9999 - ..
    dst.GVARIABLES3 = g.Fixed[1000](addr=10000)
    dst.INPUTS = g.Fixed[256](addr=11000)
    # 11256 .. 11999 - ..
    dst.OUTPUT = g.Fixed[256](addr=12000)
    # 12256 .. 12999 - ..
    dst.FILTERED_ANALOG = g.Fixed[13](addr=13000)
    dst.COOLANT_LEVEL = g.FixedFloat(addr=13013)
    dst.FILTERED_ANALOG = g.Fixed[50](addr=13014)
    # 13064 .. 13999 - ..
    dst.SETTING = g.Fixed[10000](addr=20000)
    dst.PARAMETER = g.Fixed[10000](addr=30000)
    dst.TOOL_TYP = g.Fixed[200](addr=50001)
    dst.TOOL_MATERIAL = g.Fixed[200](addr=50201)
    # 50401 .. 101000 - ..
    # 51001 .. 102300 - ..
    dst.CURRENT_OFFSET = g.Fixed[200](addr=50601)
    dst.CURRENT_OFFSET2 = g.Fixed[200](addr=50801)
    dst.VPS_TEMPLATE_OFFSET = g.Fixed[100](addr=51301)
    dst.WORK_MATERIAL = g.Fixed[200](addr=51401)
    dst.VPS_FEEDRATE = g.Fixed[200](addr=51601)
    dst.APPROX_LENGTH = g.Fixed[200](addr=51801)
    dst.APPROX_DIAMETER = g.Fixed[200](addr=52001)
    dst.EDGE_MEASURE_HEIGHT = g.Fixed[200](addr=52201)
    dst.TOOL_TOLERANCE = g.Fixed[200](addr=52401)
    dst.PROBE_TYPE = g.Fixed[200](addr=52601)
    dst.PROBE = dst.SKIP_POS
    dst.WORK = dst.WORK_POS
    dst.MACHINE = dst.MACHINE_POS
    dst.G53 = dst.MACHINE_POS
    # MACHINE GEN ABOVE
    return dst
