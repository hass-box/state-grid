_Al='constType'
_Ak='queryYear'
_Aj='provinceCode'
_Ai='access_token'
_Ah='businessType'
_Ag='qrCodeSerial'
_Af='redirect_url'
_Ae='_access_token'
_Ad='refresh_interval'
_Ac='doorAccountDict'
_Ab='refreshToken'
_Aa='accessToken'
_AZ='/osg-web0004/member/c24/f01'
_AY='BCP_00026'
_AX='serviceCode_smt'
_AW='WEBA10070900'
_AV='serviceType'
_AU='jM_custType'
_AT='jM_busiTypeCode'
_AS='doorNumberManeger'
_AR='month'
_AQ='consType'
_AP='userAccountId'
_AO='powerUserList'
_AN='publicKey'
_AM='WEBA10070800'
_AL='timeDay'
_AK='WEBA10070700'
_AJ='channelNo'
_AI='monthBillList'
_AH='yearTotalCost'
_AG='provinceId'
_AF='proCode'
_AE='loginAccount'
_AD='0000'
_AC='refresh_token'
_AB='skey'
_AA='userInfo'
_A9='0101046'
_A8='list'
_A7='userName'
_A6='acctId'
_A5='keyCode'
_A4='querytypeCode'
_A3='01010049'
_A2='account'
_A1='account_balance'
_A0='resultCode'
_z='quInfo'
_y='BCP_000026'
_x='app'
_w='WEBALIPAY_01'
_v='order'
_u='state_grid'
_t='latestBillMonth'
_s='consNo_dst'
_r='consNo'
_q=True
_p='authFlag'
_o='09'
_n='0101183'
_m='stepelect'
_l='daily_bill_list'
_k='token'
_j=False
_i='0101154'
_h='getday'
_g='bizrt'
_f='clearCache'
_e='orgNo'
_d='timestamp'
_c='promotCode'
_b='errmsg'
_a='01'
_Z='SGAPP'
_Y='devciceId'
_X='devciceIp'
_W='proNo'
_V='tenant'
_U='member'
_T='promotType'
_S='userId'
_R='target'
_Q='srvrt'
_P='subBusiTypeCode'
_O='serialNo'
_N='serCat'
_M='srvCode'
_L='0902'
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
from.utils.logger import LOGGER
from.utils.store import async_save_to_store
from.utils.crypt import a,b,c,d,e
configuration={_K:{_U:_L,_X:'',_Y:'',_V:_u},_E:_Z,_R:'32101',_I:_L,_AJ:_L,'toPublish':_a,'siteId':'2012000000033700',_M:'',_O:'',_D:'',_C:{_v:_i,'uploadPic':'0101296','pauseSCode':'0101250','pauseTCode':'0101251','listconsumers':'0101093','messageList':'0101343','submit':'0101003','sbcMsg':'0101210','powercut':'0104514','BkAuth01':'f15','BkAuth02':'f18','BkAuth03':'f02','BkAuth04':'f17','BkAuth05':'f05','BkAuth06':'f16','BkAuth07':'f01','BkAuth08':'f03'},'electricityArchives':{'servicecode':'0104505',_E:_L},'subscriptionList':{_M:'APP_SGPMS_05_030',_O:'22',_I:_L,_D:'22',_R:'-1'},'userInformation':{_C:'01008183',_E:_Z},'userInform':{_C:_n,_E:_Z},'elesum':{_I:_L,_D:_w,_c:_F,_T:_F,_C:'0101143',_E:_x},_A2:{_I:_L,_D:'WEBA1007200'},_AS:{_E:_L,_R:'-1',_I:_o,_AJ:_o,_C:_A3,_D:'WEBA40050000',_K:{_U:_L,_X:'',_Y:'',_V:_u}},'doorAuth':{_E:_Z,_C:'f04'},'xinZ':{_N:'101',_AT:'101','fJ_busiTypeCode':'102',_AU:'03','fJ_custType':'02',_AV:_a,_P:'',_D:_AK,_v:_i,_E:_Z,_A4:_F},'onedo':{_C:_A9,_E:_Z,_D:_AK,'queryType':'03'},'xinHuTongDian':{_N:'110',_J:'211',_P:'21102',_D:'WEBA10071200',_I:_L,_E:_o,_C:_n},'company':{_N:'104',_D:_AK,_AV:'02',_A4:_F,_p:_F,_E:_Z,_v:_i},'charge':{_I:_o,_D:'WEBA10071300',_AJ:'0901',_N:'102',_AU:_a,_AT:'102'},'other':{_I:_o,_D:'WEBA10079700',_N:'129',_J:'999',_P:'21501',_C:_y,_M:'',_O:''},'vatchange':{'submit':'0101003',_J:'320',_P:'',_N:'115',_D:'WEBA10074000',_p:_F},'bill':{_f:_F,_D:_w,_T:_F,_C:_y},_m:{_I:_L,_D:_w,_T:_F,_f:_o,_C:_y,_E:_x},_h:{_I:_L,_f:'11',_D:_w,_c:_F,_T:_F,_C:_y,_E:_x},'mouthOut':{_I:_L,_f:'11',_D:_w,_c:_F,_T:_F,_C:_y,_E:_x},'meter':{_N:'114',_J:'304',_D:'WEBA10071000',_P:'',_C:_A9,_O:''},'complaint':{_J:'005','srvMode':_L,'anonymousFlag':'0','replyMode':_a,'retvisitFlag':_a},'report':{_J:'006'},'tradewinds':{_J:'019'},'somesay':{_J:'091'},'faultrepair':{_D:_AW,_C:_n,_N:'111',_J:'001',_P:'21505'},'electronicInvoice':{_N:'105',_J:'0'},'rename':{_C:_A9,_D:'WEBA10076100',_J:'210',_N:'109',_p:_F,'gh_busiTypeCode':'211','gh_subusi':'21101',_O:'',_M:''},'pause':{_P:'',_C:_A3,_D:'WEBA10073600',_N:'107',_J:'203','jr_busi':'201',_O:'',_M:''},'capacityRecovery':{_C:_A3,_E:_Z,_M:'',_O:'',_D:'WEBA10073700','busiTypeCode_stop':'204','busiTypeCode_less':'202',_J:'202',_P:'',_N:'108',_AL:'5',_p:_F},'electricityPriceChange':{_C:_n,_J:'215',_P:'21502',_N:'113',_p:_F,_AL:'15',_D:'WEBA10073900WEB',_M:'',_O:''},'electricityPriceStrategyChange':{_C:'01008183',_J:'215',_P:'21506',_N:'160',_D:'WEBV00000517WEB',_M:'',_O:''},'eemandValueAdjustment':{_C:_n,_M:'',_O:'',_N:'112',_D:'WEBA10073800',_J:'215',_P:'21504',_p:_F,_AL:'5','getMonthServiceCode':_A9},'businessProgress':{_C:_n,_M:_a,_D:'WEB01'},'increase':{_E:_Z,_O:'',_M:'',_AX:_A3,_C:_i,_v:_i,_D:_AM,_A4:_F,_N:'106',_J:'111',_P:''},'fjincrea':{_N:'105',_J:'110',_P:'',_E:_Z,_D:_AM,_O:'',_M:'',_AX:_A3,_C:_i,_v:_i,_A4:_F},'persIncrea':{_N:'105',_J:'109',_v:_i,_P:'',_E:_Z,_D:_AM,_A4:_F},'fgdChange':{_C:_n,_M:_a,_I:_o,_D:_AW,_J:'215',_P:'21505',_N:'111',_p:_F},'createOrder':{_I:_L,_D:_w,_M:'BCP_000001','chargeMode':'02','conType':_a,'bizTypeId':'BT_ELEC'},'largePopulation':{_J:'383',_D:'WEBA10076800',_P:'',_M:'',_T:'',_c:'',_I:'0901',_N:'383',_C:'',_O:''},'biaoJiCode':{_C:'0104507',_E:'1704',_I:'1704'},'twoGuar':{_J:'402',_P:'40201',_D:'web_twoGuar'},'electTrend':{_C:_AY,_I:_L},'emergency':{_C:_AY,_D:'A10000000',_I:_L},'infoPublic':{_C:'2545454',_E:_x}}
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
getJiaoFeiRecordApi=_AZ
get_door_daily_bill_api=_AZ
sessionIdControlApiList=[get_qr_code_api,get_qr_code_status_api,get_qr_code_token_api,send_code_api,code_login_api]
keyCodeControlApiList=[get_qr_code_status_api,get_qr_code_token_api,send_code_api,code_login_api,getCertificationApi,get_request_authorize_api,get_web_token_api,refresh_web_token_api,get_door_number_api,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
authControlApiList=[get_door_number_api,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
tControlApiList=[getCertificationApi,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
def json_dumps(data):return json.dumps(data,separators=(',',':'),ensure_ascii=_j)
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
	hass=_G;session=_G;keyCode=_G;publicKey=_G;need_login=_j;phone=_G;codeKey=_G;serialNo=_G;qrCodeSerial=_G;userInfo=_G;accountInfo=_G;powerUserList=_G;doorAccountDict={};cookie=[];timestamp=int(time.time()*1000);accessToken=_G;refreshToken=_G;token=_G;expirationDate=_G;refresh_interval=6;is_debug=_j
	def __init__(A,hass,config=_G):
		B=config;A.hass=hass;C=aiohttp.TCPConnector(ssl=_j);D=aiohttp.CookieJar(quote_cookie=_q);A.session=aiohttp.ClientSession(cookie_jar=D,connector=C)
		if B is not _G:
			try:A.keyCode=B[_A5];A.publicKey=B[_AN];A.accessToken=B[_Aa];A.refreshToken=B[_Ab];A.token=B[_k];A.userInfo=B[_AA];A.powerUserList=B[_AO];A.doorAccountDict=B[_Ac];A.refresh_interval=B[_Ad];A.is_debug=B['is_debug']
			except Exception as E:LOGGER.error(E)
	async def save_data(A):B={};B[_A5]=A.keyCode;B[_AN]=A.publicKey;B[_Aa]=A.accessToken;B[_Ab]=A.refreshToken;B[_k]=A.token;B[_AA]=A.userInfo;B[_AO]=A.powerUserList;B[_Ac]=A.doorAccountDict;B[_Ad]=A.refresh_interval;B['is_debug']=A.is_debug;await async_save_to_store(A.hass,'state_grid.config',B)
	def encrypt_post_data(A,data):B={_Ae:A.accessToken[len(A.accessToken)//2:]if A.accessToken else'','_t':A.token[len(A.token)//2:]if A.token else'','_data':data,_d:A.timestamp};return A.encrypt_wapper_data(B)
	def encrypt_wapper_data(A,data):B=a(json_dumps(data),A.keyCode);return{_A:B+c(B+str(A.timestamp)),_AB:d(A.keyCode,A.publicKey),_d:str(A.timestamp)}
	def handle_request_result_message(E,api,result):
		D='message';C='resultMessage';A=result;B=_G
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
			if C.need_login is _q:return B
			else:return await C.__fetch(api,data)
		else:return B
	async def __fetch(B,api,data,header=_G):
		T='encryptData';S='464606a4-184c-4beb-b442-2ab7761d0796';R='key_code';Q='state';P='sign';O='grant_type';N='application/json;charset=UTF-8';M='Content-Type';L=header;K='client_secret';I='client_id';E=api;B.timestamp=int(time.time()*1000);D=B.timestamp
		if B.keyCode is _G:B.keyCode=e(32,16,2)
		F=B.keyCode;G={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36','Accept':N,M:N,'version':'1.0',_E:'0901',_d:str(D),'wsgwType':'web','appKey':appKey};A=data
		if E==get_request_key_api:A={I:appKey,K:appSecret};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AB:d(F,'042BC7AD510BF9793B7744C8854C56A8C95DD1027EE619247A332EC6ED5B279F435A23D62441FE861F4B0C963347ECD5792F380B64CA084BE8BE41151F8B8D19C8'),I:appKey,_d:str(D)}
		elif E==get_qr_code_api:A={_Ae:'','_t':'','_data':A,_d:D}
		elif E==get_request_authorize_api:
			A={I:appKey,'response_type':_H,_Af:'/test',_d:D,'rsi':B.token};A=urllib.parse.urlencode(A);G[M]='application/x-www-form-urlencoded; charset=UTF-8';G[_A5]=F
			async with B.session.post(baseApi+E,data=A,headers=G)as J:B.session.cookie_jar.update_cookies(J.cookies);C=await J.json();C=b(C[_A],B.token);C=json.loads(C);return C
		elif E==get_web_token_api:A={O:'authorization_code',P:c(appKey+str(D)),K:appSecret,Q:S,R:F,I:appKey,_d:D,_H:A[_H]};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AB:d(F,B.publicKey),_d:str(D)}
		elif E==refresh_web_token_api:A={O:_AC,P:c(appKey+str(D)),K:appSecret,Q:S,R:F,I:appKey,_d:D,_AC:B.refreshToken};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AB:d(F,B.publicKey),_d:str(D)};E=get_web_token_api
		else:A=B.encrypt_post_data(A)
		if L is not _G:G.update(L)
		if E in sessionIdControlApiList:G['sessionId']='web'+str(D)
		if E in keyCodeControlApiList:G[_A5]=F
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
		if B[_H]==_F:A.keyCode=B[_A][_A5];A.publicKey=B[_A][_AN];return{_B:0}
		return{_B:1,_b:C}
	async def __get_qr_code(B):
		C={_K:{_X:'',_V:_u,_U:_L,_Y:''},_z:{'optType':_a,_O:e(28,10,1)}};A=await B.__fetch(get_qr_code_api,C);D=B.handle_request_result_message('get_qr_code_api',A)
		if A[_H]==1:
			if A[_A]and A[_A][_Q]and A[_A][_Q][_A0]==_AD:B.qrCodeSerial=A[_A][_g][_Ag];E=A[_A][_g]['qrCode'];return{_B:0,_A:E}
		return{_B:1,_b:D}
	async def __get_qr_code_status(B):
		C={_g:{_Ag:B.qrCodeSerial}};D={_k:'98'+e(10,10,1)};A=await B.__fetch(get_qr_code_status_api,C,D);E=B.handle_request_result_message('get_qr_code_status_api',A)
		if _H in A and A[_H]==1:
			if _A in A and A[_A]!='null':B.token=A[_A];return{_B:0}
			else:return{_B:1,_b:'未使用网上国网 App 扫码或确认登录'}
		return{_B:1,_b:E}
	async def __get_qr_code_token(B):
		C={_K:{_V:_u,_U:_L,'isEncrypt':_q},_k:B.token};A=await B.__fetch(get_qr_code_token_api,C);D=B.handle_request_result_message('get_qr_code_token_api',A)
		if _Q in A and _A0 in A[_Q]and A[_Q][_A0]==_AD:B.userInfo=A[_g][_AA];return{_B:0}
		return{_B:1,_b:D}
	async def __send_code(B,phone):
		C=phone;B.phone=C;D={_K:{_X:'',_V:_u,_U:_L,_Y:''},_z:{'sendType':'0',_A2:C,_Ah:'login','accountType':''},'Channels':'web'};A=await B.__fetch(send_code_api,D);E=B.handle_request_result_message('send_code_api',A)
		if A[_H]==1:
			if A[_A]and A[_A][_Q]and A[_A][_Q][_A0]==_AD:B.codeKey=A[_A][_g]['codeKey'];return{_B:0}
		return{_B:1,_b:E}
	async def __verfiy_code(A,code):
		C={_K:{_X:'',_V:_u,_U:_L,_Y:''},_z:{_A2:A.phone,_Ah:'login',_H:code,'optSys':'ios','pushId':'00000','codeKey':A.codeKey},'Channels':'web'};B=await A.__fetch(code_login_api,C);D=A.handle_request_result_message('code_login_api',B)
		if _Q in B and _A0 in B[_Q]and B[_Q][_A0]==_AD:A.token=B[_g][_k];A.userInfo=B[_g][_AA][0];return{_B:0}
		return{_B:1,_b:D}
	async def __get_request_authorize(B):
		A=await B.__fetch(get_request_authorize_api,{});E=B.handle_request_result_message('get_request_authorize_api',A)
		if _H in A and A[_H]==_F:C=A[_A][_Af];D=C.rfind('code=');B.authorizeCode=C[D+5:D+5+32];return{_B:0}
		return{_B:1,_b:E}
	async def __get_web_token(A):
		C={_H:A.authorizeCode};B=await A.__fetch(get_web_token_api,C);D=A.handle_request_result_message('get_web_token_api',B)
		if _H in B and B[_H]==_F:A.accessToken=B[_A][_Ai];A.refreshToken=B[_A][_AC];return{_B:0}
		return{_B:1,_b:D}
	async def __refresh_web_token(B):
		A=await B.__fetch(refresh_web_token_api,{});C=B.handle_request_result_message('refresh_web_token_api',A)
		if _H in A and A[_H]==_F:B.accessToken=A[_A][_Ai];B.refreshToken=A[_A][_AC];return{_B:0}
		return{_B:1,_b:C}
	async def __get_door_number(C):
		A=configuration[_AS];D={_C:A[_C],_E:A[_E],_R:A[_R],_K:{_U:A[_K][_U],_X:A[_K][_X],_Y:A[_K][_Y],_V:A[_K][_V]},_z:{_S:C.userInfo[_S]},_k:C.token};B=await C.__fetch_safe(get_door_number_api,D);E=C.handle_request_result_message('get_door_number_api',B)
		if _H in B and B[_H]==1 and _A in B and _g in B[_A]:C.powerUserList=B[_A][_g][_AO];return{_B:0}
		return{_B:1,_b:E}
	async def __get_door_balance(B,door_account):
		A=door_account;E={_A:{_M:'',_O:'',_I:configuration[_A2][_I],_D:configuration[_A2][_D],_A6:B.userInfo[_S],_A7:B.userInfo.get(_AE,B.userInfo.get('nickname',_G)),_T:_F,_c:_F,_AP:B.userInfo[_S],_A8:[{'consNoSrc':A[_s],_AF:A.get(_W,A.get(_AG,_G)),'sceneType':A.get('consSortCode',A.get('elecTypeCode',_G)),_r:A[_r],_e:A[_e]}]},_C:'0101143',_E:configuration[_E],_R:A.get(_W,A.get(_AG,_G))};C=await B.__fetch_safe(get_door_balance_api,E);B.handle_request_result_message('get_door_balance_api',C)
		if _H in C and C[_H]==1 and _A in C and _A8 in C[_A]:
			D=C[_A][_A8]
			if len(D)!=0:A[_A1]=D[0]
	async def __get_door_bill(C,door_account,year):
		E='dataInfo';D='mothEleList';B=door_account;F={_A:{_A6:C.userInfo[_S],_I:configuration[_I],_f:'11',_AQ:B[_Al],_D:'ALIPAY_01',_e:B[_e],_AF:B[_W],_c:_F,_T:_F,_O:'',_M:'',_A7:'',_Aj:B[_W],_AP:C.userInfo[_S],_r:B[_r],_Ak:year},_C:_y,_E:_x,_R:B[_W]};A=await C.__fetch_safe(get_door_bill_api,F);C.handle_request_result_message('get_door_bill_api',A)
		if _H in A and A[_H]==1 and _A in A:
			if E in A[_A]:B[_AH]=A[_A][E]
			if D in A[_A]:
				B[_AI]=A[_A][D]
				if len(A[_A][D])!=0:B[_t]=A[_A][D][-1]
	async def __get_door_ladder(B,door_account,month):
		F='ladder_flag';E=month;A=door_account;G=A[_s];H={_A:{_I:configuration[_m][_I],_D:configuration[_m][_D],_T:configuration[_m][_T],_f:configuration[_m][_f],_r:A[_s],_c:A[_W],_e:A[_e],'queryDate':E,_Aj:A[_W],_AQ:A[_Al],_AP:B.userInfo[_S],_O:'',_M:'',_A7:B.userInfo[_AE],_A6:B.userInfo[_S]},_C:configuration[_m][_C],_E:configuration[_m][_E],_R:A[_W]};C=await B.__fetch(get_door_ladder_api,H);I=B.handle_request_result_message('get_door_ladder_api',C)
		if _H in C and C[_H]==1 and _A in C and _A8 in C[_A]:
			D=C[_A][_A8]
			if len(D)!=0:
				D=D[0];D[_AR]=E
				if D['electricParticulars']['levelFlag']=='2':A[F]=1
				else:A[F]=0
				B.doorAccountDict[G]['ladder']=D
	async def __get_door_daily_bill(B,door_account,year,start_date,end_date):
		D='sevenEleList';A=door_account;E={'params1':{_C:configuration[_C],_E:configuration[_E],_R:configuration[_R],_K:{_U:configuration[_K][_U],_X:configuration[_K][_X],_Y:configuration[_K][_Y],_V:configuration[_K][_V]},_z:{_S:B.userInfo[_S]},_k:B.token},'params3':{_A:{_A6:B.userInfo[_S],_r:A[_s],_AQ:_a,'endTime':end_date,_e:A[_e],_Ak:year,_AF:A.get(_W,A.get(_AG,_G)),_O:'',_M:'','startTime':start_date,_A7:B.userInfo[_AE],_D:configuration[_h][_D],_I:configuration[_h][_I],_f:configuration[_h][_f],_c:configuration[_h][_c],_T:configuration[_h][_T]},_C:configuration[_h][_C],_E:configuration[_h][_E],_R:A.get(_W,A.get(_AG,_G))},'params4':'010103'};C=await B.__fetch_safe(get_door_daily_bill_api,E);F=B.handle_request_result_message('get_door_daily_bill_api',C)
		if _H in C and C[_H]==1 and _A in C and D in C[_A]:A[_l]=C[_A][D]
	async def __get_door_pay_record(A,door_account):B=door_account;D=B[_s];C={'params1':{_C:configuration[_C],_E:configuration[_E],_R:configuration[_R],_K:{_U:configuration[_K][_U],_X:configuration[_K][_X],_Y:configuration[_K][_Y],_V:configuration[_K][_V]},_z:{_S:A.userInfo[_S]},_k:A.token},'params3':{_A:{_A6:A.userInfo[_S],'bgnPayDate':'2023-04-24',_I:configuration[_I],_r:B[_s],'endPayDate':'2024-04-24',_D:'webALIPAY_01','number':100,_e:B[_e],'page':_F,_AF:B[_W],_c:_F,_T:_F,_O:'',_M:'',_A7:A.userInfo[_AE]},_C:'0101051',_E:_a,_R:B[_W]},'params4':'010104'};E=await A.__fetch(getJiaoFeiRecordApi,C)
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
		B.need_login=_j;await B.save_data();return{_B:0,_A:B.powerUserList}
	async def __refresh_token(A):
		B=await A.__get_request_key()
		if _B in B and B[_B]!=0:return
		B=await A.__refresh_web_token()
		if _B in B and B[_B]==0:A.need_login=_j;await A.save_data()
		else:A.need_login=_q;LOGGER.error('国家电网刷新 Token 失败')
	async def refresh_data(C,setup=_j):
		l='last_month_ele_cost';k='monthEleNum';j='year_ele_cost';i='thisTPq';h='thisNPq';g='thisVPq';f='thisPPq';e='refresh_time';U=setup;T='ladder_level_num';S='ladder_level';R='last_month_ele_num';Q='year_ele_num';L='%Y%m%d';K='day';I='dayElePq';H='balance'
		if U is _q:
			V=await C.__get_door_number()
			if _B in V and V[_B]!=0:C.need_login=_q
		if C.need_login is _q:
			if C.powerUserList is not _G:
				for A in C.get_door_account_list():A[e]='刷新 Token 失败，需重新登录！'
			LOGGER.error('国家电网需要重新登录！');return
		m=U or int(time.time()*1000)-C.timestamp>C.refresh_interval*3600*1000
		if m is _j:return
		M=datetime.datetime.now();J=M-datetime.timedelta(days=1);n=f"{J.year}-{J.month:02d}-{J.day:02d}";N=J-datetime.timedelta(days=40);o=f"{N.year}-{N.month:02d}-{N.day:02d}"
		for A in C.powerUserList:
			p=A[_s];C.doorAccountDict[p]=A;await C.__get_door_balance(A)
			if _A1 in A:
				q=catchFloat(A[_A1],'estiAmt');W=catchFloat(A[_A1],'prepayBal');r=catchFloat(A[_A1],'sumMoney')
				if W==0:A[H]=r
				else:A[H]=W-q
				X=catchFloat(A[_A1],'historyOwe')
				if X>0:A[H]=-X
			else:LOGGER.error('国家电网账户余额获取失败！')
			if H not in A:A[H]=0
			await C.__get_door_daily_bill(A,M.year,o,n)
			if _l not in A:LOGGER.error('国家电网无法获取日用电数据！');return
			O=0
			for Y in range(10):
				D=A[_l][Y]
				try:float(D[I]);break
				except:O=O+1
			for Y in range(O):A[_l].pop(0)
			D=A[_l][0];E=datetime.datetime.strptime(D[K],L);A['daily_ele_num']=catchFloat(D,I);A['daily_p_ele_num']=catchFloat(D,f);A['daily_v_ele_num']=catchFloat(D,g);A['daily_n_ele_num']=catchFloat(D,h);A['daily_t_ele_num']=catchFloat(D,i);Z=0;a=0;b=0;c=0;d=0
			for B in A[_l]:
				G=datetime.datetime.strptime(B[K],L)
				if G.month!=E.month:break
				Z+=catchFloat(B,I);a+=catchFloat(B,f);b+=catchFloat(B,g);c+=catchFloat(B,h);d+=catchFloat(B,i)
			A['month_ele_num']=normal_round(Z,2);A['month_p_ele_num']=normal_round(a,2);A['month_v_ele_num']=normal_round(b,2);A['month_n_ele_num']=normal_round(c,2);A['month_t_ele_num']=normal_round(d,2);P=E-datetime.timedelta(days=E.day);s=f"{P.year}-{P.month:02d}"
			if _t not in A or A[_t][_AR]!=s:await C.__get_door_bill(A,P.year)
			if _t not in A:LOGGER.error('国家电网无法获取年度用电数据！');return
			if _AH in A:A[Q]=catchFloat(A[_AH],'totalEleNum');A[j]=catchFloat(A[_AH],'totalEleCost')
			if Q not in A:A[Q]=0;A[j]=0
			if _AI in A:A[R]=catchFloat(A[_t],k);A[l]=catchFloat(A[_t],'monthEleCost')
			if R not in A:A[R]=0;A[l]=0
			t=datetime.datetime.strptime(A[_t][_AR],'%Y%m')
			if t.month==12:
				F=0
				for B in A[_l]:
					G=datetime.datetime.strptime(B[K],L)
					if G.month!=12:break
					F+=catchFloat(B,I)
			else:
				F=0
				for B in A[_AI]:F+=catchFloat(B,k)
				u=len(A[_AI])
				for B in A[_l]:
					G=datetime.datetime.strptime(B[K],L)
					if G.month<=u:break
					F+=catchFloat(B,I)
			if F<=2760:A[S]='第一阶梯';A[T]=1
			elif F<=4800:A[S]='第二阶梯';A[T]=2
			else:A[S]='第三阶梯';A[T]=3
			A['daily_lasted_date']=f"{E.year}-{E.month:02d}-{E.day:02d}";A[e]=datetime.datetime.strftime(M,'%Y-%m-%d %H:%M:%S')
		await C.save_data()
	def get_door_account_list(A):return list(A.doorAccountDict.values())
	def get_door_account(A):return A.doorAccountDict