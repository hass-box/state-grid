_Ay='%Y-%m-%d %H:%M:%S'
_Ax='month_ele_type'
_Aw='month_meter_num'
_Av='get_door_ladder_api'
_Au='queryDate'
_At='queryYear'
_As='access_token'
_Ar='businessType'
_Aq='qrCodeSerial'
_Ap='redirect_url'
_Ao='_access_token'
_An='dataVersion'
_Am='refresh_interval'
_Al='doorAccountDict'
_Ak='refreshToken'
_Aj='accessToken'
_Ai='/osg-web0004/member/c24/f01'
_Ah='BCP_00026'
_Ag='serviceCode_smt'
_Af='WEBA10070900'
_Ae='serviceType'
_Ad='jM_custType'
_Ac='jM_busiTypeCode'
_Ab='doorNumberManeger'
_Aa='constType'
_AZ='provinceCode'
_AY='elecTypeCode'
_AX='powerUserList'
_AW='publicKey'
_AV='WEBA10070800'
_AU='timeDay'
_AT='WEBA10070700'
_AS='channelNo'
_AR='yearTotalCost'
_AQ='provinceId'
_AP='proCode'
_AO='userAccountId'
_AN='0000'
_AM='refresh_token'
_AL='skey'
_AK='userInfo'
_AJ='0101046'
_AI='consType'
_AH='loginAccount'
_AG='keyCode'
_AF='querytypeCode'
_AE='01010049'
_AD='account'
_AC='daily_bill_list'
_AB='month_ele_num'
_AA='userName'
_A9='acctId'
_A8='resultCode'
_A7='quInfo'
_A6='BCP_000026'
_A5='app'
_A4='WEBALIPAY_01'
_A3='order'
_A2='state_grid'
_A1='month_t_ele_num'
_A0='month_n_ele_num'
_z='month_v_ele_num'
_y='month_p_ele_num'
_x='month'
_w='list'
_v='authFlag'
_u='09'
_t='0101183'
_s='latestBillMonth'
_r='consNo'
_q='token'
_p='0101154'
_o='getday'
_n='monthBillList'
_m='bizrt'
_l='account_balance'
_k='timestamp'
_j='consNo_dst'
_i='errmsg'
_h=True
_g=False
_f='clearCache'
_e='promotCode'
_d='01'
_c='SGAPP'
_b='devciceId'
_a='devciceIp'
_Z='orgNo'
_Y='tenant'
_X='member'
_W='stepelect'
_V='month_ele'
_U='proNo'
_T='promotType'
_S='target'
_R='userId'
_Q='srvrt'
_P='subBusiTypeCode'
_O='serCat'
_N='serialNo'
_M='0902'
_L='srvCode'
_K='uscInfo'
_J='busiTypeCode'
_I='channelCode'
_H='code'
_G=None
_F='1'
_E='source'
_D='funcCode'
_C='serviceCode'
_B='errcode'
_A='data'
import json,time,aiohttp,urllib.parse,datetime
from.const import VERSION
from.utils.logger import LOGGER
from.utils.store import async_save_to_store
from.utils.crypt import a,b,c,d,e
from homeassistant.components import persistent_notification
configuration={_K:{_X:_M,_a:'',_b:'',_Y:_A2},_E:_c,_S:'32101',_I:_M,_AS:_M,'toPublish':_d,'siteId':'2012000000033700',_L:'',_N:'',_D:'',_C:{_A3:_p,'uploadPic':'0101296','pauseSCode':'0101250','pauseTCode':'0101251','listconsumers':'0101093','messageList':'0101343','submit':'0101003','sbcMsg':'0101210','powercut':'0104514','BkAuth01':'f15','BkAuth02':'f18','BkAuth03':'f02','BkAuth04':'f17','BkAuth05':'f05','BkAuth06':'f16','BkAuth07':'f01','BkAuth08':'f03'},'electricityArchives':{'servicecode':'0104505',_E:_M},'subscriptionList':{_L:'APP_SGPMS_05_030',_N:'22',_I:_M,_D:'22',_S:'-1'},'userInformation':{_C:'01008183',_E:_c},'userInform':{_C:_t,_E:_c},'elesum':{_I:_M,_D:_A4,_e:_F,_T:_F,_C:'0101143',_E:_A5},_AD:{_I:_M,_D:'WEBA1007200'},_Ab:{_E:_M,_S:'-1',_I:_u,_AS:_u,_C:_AE,_D:'WEBA40050000',_K:{_X:_M,_a:'',_b:'',_Y:_A2}},'doorAuth':{_E:_c,_C:'f04'},'xinZ':{_O:'101',_Ac:'101','fJ_busiTypeCode':'102',_Ad:'03','fJ_custType':'02',_Ae:_d,_P:'',_D:_AT,_A3:_p,_E:_c,_AF:_F},'onedo':{_C:_AJ,_E:_c,_D:_AT,'queryType':'03'},'xinHuTongDian':{_O:'110',_J:'211',_P:'21102',_D:'WEBA10071200',_I:_M,_E:_u,_C:_t},'company':{_O:'104',_D:_AT,_Ae:'02',_AF:_F,_v:_F,_E:_c,_A3:_p},'charge':{_I:_u,_D:'WEBA10071300',_AS:'0901',_O:'102',_Ad:_d,_Ac:'102'},'other':{_I:_u,_D:'WEBA10079700',_O:'129',_J:'999',_P:'21501',_C:_A6,_L:'',_N:''},'vatchange':{'submit':'0101003',_J:'320',_P:'',_O:'115',_D:'WEBA10074000',_v:_F},'bill':{_f:_F,_D:_A4,_T:_F,_C:_A6},_W:{_I:_M,_D:_A4,_T:_F,_f:_u,_C:_A6,_E:_A5},_o:{_I:_M,_f:'11',_D:_A4,_e:_F,_T:_F,_C:_A6,_E:_A5},'mouthOut':{_I:_M,_f:'11',_D:_A4,_e:_F,_T:_F,_C:_A6,_E:_A5},'meter':{_O:'114',_J:'304',_D:'WEBA10071000',_P:'',_C:_AJ,_N:''},'complaint':{_J:'005','srvMode':_M,'anonymousFlag':'0','replyMode':_d,'retvisitFlag':_d},'report':{_J:'006'},'tradewinds':{_J:'019'},'somesay':{_J:'091'},'faultrepair':{_D:_Af,_C:_t,_O:'111',_J:'001',_P:'21505'},'electronicInvoice':{_O:'105',_J:'0'},'rename':{_C:_AJ,_D:'WEBA10076100',_J:'210',_O:'109',_v:_F,'gh_busiTypeCode':'211','gh_subusi':'21101',_N:'',_L:''},'pause':{_P:'',_C:_AE,_D:'WEBA10073600',_O:'107',_J:'203','jr_busi':'201',_N:'',_L:''},'capacityRecovery':{_C:_AE,_E:_c,_L:'',_N:'',_D:'WEBA10073700','busiTypeCode_stop':'204','busiTypeCode_less':'202',_J:'202',_P:'',_O:'108',_AU:'5',_v:_F},'electricityPriceChange':{_C:_t,_J:'215',_P:'21502',_O:'113',_v:_F,_AU:'15',_D:'WEBA10073900WEB',_L:'',_N:''},'electricityPriceStrategyChange':{_C:'01008183',_J:'215',_P:'21506',_O:'160',_D:'WEBV00000517WEB',_L:'',_N:''},'eemandValueAdjustment':{_C:_t,_L:'',_N:'',_O:'112',_D:'WEBA10073800',_J:'215',_P:'21504',_v:_F,_AU:'5','getMonthServiceCode':_AJ},'businessProgress':{_C:_t,_L:_d,_D:'WEB01'},'increase':{_E:_c,_N:'',_L:'',_Ag:_AE,_C:_p,_A3:_p,_D:_AV,_AF:_F,_O:'106',_J:'111',_P:''},'fjincrea':{_O:'105',_J:'110',_P:'',_E:_c,_D:_AV,_N:'',_L:'',_Ag:_AE,_C:_p,_A3:_p,_AF:_F},'persIncrea':{_O:'105',_J:'109',_A3:_p,_P:'',_E:_c,_D:_AV,_AF:_F},'fgdChange':{_C:_t,_L:_d,_I:_u,_D:_Af,_J:'215',_P:'21505',_O:'111',_v:_F},'createOrder':{_I:_M,_D:_A4,_L:'BCP_000001','chargeMode':'02','conType':_d,'bizTypeId':'BT_ELEC'},'largePopulation':{_J:'383',_D:'WEBA10076800',_P:'',_L:'',_T:'',_e:'',_I:'0901',_O:'383',_C:'',_N:''},'biaoJiCode':{_C:'0104507',_E:'1704',_I:'1704'},'twoGuar':{_J:'402',_P:'40201',_D:'web_twoGuar'},'electTrend':{_C:_Ah,_I:_M},'emergency':{_C:_Ah,_D:'A10000000',_I:_M},'infoPublic':{_C:'2545454',_E:_A5}}
appKey='3def6c365d284881bf1a9b2b502ee68c'
appSecret='ab7357dae64944a197ace37398897f64'
baseApi='https://www.95598.cn/api'
get_request_key_api='/oauth2/outer/c02/f02'
get_qr_code_api='/osg-open-uc0001/member/c8/f24'
get_qr_code_status_api='/osg-web0004/open/c50/f02'
get_qr_code_token_api='/osg-uc0013/member/c4/f04'
send_code_api='/osg-open-uc0001/member/c8/f04'
code_login_api='/osg-uc0013/member/c4/f02'
getCertificationApi='/osg-open-uc0001/member/c8/f11'
get_request_authorize_api='/oauth2/oauth/authorize'
get_web_token_api='/oauth2/outer/getWebToken'
refresh_web_token_api='/oauth2/outer/refresh_web_token'
get_door_number_api='/osg-open-uc0001/member/c9/f02'
get_door_balance_api='/osg-open-bc0001/member/c05/f01'
get_door_bill_api='/osg-open-bc0001/member/c01/f02'
get_door_ladder_api='/osg-open-bc0001/member/c04/f03'
getJiaoFeiRecordApi=_Ai
get_door_daily_bill_api=_Ai
sessionIdControlApiList=[get_qr_code_api,get_qr_code_status_api,get_qr_code_token_api,send_code_api,code_login_api]
keyCodeControlApiList=[get_qr_code_status_api,get_qr_code_token_api,send_code_api,code_login_api,getCertificationApi,get_request_authorize_api,get_web_token_api,refresh_web_token_api,get_door_number_api,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
authControlApiList=[get_door_number_api,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
tControlApiList=[getCertificationApi,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
def json_dumps(data):return json.dumps(data,separators=(',',':'),ensure_ascii=_g)
def normal_round(num,ndigits=0):
	A=ndigits
	if A==0:return int(num+.5)
	else:B=10**A;return int(num*B+.5)/B
def catchFloat(data,key):
	if key in data:
		try:return normal_round(float(data[key]),2)
		except:return 0
	else:return 0
def catchInt(data,key):
	if key in data:
		try:return normal_round(float(data[key]),0)
		except:return 0
	else:return 0
class StateGridDataClient:
	hass=_G;coordinator=_G;session=_G;dataVersion=_G;keyCode=_G;publicKey=_G;need_login=_g;retry_times=0;phone=_G;codeKey=_G;serialNo=_G;qrCodeSerial=_G;userInfo=_G;accountInfo=_G;powerUserList=_G;doorAccountDict={};cookie=[];timestamp=int(time.time()*1000);accessToken=_G;refreshToken=_G;token=_G;expirationDate=_G;refresh_interval=1;is_debug=_h;shown_notification=_g
	def __init__(A,hass,config=_G):
		B=config;A.hass=hass;C=aiohttp.TCPConnector(ssl=_g);D=aiohttp.CookieJar(quote_cookie=_h);A.session=aiohttp.ClientSession(cookie_jar=D,connector=C)
		if B is not _G:
			try:A.keyCode=B[_AG];A.publicKey=B[_AW];A.accessToken=B[_Aj];A.refreshToken=B[_Ak];A.token=B[_q];A.userInfo=B[_AK];A.powerUserList=B[_AX];A.doorAccountDict=B[_Al];A.refresh_interval=B[_Am];A.is_debug=B['is_debug'];A.dataVersion=B[_An]
			except Exception as E:LOGGER.error(E)
	async def save_data(B):A={};A[_AG]=B.keyCode;A[_AW]=B.publicKey;A[_Aj]=B.accessToken;A[_Ak]=B.refreshToken;A[_q]=B.token;A[_AK]=B.userInfo;A[_AX]=B.powerUserList;A[_Al]=B.doorAccountDict;A[_Am]=B.refresh_interval;A['is_debug']=B.is_debug;A[_An]=VERSION;await async_save_to_store(B.hass,'state_grid.config',A)
	def encrypt_post_data(A,data):B={_Ao:A.accessToken[len(A.accessToken)//2:]if A.accessToken else'','_t':A.token[len(A.token)//2:]if A.token else'','_data':data,_k:A.timestamp};return A.encrypt_wapper_data(B)
	def encrypt_wapper_data(A,data):B=a(json_dumps(data),A.keyCode);return{_A:B+c(B+str(A.timestamp)),_AL:d(A.keyCode,A.publicKey),_k:str(A.timestamp)}
	def handle_request_result_message(E,api,result):
		D='message';C='resultMessage';A=result
		if E.is_debug:LOGGER.error(api+'-'+json_dumps(A))
		B=_G
		if _A in A and _Q in A[_A]and C in A[_A][_Q]:B=A[_A][_Q][C]
		elif _Q in A and C in A[_Q]:B=A[_Q][C]
		elif D in A:B=A[D]
		else:B=json_dumps(A)
		return B
	async def __fetch_safe(C,api,data):
		B=await C.__fetch(api,data)
		if _H not in B:return B
		A=B[_H]
		if 10015==A or 10108==A or 10009==A or 10207==A or 10005==A or 10010==A or 30010==A or 10002==A:
			await C.__refresh_token()
			if C.need_login is _h:return B
			else:return await C.__fetch(api,data)
		else:return B
	async def __fetch(B,api,data,header=_G):
		T='encryptData';S='464606a4-184c-4beb-b442-2ab7761d0796';R='key_code';Q='state';P='sign';O='grant_type';N='application/json;charset=UTF-8';M='Content-Type';L=header;K='client_secret';I='client_id';E=api;B.timestamp=int(time.time()*1000);D=B.timestamp
		if B.keyCode is _G:B.keyCode=e(32,16,2)
		F=B.keyCode;G={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36','Accept':N,M:N,'version':'1.0',_E:'0901',_k:str(D),'wsgwType':'web','appKey':appKey};A=data
		if E==get_request_key_api:A={I:appKey,K:appSecret};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AL:d(F,'042BC7AD510BF9793B7744C8854C56A8C95DD1027EE619247A332EC6ED5B279F435A23D62441FE861F4B0C963347ECD5792F380B64CA084BE8BE41151F8B8D19C8'),I:appKey,_k:str(D)}
		elif E==get_qr_code_api:A={_Ao:'','_t':'','_data':A,_k:D}
		elif E==get_request_authorize_api:
			A={I:appKey,'response_type':_H,_Ap:'/test',_k:D,'rsi':B.token};A=urllib.parse.urlencode(A);G[M]='application/x-www-form-urlencoded; charset=UTF-8';G[_AG]=F
			async with B.session.post(baseApi+E,data=A,headers=G)as J:B.session.cookie_jar.update_cookies(J.cookies);C=await J.json();C=b(C[_A],B.token);C=json.loads(C);return C
		elif E==get_web_token_api:A={O:'authorization_code',P:c(appKey+str(D)),K:appSecret,Q:S,R:F,I:appKey,_k:D,_H:A[_H]};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AL:d(F,B.publicKey),_k:str(D)}
		elif E==refresh_web_token_api:A={O:_AM,P:c(appKey+str(D)),K:appSecret,Q:S,R:F,I:appKey,_k:D,_AM:B.refreshToken};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AL:d(F,B.publicKey),_k:str(D)};E=get_web_token_api
		else:A=B.encrypt_post_data(A)
		if L is not _G:G.update(L)
		if E in sessionIdControlApiList:G['sessionId']='web'+str(D)
		if E in keyCodeControlApiList:G[_AG]=F
		if E in authControlApiList:G['Authorization']='Bearer '+B.accessToken[:len(B.accessToken)//2]
		if E in tControlApiList:G['t']=B.token[:len(B.token)//2]
		async with B.session.post(baseApi+E,json=A,headers=G)as J:
			C=await J.text()
			if C.startswith('{'):
				C=json.loads(C)
				if T in C:C=b(C[T],F);C=json.loads(C)
			return C
	async def __get_request_key(A):
		A.keyCode=_G;B=await A.__fetch(get_request_key_api,{});C=A.handle_request_result_message('get_request_key_api',B)
		if B[_H]==_F:A.keyCode=B[_A][_AG];A.publicKey=B[_A][_AW];return{_B:0}
		return{_B:1,_i:C}
	async def __get_qr_code(B):
		C={_K:{_a:'',_Y:_A2,_X:_M,_b:''},_A7:{'optType':_d,_N:e(28,10,1)}};A=await B.__fetch(get_qr_code_api,C);D=B.handle_request_result_message('get_qr_code_api',A)
		if A[_H]==1:
			if A[_A]and A[_A][_Q]and A[_A][_Q][_A8]==_AN:B.qrCodeSerial=A[_A][_m][_Aq];E=A[_A][_m]['qrCode'];return{_B:0,_A:E}
		return{_B:1,_i:D}
	async def __get_qr_code_status(B):
		C={_m:{_Aq:B.qrCodeSerial}};D={_q:'98'+e(10,10,1)};A=await B.__fetch(get_qr_code_status_api,C,D);E=B.handle_request_result_message('get_qr_code_status_api',A)
		if _H in A and A[_H]==1:
			if _A in A and A[_A]!='null':B.token=A[_A];return{_B:0}
			else:return{_B:1,_i:'未使用网上国网 App 扫码或确认登录'}
		return{_B:1,_i:E}
	async def __get_qr_code_token(B):
		C={_K:{_Y:_A2,_X:_M,'isEncrypt':_h},_q:B.token};A=await B.__fetch(get_qr_code_token_api,C);D=B.handle_request_result_message('get_qr_code_token_api',A)
		if _Q in A and _A8 in A[_Q]and A[_Q][_A8]==_AN:B.userInfo=A[_m][_AK];return{_B:0}
		return{_B:1,_i:D}
	async def __send_code(B,phone):
		C=phone;B.phone=C;D={_K:{_a:'',_Y:_A2,_X:_M,_b:''},_A7:{'sendType':'0',_AD:C,_Ar:'login','accountType':''},'Channels':'web'};A=await B.__fetch(send_code_api,D);E=B.handle_request_result_message('send_code_api',A)
		if A[_H]==1:
			if A[_A]and A[_A][_Q]and A[_A][_Q][_A8]==_AN:B.codeKey=A[_A][_m]['codeKey'];return{_B:0}
		return{_B:1,_i:E}
	async def __verfiy_code(A,code):
		C={_K:{_a:'',_Y:_A2,_X:_M,_b:''},_A7:{_AD:A.phone,_Ar:'login',_H:code,'optSys':'ios','pushId':'00000','codeKey':A.codeKey},'Channels':'web'};B=await A.__fetch(code_login_api,C);D=A.handle_request_result_message('code_login_api',B)
		if _Q in B and _A8 in B[_Q]and B[_Q][_A8]==_AN:A.token=B[_m][_q];A.userInfo=B[_m][_AK][0];return{_B:0}
		return{_B:1,_i:D}
	async def __get_request_authorize(B):
		A=await B.__fetch(get_request_authorize_api,{});E=B.handle_request_result_message('get_request_authorize_api',A)
		if _H in A and A[_H]==_F:C=A[_A][_Ap];D=C.rfind('code=');B.authorizeCode=C[D+5:D+5+32];return{_B:0}
		return{_B:1,_i:E}
	async def __get_web_token(A):
		C={_H:A.authorizeCode};B=await A.__fetch(get_web_token_api,C);D=A.handle_request_result_message('get_web_token_api',B)
		if _H in B and B[_H]==_F:A.accessToken=B[_A][_As];A.refreshToken=B[_A][_AM];return{_B:0}
		return{_B:1,_i:D}
	async def __refresh_web_token(B):
		A=await B.__fetch(refresh_web_token_api,{});C=B.handle_request_result_message('refresh_web_token_api',A)
		if _H in A and A[_H]==_F:B.accessToken=A[_A][_As];B.refreshToken=A[_A][_AM];return{_B:0}
		return{_B:1,_i:C}
	async def __get_door_number(A):
		B=configuration[_Ab];G={_C:B[_C],_E:B[_E],_S:B[_S],_K:{_X:B[_K][_X],_a:B[_K][_a],_b:B[_K][_b],_Y:B[_K][_Y]},_A7:{_R:A.userInfo[_R]},_q:A.token};C=await A.__fetch_safe(get_door_number_api,G);H=A.handle_request_result_message('get_door_number_api',C)
		if _H in C and C[_H]==1 and _A in C and _m in C[_A]:
			E={}
			if A.powerUserList is not _G:E={A[_j]:A for A in A.powerUserList}
			F=[]
			for D in C[_A][_m][_AX]:
				if D[_j]in E:F.append(E[D[_j]])
				elif _AY in D and D[_AY]!='05':F.append(D)
			A.powerUserList=F;return{_B:0}
		return{_B:1,_i:H}
	async def __get_door_balance(B,door_account):
		A=door_account;E={_A:{_L:'',_N:'',_I:configuration[_AD][_I],_D:configuration[_AD][_D],_A9:B.userInfo[_R],_AA:B.userInfo.get(_AH,B.userInfo.get('nickname',_G)),_T:_F,_e:_F,_AO:B.userInfo[_R],_w:[{'consNoSrc':A[_j],_AP:A.get(_U,A.get(_AQ,_G)),'sceneType':A.get('consSortCode',A.get(_AY,_G)),_r:A[_r],_Z:A[_Z]}]},_C:'0101143',_E:configuration[_E],_S:A.get(_U,A.get(_AQ,_G))};C=await B.__fetch_safe(get_door_balance_api,E);B.handle_request_result_message('get_door_balance_api',C)
		if _H in C and C[_H]==1 and _A in C and _w in C[_A]:
			D=C[_A][_w]
			if len(D)!=0:A[_l]=D[0]
	async def __get_door_bill(C,door_account,monthDate):
		J='dataInfo';H='billYear';G='mothEleList';E=monthDate;A=door_account;K={_A:{_A9:C.userInfo[_R],_I:configuration[_I],_f:'11',_AI:A[_Aa],_D:'ALIPAY_01',_Z:A[_Z],_AP:A[_U],_e:_F,_T:_F,_N:'',_L:'',_AA:'',_AZ:A[_U],_AO:C.userInfo[_R],_r:A[_r],_At:E.year},_C:_A6,_E:_A5,_S:A[_U]};B=await C.__fetch_safe(get_door_bill_api,K);C.handle_request_result_message('get_door_bill_api',B)
		if _H in B and B[_H]==1 and _A in B:
			if J in B[_A]:A[_AR]=B[_A][J]
			if G in B[_A]:
				if H not in A or A[H]!=E.year:A[_n]=B[_A][G];A[H]=E.year
				else:
					F={A[_x]:A for A in A[_n]};I=B[_A][G]
					for D in I:
						if D[_x]in F and _V in F[D[_x]]:D[_V]=F[D[_x]][_V]
					A[_n]=I
				if len(A[_n])>0:A[_s]=A[_n][-1]
	async def __get_door_ladder(C,door_account,monthBill):
		E=monthBill;A=door_account;I=A[_j];F=datetime.datetime.strptime(E[_x],'%Y%m');G=f"{F.year}-{F.month:02d}";H={_A:{_I:configuration[_W][_I],_D:configuration[_W][_D],_T:configuration[_W][_T],_f:configuration[_W][_f],_r:A[_j],_e:A[_U],_Z:A[_Z],_Au:G,_AZ:A[_U],_AI:A[_Aa],_AO:C.userInfo[_R],_N:'',_L:'',_AA:C.userInfo[_AH],_A9:C.userInfo[_R]},_C:configuration[_W][_C],_E:configuration[_W][_E],_S:A[_U]};B=await C.__fetch(get_door_ladder_api,H);J=C.handle_request_result_message(_Av,B)
		if _H in B and B[_H]==1 and _A in B and _w in B[_A]:
			D=B[_A][_w]
			if len(D)!=0:D=D[0];E['ladder']=D
	async def __get_door_mouth_bill(K,door_account,monthBill):
		Y='elecType';X='billRead';S=monthBill;O='quantity';N='priceName';M='amtGroupList';J='readList';G=door_account;D='amtList';B='pointList';T=datetime.datetime.strptime(S[_x],'%Y%m');Z=f"{T.year}-{T.month:02d}";a={_A:{_I:configuration[_W][_I],_D:configuration[_W][_D],_T:configuration[_W][_T],_f:configuration[_W][_f],_r:G[_j],_e:G[_U],_Z:G[_Z],_Au:Z,_AZ:G[_U],_AI:G[_Aa],_AO:K.userInfo[_R],_N:'',_L:'',_AA:K.userInfo[_AH],_A9:K.userInfo[_R]},_C:configuration[_W][_C],_E:configuration[_W][_E],_S:G[_U]};H=await K.__fetch(get_door_ladder_api,a);b=K.handle_request_result_message(_Av,H)
		if _H in H and H[_H]==1 and _A in H and _w in H[_A]:
			A=H[_A][_w][0];P=0;U=0;V=0;Q=0;W=0;I=[]
			if J in A and len(A[J])>0:I=A[J]
			elif B in A and len(A[B])>0 and J in A[B][0]and len(A[B][0][J])>0:I=A[B][0][J]
			R=0
			if len(I)>0:
				P=catchFloat(I[0],'activeCount')
				if X in I[0]:
					for C in I[0][X]:R=max(R,catchInt(C,'currentNumber'))
			L=[]
			if D in A and len(A[D])>0:L=A[D]
			elif B in A and len(A[B])>0 and D in A[B][0]and len(A[B][0][D])>0:L=A[B][0][D]
			elif B in A and len(A[B])>0 and M in A[B][0]and len(A[B][0][M])>0 and D in A[B][0][M][0]and len(A[B][0][M][0][D])>0:L=A[B][0][M][0][D]
			F=0
			if len(L)>0 and P>0:
				for C in L:
					if C[N]=='峰':U=catchFloat(C,O);F=1
					elif C[N]=='谷':V=catchFloat(C,O);F=1
					elif C[N]=='尖':W=catchFloat(C,O);F=1
					elif C[N]=='平':Q=catchFloat(C,O)
					elif Y in C and C[Y]==_F:F=3
				if F==0 and Q!=0:F=2
			E={};E[_Aw]=R;E[_Ax]=F;E[_AB]=normal_round(P,2);E[_y]=normal_round(U,2);E[_z]=normal_round(V,2);E[_A0]=normal_round(Q,2);E[_A1]=normal_round(W,2);S[_V]=E
	async def __get_door_daily_bill(B,door_account,year,start_date,end_date):
		D='sevenEleList';A=door_account;E={'params1':{_C:configuration[_C],_E:configuration[_E],_S:configuration[_S],_K:{_X:configuration[_K][_X],_a:configuration[_K][_a],_b:configuration[_K][_b],_Y:configuration[_K][_Y]},_A7:{_R:B.userInfo[_R]},_q:B.token},'params3':{_A:{_A9:B.userInfo[_R],_r:A[_j],_AI:_d,'endTime':end_date,_Z:A[_Z],_At:year,_AP:A.get(_U,A.get(_AQ,_G)),_N:'',_L:'','startTime':start_date,_AA:B.userInfo[_AH],_D:configuration[_o][_D],_I:configuration[_o][_I],_f:configuration[_o][_f],_e:configuration[_o][_e],_T:configuration[_o][_T]},_C:configuration[_o][_C],_E:configuration[_o][_E],_S:A.get(_U,A.get(_AQ,_G))},'params4':'010103'};C=await B.__fetch_safe(get_door_daily_bill_api,E);F=B.handle_request_result_message('get_door_daily_bill_api',C)
		if _H in C and C[_H]==1 and _A in C and D in C[_A]:A[_AC]=C[_A][D]
	async def __get_door_pay_record(A,door_account):B=door_account;D=B[_j];C={'params1':{_C:configuration[_C],_E:configuration[_E],_S:configuration[_S],_K:{_X:configuration[_K][_X],_a:configuration[_K][_a],_b:configuration[_K][_b],_Y:configuration[_K][_Y]},_A7:{_R:A.userInfo[_R]},_q:A.token},'params3':{_A:{_A9:A.userInfo[_R],'bgnPayDate':'2023-04-24',_I:configuration[_I],_r:B[_j],'endPayDate':'2024-04-24',_D:'webALIPAY_01','number':100,_Z:B[_Z],'page':_F,_AP:B[_U],_e:_F,_T:_F,_N:'',_L:'',_AA:A.userInfo[_AH]},_C:'0101051',_E:_d,_S:B[_U]},'params4':'010104'};E=await A.__fetch(getJiaoFeiRecordApi,C)
	async def get_qr_code(B):
		A=await B.__get_request_key()
		if _B in A and A[_B]!=0:return A
		return await B.__get_qr_code()
	async def check_qr_code(B):
		A=await B.__get_qr_code_status()
		if _B in A and A[_B]!=0:return A
		A=await B.__get_qr_code_token()
		if _B in A and A[_B]!=0:return A
		return await B.__get_token()
	async def send_phone_code(B,phone):
		A=await B.__get_request_key()
		if _B in A and A[_B]!=0:return A
		return await B.__send_code(phone)
	async def verfiy_phone_code(B,code):
		A=await B.__verfiy_code(code)
		if _B in A and A[_B]!=0:return A
		return await B.__get_token()
	async def __get_token(B):
		A=await B.__get_request_key()
		if _B in A and A[_B]!=0:return A
		A=await B.__get_request_authorize()
		if _B in A and A[_B]!=0:return A
		A=await B.__get_web_token()
		if _B in A and A[_B]!=0:return A
		A=await B.__get_door_number()
		if _B in A and A[_B]!=0:return A
		B.need_login=_g;await B.save_data();return{_B:0,_A:B.powerUserList}
	async def __refresh_token(A):
		B=await A.__get_request_key()
		if _B in B and B[_B]!=0:return
		B=await A.__refresh_web_token()
		if _B in B and B[_B]==0:A.need_login=_g;A.shown_notification=_g;A.retry_times=0;await A.save_data()
		elif A.retry_times>=3:A.need_login=_h
		else:A.retry_times=A.retry_times+1
	def _show_token_notification(A):
		if A.shown_notification==_h:return
		A.shown_notification=_h;B=datetime.datetime.strftime(datetime.datetime.now(),_Ay);LOGGER.error('国家电网 - Token刷新失败，可在国家电网集成页面点击配置重新登录');persistent_notification.create(A.hass,'Token刷新失败，可在国家电网集成页面点击配置重新登录\n过期时间：'+B,title='国家电网')
	async def refresh_data(B,setup=_g,force_refresh=_g):
		A3='last_month_ele_cost';A2='year_ele_cost';A1='daily_ele_num';A0='thisTPq';z='thisNPq';y='thisVPq';x='thisPPq';w='%Y%m%d';v='day';u='daily_lasted_date';t='isMent';a=setup;Z='last_month_ele_num';Y='daily_t_ele_num';X='daily_n_ele_num';W='daily_v_ele_num';V='daily_p_ele_num';U='dayElePq';O='year_ele_num';G='balance'
		if a is _h:
			if B.dataVersion!=VERSION:B.powerUserList=_G
			b=await B.__get_door_number()
			if _B in b and b[_B]!=0:B.need_login=_h
		if B.need_login is _h:B._show_token_notification();return
		A4=a or force_refresh or int(time.time()*1000)-B.timestamp>B.refresh_interval*3600*1000
		if A4 is _g:return
		F=datetime.datetime.now();H=F-datetime.timedelta(days=1);A5=f"{H.year}-{H.month:02d}-{H.day:02d}";P=H-datetime.timedelta(days=40);A6=f"{P.year}-{P.month:02d}-{P.day:02d}"
		for A in B.powerUserList:
			A7=A[_j];B.doorAccountDict[A7]=A;await B.__get_door_balance(A)
			if B.retry_times!=0:return
			if _l in A:
				c=catchFloat(A[_l],'accountBalance');AB=catchFloat(A[_l],'estiAmt');AC=catchFloat(A[_l],'prepayBal');Q=catchFloat(A[_l],'sumMoney');AD=catchFloat(A[_l],'historyOwe');d=A[_l][_AI];e=''
				if t in A[_l]:e=A[_l][t]
				A8=d==_F;R=d=='0';f=not(not R or e!=_F)
				if A8:A[G]=Q
				if R and not f:A[G]=-abs(Q)
				if R and f:A[G]=Q
				if c!=0:A[G]=c
			else:LOGGER.error('国家电网账户余额获取失败！')
			if G not in A:A[G]=0
			await B.__get_door_daily_bill(A,F.year,A6,A5)
			if _AC not in A:LOGGER.error('国家电网无法获取日用电数据！');continue
			S=0;I=_g
			for g in range(10):
				D=A[_AC][g]
				try:float(D[U]);I=_h;break
				except:S=S+1
			h=0;i=0;j=0;k=0;l=0;A[u]=f"{F.year}-{F.month:02d}-{F.day:02d}"
			if I:
				for g in range(S):A[_AC].pop(0)
				D=A[_AC][0];E=datetime.datetime.strptime(D[v],w);A[u]=f"{E.year}-{E.month:02d}-{E.day:02d}";h=catchFloat(D,U);i=catchFloat(D,x);j=catchFloat(D,y);k=catchFloat(D,z);l=catchFloat(D,A0)
			A[A1]=normal_round(h,2);A[V]=normal_round(i,2);A[W]=normal_round(j,2);A[X]=normal_round(k,2);A[Y]=normal_round(l,2);m=0;n=0;o=0;p=0;q=0
			if I:
				for C in A[_AC]:
					A9=datetime.datetime.strptime(C[v],w)
					if A9.month!=E.month:break
					m+=catchFloat(C,U);n+=catchFloat(C,x);o+=catchFloat(C,y);p+=catchFloat(C,z);q+=catchFloat(C,A0)
			A[_AB]=normal_round(m,2);A[_y]=normal_round(n,2);A[_z]=normal_round(o,2);A[_A0]=normal_round(p,2);A[_A1]=normal_round(q,2)
			if I:
				AA=E-datetime.timedelta(days=E.day);await B.__get_door_bill(A,AA)
				if _n in A:
					for C in A[_n]:
						if _V not in C:await B.__get_door_mouth_bill(A,C)
			if _AR in A:A[O]=catchFloat(A[_AR],'totalEleNum');A[A2]=catchFloat(A[_AR],'totalEleCost')
			if O not in A:A[O]=0;A[A2]=0
			r=0;T=H
			if _s in A:
				A[Z]=catchFloat(A[_s],'monthEleNum');A[A3]=catchFloat(A[_s],'monthEleCost')
				if _V in A[_s]:
					r=A[_s][_V][_Aw];s=A[_s][_V][_Ax]
					if s==2:A[V]=0;A[W]=0;A[X]=A[A1];A[Y]=0;A[_y]=0;A[_z]=0;A[_A0]=A[_AB];A[_A1]=0
					elif s==3:A[V]=0;A[W]=0;A[X]=0;A[Y]=0;A[_y]=0;A[_z]=0;A[_A0]=0;A[_A1]=0
				T=datetime.datetime.strptime(A[_s][_x],'%Y%m')
			if Z not in A:A[Z]=0;A[A3]=0
			A['last_month_meter_num']=r;J=0;K=0;L=0;M=0;N=0
			if T.month==12:J=A[_AB];K=A[_y];L=A[_z];M=A[_A0];N=A[_A1]
			else:
				if _n in A:
					for C in A[_n]:
						if _V in C:J+=C[_V][_AB];K+=C[_V][_y];L+=C[_V][_z];M+=C[_V][_A0];N+=C[_V][_A1]
				if I and E.month!=T.month:J+=A[_AB];K+=A[_y];L+=A[_z];M+=A[_A0];N+=A[_A1]
			A[O]=normal_round(J,2);A['year_p_ele_num']=normal_round(K,2);A['year_v_ele_num']=normal_round(L,2);A['year_n_ele_num']=normal_round(M,2);A['year_t_ele_num']=normal_round(N,2);A['refresh_time']=datetime.datetime.strftime(F,_Ay)
		await B.save_data()
	def get_door_account_list(A):return list(A.doorAccountDict.values())
	def get_door_account(A):return A.doorAccountDict