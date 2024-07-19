_Aw='get_door_ladder_api'
_Av='queryDate'
_Au='queryYear'
_At='access_token'
_As='businessType'
_Ar='qrCodeSerial'
_Aq='redirect_url'
_Ap='_access_token'
_Ao='dataVersion'
_An='refresh_interval'
_Am='doorAccountDict'
_Al='refreshToken'
_Ak='accessToken'
_Aj='/osg-web0004/member/c24/f01'
_Ai='BCP_00026'
_Ah='serviceCode_smt'
_Ag='WEBA10070900'
_Af='serviceType'
_Ae='jM_custType'
_Ad='jM_busiTypeCode'
_Ac='doorNumberManeger'
_Ab='month_t_ele_num'
_Aa='month_n_ele_num'
_AZ='month_v_ele_num'
_AY='month_p_ele_num'
_AX='month_ele_num'
_AW='constType'
_AV='provinceCode'
_AU='elecTypeCode'
_AT='powerUserList'
_AS='publicKey'
_AR='WEBA10070800'
_AQ='timeDay'
_AP='WEBA10070700'
_AO='channelNo'
_AN='month'
_AM='yearTotalCost'
_AL='consType'
_AK='provinceId'
_AJ='proCode'
_AI='userAccountId'
_AH='0000'
_AG='refresh_token'
_AF='skey'
_AE='userInfo'
_AD='0101046'
_AC='billYear'
_AB='loginAccount'
_AA='keyCode'
_A9='querytypeCode'
_A8='01010049'
_A7='account'
_A6='daily_bill_list'
_A5='account_balance'
_A4='userName'
_A3='acctId'
_A2='resultCode'
_A1='quInfo'
_A0='BCP_000026'
_z='app'
_y='WEBALIPAY_01'
_x='order'
_w='state_grid'
_v='latestBillMonth'
_u='list'
_t='authFlag'
_s='09'
_r='0101183'
_q='consNo'
_p='token'
_o=True
_n='0101154'
_m='getday'
_l='monthBillList'
_k='bizrt'
_j='timestamp'
_i=False
_h='month_ele'
_g='consNo_dst'
_f='errmsg'
_e='clearCache'
_d='promotCode'
_c='01'
_b='SGAPP'
_a='devciceId'
_Z='devciceIp'
_Y='orgNo'
_X='tenant'
_W='member'
_V='stepelect'
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
_G='1'
_F=None
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
configuration={_K:{_W:_M,_Z:'',_a:'',_X:_w},_E:_b,_S:'32101',_I:_M,_AO:_M,'toPublish':_c,'siteId':'2012000000033700',_L:'',_N:'',_D:'',_C:{_x:_n,'uploadPic':'0101296','pauseSCode':'0101250','pauseTCode':'0101251','listconsumers':'0101093','messageList':'0101343','submit':'0101003','sbcMsg':'0101210','powercut':'0104514','BkAuth01':'f15','BkAuth02':'f18','BkAuth03':'f02','BkAuth04':'f17','BkAuth05':'f05','BkAuth06':'f16','BkAuth07':'f01','BkAuth08':'f03'},'electricityArchives':{'servicecode':'0104505',_E:_M},'subscriptionList':{_L:'APP_SGPMS_05_030',_N:'22',_I:_M,_D:'22',_S:'-1'},'userInformation':{_C:'01008183',_E:_b},'userInform':{_C:_r,_E:_b},'elesum':{_I:_M,_D:_y,_d:_G,_T:_G,_C:'0101143',_E:_z},_A7:{_I:_M,_D:'WEBA1007200'},_Ac:{_E:_M,_S:'-1',_I:_s,_AO:_s,_C:_A8,_D:'WEBA40050000',_K:{_W:_M,_Z:'',_a:'',_X:_w}},'doorAuth':{_E:_b,_C:'f04'},'xinZ':{_O:'101',_Ad:'101','fJ_busiTypeCode':'102',_Ae:'03','fJ_custType':'02',_Af:_c,_P:'',_D:_AP,_x:_n,_E:_b,_A9:_G},'onedo':{_C:_AD,_E:_b,_D:_AP,'queryType':'03'},'xinHuTongDian':{_O:'110',_J:'211',_P:'21102',_D:'WEBA10071200',_I:_M,_E:_s,_C:_r},'company':{_O:'104',_D:_AP,_Af:'02',_A9:_G,_t:_G,_E:_b,_x:_n},'charge':{_I:_s,_D:'WEBA10071300',_AO:'0901',_O:'102',_Ae:_c,_Ad:'102'},'other':{_I:_s,_D:'WEBA10079700',_O:'129',_J:'999',_P:'21501',_C:_A0,_L:'',_N:''},'vatchange':{'submit':'0101003',_J:'320',_P:'',_O:'115',_D:'WEBA10074000',_t:_G},'bill':{_e:_G,_D:_y,_T:_G,_C:_A0},_V:{_I:_M,_D:_y,_T:_G,_e:_s,_C:_A0,_E:_z},_m:{_I:_M,_e:'11',_D:_y,_d:_G,_T:_G,_C:_A0,_E:_z},'mouthOut':{_I:_M,_e:'11',_D:_y,_d:_G,_T:_G,_C:_A0,_E:_z},'meter':{_O:'114',_J:'304',_D:'WEBA10071000',_P:'',_C:_AD,_N:''},'complaint':{_J:'005','srvMode':_M,'anonymousFlag':'0','replyMode':_c,'retvisitFlag':_c},'report':{_J:'006'},'tradewinds':{_J:'019'},'somesay':{_J:'091'},'faultrepair':{_D:_Ag,_C:_r,_O:'111',_J:'001',_P:'21505'},'electronicInvoice':{_O:'105',_J:'0'},'rename':{_C:_AD,_D:'WEBA10076100',_J:'210',_O:'109',_t:_G,'gh_busiTypeCode':'211','gh_subusi':'21101',_N:'',_L:''},'pause':{_P:'',_C:_A8,_D:'WEBA10073600',_O:'107',_J:'203','jr_busi':'201',_N:'',_L:''},'capacityRecovery':{_C:_A8,_E:_b,_L:'',_N:'',_D:'WEBA10073700','busiTypeCode_stop':'204','busiTypeCode_less':'202',_J:'202',_P:'',_O:'108',_AQ:'5',_t:_G},'electricityPriceChange':{_C:_r,_J:'215',_P:'21502',_O:'113',_t:_G,_AQ:'15',_D:'WEBA10073900WEB',_L:'',_N:''},'electricityPriceStrategyChange':{_C:'01008183',_J:'215',_P:'21506',_O:'160',_D:'WEBV00000517WEB',_L:'',_N:''},'eemandValueAdjustment':{_C:_r,_L:'',_N:'',_O:'112',_D:'WEBA10073800',_J:'215',_P:'21504',_t:_G,_AQ:'5','getMonthServiceCode':_AD},'businessProgress':{_C:_r,_L:_c,_D:'WEB01'},'increase':{_E:_b,_N:'',_L:'',_Ah:_A8,_C:_n,_x:_n,_D:_AR,_A9:_G,_O:'106',_J:'111',_P:''},'fjincrea':{_O:'105',_J:'110',_P:'',_E:_b,_D:_AR,_N:'',_L:'',_Ah:_A8,_C:_n,_x:_n,_A9:_G},'persIncrea':{_O:'105',_J:'109',_x:_n,_P:'',_E:_b,_D:_AR,_A9:_G},'fgdChange':{_C:_r,_L:_c,_I:_s,_D:_Ag,_J:'215',_P:'21505',_O:'111',_t:_G},'createOrder':{_I:_M,_D:_y,_L:'BCP_000001','chargeMode':'02','conType':_c,'bizTypeId':'BT_ELEC'},'largePopulation':{_J:'383',_D:'WEBA10076800',_P:'',_L:'',_T:'',_d:'',_I:'0901',_O:'383',_C:'',_N:''},'biaoJiCode':{_C:'0104507',_E:'1704',_I:'1704'},'twoGuar':{_J:'402',_P:'40201',_D:'web_twoGuar'},'electTrend':{_C:_Ai,_I:_M},'emergency':{_C:_Ai,_D:'A10000000',_I:_M},'infoPublic':{_C:'2545454',_E:_z}}
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
getJiaoFeiRecordApi=_Aj
get_door_daily_bill_api=_Aj
sessionIdControlApiList=[get_qr_code_api,get_qr_code_status_api,get_qr_code_token_api,send_code_api,code_login_api]
keyCodeControlApiList=[get_qr_code_status_api,get_qr_code_token_api,send_code_api,code_login_api,getCertificationApi,get_request_authorize_api,get_web_token_api,refresh_web_token_api,get_door_number_api,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
authControlApiList=[get_door_number_api,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
tControlApiList=[getCertificationApi,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
def json_dumps(data):return json.dumps(data,separators=(',',':'),ensure_ascii=_i)
def normal_round(num,ndigits=0):
	A=ndigits
	if A==0:return int(num+.5)
	else:B=10**A;return int(num*B+.5)/B
def catchFloat(data,key):
	if key in data:
		try:return normal_round(float(data[key]),2)
		except:return 0
	else:return 0
class StateGridDataClient:
	hass=_F;coordinator=_F;session=_F;dataVersion=_F;keyCode=_F;publicKey=_F;need_login=_i;retry_times=0;phone=_F;codeKey=_F;serialNo=_F;qrCodeSerial=_F;userInfo=_F;accountInfo=_F;powerUserList=_F;doorAccountDict={};cookie=[];timestamp=int(time.time()*1000);accessToken=_F;refreshToken=_F;token=_F;expirationDate=_F;refresh_interval=6;is_debug=_i
	def __init__(A,hass,config=_F):
		B=config;A.hass=hass;C=aiohttp.TCPConnector(ssl=_i);D=aiohttp.CookieJar(quote_cookie=_o);A.session=aiohttp.ClientSession(cookie_jar=D,connector=C)
		if B is not _F:
			try:A.keyCode=B[_AA];A.publicKey=B[_AS];A.accessToken=B[_Ak];A.refreshToken=B[_Al];A.token=B[_p];A.userInfo=B[_AE];A.powerUserList=B[_AT];A.doorAccountDict=B[_Am];A.refresh_interval=B[_An];A.is_debug=B['is_debug'];A.dataVersion=B[_Ao]
			except Exception as E:LOGGER.error(E)
	async def save_data(B):A={};A[_AA]=B.keyCode;A[_AS]=B.publicKey;A[_Ak]=B.accessToken;A[_Al]=B.refreshToken;A[_p]=B.token;A[_AE]=B.userInfo;A[_AT]=B.powerUserList;A[_Am]=B.doorAccountDict;A[_An]=B.refresh_interval;A['is_debug']=B.is_debug;A[_Ao]=VERSION;await async_save_to_store(B.hass,'state_grid.config',A)
	def encrypt_post_data(A,data):B={_Ap:A.accessToken[len(A.accessToken)//2:]if A.accessToken else'','_t':A.token[len(A.token)//2:]if A.token else'','_data':data,_j:A.timestamp};return A.encrypt_wapper_data(B)
	def encrypt_wapper_data(A,data):B=a(json_dumps(data),A.keyCode);return{_A:B+c(B+str(A.timestamp)),_AF:d(A.keyCode,A.publicKey),_j:str(A.timestamp)}
	def handle_request_result_message(E,api,result):
		D='message';C='resultMessage';A=result;B=_F
		if _A in A and _Q in A[_A]and C in A[_A][_Q]:B=A[_A][_Q][C]
		elif _Q in A and C in A[_Q]:B=A[_Q][C]
		elif D in A:B=A[D]
		else:B=json_dumps(A)
		if E.is_debug:LOGGER.error(api+': '+B);LOGGER.error(json_dumps(A))
		return B
	async def __fetch_safe(C,api,data):
		B=await C.__fetch(api,data)
		if _H not in B:return B
		A=B[_H]
		if 10015==A or 10108==A or 10009==A or 10207==A or 10005==A or 10010==A or 30010==A or 10002==A:
			await C.__refresh_token()
			if C.need_login is _o:return B
			else:return await C.__fetch(api,data)
		else:return B
	async def __fetch(B,api,data,header=_F):
		T='encryptData';S='464606a4-184c-4beb-b442-2ab7761d0796';R='key_code';Q='state';P='sign';O='grant_type';N='application/json;charset=UTF-8';M='Content-Type';L=header;K='client_secret';I='client_id';E=api;B.timestamp=int(time.time()*1000);D=B.timestamp
		if B.keyCode is _F:B.keyCode=e(32,16,2)
		F=B.keyCode;G={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36','Accept':N,M:N,'version':'1.0',_E:'0901',_j:str(D),'wsgwType':'web','appKey':appKey};A=data
		if E==get_request_key_api:A={I:appKey,K:appSecret};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AF:d(F,'042BC7AD510BF9793B7744C8854C56A8C95DD1027EE619247A332EC6ED5B279F435A23D62441FE861F4B0C963347ECD5792F380B64CA084BE8BE41151F8B8D19C8'),I:appKey,_j:str(D)}
		elif E==get_qr_code_api:A={_Ap:'','_t':'','_data':A,_j:D}
		elif E==get_request_authorize_api:
			A={I:appKey,'response_type':_H,_Aq:'/test',_j:D,'rsi':B.token};A=urllib.parse.urlencode(A);G[M]='application/x-www-form-urlencoded; charset=UTF-8';G[_AA]=F
			async with B.session.post(baseApi+E,data=A,headers=G)as J:B.session.cookie_jar.update_cookies(J.cookies);C=await J.json();C=b(C[_A],B.token);C=json.loads(C);return C
		elif E==get_web_token_api:A={O:'authorization_code',P:c(appKey+str(D)),K:appSecret,Q:S,R:F,I:appKey,_j:D,_H:A[_H]};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AF:d(F,B.publicKey),_j:str(D)}
		elif E==refresh_web_token_api:A={O:_AG,P:c(appKey+str(D)),K:appSecret,Q:S,R:F,I:appKey,_j:D,_AG:B.refreshToken};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AF:d(F,B.publicKey),_j:str(D)};E=get_web_token_api
		else:A=B.encrypt_post_data(A)
		if L is not _F:G.update(L)
		if E in sessionIdControlApiList:G['sessionId']='web'+str(D)
		if E in keyCodeControlApiList:G[_AA]=F
		if E in authControlApiList:G['Authorization']='Bearer '+B.accessToken[:len(B.accessToken)//2]
		if E in tControlApiList:G['t']=B.token[:len(B.token)//2]
		async with B.session.post(baseApi+E,json=A,headers=G)as J:
			C=await J.text()
			if C.startswith('{'):
				C=json.loads(C)
				if T in C:C=b(C[T],F);C=json.loads(C)
			return C
	async def __get_request_key(A):
		A.keyCode=_F;B=await A.__fetch(get_request_key_api,{});C=A.handle_request_result_message('get_request_key_api',B)
		if B[_H]==_G:A.keyCode=B[_A][_AA];A.publicKey=B[_A][_AS];return{_B:0}
		return{_B:1,_f:C}
	async def __get_qr_code(B):
		C={_K:{_Z:'',_X:_w,_W:_M,_a:''},_A1:{'optType':_c,_N:e(28,10,1)}};A=await B.__fetch(get_qr_code_api,C);D=B.handle_request_result_message('get_qr_code_api',A)
		if A[_H]==1:
			if A[_A]and A[_A][_Q]and A[_A][_Q][_A2]==_AH:B.qrCodeSerial=A[_A][_k][_Ar];E=A[_A][_k]['qrCode'];return{_B:0,_A:E}
		return{_B:1,_f:D}
	async def __get_qr_code_status(B):
		C={_k:{_Ar:B.qrCodeSerial}};D={_p:'98'+e(10,10,1)};A=await B.__fetch(get_qr_code_status_api,C,D);E=B.handle_request_result_message('get_qr_code_status_api',A)
		if _H in A and A[_H]==1:
			if _A in A and A[_A]!='null':B.token=A[_A];return{_B:0}
			else:return{_B:1,_f:'未使用网上国网 App 扫码或确认登录'}
		return{_B:1,_f:E}
	async def __get_qr_code_token(B):
		C={_K:{_X:_w,_W:_M,'isEncrypt':_o},_p:B.token};A=await B.__fetch(get_qr_code_token_api,C);D=B.handle_request_result_message('get_qr_code_token_api',A)
		if _Q in A and _A2 in A[_Q]and A[_Q][_A2]==_AH:B.userInfo=A[_k][_AE];return{_B:0}
		return{_B:1,_f:D}
	async def __send_code(B,phone):
		C=phone;B.phone=C;D={_K:{_Z:'',_X:_w,_W:_M,_a:''},_A1:{'sendType':'0',_A7:C,_As:'login','accountType':''},'Channels':'web'};A=await B.__fetch(send_code_api,D);E=B.handle_request_result_message('send_code_api',A)
		if A[_H]==1:
			if A[_A]and A[_A][_Q]and A[_A][_Q][_A2]==_AH:B.codeKey=A[_A][_k]['codeKey'];return{_B:0}
		return{_B:1,_f:E}
	async def __verfiy_code(A,code):
		C={_K:{_Z:'',_X:_w,_W:_M,_a:''},_A1:{_A7:A.phone,_As:'login',_H:code,'optSys':'ios','pushId':'00000','codeKey':A.codeKey},'Channels':'web'};B=await A.__fetch(code_login_api,C);D=A.handle_request_result_message('code_login_api',B)
		if _Q in B and _A2 in B[_Q]and B[_Q][_A2]==_AH:A.token=B[_k][_p];A.userInfo=B[_k][_AE][0];return{_B:0}
		return{_B:1,_f:D}
	async def __get_request_authorize(B):
		A=await B.__fetch(get_request_authorize_api,{});E=B.handle_request_result_message('get_request_authorize_api',A)
		if _H in A and A[_H]==_G:C=A[_A][_Aq];D=C.rfind('code=');B.authorizeCode=C[D+5:D+5+32];return{_B:0}
		return{_B:1,_f:E}
	async def __get_web_token(A):
		C={_H:A.authorizeCode};B=await A.__fetch(get_web_token_api,C);D=A.handle_request_result_message('get_web_token_api',B)
		if _H in B and B[_H]==_G:A.accessToken=B[_A][_At];A.refreshToken=B[_A][_AG];return{_B:0}
		return{_B:1,_f:D}
	async def __refresh_web_token(B):
		A=await B.__fetch(refresh_web_token_api,{});C=B.handle_request_result_message('refresh_web_token_api',A)
		if _H in A and A[_H]==_G:B.accessToken=A[_A][_At];B.refreshToken=A[_A][_AG];return{_B:0}
		return{_B:1,_f:C}
	async def __get_door_number(A):
		B=configuration[_Ac];G={_C:B[_C],_E:B[_E],_S:B[_S],_K:{_W:B[_K][_W],_Z:B[_K][_Z],_a:B[_K][_a],_X:B[_K][_X]},_A1:{_R:A.userInfo[_R]},_p:A.token};C=await A.__fetch_safe(get_door_number_api,G);H=A.handle_request_result_message('get_door_number_api',C)
		if _H in C and C[_H]==1 and _A in C and _k in C[_A]:
			E={}
			if A.powerUserList is not _F:E={A[_g]:A for A in A.powerUserList}
			F=[]
			for D in C[_A][_k][_AT]:
				if D[_g]in E:F.append(E[D[_g]])
				elif _AU in D and D[_AU]!='05':F.append(D)
			A.powerUserList=F;return{_B:0}
		return{_B:1,_f:H}
	async def __get_door_balance(B,door_account):
		A=door_account;E={_A:{_L:'',_N:'',_I:configuration[_A7][_I],_D:configuration[_A7][_D],_A3:B.userInfo[_R],_A4:B.userInfo.get(_AB,B.userInfo.get('nickname',_F)),_T:_G,_d:_G,_AI:B.userInfo[_R],_u:[{'consNoSrc':A[_g],_AJ:A.get(_U,A.get(_AK,_F)),'sceneType':A.get('consSortCode',A.get(_AU,_F)),_q:A[_q],_Y:A[_Y]}]},_C:'0101143',_E:configuration[_E],_S:A.get(_U,A.get(_AK,_F))};C=await B.__fetch_safe(get_door_balance_api,E);B.handle_request_result_message('get_door_balance_api',C)
		if _H in C and C[_H]==1 and _A in C and _u in C[_A]:
			D=C[_A][_u]
			if len(D)!=0:A[_A5]=D[0]
	async def __get_door_bill(C,door_account,monthDate):
		I='dataInfo';G='mothEleList';E=monthDate;A=door_account;J={_A:{_A3:C.userInfo[_R],_I:configuration[_I],_e:'11',_AL:A[_AW],_D:'ALIPAY_01',_Y:A[_Y],_AJ:A[_U],_d:_G,_T:_G,_N:'',_L:'',_A4:'',_AV:A[_U],_AI:C.userInfo[_R],_q:A[_q],_Au:E.year},_C:_A0,_E:_z,_S:A[_U]};B=await C.__fetch_safe(get_door_bill_api,J);C.handle_request_result_message('get_door_bill_api',B)
		if _H in B and B[_H]==1 and _A in B:
			if I in B[_A]:A[_AM]=B[_A][I]
			if G in B[_A]:
				if _AC not in A or A[_AC]!=E.year:A[_l]=B[_A][G];A[_AC]=E.year
				else:
					F={A.month:A for A in A[_l]};H=B[_A][G]
					for D in H:
						if D.month in F and _h in F[D.month]:D[_h]=F[D.month][_h]
					A[_l]=H
				if len(A[_l])>0:A[_v]=A[_l][-1]
	async def __get_door_ladder(C,door_account,monthBill):
		E=monthBill;A=door_account;I=A[_g];F=datetime.datetime.strptime(E[_AN],'%Y%m');G=f"{F.year}-{F.month:02d}";H={_A:{_I:configuration[_V][_I],_D:configuration[_V][_D],_T:configuration[_V][_T],_e:configuration[_V][_e],_q:A[_g],_d:A[_U],_Y:A[_Y],_Av:G,_AV:A[_U],_AL:A[_AW],_AI:C.userInfo[_R],_N:'',_L:'',_A4:C.userInfo[_AB],_A3:C.userInfo[_R]},_C:configuration[_V][_C],_E:configuration[_V][_E],_S:A[_U]};B=await C.__fetch(get_door_ladder_api,H);J=C.handle_request_result_message(_Aw,B)
		if _H in B and B[_H]==1 and _A in B and _u in B[_A]:
			D=B[_A][_u]
			if len(D)!=0:D=D[0];E['ladder']=D
	async def __get_door_mouth_bill(E,door_account,monthBill):
		O='pointList';H=monthBill;G='quantity';F='priceName';B=door_account;I=datetime.datetime.strptime(H[_AN],'%Y%m');P=f"{I.year}-{I.month:02d}";Q={_A:{_I:configuration[_V][_I],_D:configuration[_V][_D],_T:configuration[_V][_T],_e:configuration[_V][_e],_q:B[_g],_d:B[_U],_Y:B[_Y],_Av:P,_AV:B[_U],_AL:B[_AW],_AI:E.userInfo[_R],_N:'',_L:'',_A4:E.userInfo[_AB],_A3:E.userInfo[_R]},_C:configuration[_V][_C],_E:configuration[_V][_E],_S:B[_U]};C=await E.__fetch(get_door_ladder_api,Q);S=E.handle_request_result_message(_Aw,C)
		if _H in C and C[_H]==1 and _A in C and _u in C[_A]:
			J=C[_A][_u][0];R=catchFloat(J[O][0]['readList'][0],'activeCount');K=0;L=0;M=0;N=0
			for A in J[O][0]['amtGroupList'][0]['amtList']:
				if A[F]=='峰':K=catchFloat(A,G)
				elif A[F]=='谷':L=catchFloat(A,G)
				elif A[F]=='平':M=catchFloat(A,G)
				elif A[F]=='尖':N=catchFloat(A,G)
			D={};D[_AX]=normal_round(R,2);D[_AY]=normal_round(K,2);D[_AZ]=normal_round(L,2);D[_Aa]=normal_round(M,2);D[_Ab]=normal_round(N,2);H[_h]=D
	async def __get_door_daily_bill(B,door_account,year,start_date,end_date):
		D='sevenEleList';A=door_account;E={'params1':{_C:configuration[_C],_E:configuration[_E],_S:configuration[_S],_K:{_W:configuration[_K][_W],_Z:configuration[_K][_Z],_a:configuration[_K][_a],_X:configuration[_K][_X]},_A1:{_R:B.userInfo[_R]},_p:B.token},'params3':{_A:{_A3:B.userInfo[_R],_q:A[_g],_AL:_c,'endTime':end_date,_Y:A[_Y],_Au:year,_AJ:A.get(_U,A.get(_AK,_F)),_N:'',_L:'','startTime':start_date,_A4:B.userInfo[_AB],_D:configuration[_m][_D],_I:configuration[_m][_I],_e:configuration[_m][_e],_d:configuration[_m][_d],_T:configuration[_m][_T]},_C:configuration[_m][_C],_E:configuration[_m][_E],_S:A.get(_U,A.get(_AK,_F))},'params4':'010103'};C=await B.__fetch_safe(get_door_daily_bill_api,E);F=B.handle_request_result_message('get_door_daily_bill_api',C)
		if _H in C and C[_H]==1 and _A in C and D in C[_A]:A[_A6]=C[_A][D]
	async def __get_door_pay_record(A,door_account):B=door_account;D=B[_g];C={'params1':{_C:configuration[_C],_E:configuration[_E],_S:configuration[_S],_K:{_W:configuration[_K][_W],_Z:configuration[_K][_Z],_a:configuration[_K][_a],_X:configuration[_K][_X]},_A1:{_R:A.userInfo[_R]},_p:A.token},'params3':{_A:{_A3:A.userInfo[_R],'bgnPayDate':'2023-04-24',_I:configuration[_I],_q:B[_g],'endPayDate':'2024-04-24',_D:'webALIPAY_01','number':100,_Y:B[_Y],'page':_G,_AJ:B[_U],_d:_G,_T:_G,_N:'',_L:'',_A4:A.userInfo[_AB]},_C:'0101051',_E:_c,_S:B[_U]},'params4':'010104'};E=await A.__fetch(getJiaoFeiRecordApi,C)
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
		B.need_login=_i;await B.save_data();return{_B:0,_A:B.powerUserList}
	async def __refresh_token(A):
		B=await A.__get_request_key()
		if _B in B and B[_B]!=0:return
		B=await A.__refresh_web_token()
		if _B in B and B[_B]==0:A.need_login=_i;A.retry_times=0;await A.save_data()
		elif A.retry_times>=3:A.need_login=_o
		else:A.retry_times=A.retry_times+1
	async def refresh_data(B,setup=_i,force_refresh=_i):
		t='last_month_ele_cost';s='year_ele_cost';r='thisTPq';q='thisNPq';p='thisVPq';o='thisPPq';n='%Y%m%d';m='day';l='refresh_time';a=setup;Z='last_month_ele_num';Y='dayElePq';T='year_ele_num';G='balance'
		if a is _o:
			if B.dataVersion!=VERSION:B.powerUserList=_F
			b=await B.__get_door_number()
			if _B in b and b[_B]!=0:B.need_login=_o
		if B.need_login is _o:
			if B.powerUserList is not _F:
				for A in B.get_door_account_list():A[l]='Token刷新失败，请重新登录'
			LOGGER.error('国家电网 - Token刷新失败，请重新登录！');return
		u=a or force_refresh or int(time.time()*1000)-B.timestamp>B.refresh_interval*3600*1000
		if u is _i:return
		U=datetime.datetime.now();F=U-datetime.timedelta(days=1);v=f"{F.year}-{F.month:02d}-{F.day:02d}";V=F-datetime.timedelta(days=40);w=f"{V.year}-{V.month:02d}-{V.day:02d}"
		for A in B.powerUserList:
			x=A[_g];B.doorAccountDict[x]=A;await B.__get_door_balance(A)
			if B.retry_times!=0:return
			if _A5 in A:
				y=catchFloat(A[_A5],'estiAmt');W=catchFloat(A[_A5],'prepayBal');c=catchFloat(A[_A5],'sumMoney')
				if W==0 or W==c:A[G]=c
				else:A[G]=W-y
				d=catchFloat(A[_A5],'historyOwe')
				if d>0:A[G]=-d
			else:LOGGER.error('国家电网账户余额获取失败！')
			if G not in A:A[G]=0
			await B.__get_door_daily_bill(A,U.year,w,v)
			if _A6 not in A:LOGGER.error('国家电网无法获取日用电数据！');continue
			X=0;H=_i
			for e in range(10):
				D=A[_A6][e]
				try:float(D[Y]);H=_o;break
				except:X=X+1
			f=0;g=0;h=0;i=0;j=0
			if H:
				for e in range(X):A[_A6].pop(0)
				D=A[_A6][0];E=datetime.datetime.strptime(D[m],n);A['daily_lasted_date']=f"{E.year}-{E.month:02d}-{E.day:02d}";f=catchFloat(D,Y);g=catchFloat(D,o);h=catchFloat(D,p);i=catchFloat(D,q);j=catchFloat(D,r)
			A['daily_ele_num']=normal_round(f,2);A['daily_p_ele_num']=normal_round(g,2);A['daily_v_ele_num']=normal_round(h,2);A['daily_n_ele_num']=normal_round(i,2);A['daily_t_ele_num']=normal_round(j,2);I=0;J=0;K=0;L=0;M=0
			if H:
				for C in A[_A6]:
					z=datetime.datetime.strptime(C[m],n)
					if z.month!=E.month:break
					I+=catchFloat(C,Y);J+=catchFloat(C,o);K+=catchFloat(C,p);L+=catchFloat(C,q);M+=catchFloat(C,r)
			A[_AX]=normal_round(I,2);A[_AY]=normal_round(J,2);A[_AZ]=normal_round(K,2);A[_Aa]=normal_round(L,2);A[_Ab]=normal_round(M,2)
			if H:
				N=E-datetime.timedelta(days=E.day);A0=f"{N.year}{N.month:02d}"
				if _AC not in A or A[_AC]!=N.year or _v not in A or A[_v][_AN]!=A0:await B.__get_door_bill(A,N)
				if _l in A:
					for C in A[_l]:
						if _h not in C:await B.__get_door_mouth_bill(A,C)
			if _AM in A:A[T]=catchFloat(A[_AM],'totalEleNum');A[s]=catchFloat(A[_AM],'totalEleCost')
			if T not in A:A[T]=0;A[s]=0
			if _v in A:A[Z]=catchFloat(A[_v],'monthEleNum');A[t]=catchFloat(A[_v],'monthEleCost');k=datetime.datetime.strptime(A[_v][_AN],'%Y%m')
			if Z not in A:A[Z]=0;A[t]=0;k=F.month
			O=0;P=0;Q=0;R=0;S=0
			if k.month==12:O=I;P=J;Q=K;R=L;S=M
			else:
				if _l in A:
					for C in A[_l]:
						if _h in C:O+=C[_h][_AX];P+=C[_h][_AY];Q+=C[_h][_AZ];R+=C[_h][_Aa];S+=C[_h][_Ab]
				O+=I;P+=J;Q+=K;R+=L;S+=M
			A[T]=normal_round(O,2);A['year_p_ele_num']=normal_round(P,2);A['year_v_ele_num']=normal_round(Q,2);A['year_n_ele_num']=normal_round(R,2);A['year_t_ele_num']=normal_round(S,2);A[l]=datetime.datetime.strftime(U,'%Y-%m-%d %H:%M:%S')
		await B.save_data()
	def get_door_account_list(A):return list(A.doorAccountDict.values())
	def get_door_account(A):return A.doorAccountDict