_G='Data length error!'
_F='%08x'
_E='utf8'
_D='%%0%dx'
_C=None
_B='utf-8'
_A='p'
import random,urllib.parse,base64,binascii
from math import ceil
import copy
def str_to_bytes(input_str):
	A=[]
	for B in input_str:
		C=urllib.parse.quote(B)
		if len(C)==1:A.append(ord(B))
		else:
			for D in C.split('%')[1:]:A.append(int('0x'+D,16))
	return A
def bytes_to_hex(bytes_input):
	B=''
	for C in bytes_input:
		A=hex(C)[2:]
		if len(A)==1:A='0'+A
		B+=A
	return B
def string_to_hex(s):return''if s==''else bytes_to_hex(str_to_bytes(s))
def d(data,publicKey):A=data;A=string_to_hex(A).encode();B=BB(public_key=publicKey,mode=1);C=B.encrypt(A);return'04'+C.hex()
def e(e=_C,c=_C,n=_C):
	D='0123456789';A=list(D)
	if n==1:A=list(D)
	else:A=list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
	B=[]
	if c is _C:c=len(A)
	if e:
		for E in range(e):B.append(A[int(random.random()*c)])
	else:
		for C in range(36):
			if C in[8,13,18,23]:B.append('-')
			elif C==14:B.append('4')
			else:
				e=int(random.random()*16)
				if C==19:B.append(A[3&e|8])
				else:B.append(A[e])
	return''.join(B)
def a(data,key):B=data;A=key;B=B.encode(_B);A=A.encode(_B);C=AA(padding_mode=3);C.set_key(A,SM4_ENCRYPT);D=C.crypt_cbc(A[0:8]+A[-8:],B);E=base64.b64encode(D);return E.decode()
def b(data,key):B=data;A=key;B=B.encode(_B);A=A.encode(_B);D=base64.b64decode(B);C=AA(padding_mode=3);C.set_key(A,SM4_DECRYPT);E=C.crypt_cbc(A[0:8]+A[-8:],D);return E.decode()
def c(data):A=data;A=A.encode(_B);A=bytes_to_list(A);return m_hash(A)
xor=lambda a,b:list(map(lambda x,y:x^y,a,b))
rotl=lambda x,n:x<<n&4294967295|x>>32-n&4294967295
get_uint32_be=lambda key_data:key_data[0]<<24|key_data[1]<<16|key_data[2]<<8|key_data[3]
put_uint32_be=lambda n:[n>>24&255,n>>16&255,n>>8&255,n&255]
pkcs7_padding=lambda data,block=16:data+[16-len(data)%block for A in range(16-len(data)%block)]
zero_padding=lambda data,block=16:data+[0 for A in range(16-len(data)%block)]
pkcs7_unpadding=lambda data:data[:-data[-1]]
zero_unpadding=lambda data,i=1:data[:-i]if data[-i]==0 else i+1
list_to_bytes=lambda data:b''.join([bytes((A,))for A in data])
bytes_to_list=lambda data:[A for A in data]
random_hex=lambda x:''.join([random.choice('0123456789abcdef')for A in range(x)])
def pboc_padding(data,block=16):
	B=block;A=data;A=A.hex().upper();B=B*2
	if len(A)%B!=0:A=A+'80'
	while len(A)%B!=0:A=A+'00'
	return bytes_to_list(bytes.fromhex(A))
def iso9797m2_padding(data,block=16):
	B=block;A=data;A=A.hex().upper();B=B*2;A=A+'80'
	while len(A)%B!=0:A=A+'00'
	return bytes_to_list(bytes.fromhex(A))
def pboc_unpadding(data):
	A=data
	if len(A)<16:raise Exception(_G)
	if len(A)==16:0
	else:
		while A[-1:]!=[128]:A.pop()
		A.pop()
	return A
def iso9797m2_unpadding(data):
	A=data
	if len(A)<=16:raise Exception(_G)
	while A[-1:]!=[128]:A.pop()
	A.pop();return A
default_ecc_table={'n':'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123',_A:'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF','g':'32c4ae2c1f1981195f9904466a39c9948fe30bbff2660be1715a4589334c74c7bc3736a2f4f6779c59bdcee36b692153d0a9877cc62a474002df32e52139f0a0','a':'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC','b':'28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93'}
class BB:
	def __init__(A,public_key,ecc_table=default_ecc_table,mode=1,asn1=False):'\n        mode: 0-C1C2C3, 1-C1C3C2 (default is 1)\n        ';C=ecc_table;B=public_key;A.public_key=B[2:]if B.startswith('04')and len(B)==130 else B;A.para_len=len(C['n']);A.ecc_a3=(int(C['a'],base=16)+3)%int(C[_A],base=16);A.ecc_table=C;assert mode in(0,1),'mode must be one of (0, 1)';A.mode=mode;A.asn1=asn1
	def _kg(B,k,Point):
		C=Point;C='%s%s'%(C,'1');E='8'
		for G in range(B.para_len-1):E+='0'
		F=int(E,16);A=C;D=False
		for H in range(B.para_len*4):
			if D:A=B._double_point(A)
			if k&F!=0:
				if D:A=B._add_point(A,C)
				else:D=True;A=C
			k=k<<1
		return B._convert_jacb_to_nor(A)
	def _double_point(A,Point):
		G=Point;N=len(G);J=2*A.para_len
		if N<A.para_len*2:return
		else:
			K=int(G[0:A.para_len],16);L=int(G[A.para_len:J],16)
			if N==J:H=1
			else:H=int(G[J:],16)
			C=H*H%int(A.ecc_table[_A],base=16);I=L*L%int(A.ecc_table[_A],base=16);D=(K+C)%int(A.ecc_table[_A],base=16);E=(K-C)%int(A.ecc_table[_A],base=16);B=D*E%int(A.ecc_table[_A],base=16);D=L*H%int(A.ecc_table[_A],base=16);E=I*8%int(A.ecc_table[_A],base=16);F=K*E%int(A.ecc_table[_A],base=16);B=B*3%int(A.ecc_table[_A],base=16);C=C*C%int(A.ecc_table[_A],base=16);C=A.ecc_a3*C%int(A.ecc_table[_A],base=16);B=(B+C)%int(A.ecc_table[_A],base=16);O=(D+D)%int(A.ecc_table[_A],base=16);D=B*B%int(A.ecc_table[_A],base=16);I=I*E%int(A.ecc_table[_A],base=16);P=(D-F)%int(A.ecc_table[_A],base=16)
			if F%2==1:E=(F+(F+int(A.ecc_table[_A],base=16)>>1)-D)%int(A.ecc_table[_A],base=16)
			else:E=(F+(F>>1)-D)%int(A.ecc_table[_A],base=16)
			B=B*E%int(A.ecc_table[_A],base=16);Q=(B-I)%int(A.ecc_table[_A],base=16);M=_D%A.para_len;M=M*3;return M%(P,Q,O)
	def _add_point(A,P1,P2):
		E=2*A.para_len;J=len(P1);M=len(P2)
		if J<E or M<E:return
		else:
			H=int(P1[0:A.para_len],16);K=int(P1[A.para_len:E],16)
			if J==E:F=1
			else:F=int(P1[E:],16)
			N=int(P2[0:A.para_len],16);O=int(P2[A.para_len:E],16);B=F*F%int(A.ecc_table[_A],base=16);C=O*F%int(A.ecc_table[_A],base=16);D=N*B%int(A.ecc_table[_A],base=16);B=B*C%int(A.ecc_table[_A],base=16);C=(D-H)%int(A.ecc_table[_A],base=16);D=(D+H)%int(A.ecc_table[_A],base=16);G=C*C%int(A.ecc_table[_A],base=16);B=(B-K)%int(A.ecc_table[_A],base=16);P=F*C%int(A.ecc_table[_A],base=16);C=C*G%int(A.ecc_table[_A],base=16);D=D*G%int(A.ecc_table[_A],base=16);Q=B*B%int(A.ecc_table[_A],base=16);G=H*G%int(A.ecc_table[_A],base=16);L=(Q-D)%int(A.ecc_table[_A],base=16);C=K*C%int(A.ecc_table[_A],base=16);D=(G-L)%int(A.ecc_table[_A],base=16);B=B*D%int(A.ecc_table[_A],base=16);R=(B-C)%int(A.ecc_table[_A],base=16);I=_D%A.para_len;I=I*3;return I%(L,R,P)
	def _convert_jacb_to_nor(A,Point):
		C=Point;E=2*A.para_len;H=int(C[0:A.para_len],16);I=int(C[A.para_len:E],16);F=int(C[E:],16);B=pow(F,int(A.ecc_table[_A],base=16)-2,int(A.ecc_table[_A],base=16));G=B*B%int(A.ecc_table[_A],base=16);J=G*B%int(A.ecc_table[_A],base=16);K=H*G%int(A.ecc_table[_A],base=16);L=I*J%int(A.ecc_table[_A],base=16);M=F*B%int(A.ecc_table[_A],base=16)
		if M==1:D=_D%A.para_len;D=D*2;return D%(K,L)
		else:return
	def encrypt(A,data):
		D='%s%s%s';B=data.hex();E=random_hex(A.para_len);F=A._kg(int(E,16),A.ecc_table['g']);C=A._kg(int(E,16),A.public_key);K=C[0:A.para_len];L=C[A.para_len:2*A.para_len];G=len(B);H=m_kdf(C.encode(_E),G/2)
		if int(H,16)==0:return
		else:
			M=_D%G;I=M%(int(B,16)^int(H,16));J=m_hash([A for A in bytes.fromhex(D%(K,B,L))])
			if A.mode:return bytes.fromhex(D%(F,J,I))
			else:return bytes.fromhex(D%(F,I,J))
		N=binascii.a2b_hex(A._m_z(data).encode(_B));return A.verify(sign,N)
IV=[1937774191,1226093241,388252375,3666478592,2842636476,372324522,3817729613,2969243214]
T_j=[2043430169,2043430169,2043430169,2043430169,2043430169,2043430169,2043430169,2043430169,2043430169,2043430169,2043430169,2043430169,2043430169,2043430169,2043430169,2043430169,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042,2055708042]
def m_ff_j(x,y,z,j):
	if 0<=j and j<16:A=x^y^z
	elif 16<=j and j<64:A=x&y|x&z|y&z
	return A
def m_gg_j(x,y,z,j):
	if 0<=j and j<16:A=x^y^z
	elif 16<=j and j<64:A=x&y|~x&z
	return A
def m_p_0(x):return x^rotl(x,9%32)^rotl(x,17%32)
def m_p_1(x):return x^rotl(x,15%32)^rotl(x,23%32)
def m_cf(v_i,b_i):
	B=[]
	for N in range(16):
		L=16777216;M=0
		for P in range(N*4,(N+1)*4):M=M+b_i[P]*L;L=int(L/256)
		B.append(M)
	for A in range(16,68):B.append(0);B[A]=m_p_1(B[A-16]^B[A-9]^rotl(B[A-3],15%32))^rotl(B[A-13],7%32)^B[A-6];Q=_F%B[A]
	K=[]
	for A in range(0,64):K.append(0);K[A]=B[A]^B[A+4];Q=_F%K[A]
	C,E,F,I,D,G,H,J=v_i
	for A in range(0,64):O=rotl(rotl(C,12%32)+D+rotl(T_j[A],A%32)&4294967295,7%32);R=O^rotl(C,12%32);S=m_ff_j(C,E,F,A)+I+R+K[A]&4294967295;T=m_gg_j(D,G,H,A)+J+O+B[A]&4294967295;I=F;F=rotl(E,9%32);E=C;C=S;J=H;H=rotl(G,19%32);G=D;D=m_p_0(T);C,E,F,I,D,G,H,J=map(lambda x:x&4294967295,[C,E,F,I,D,G,H,J])
	U=[C,E,F,I,D,G,H,J];return[U[A]^v_i[A]for A in range(8)]
def m_hash(msg):
	B=msg;H=len(B);C=H%64;B.append(128);C=C+1;D=56
	if C>D:D=D+64
	for A in range(C,D):B.append(0)
	E=H*8;I=[E%256]
	for A in range(7):E=int(E/256);I.append(E%256)
	for A in range(8):B.append(I[7-A])
	J=round(len(B)/64);K=[]
	for A in range(0,J):K.append(B[A*64:(A+1)*64])
	F=[];F.append(IV)
	for A in range(0,J):F.append(m_cf(F[A],K[A]))
	L=F[A+1];G=''
	for A in L:G='%s%08x'%(G,A)
	return G
def m_kdf(z,klen):
	A=klen;A=int(A);C=1;D=ceil(A/32);E=[A for A in bytes.fromhex(z.decode(_E))];B=''
	for G in range(D):F=E+[A for A in binascii.a2b_hex((_F%C).encode(_E))];B=B+m_hash(F);C+=1
	return B[0:A*2]
SM4_BOXES_TABLE=[214,144,233,254,204,225,61,183,22,182,20,194,40,251,44,5,43,103,154,118,42,190,4,195,170,68,19,38,73,134,6,153,156,66,80,244,145,239,152,122,51,84,11,67,237,207,172,98,228,179,28,169,201,8,232,149,128,223,148,250,117,143,63,166,71,7,167,252,243,115,23,186,131,89,60,25,230,133,79,168,104,107,129,178,113,100,218,139,248,235,15,75,112,86,157,53,30,36,14,94,99,88,209,162,37,34,124,59,1,33,120,135,212,0,70,87,159,211,39,82,76,54,2,231,160,196,200,158,234,191,138,210,64,199,56,181,163,247,242,206,249,97,21,161,224,174,93,164,155,52,26,85,173,147,50,48,245,140,177,227,29,246,226,46,130,102,202,96,192,41,35,171,13,83,78,111,213,219,55,69,222,253,142,47,3,255,106,114,109,108,91,81,141,27,175,146,187,221,188,127,17,217,92,65,31,16,90,216,10,193,49,136,165,205,123,189,45,116,208,18,184,229,180,176,137,105,151,74,12,150,119,126,101,185,241,9,197,110,198,132,24,240,125,236,58,220,77,32,121,238,95,62,215,203,57,72]
SM4_FK=[2746333894,1453994832,1736282519,2993693404]
SM4_CK=[462357,472066609,943670861,1415275113,1886879365,2358483617,2830087869,3301692121,3773296373,4228057617,404694573,876298825,1347903077,1819507329,2291111581,2762715833,3234320085,3705924337,4177462797,337322537,808926789,1280531041,1752135293,2223739545,2695343797,3166948049,3638552301,4110090761,269950501,741554753,1213159005,1684763257]
SM4_ENCRYPT=0
SM4_DECRYPT=1
NoPadding=0
ZERO=1
ISO9797M2=2
PKCS7=3
PBOC=4
class AA:
	def __init__(A,mode=SM4_ENCRYPT,padding_mode=PKCS7):A.sk=[0]*32;A.mode=mode;A.padding_mode=padding_mode
	@classmethod
	def _round_key(E,ka):A=[0,0,0,0];B=put_uint32_be(ka);A[0]=SM4_BOXES_TABLE[B[0]];A[1]=SM4_BOXES_TABLE[B[1]];A[2]=SM4_BOXES_TABLE[B[2]];A[3]=SM4_BOXES_TABLE[B[3]];C=get_uint32_be(A[0:4]);D=C^rotl(C,13)^rotl(C,23);return D
	@classmethod
	def _f(B,x0,x1,x2,x3,rk):
		def A(ka):A=[0,0,0,0];C=put_uint32_be(ka);A[0]=SM4_BOXES_TABLE[C[0]];A[1]=SM4_BOXES_TABLE[C[1]];A[2]=SM4_BOXES_TABLE[C[2]];A[3]=SM4_BOXES_TABLE[C[3]];B=get_uint32_be(A[0:4]);D=B^rotl(B,2)^rotl(B,10)^rotl(B,18)^rotl(B,24);return D
		return x0^A(x1^x2^x3^rk)
	def set_key(B,key,mode):
		D=key;D=bytes_to_list(D);E=[0,0,0,0];C=[0]*36;E[0]=get_uint32_be(D[0:4]);E[1]=get_uint32_be(D[4:8]);E[2]=get_uint32_be(D[8:12]);E[3]=get_uint32_be(D[12:16]);C[0:4]=xor(E[0:4],SM4_FK[0:4])
		for A in range(32):C[A+4]=C[A]^B._round_key(C[A+1]^C[A+2]^C[A+3]^SM4_CK[A]);B.sk[A]=C[A+4]
		B.mode=mode
		if mode==SM4_DECRYPT:
			for F in range(16):G=B.sk[F];B.sk[F]=B.sk[31-F];B.sk[31-F]=G
	def one_round(E,sk,in_put):
		D=in_put;C=[];A=[0]*36;A[0]=get_uint32_be(D[0:4]);A[1]=get_uint32_be(D[4:8]);A[2]=get_uint32_be(D[8:12]);A[3]=get_uint32_be(D[12:16])
		for B in range(32):A[B+4]=E._f(A[B],A[B+1],A[B+2],A[B+3],sk[B])
		C+=put_uint32_be(A[35]);C+=put_uint32_be(A[34]);C+=put_uint32_be(A[33]);C+=put_uint32_be(A[32]);return C
	def crypt_ecb(A,input_data):
		B=input_data
		if A.mode==SM4_ENCRYPT:
			if A.padding_mode==NoPadding:0
			if A.padding_mode==ZERO:B=zero_padding(bytes_to_list(B))
			if A.padding_mode==ISO9797M2:B=iso9797m2_padding(B)
			if A.padding_mode==PKCS7:B=pkcs7_padding(bytes_to_list(B))
			if A.padding_mode==PBOC:B=pboc_padding(B)
		E=len(B);D=0;C=[]
		while E>0:C+=A.one_round(A.sk,B[D:D+16]);D+=16;E-=16
		if A.mode==SM4_DECRYPT:
			if A.padding_mode==NoPadding:0
			if A.padding_mode==ZERO:return list_to_bytes(zero_unpadding(C))
			if A.padding_mode==ISO9797M2:return list_to_bytes(iso9797m2_unpadding(C))
			if A.padding_mode==PKCS7:return list_to_bytes(pkcs7_unpadding(C))
			if A.padding_mode==PBOC:return list_to_bytes(pboc_unpadding(C))
		return list_to_bytes(C)
	def crypt_cbc(A,iv,input_data):
		E=iv;C=input_data;B=0;D=[];G=[0]*16;E=bytes_to_list(E)
		if A.mode==SM4_ENCRYPT:
			if A.padding_mode==NoPadding:0
			if A.padding_mode==ZERO:C=zero_padding(bytes_to_list(C))
			if A.padding_mode==ISO9797M2:C=iso9797m2_padding(C)
			if A.padding_mode==PKCS7:C=pkcs7_padding(bytes_to_list(C))
			if A.padding_mode==PBOC:C=pboc_padding(C)
			F=len(C)
			while F>0:G[0:16]=xor(C[B:B+16],E[0:16]);D+=A.one_round(A.sk,G[0:16]);E=copy.deepcopy(D[B:B+16]);B+=16;F-=16
			return list_to_bytes(D)
		else:
			F=len(C)
			while F>0:D+=A.one_round(A.sk,C[B:B+16]);D[B:B+16]=xor(D[B:B+16],E[0:16]);E=copy.deepcopy(C[B:B+16]);B+=16;F-=16
			if A.padding_mode==NoPadding:0
			if A.padding_mode==ZERO:return list_to_bytes(zero_unpadding(D))
			if A.padding_mode==ISO9797M2:return list_to_bytes(iso9797m2_unpadding(D))
			if A.padding_mode==PKCS7:return list_to_bytes(pkcs7_unpadding(D))
			if A.padding_mode==PBOC:return list_to_bytes(pboc_unpadding(D))
			return list_to_bytes(D)