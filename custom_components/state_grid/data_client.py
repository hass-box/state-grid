_B5='get_door_daily_bill_api'
_B4='startTime'
_B3='constType'
_B2='provinceCode'
_B1='access_token'
_B0='businessType'
_A_='qrCodeSerial'
_Az='redirect_url'
_Ay='_access_token'
_Ax='dataVersion'
_Aw='refresh_interval'
_Av='doorAccountDict'
_Au='refreshToken'
_At='accessToken'
_As='/osg-web0004/member/c24/f01'
_Ar='BCP_00026'
_Aq='serviceCode_smt'
_Ap='WEBA10070900'
_Ao='serviceType'
_An='jM_custType'
_Am='jM_busiTypeCode'
_Al='doorNumberManeger'
_Ak='month_t_ele_num'
_Aj='month_n_ele_num'
_Ai='month_v_ele_num'
_Ah='month_p_ele_num'
_Ag='month_ele_num'
_Af='thisTPq'
_Ae='thisNPq'
_Ad='thisVPq'
_Ac='thisPPq'
_Ab='%Y%m%d'
_Aa='params4'
_AZ='params3'
_AY='params1'
_AX='queryYear'
_AW='userAccountId'
_AV='elecTypeCode'
_AU='powerUserList'
_AT='publicKey'
_AS='WEBA10070800'
_AR='timeDay'
_AQ='WEBA10070700'
_AP='channelNo'
_AO='dayElePq'
_AN='sevenEleList'
_AM='month'
_AL='yearTotalCost'
_AK='consType'
_AJ='0000'
_AI='refresh_token'
_AH='skey'
_AG='userInfo'
_AF='0101046'
_AE='billYear'
_AD='proCode'
_AC='loginAccount'
_AB='list'
_AA='keyCode'
_A9='querytypeCode'
_A8='01010049'
_A7='account'
_A6='daily_bill_list'
_A5='account_balance'
_A4='provinceId'
_A3='userName'
_A2='acctId'
_A1='resultCode'
_A0='BCP_000026'
_z='app'
_y='WEBALIPAY_01'
_x='order'
_w='state_grid'
_v='latestBillMonth'
_u='quInfo'
_t='authFlag'
_s='09'
_r='0101183'
_q='stepelect'
_p='consNo'
_o=True
_n='0101154'
_m='monthBillList'
_l='bizrt'
_k='token'
_j='timestamp'
_i=False
_h='month_ele'
_g='consNo_dst'
_f='errmsg'
_e='clearCache'
_d='SGAPP'
_c='orgNo'
_b='promotCode'
_a='01'
_Z='devciceId'
_Y='devciceIp'
_X='proNo'
_W='tenant'
_V='member'
_U='promotType'
_T='getday'
_S='srvrt'
_R='userId'
_Q='subBusiTypeCode'
_P='target'
_O='serCat'
_N='serialNo'
_M='0902'
_L='srvCode'
_K='busiTypeCode'
_J='uscInfo'
_I='channelCode'
_H='code'
_G='1'
_F=None
_E='source'
_D='funcCode'
_C='errcode'
_B='serviceCode'
_A='data'
import json,time,aiohttp,urllib.parse,datetime
from.const import VERSION
from.utils.logger import LOGGER
from.utils.store import async_save_to_store
from.utils.crypt import a,b,c,d,e
configuration={_J:{_V:_M,_Y:'',_Z:'',_W:_w},_E:_d,_P:'32101',_I:_M,_AP:_M,'toPublish':_a,'siteId':'2012000000033700',_L:'',_N:'',_D:'',_B:{_x:_n,'uploadPic':'0101296','pauseSCode':'0101250','pauseTCode':'0101251','listconsumers':'0101093','messageList':'0101343','submit':'0101003','sbcMsg':'0101210','powercut':'0104514','BkAuth01':'f15','BkAuth02':'f18','BkAuth03':'f02','BkAuth04':'f17','BkAuth05':'f05','BkAuth06':'f16','BkAuth07':'f01','BkAuth08':'f03'},'electricityArchives':{'servicecode':'0104505',_E:_M},'subscriptionList':{_L:'APP_SGPMS_05_030',_N:'22',_I:_M,_D:'22',_P:'-1'},'userInformation':{_B:'01008183',_E:_d},'userInform':{_B:_r,_E:_d},'elesum':{_I:_M,_D:_y,_b:_G,_U:_G,_B:'0101143',_E:_z},_A7:{_I:_M,_D:'WEBA1007200'},_Al:{_E:_M,_P:'-1',_I:_s,_AP:_s,_B:_A8,_D:'WEBA40050000',_J:{_V:_M,_Y:'',_Z:'',_W:_w}},'doorAuth':{_E:_d,_B:'f04'},'xinZ':{_O:'101',_Am:'101','fJ_busiTypeCode':'102',_An:'03','fJ_custType':'02',_Ao:_a,_Q:'',_D:_AQ,_x:_n,_E:_d,_A9:_G},'onedo':{_B:_AF,_E:_d,_D:_AQ,'queryType':'03'},'xinHuTongDian':{_O:'110',_K:'211',_Q:'21102',_D:'WEBA10071200',_I:_M,_E:_s,_B:_r},'company':{_O:'104',_D:_AQ,_Ao:'02',_A9:_G,_t:_G,_E:_d,_x:_n},'charge':{_I:_s,_D:'WEBA10071300',_AP:'0901',_O:'102',_An:_a,_Am:'102'},'other':{_I:_s,_D:'WEBA10079700',_O:'129',_K:'999',_Q:'21501',_B:_A0,_L:'',_N:''},'vatchange':{'submit':'0101003',_K:'320',_Q:'',_O:'115',_D:'WEBA10074000',_t:_G},'bill':{_e:_G,_D:_y,_U:_G,_B:_A0},_q:{_I:_M,_D:_y,_U:_G,_e:_s,_B:_A0,_E:_z},_T:{_I:_M,_e:'11',_D:_y,_b:_G,_U:_G,_B:_A0,_E:_z},'mouthOut':{_I:_M,_e:'11',_D:_y,_b:_G,_U:_G,_B:_A0,_E:_z},'meter':{_O:'114',_K:'304',_D:'WEBA10071000',_Q:'',_B:_AF,_N:''},'complaint':{_K:'005','srvMode':_M,'anonymousFlag':'0','replyMode':_a,'retvisitFlag':_a},'report':{_K:'006'},'tradewinds':{_K:'019'},'somesay':{_K:'091'},'faultrepair':{_D:_Ap,_B:_r,_O:'111',_K:'001',_Q:'21505'},'electronicInvoice':{_O:'105',_K:'0'},'rename':{_B:_AF,_D:'WEBA10076100',_K:'210',_O:'109',_t:_G,'gh_busiTypeCode':'211','gh_subusi':'21101',_N:'',_L:''},'pause':{_Q:'',_B:_A8,_D:'WEBA10073600',_O:'107',_K:'203','jr_busi':'201',_N:'',_L:''},'capacityRecovery':{_B:_A8,_E:_d,_L:'',_N:'',_D:'WEBA10073700','busiTypeCode_stop':'204','busiTypeCode_less':'202',_K:'202',_Q:'',_O:'108',_AR:'5',_t:_G},'electricityPriceChange':{_B:_r,_K:'215',_Q:'21502',_O:'113',_t:_G,_AR:'15',_D:'WEBA10073900WEB',_L:'',_N:''},'electricityPriceStrategyChange':{_B:'01008183',_K:'215',_Q:'21506',_O:'160',_D:'WEBV00000517WEB',_L:'',_N:''},'eemandValueAdjustment':{_B:_r,_L:'',_N:'',_O:'112',_D:'WEBA10073800',_K:'215',_Q:'21504',_t:_G,_AR:'5','getMonthServiceCode':_AF},'businessProgress':{_B:_r,_L:_a,_D:'WEB01'},'increase':{_E:_d,_N:'',_L:'',_Aq:_A8,_B:_n,_x:_n,_D:_AS,_A9:_G,_O:'106',_K:'111',_Q:''},'fjincrea':{_O:'105',_K:'110',_Q:'',_E:_d,_D:_AS,_N:'',_L:'',_Aq:_A8,_B:_n,_x:_n,_A9:_G},'persIncrea':{_O:'105',_K:'109',_x:_n,_Q:'',_E:_d,_D:_AS,_A9:_G},'fgdChange':{_B:_r,_L:_a,_I:_s,_D:_Ap,_K:'215',_Q:'21505',_O:'111',_t:_G},'createOrder':{_I:_M,_D:_y,_L:'BCP_000001','chargeMode':'02','conType':_a,'bizTypeId':'BT_ELEC'},'largePopulation':{_K:'383',_D:'WEBA10076800',_Q:'',_L:'',_U:'',_b:'',_I:'0901',_O:'383',_B:'',_N:''},'biaoJiCode':{_B:'0104507',_E:'1704',_I:'1704'},'twoGuar':{_K:'402',_Q:'40201',_D:'web_twoGuar'},'electTrend':{_B:_Ar,_I:_M},'emergency':{_B:_Ar,_D:'A10000000',_I:_M},'infoPublic':{_B:'2545454',_E:_z}}
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
getJiaoFeiRecordApi=_As
get_door_daily_bill_api=_As
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
			try:A.keyCode=B[_AA];A.publicKey=B[_AT];A.accessToken=B[_At];A.refreshToken=B[_Au];A.token=B[_k];A.userInfo=B[_AG];A.powerUserList=B[_AU];A.doorAccountDict=B[_Av];A.refresh_interval=B[_Aw];A.is_debug=B['is_debug'];A.dataVersion=B[_Ax]
			except Exception as E:LOGGER.error(E)
	async def save_data(B):A={};A[_AA]=B.keyCode;A[_AT]=B.publicKey;A[_At]=B.accessToken;A[_Au]=B.refreshToken;A[_k]=B.token;A[_AG]=B.userInfo;A[_AU]=B.powerUserList;A[_Av]=B.doorAccountDict;A[_Aw]=B.refresh_interval;A['is_debug']=B.is_debug;A[_Ax]=VERSION;await async_save_to_store(B.hass,'state_grid.config',A)
	def encrypt_post_data(A,data):B={_Ay:A.accessToken[len(A.accessToken)//2:]if A.accessToken else'','_t':A.token[len(A.token)//2:]if A.token else'','_data':data,_j:A.timestamp};return A.encrypt_wapper_data(B)
	def encrypt_wapper_data(A,data):B=a(json_dumps(data),A.keyCode);return{_A:B+c(B+str(A.timestamp)),_AH:d(A.keyCode,A.publicKey),_j:str(A.timestamp)}
	def handle_request_result_message(E,api,result):
		D='message';C='resultMessage';A=result;B=_F
		if _A in A and _S in A[_A]and C in A[_A][_S]:B=A[_A][_S][C]
		elif _S in A and C in A[_S]:B=A[_S][C]
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
		if E==get_request_key_api:A={I:appKey,K:appSecret};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AH:d(F,'042BC7AD510BF9793B7744C8854C56A8C95DD1027EE619247A332EC6ED5B279F435A23D62441FE861F4B0C963347ECD5792F380B64CA084BE8BE41151F8B8D19C8'),I:appKey,_j:str(D)}
		elif E==get_qr_code_api:A={_Ay:'','_t':'','_data':A,_j:D}
		elif E==get_request_authorize_api:
			A={I:appKey,'response_type':_H,_Az:'/test',_j:D,'rsi':B.token};A=urllib.parse.urlencode(A);G[M]='application/x-www-form-urlencoded; charset=UTF-8';G[_AA]=F
			async with B.session.post(baseApi+E,data=A,headers=G)as J:B.session.cookie_jar.update_cookies(J.cookies);C=await J.json();C=b(C[_A],B.token);C=json.loads(C);return C
		elif E==get_web_token_api:A={O:'authorization_code',P:c(appKey+str(D)),K:appSecret,Q:S,R:F,I:appKey,_j:D,_H:A[_H]};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AH:d(F,B.publicKey),_j:str(D)}
		elif E==refresh_web_token_api:A={O:_AI,P:c(appKey+str(D)),K:appSecret,Q:S,R:F,I:appKey,_j:D,_AI:B.refreshToken};H=a(json_dumps(A),F);A={_A:H+c(H+str(D)),_AH:d(F,B.publicKey),_j:str(D)};E=get_web_token_api
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
		if B[_H]==_G:A.keyCode=B[_A][_AA];A.publicKey=B[_A][_AT];return{_C:0}
		return{_C:1,_f:C}
	async def __get_qr_code(B):
		C={_J:{_Y:'',_W:_w,_V:_M,_Z:''},_u:{'optType':_a,_N:e(28,10,1)}};A=await B.__fetch(get_qr_code_api,C);D=B.handle_request_result_message('get_qr_code_api',A)
		if A[_H]==1:
			if A[_A]and A[_A][_S]and A[_A][_S][_A1]==_AJ:B.qrCodeSerial=A[_A][_l][_A_];E=A[_A][_l]['qrCode'];return{_C:0,_A:E}
		return{_C:1,_f:D}
	async def __get_qr_code_status(B):
		C={_l:{_A_:B.qrCodeSerial}};D={_k:'98'+e(10,10,1)};A=await B.__fetch(get_qr_code_status_api,C,D);E=B.handle_request_result_message('get_qr_code_status_api',A)
		if _H in A and A[_H]==1:
			if _A in A and A[_A]!='null':B.token=A[_A];return{_C:0}
			else:return{_C:1,_f:'未使用网上国网 App 扫码或确认登录'}
		return{_C:1,_f:E}
	async def __get_qr_code_token(B):
		C={_J:{_W:_w,_V:_M,'isEncrypt':_o},_k:B.token};A=await B.__fetch(get_qr_code_token_api,C);D=B.handle_request_result_message('get_qr_code_token_api',A)
		if _S in A and _A1 in A[_S]and A[_S][_A1]==_AJ:B.userInfo=A[_l][_AG];return{_C:0}
		return{_C:1,_f:D}
	async def __send_code(B,phone):
		C=phone;B.phone=C;D={_J:{_Y:'',_W:_w,_V:_M,_Z:''},_u:{'sendType':'0',_A7:C,_B0:'login','accountType':''},'Channels':'web'};A=await B.__fetch(send_code_api,D);E=B.handle_request_result_message('send_code_api',A)
		if A[_H]==1:
			if A[_A]and A[_A][_S]and A[_A][_S][_A1]==_AJ:B.codeKey=A[_A][_l]['codeKey'];return{_C:0}
		return{_C:1,_f:E}
	async def __verfiy_code(A,code):
		C={_J:{_Y:'',_W:_w,_V:_M,_Z:''},_u:{_A7:A.phone,_B0:'login',_H:code,'optSys':'ios','pushId':'00000','codeKey':A.codeKey},'Channels':'web'};B=await A.__fetch(code_login_api,C);D=A.handle_request_result_message('code_login_api',B)
		if _S in B and _A1 in B[_S]and B[_S][_A1]==_AJ:A.token=B[_l][_k];A.userInfo=B[_l][_AG][0];return{_C:0}
		return{_C:1,_f:D}
	async def __get_request_authorize(B):
		A=await B.__fetch(get_request_authorize_api,{});E=B.handle_request_result_message('get_request_authorize_api',A)
		if _H in A and A[_H]==_G:C=A[_A][_Az];D=C.rfind('code=');B.authorizeCode=C[D+5:D+5+32];return{_C:0}
		return{_C:1,_f:E}
	async def __get_web_token(A):
		C={_H:A.authorizeCode};B=await A.__fetch(get_web_token_api,C);D=A.handle_request_result_message('get_web_token_api',B)
		if _H in B and B[_H]==_G:A.accessToken=B[_A][_B1];A.refreshToken=B[_A][_AI];return{_C:0}
		return{_C:1,_f:D}
	async def __refresh_web_token(B):
		A=await B.__fetch(refresh_web_token_api,{});C=B.handle_request_result_message('refresh_web_token_api',A)
		if _H in A and A[_H]==_G:B.accessToken=A[_A][_B1];B.refreshToken=A[_A][_AI];return{_C:0}
		return{_C:1,_f:C}
	async def __get_door_number(A):
		B=configuration[_Al];G={_B:B[_B],_E:B[_E],_P:B[_P],_J:{_V:B[_J][_V],_Y:B[_J][_Y],_Z:B[_J][_Z],_W:B[_J][_W]},_u:{_R:A.userInfo[_R]},_k:A.token};C=await A.__fetch_safe(get_door_number_api,G);H=A.handle_request_result_message('get_door_number_api',C)
		if _H in C and C[_H]==1 and _A in C and _l in C[_A]:
			E={}
			if A.powerUserList is not _F:E={A[_g]:A for A in A.powerUserList}
			F=[]
			for D in C[_A][_l][_AU]:
				if D[_g]in E:F.append(E[D[_g]])
				elif _AV in D and D[_AV]!='05':F.append(D)
			A.powerUserList=F;return{_C:0}
		return{_C:1,_f:H}
	async def __get_door_balance(B,door_account):
		A=door_account;E={_A:{_L:'',_N:'',_I:configuration[_A7][_I],_D:configuration[_A7][_D],_A2:B.userInfo[_R],_A3:B.userInfo.get(_AC,B.userInfo.get('nickname',_F)),_U:_G,_b:_G,_AW:B.userInfo[_R],_AB:[{'consNoSrc':A[_g],_AD:A.get(_X,A.get(_A4,_F)),'sceneType':A.get('consSortCode',A.get(_AV,_F)),_p:A[_p],_c:A[_c]}]},_B:'0101143',_E:configuration[_E],_P:A.get(_X,A.get(_A4,_F))};C=await B.__fetch_safe(get_door_balance_api,E);B.handle_request_result_message('get_door_balance_api',C)
		if _H in C and C[_H]==1 and _A in C and _AB in C[_A]:
			D=C[_A][_AB]
			if len(D)!=0:A[_A5]=D[0]
	async def __get_door_bill(C,door_account,monthDate):
		I='dataInfo';G='mothEleList';E=monthDate;A=door_account;J={_A:{_A2:C.userInfo[_R],_I:configuration[_I],_e:'11',_AK:A[_B3],_D:'ALIPAY_01',_c:A[_c],_AD:A[_X],_b:_G,_U:_G,_N:'',_L:'',_A3:'',_B2:A[_X],_AW:C.userInfo[_R],_p:A[_p],_AX:E.year},_B:_A0,_E:_z,_P:A[_X]};B=await C.__fetch_safe(get_door_bill_api,J);C.handle_request_result_message('get_door_bill_api',B)
		if _H in B and B[_H]==1 and _A in B:
			if I in B[_A]:A[_AL]=B[_A][I]
			if G in B[_A]:
				if _AE not in A or A[_AE]!=E.year:A[_m]=B[_A][G];A[_AE]=E.year
				else:
					F={A.month:A for A in A[_m]};H=B[_A][G]
					for D in H:
						if D.month in F and _h in F[D.month]:D[_h]=F[D.month][_h]
					A[_m]=H
				if len(A[_m])>0:A[_v]=A[_m][-1]
	async def __get_door_ladder(C,door_account,monthBill):
		E=monthBill;A=door_account;I=A[_g];F=datetime.datetime.strptime(E[_AM],'%Y%m');G=f"{F.year}-{F.month:02d}";H={_A:{_I:configuration[_q][_I],_D:configuration[_q][_D],_U:configuration[_q][_U],_e:configuration[_q][_e],_p:A[_g],_b:A[_X],_c:A[_c],'queryDate':G,_B2:A[_X],_AK:A[_B3],_AW:C.userInfo[_R],_N:'',_L:'',_A3:C.userInfo[_AC],_A2:C.userInfo[_R]},_B:configuration[_q][_B],_E:configuration[_q][_E],_P:A[_X]};B=await C.__fetch(get_door_ladder_api,H);J=C.handle_request_result_message('get_door_ladder_api',B)
		if _H in B and B[_H]==1 and _A in B and _AB in B[_A]:
			D=B[_A][_AB]
			if len(D)!=0:D=D[0];E['ladder']=D
	async def __get_door_mouth_daily_bill(B,door_account,monthBill):
		I=monthBill;C=door_account;A=datetime.datetime.strptime(I[_AM],'%Y%m');H=datetime.date(A.year,A.month,1)
		if A.month==12:D=datetime.date(A.year+1,1,1)
		else:D=datetime.date(A.year,A.month+1,1)
		D=D-datetime.timedelta(days=1);O=f"{H.year}-{H.month:02d}-{H.day:02d}";P=f"{D.year}-{D.month:02d}-{D.day:02d}";Q={_AY:{_B:configuration[_B],_E:configuration[_E],_P:configuration[_P],_J:{_V:configuration[_J][_V],_Y:configuration[_J][_Y],_Z:configuration[_J][_Z],_W:configuration[_J][_W]},_u:{_R:B.userInfo[_R]},_k:B.token},_AZ:{_A:{_A2:B.userInfo[_R],_p:C[_g],_AK:_a,'endTime':P,_c:C[_c],_AX:str(A.year),_AD:C.get(_X,C.get(_A4,_F)),_N:'',_L:'',_B4:O,_A3:B.userInfo[_AC],_D:configuration[_T][_D],_I:configuration[_T][_I],_e:configuration[_T][_e],_b:configuration[_T][_b],_U:configuration[_T][_U]},_B:configuration[_T][_B],_E:configuration[_T][_E],_P:C.get(_X,C.get(_A4,_F))},_Aa:'010103'};E=await B.__fetch_safe(get_door_daily_bill_api,Q);R=B.handle_request_result_message(_B5,E)
		if _H in E and E[_H]==1 and _A in E and _AN in E[_A]:
			J=0;K=0;L=0;M=0;N=0
			for F in E[_A][_AN]:S=datetime.datetime.strptime(F['day'],_Ab);J+=catchFloat(F,_AO);K+=catchFloat(F,_Ac);L+=catchFloat(F,_Ad);M+=catchFloat(F,_Ae);N+=catchFloat(F,_Af)
			G={};G[_Ag]=normal_round(J,2);G[_Ah]=normal_round(K,2);G[_Ai]=normal_round(L,2);G[_Aj]=normal_round(M,2);G[_Ak]=normal_round(N,2);I[_h]=G
	async def __get_door_daily_bill(B,door_account,year,start_date,end_date):
		A=door_account;D={_AY:{_B:configuration[_B],_E:configuration[_E],_P:configuration[_P],_J:{_V:configuration[_J][_V],_Y:configuration[_J][_Y],_Z:configuration[_J][_Z],_W:configuration[_J][_W]},_u:{_R:B.userInfo[_R]},_k:B.token},_AZ:{_A:{_A2:B.userInfo[_R],_p:A[_g],_AK:_a,'endTime':end_date,_c:A[_c],_AX:year,_AD:A.get(_X,A.get(_A4,_F)),_N:'',_L:'',_B4:start_date,_A3:B.userInfo[_AC],_D:configuration[_T][_D],_I:configuration[_T][_I],_e:configuration[_T][_e],_b:configuration[_T][_b],_U:configuration[_T][_U]},_B:configuration[_T][_B],_E:configuration[_T][_E],_P:A.get(_X,A.get(_A4,_F))},_Aa:'010103'};C=await B.__fetch_safe(get_door_daily_bill_api,D);E=B.handle_request_result_message(_B5,C)
		if _H in C and C[_H]==1 and _A in C and _AN in C[_A]:A[_A6]=C[_A][_AN]
	async def __get_door_pay_record(A,door_account):B=door_account;D=B[_g];C={_AY:{_B:configuration[_B],_E:configuration[_E],_P:configuration[_P],_J:{_V:configuration[_J][_V],_Y:configuration[_J][_Y],_Z:configuration[_J][_Z],_W:configuration[_J][_W]},_u:{_R:A.userInfo[_R]},_k:A.token},_AZ:{_A:{_A2:A.userInfo[_R],'bgnPayDate':'2023-04-24',_I:configuration[_I],_p:B[_g],'endPayDate':'2024-04-24',_D:'webALIPAY_01','number':100,_c:B[_c],'page':_G,_AD:B[_X],_b:_G,_U:_G,_N:'',_L:'',_A3:A.userInfo[_AC]},_B:'0101051',_E:_a,_P:B[_X]},_Aa:'010104'};E=await A.__fetch(getJiaoFeiRecordApi,C)
	async def get_qr_code(B):
		A=await B.__get_request_key()
		if _C in A and A[_C]!=0:return A
		return await B.__get_qr_code()
	async def check_qr_code(B):
		A=await B.__get_qr_code_status()
		if _C in A and A[_C]!=0:return A
		A=await B.__get_qr_code_token()
		if _C in A and A[_C]!=0:return A
		return await B.__get_token()
	async def send_phone_code(B,phone):
		A=await B.__get_request_key()
		if _C in A and A[_C]!=0:return A
		return await B.__send_code(phone)
	async def verfiy_phone_code(B,code):
		A=await B.__verfiy_code(code)
		if _C in A and A[_C]!=0:return A
		return await B.__get_token()
	async def __get_token(B):
		A=await B.__get_request_key()
		if _C in A and A[_C]!=0:return A
		A=await B.__get_request_authorize()
		if _C in A and A[_C]!=0:return A
		A=await B.__get_web_token()
		if _C in A and A[_C]!=0:return A
		A=await B.__get_door_number()
		if _C in A and A[_C]!=0:return A
		B.need_login=_i;await B.save_data();return{_C:0,_A:B.powerUserList}
	async def __refresh_token(A):
		B=await A.__get_request_key()
		if _C in B and B[_C]!=0:return
		B=await A.__refresh_web_token()
		if _C in B and B[_C]==0:A.need_login=_i;A.retry_times=0;await A.save_data()
		elif A.retry_times>=3:A.need_login=_o
		else:A.retry_times=A.retry_times+1
	async def refresh_data(B,setup=_i,force_refresh=_i):
		p='last_month_ele_cost';o='year_ele_cost';n='%Y-%m-%d %H:%M:%S';b=setup;a='last_month_ele_num';Z='daily_lasted_date';Y='refresh_time';U='year_ele_num';G='balance'
		if b is _o:
			if B.dataVersion!=VERSION:B.powerUserList=_F
			c=await B.__get_door_number()
			if _C in c and c[_C]!=0:B.need_login=_o
		if B.need_login is _o:
			if B.powerUserList is not _F:
				for A in B.get_door_account_list():A[Y]='Token刷新失败，请重新登录'
			LOGGER.error('国家电网 - Token刷新失败，请重新登录！');return
		q=b or force_refresh or int(time.time()*1000)-B.timestamp>B.refresh_interval*3600*1000
		if q is _i:return
		H=datetime.datetime.now();F=H-datetime.timedelta(days=1);d=f"{F.year}-{F.month:02d}-{F.day:02d}";V=F-datetime.timedelta(days=40);r=f"{V.year}-{V.month:02d}-{V.day:02d}"
		for A in B.powerUserList:
			s=A[_g];B.doorAccountDict[s]=A
			if Z in A and A[Z]==d:A[Y]=datetime.datetime.strftime(H,n);continue
			await B.__get_door_balance(A)
			if B.retry_times!=0:return
			if _A5 in A:
				t=catchFloat(A[_A5],'estiAmt');W=catchFloat(A[_A5],'prepayBal');e=catchFloat(A[_A5],'sumMoney')
				if W==0 or W==e:A[G]=e
				else:A[G]=W-t
				f=catchFloat(A[_A5],'historyOwe')
				if f>0:A[G]=-f
			else:LOGGER.error('国家电网账户余额获取失败！')
			if G not in A:A[G]=0
			await B.__get_door_daily_bill(A,H.year,r,d)
			if _A6 not in A:LOGGER.error('国家电网无法获取日用电数据！');continue
			X=0;I=_i
			for g in range(10):
				D=A[_A6][g]
				try:float(D[_AO]);I=_o;break
				except:X=X+1
			h=0;i=0;j=0;k=0;l=0
			if I:
				for g in range(X):A[_A6].pop(0)
				D=A[_A6][0];E=datetime.datetime.strptime(D['day'],_Ab);A[Z]=f"{E.year}-{E.month:02d}-{E.day:02d}";h=catchFloat(D,_AO);i=catchFloat(D,_Ac);j=catchFloat(D,_Ad);k=catchFloat(D,_Ae);l=catchFloat(D,_Af)
			A['daily_ele_num']=normal_round(h,2);A['daily_p_ele_num']=normal_round(i,2);A['daily_v_ele_num']=normal_round(j,2);A['daily_n_ele_num']=normal_round(k,2);A['daily_t_ele_num']=normal_round(l,2);J=0;K=0;L=0;M=0;N=0
			if I:
				for C in A[_A6]:
					u=datetime.datetime.strptime(C['day'],_Ab)
					if u.month!=E.month:break
					J+=catchFloat(C,_AO);K+=catchFloat(C,_Ac);L+=catchFloat(C,_Ad);M+=catchFloat(C,_Ae);N+=catchFloat(C,_Af)
			A[_Ag]=normal_round(J,2);A[_Ah]=normal_round(K,2);A[_Ai]=normal_round(L,2);A[_Aj]=normal_round(M,2);A[_Ak]=normal_round(N,2)
			if I:
				O=E-datetime.timedelta(days=E.day);v=f"{O.year}{O.month:02d}"
				if _AE not in A or A[_AE]!=O.year or _v not in A or A[_v][_AM]!=v:await B.__get_door_bill(A,O)
				if _m in A:
					for C in A[_m]:
						if _h not in C:await B.__get_door_mouth_daily_bill(A,C)
			if _AL in A:A[U]=catchFloat(A[_AL],'totalEleNum');A[o]=catchFloat(A[_AL],'totalEleCost')
			if U not in A:A[U]=0;A[o]=0
			if _v in A:A[a]=catchFloat(A[_v],'monthEleNum');A[p]=catchFloat(A[_v],'monthEleCost');m=datetime.datetime.strptime(A[_v][_AM],'%Y%m')
			if a not in A:A[a]=0;A[p]=0;m=F.month
			P=0;Q=0;R=0;S=0;T=0
			if m.month==12:P=J;Q=K;R=L;S=M;T=N
			else:
				if _m in A:
					for C in A[_m]:
						if _h in C:P+=C[_h][_Ag];Q+=C[_h][_Ah];R+=C[_h][_Ai];S+=C[_h][_Aj];T+=C[_h][_Ak]
				P+=J;Q+=K;R+=L;S+=M;T+=N
			A[U]=normal_round(P,2);A['year_p_ele_num']=normal_round(Q,2);A['year_v_ele_num']=normal_round(R,2);A['year_n_ele_num']=normal_round(S,2);A['year_t_ele_num']=normal_round(T,2);A[Y]=datetime.datetime.strftime(H,n)
		await B.save_data()
	def get_door_account_list(A):return list(A.doorAccountDict.values())
	def get_door_account(A):return A.doorAccountDict