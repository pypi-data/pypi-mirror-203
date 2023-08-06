from bfrac import bfrac

print("Hellow")

appconfig = bfrac.AppConfig("D:/PROJECTS/BFRAC/cj_config.ini")
#print(appconfig.get_key())

rac = bfrac.RiotAPICaller(appconfig)

qc = bfrac.QueryContext(rac)

qc.set_region_server("na1")

qc.get_summoner_by_name("deamonpog")

ml = qc.get_matches(5, "ranked")

qc.get_match_info(ml[0])
