_Al='queryYear'
_Ak='provinceCode'
_Aj='sceneType'
_Ai='consNoSrc'
_Ah='access_token'
_Ag='businessType'
_Af='qrCodeSerial'
_Ae='redirect_url'
_Ad='_access_token'
_Ac='refresh_interval'
_Ab='doorAccountDict'
_Aa='refreshToken'
_AZ='accessToken'
_AY='/osg-web0004/member/c24/f01'
_AX='BCP_00026'
_AW='serviceCode_smt'
_AV='WEBA10070900'
_AU='serviceType'
_AT='jM_custType'
_AS='jM_busiTypeCode'
_AR='consType'
_AQ='constType'
_AP='powerUserList'
_AO='publicKey'
_AN='WEBA10070800'
_AM='timeDay'
_AL='WEBA10070700'
_AK='0101143'
_AJ='channelNo'
_AI='latestBillMonth'
_AH='yearTotalCost'
_AG='userAccountId'
_AF='0000'
_AE='refresh_token'
_AD='skey'
_AC='userInfo'
_AB='0101046'
_AA='proCode'
_A9='loginAccount'
_A8='keyCode'
_A7='querytypeCode'
_A6='01010049'
_A5='doorNumberManeger'
_A4='monthBillList'
_A3='accountBalance'
_A2='list'
_A1='userName'
_A0='acctId'
_z='resultCode'
_y='quInfo'
_x='BCP_000026'
_w='app'
_v='WEBALIPAY_01'
_u='order'
_t='state_grid'
_s=False
_r='authFlag'
_q='09'
_p='0101183'
_o='stepelect'
_n='account'
_m='consNo_dst'
_l='token'
_k='0101154'
_j='getday'
_i='consNo'
_h='bizrt'
_g='clearCache'
_f='timestamp'
_e='errmsg'
_d='promotCode'
_c='01'
_b='SGAPP'
_a='devciceId'
_Z='devciceIp'
_Y='orgNo'
_X='tenant'
_W='member'
_V='daily_bill_list'
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
_J=None
_I='busiTypeCode'
_H='code'
_G='channelCode'
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
appKey='3def6c365d284881bf1a9b2b502ee68c'
appSecret='ab7357dae64944a197ace37398897f64'
configuration={_K:{_W:_M,_Z:'',_a:'',_X:_t},_E:_b,_S:'32101',_G:_M,_AJ:_M,'toPublish':_c,'siteId':'2012000000033700',_L:'',_N:'',_D:'',_C:{_u:_k,'uploadPic':'0101296','pauseSCode':'0101250','pauseTCode':'0101251','listconsumers':'0101093','messageList':'0101343','submit':'0101003','sbcMsg':'0101210','powercut':'0104514','BkAuth01':'f15','BkAuth02':'f18','BkAuth03':'f02','BkAuth04':'f17','BkAuth05':'f05','BkAuth06':'f16','BkAuth07':'f01','BkAuth08':'f03'},'electricityArchives':{'servicecode':'0104505',_E:_M},'subscriptionList':{_L:'APP_SGPMS_05_030',_N:'22',_G:_M,_D:'22',_S:'-1'},'userInformation':{_C:'01008183',_E:_b},'userInform':{_C:_p,_E:_b},'elesum':{_G:_M,_D:_v,_d:_F,_T:_F,_C:_AK,_E:_w},_n:{_G:_M,_D:'WEBA1007200'},_A5:{_E:_M,_S:'-1',_G:_q,_AJ:_q,_C:_A6,_D:'WEBA40050000',_K:{_W:_M,_Z:'',_a:'',_X:_t}},'doorAuth':{_E:_b,_C:'f04'},'xinZ':{_O:'101',_AS:'101','fJ_busiTypeCode':'102',_AT:'03','fJ_custType':'02',_AU:_c,_P:'',_D:_AL,_u:_k,_E:_b,_A7:_F},'onedo':{_C:_AB,_E:_b,_D:_AL,'queryType':'03'},'xinHuTongDian':{_O:'110',_I:'211',_P:'21102',_D:'WEBA10071200',_G:_M,_E:_q,_C:_p},'company':{_O:'104',_D:_AL,_AU:'02',_A7:_F,_r:_F,_E:_b,_u:_k},'charge':{_G:_q,_D:'WEBA10071300',_AJ:'0901',_O:'102',_AT:_c,_AS:'102'},'other':{_G:_q,_D:'WEBA10079700',_O:'129',_I:'999',_P:'21501',_C:_x,_L:'',_N:''},'vatchange':{'submit':'0101003',_I:'320',_P:'',_O:'115',_D:'WEBA10074000',_r:_F},'bill':{_g:_F,_D:_v,_T:_F,_C:_x},_o:{_G:_M,_D:_v,_T:_F,_g:_q,_C:_x,_E:_w},_j:{_G:_M,_g:'11',_D:_v,_d:_F,_T:_F,_C:_x,_E:_w},'mouthOut':{_G:_M,_g:'11',_D:_v,_d:_F,_T:_F,_C:_x,_E:_w},'meter':{_O:'114',_I:'304',_D:'WEBA10071000',_P:'',_C:_AB,_N:''},'complaint':{_I:'005','srvMode':_M,'anonymousFlag':'0','replyMode':_c,'retvisitFlag':_c},'report':{_I:'006'},'tradewinds':{_I:'019'},'somesay':{_I:'091'},'faultrepair':{_D:_AV,_C:_p,_O:'111',_I:'001',_P:'21505'},'electronicInvoice':{_O:'105',_I:'0'},'rename':{_C:_AB,_D:'WEBA10076100',_I:'210',_O:'109',_r:_F,'gh_busiTypeCode':'211','gh_subusi':'21101',_N:'',_L:''},'pause':{_P:'',_C:_A6,_D:'WEBA10073600',_O:'107',_I:'203','jr_busi':'201',_N:'',_L:''},'capacityRecovery':{_C:_A6,_E:_b,_L:'',_N:'',_D:'WEBA10073700','busiTypeCode_stop':'204','busiTypeCode_less':'202',_I:'202',_P:'',_O:'108',_AM:'5',_r:_F},'electricityPriceChange':{_C:_p,_I:'215',_P:'21502',_O:'113',_r:_F,_AM:'15',_D:'WEBA10073900WEB',_L:'',_N:''},'electricityPriceStrategyChange':{_C:'01008183',_I:'215',_P:'21506',_O:'160',_D:'WEBV00000517WEB',_L:'',_N:''},'eemandValueAdjustment':{_C:_p,_L:'',_N:'',_O:'112',_D:'WEBA10073800',_I:'215',_P:'21504',_r:_F,_AM:'5','getMonthServiceCode':_AB},'businessProgress':{_C:_p,_L:_c,_D:'WEB01'},'increase':{_E:_b,_N:'',_L:'',_AW:_A6,_C:_k,_u:_k,_D:_AN,_A7:_F,_O:'106',_I:'111',_P:''},'fjincrea':{_O:'105',_I:'110',_P:'',_E:_b,_D:_AN,_N:'',_L:'',_AW:_A6,_C:_k,_u:_k,_A7:_F},'persIncrea':{_O:'105',_I:'109',_u:_k,_P:'',_E:_b,_D:_AN,_A7:_F},'fgdChange':{_C:_p,_L:_c,_G:_q,_D:_AV,_I:'215',_P:'21505',_O:'111',_r:_F},'createOrder':{_G:_M,_D:_v,_L:'BCP_000001','chargeMode':'02','conType':_c,'bizTypeId':'BT_ELEC'},'largePopulation':{_I:'383',_D:'WEBA10076800',_P:'',_L:'',_T:'',_d:'',_G:'0901',_O:'383',_C:'',_N:''},'biaoJiCode':{_C:'0104507',_E:'1704',_G:'1704'},'twoGuar':{_I:'402',_P:'40201',_D:'web_twoGuar'},'electTrend':{_C:_AX,_G:_M},'emergency':{_C:_AX,_D:'A10000000',_G:_M},'infoPublic':{_C:'2545454',_E:_w}}
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
getJiaoFeiRecordApi=_AY
get_door_daily_bill_api=_AY
sessionIdControlApiList=[get_qr_code_api,get_qr_code_status_api,get_qr_code_token_api,send_code_api,code_login_api]
keyCodeControlApiList=[get_qr_code_status_api,get_qr_code_token_api,send_code_api,code_login_api,getCertificationApi,get_request_authorize_api,get_web_token_api,refresh_web_token_api,get_door_number_api,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
authControlApiList=[get_door_number_api,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
tControlApiList=[getCertificationApi,get_door_balance_api,get_door_bill_api,get_door_ladder_api,getJiaoFeiRecordApi,get_door_daily_bill_api]
def json_dumps(data):return json.dumps(data,separators=(',',':'),ensure_ascii=_s)
def catchFloat(data,key):
	if key in data:
		try:return float(data[key])
		except:return 0
	else:return 0
class StateGridDataClient:
	hass=_J;session=_J;keyCode=_J;publicKey=_J;need_login=_s;phone=_J;codeKey=_J;serialNo=_J;qrCodeSerial=_J;userInfo=_J;accountInfo=_J;powerUserList=_J;doorAccountDict={};cookie=[];timestamp=int(time.time()*1000);accessToken=_J;refreshToken=_J;token=_J;expirationDate=_J;refresh_interval=12;is_debug=_s
	def __init__(A,hass,config=_J):
		B=config;A.hass=hass;C=aiohttp.TCPConnector(ssl=_s);D=aiohttp.CookieJar(quote_cookie=True);A.session=aiohttp.ClientSession(cookie_jar=D,connector=C)
		if B is not _J:
			try:A.keyCode=B[_A8];A.publicKey=B[_AO];A.accessToken=B[_AZ];A.refreshToken=B[_Aa];A.token=B[_l];A.userInfo=B[_AC];A.powerUserList=B[_AP];A.doorAccountDict=B[_Ab];A.refresh_interval=B[_Ac];A.is_debug=B['is_debug']
			except Exception as E:LOGGER.error(E)
	async def save_data(A):B={};B[_A8]=A.keyCode;B[_AO]=A.publicKey;B[_AZ]=A.accessToken;B[_Aa]=A.refreshToken;B[_l]=A.token;B[_AC]=A.userInfo;B[_AP]=A.powerUserList;B[_Ab]=A.doorAccountDict;B[_Ac]=A.refresh_interval;B['is_debug']=A.is_debug;await async_save_to_store(A.hass,'state_grid.config',B)
	def encrypt_post_data(A,data):B={_Ad:A.accessToken[len(A.accessToken)//2:]if A.accessToken else'','_t':A.token[len(A.token)//2:]if A.token else'','_data':data,_f:A.timestamp};return A.encrypt_wapper_data(B)
	def encrypt_wapper_data(A,data):B=a(json_dumps(data),A.keyCode);return{_A:B+c(B+str(A.timestamp)),_AD:d(A.keyCode,A.publicKey),_f:str(A.timestamp)}
	def handle_request_result_message(E,api,result):
		D='message';C='resultMessage';A=result;B=_J
		if _A in A and _Q in A[_A]and C in A[_A][_Q]:B=A[_A][_Q][C]
		elif _Q in A and C in A[_Q]:B=A[_Q][C]
		elif D in A:B=A[D]
		else:B=json_dumps(A)
		if E.is_debug:LOGGER.error(api+': '+B);LOGGER.error(json_dumps(A))
		return B
	async def fetch(B,api,data,header=_J):
		T='encryptData';S='464606a4-184c-4beb-b442-2ab7761d0796';R='key_code';Q='state';P='sign';O='grant_type';N='application/json;charset=UTF-8';M='Content-Type';L=header;K='client_secret';I='client_id';E=api;B.timestamp=int(time.time()*1000);D=B.timestamp
		if B.keyCode is _J:B.keyCode=e(32,16,2)
		F=B.keyCode;G={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36','Accept':N,M:N,'version':'1.0',_E:'0901',_f:str(D),'wsgwType':'web','appKey':appKey};A=data
		if E==get_request_key_api:A={I:appKey,K:appSecret};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AD:d(F,'042BC7AD510BF9793B7744C8854C56A8C95DD1027EE619247A332EC6ED5B279F435A23D62441FE861F4B0C963347ECD5792F380B64CA084BE8BE41151F8B8D19C8'),I:appKey,_f:str(D)}
		elif E==get_qr_code_api:A={_Ad:'','_t':'','_data':A,_f:D}
		elif E==get_request_authorize_api:
			A={I:appKey,'response_type':_H,_Ae:'/test',_f:D,'rsi':B.token};A=urllib.parse.urlencode(A);G[M]='application/x-www-form-urlencoded; charset=UTF-8';G[_A8]=F
			async with B.session.post(baseApi+E,data=A,headers=G)as J:B.session.cookie_jar.update_cookies(J.cookies);C=await J.json();C=b(C[_A],B.token);C=json.loads(C);return C
		elif E==get_web_token_api:A={O:'authorization_code',P:c(appKey+str(D)),K:appSecret,Q:S,R:F,I:appKey,_f:D,_H:A[_H]};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AD:d(F,B.publicKey),_f:str(D)}
		elif E==refresh_web_token_api:A={O:_AE,P:c(appKey+str(D)),K:appSecret,Q:S,R:F,I:appKey,_f:D,_AE:B.refreshToken};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AD:d(F,B.publicKey),_f:str(D)};E=get_web_token_api
		else:A=B.encrypt_post_data(A)
		if L is not _J:G.update(L)
		if E in sessionIdControlApiList:G['sessionId']='web'+str(D)
		if E in keyCodeControlApiList:G[_A8]=F
		if E in authControlApiList:G['Authorization']='Bearer '+B.accessToken[:len(B.accessToken)//2]
		if E in tControlApiList:G['t']=B.token[:len(B.token)//2]
		async with B.session.post(baseApi+E,json=A,headers=G)as J:
			C=await J.text()
			if C.startswith('{'):
				C=json.loads(C)
				if T in C:C=b(C[T],F);C=json.loads(C)
			return C
	async def __get_request_key(A):
		A.keyCode=_J;B=await A.fetch(get_request_key_api,{});C=A.handle_request_result_message('get_request_key_api',B)
		if B[_H]==_F:A.keyCode=B[_A][_A8];A.publicKey=B[_A][_AO];return{_B:0}
		return{_B:1,_e:C}
	async def __get_qr_code(B):
		C={_K:{_Z:'',_X:_t,_W:_M,_a:''},_y:{'optType':_c,_N:e(28,10,1)}};A=await B.fetch(get_qr_code_api,C);D=B.handle_request_result_message('get_qr_code_api',A)
		if A[_H]==1:
			if A[_A]and A[_A][_Q]and A[_A][_Q][_z]==_AF:B.qrCodeSerial=A[_A][_h][_Af];E=A[_A][_h]['qrCode'];return{_B:0,_A:E}
		return{_B:1,_e:D}
	async def __get_qr_code_status(B):
		C={_h:{_Af:B.qrCodeSerial}};D={_l:'98'+e(10,10,1)};A=await B.fetch(get_qr_code_status_api,C,D);E=B.handle_request_result_message('get_qr_code_status_api',A)
		if _H in A and A[_H]==1:
			if _A in A and A[_A]!='null':B.token=A[_A];return{_B:0}
			else:return{_B:1,_e:'未使用网上国网 App 扫码或确认登录'}
		return{_B:1,_e:E}
	async def __get_qr_code_token(B):
		C={_K:{_X:_t,_W:_M,'isEncrypt':True},_l:B.token};A=await B.fetch(get_qr_code_token_api,C);D=B.handle_request_result_message('get_qr_code_token_api',A)
		if _Q in A and _z in A[_Q]and A[_Q][_z]==_AF:B.userInfo=A[_h][_AC];return{_B:0}
		return{_B:1,_e:D}
	async def __send_code(B,phone):
		C=phone;B.phone=C;D={_K:{_Z:'',_X:_t,_W:_M,_a:''},_y:{'sendType':'0',_n:C,_Ag:'login','accountType':''},'Channels':'web'};A=await B.fetch(send_code_api,D);E=B.handle_request_result_message('send_code_api',A)
		if A[_H]==1:
			if A[_A]and A[_A][_Q]and A[_A][_Q][_z]==_AF:B.codeKey=A[_A][_h]['codeKey'];return{_B:0}
		return{_B:1,_e:E}
	async def __verfiy_code(A,code):
		C={_K:{_Z:'',_X:_t,_W:_M,_a:''},_y:{_n:A.phone,_Ag:'login',_H:code,'optSys':'ios','pushId':'00000','codeKey':A.codeKey},'Channels':'web'};B=await A.fetch(code_login_api,C);D=A.handle_request_result_message('code_login_api',B)
		if _Q in B and _z in B[_Q]and B[_Q][_z]==_AF:A.token=B[_h][_l];A.userInfo=B[_h][_AC][0];return{_B:0}
		return{_B:1,_e:D}
	async def __get_request_authorize(B):
		A=await B.fetch(get_request_authorize_api,{});E=B.handle_request_result_message('get_request_authorize_api',A)
		if _H in A and A[_H]==_F:C=A[_A][_Ae];D=C.rfind('code=');B.authorizeCode=C[D+5:D+5+32];return{_B:0}
		return{_B:1,_e:E}
	async def __get_web_token(A):
		C={_H:A.authorizeCode};B=await A.fetch(get_web_token_api,C);D=A.handle_request_result_message('get_web_token_api',B)
		if _H in B and B[_H]==_F:A.accessToken=B[_A][_Ah];A.refreshToken=B[_A][_AE];return{_B:0}
		return{_B:1,_e:D}
	async def __refresh_web_token(B):
		A=await B.fetch(refresh_web_token_api,{});C=B.handle_request_result_message('refresh_web_token_api',A)
		if _H in A and A[_H]==_F:B.accessToken=A[_A][_Ah];B.refreshToken=A[_A][_AE];return{_B:0}
		return{_B:1,_e:C}
	async def __get_door_number(B):
		C={_C:configuration[_C],_E:configuration[_E],_S:configuration[_S],_K:{_W:configuration[_A5][_K][_W],_Z:configuration[_A5][_K][_Z],_a:configuration[_A5][_K][_a],_X:configuration[_A5][_K][_X]},_y:{_R:B.userInfo[_R]},_l:B.token};A=await B.fetch(get_door_number_api,C);D=B.handle_request_result_message('get_door_number_api',A)
		if _H in A and A[_H]==1 and _A in A and _h in A[_A]:B.powerUserList=A[_A][_h][_AP];return{_B:0}
		return{_B:1,_e:D}
	async def __get_door_balance(C,door_account):
		A=door_account;E={_A:{_L:'',_N:'',_G:configuration[_n][_G],_D:configuration[_n][_D],_A0:C.userInfo[_R],_A1:C.userInfo[_A9],_T:_F,_d:_F,_AG:C.userInfo[_R],_A2:[{_Ai:A[_m],_AA:A[_U],_Aj:A[_AQ],_i:A[_i],_Y:A[_Y]}]},_C:_AK,_E:configuration[_E],_S:A[_U]};B=await C.fetch(get_door_balance_api,E);C.handle_request_result_message('get_door_balance_api',B)
		if _H in B and B[_H]==1 and _A in B and _A2 in B[_A]:
			D=B[_A][_A2]
			if len(D)!=0:A[_A3]=D[0]
	async def __get_door_bill(C,door_account,year):
		F='dataInfo';D='mothEleList';A=door_account;E={_A:{_L:'',_N:'',_G:configuration[_n][_G],_D:configuration[_n][_D],_A0:C.userInfo[_R],_A1:C.userInfo[_A9],_T:_F,_d:_F,_AG:C.userInfo[_R],_A2:[{_Ai:A[_m],_AA:A[_U],_Aj:A['consSortCode'],_i:A[_i],_Y:A[_Y]}]},_C:_AK,_E:configuration[_E],_S:A[_U]};E={_A:{_A0:C.userInfo[_R],_G:configuration[_G],_g:'11',_AR:A[_AQ],_D:'ALIPAY_01',_Y:A[_Y],_AA:A[_U],_d:_F,_T:_F,_N:'',_L:'',_A1:'',_Ak:A[_U],_AG:C.userInfo[_R],_i:A[_i],_Al:year},_C:_x,_E:_w,_S:A[_U]};B=await C.fetch(get_door_bill_api,E);C.handle_request_result_message('get_door_bill_api',B)
		if _H in B and B[_H]==1 and _A in B:
			if F in B[_A]:A[_AH]=B[_A][F]
			if D in B[_A]:A[_A4]=B[_A][D];A[_AI]=B[_A][D][-1]['month']
	async def __get_door_ladder(B,door_account,month):
		F='ladder_flag';E=month;A=door_account;G=A[_m];H={_A:{_G:configuration[_o][_G],_D:configuration[_o][_D],_T:configuration[_o][_T],_g:configuration[_o][_g],_i:A[_m],_d:A[_U],_Y:A[_Y],'queryDate':E,_Ak:A[_U],_AR:A[_AQ],_AG:B.userInfo[_R],_N:'',_L:'',_A1:B.userInfo[_A9],_A0:B.userInfo[_R]},_C:configuration[_o][_C],_E:configuration[_o][_E],_S:A[_U]};C=await B.fetch(get_door_ladder_api,H);I=B.handle_request_result_message('get_door_ladder_api',C)
		if _H in C and C[_H]==1 and _A in C and _A2 in C[_A]:
			D=C[_A][_A2]
			if len(D)!=0:
				D=D[0];D['month']=E
				if D['electricParticulars']['levelFlag']=='2':A[F]=1
				else:A[F]=0
				B.doorAccountDict[G]['ladder']=D
	async def __get_door_daily_bill(A,door_account,year,start_date,end_date):
		D='sevenEleList';C=door_account;E={'params1':{_C:configuration[_C],_E:configuration[_E],_S:configuration[_S],_K:{_W:configuration[_K][_W],_Z:configuration[_K][_Z],_a:configuration[_K][_a],_X:configuration[_K][_X]},_y:{_R:A.userInfo[_R]},_l:A.token},'params3':{_A:{_A0:A.userInfo[_R],_i:C[_m],_AR:_c,'endTime':end_date,_Y:C[_Y],_Al:year,_AA:C[_U],_N:'',_L:'','startTime':start_date,_A1:A.userInfo[_A9],_D:configuration[_j][_D],_G:configuration[_j][_G],_g:configuration[_j][_g],_d:configuration[_j][_d],_T:configuration[_j][_T]},_C:configuration[_j][_C],_E:configuration[_j][_E],_S:C[_U]},'params4':'010103'};B=await A.fetch(get_door_daily_bill_api,E);F=A.handle_request_result_message('get_door_daily_bill_api',B)
		if _H in B and B[_H]==1 and _A in B and D in B[_A]:C[_V]=B[_A][D]
	async def __get_door_pay_record(A,door_account):B=door_account;D=B[_m];C={'params1':{_C:configuration[_C],_E:configuration[_E],_S:configuration[_S],_K:{_W:configuration[_K][_W],_Z:configuration[_K][_Z],_a:configuration[_K][_a],_X:configuration[_K][_X]},_y:{_R:A.userInfo[_R]},_l:A.token},'params3':{_A:{_A0:A.userInfo[_R],'bgnPayDate':'2023-04-24',_G:configuration[_G],_i:B[_m],'endPayDate':'2024-04-24',_D:'webALIPAY_01','number':100,_Y:B[_Y],'page':_F,_AA:B[_U],_d:_F,_T:_F,_N:'',_L:'',_A1:A.userInfo[_A9]},_C:'0101051',_E:_c,_S:B[_U]},'params4':'010104'};E=await A.fetch(getJiaoFeiRecordApi,C)
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
		B.need_login=_s;await B.save_data();return{_B:0,_A:B.powerUserList}
	async def refresh_data(B,setup=_s):
		n='daily_t_ele_num';m='daily_n_ele_num';l='daily_v_ele_num';k='daily_p_ele_num';j='daily_ele_num';i='last_month_ele_cost';h='last_month_ele_num';g='year_ele_cost';f='year_ele_num';e='monthEleNum';d='thisTPq';c='thisNPq';b='thisVPq';a='thisPPq';R='ladder_level_num';Q='ladder_level';L='balance';K='%Y%m%d';J='day';H='dayElePq'
		if B.need_login is True:LOGGER.error('国家电网需要重新登录！');return
		o=setup or int(time.time()*1000)-B.timestamp>B.refresh_interval*3600*1000
		if o is _s:return
		D=await B.__get_door_number()
		if _B in D and D[_B]!=0:
			LOGGER.warning('刷新 Token');D=await B.__get_request_key()
			if _B in D and D[_B]!=0:return
			D=await B.__refresh_web_token()
			if _B in D and D[_B]==0:await B.save_data()
			else:B.need_login=True;LOGGER.error('刷新 Token 失败');return
			D=await B.__get_door_number()
			if _B in D and D[_B]!=0:B.need_login=True;LOGGER.error('重新请求失败');return
		M=datetime.datetime.now();I=M-datetime.timedelta(days=1);p=f"{I.year}-{I.month:02d}-{I.day:02d}";N=I-datetime.timedelta(days=40);q=f"{N.year}-{N.month:02d}-{N.day:02d}"
		for A in B.powerUserList:
			r=A[_m];B.doorAccountDict[r]=A;await B.__get_door_balance(A);await B.__get_door_daily_bill(A,M.year,q,p);O=A[_V][0]
			try:float(O[H])
			except:A[_V].pop(0)
			O=A[_V][0];E=datetime.datetime.strptime(O[J],K);S=0;T=0;U=0;V=0;W=0
			for C in A[_V]:
				G=datetime.datetime.strptime(C[J],K)
				if G.month!=E.month:break
				S+=catchFloat(C,H);T+=catchFloat(C,a);U+=catchFloat(C,b);V+=catchFloat(C,c);W+=catchFloat(C,d)
			P=E-datetime.timedelta(days=E.day);X=f"{P.year}-{P.month:02d}"
			if _AI not in A or A[_AI]!=X:await B.__get_door_bill(A,P.year);await B.__get_door_ladder(A,X)
			s=datetime.datetime.strptime(A[_AI],'%Y%m')
			if s.month==12:
				F=0
				for C in A[_V]:
					G=datetime.datetime.strptime(C[J],K)
					if G.month!=12:break
					F+=catchFloat(C,H)
			else:
				F=0
				for C in A[_A4]:F+=catchFloat(C,e)
				t=len(A[_A4])
				for C in A[_V]:
					G=datetime.datetime.strptime(C[J],K)
					if G.month<=t:break
					F+=catchFloat(C,H)
			if F<=2760:A[Q]='第一阶梯';A[R]=1
			elif F<=4800:A[Q]='第二阶梯';A[R]=2
			else:A[Q]='第三阶梯';A[R]=3
			if _A3 in A:
				u=catchFloat(A[_A3],'estiAmt');Y=catchFloat(A[_A3],'prepayBal');v=catchFloat(A[_A3],'sumMoney')
				if Y==0:A[L]=v
				else:A[L]=Y-u
				Z=catchFloat(A[_A3],'historyOwe')
				if Z>0:A[L]=-Z
			else:A[L]=0
			if _AH in A:A[f]=catchFloat(A[_AH],'totalEleNum');A[g]=catchFloat(A[_AH],'totalEleCost')
			else:A[f]=0;A[g]=0
			if _A4 in A:A[h]=catchFloat(A[_A4][-1],e);A[i]=catchFloat(A[_A4][-1],'monthEleCost')
			else:A[h]=0;A[i]=0
			if _V in A:A[j]=catchFloat(A[_V][0],H);A[k]=catchFloat(A[_V][0],a);A[l]=catchFloat(A[_V][0],b);A[m]=catchFloat(A[_V][0],c);A[n]=catchFloat(A[_V][0],d)
			else:A[j]=0;A[k]=0;A[l]=0;A[m]=0;A[n]=0
			A['month_ele_num']=S;A['month_p_ele_num']=T;A['month_v_ele_num']=U;A['month_n_ele_num']=V;A['month_t_ele_num']=W;A['daily_lasted_date']=f"{E.year}-{E.month:02d}-{E.day:02d}";A['refresh_time']=datetime.datetime.strftime(M,'%Y-%m-%d %H:%M:%S')
		await B.save_data()
	async def get_door_account_list(A):return list(A.doorAccountDict.values())
	def get_door_account(A):return A.doorAccountDict