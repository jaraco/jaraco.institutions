definitions = {

'Sandia Laboratory FCU': dict(
	caps = ["SIGNON", "BASTMT"],
	fid = "1001",
	fiorg = "SLFCU",
	url = "https://www.cu-athome.org/scripts/serverext.dll",
	bankid = "307083911",
),

'Chase (credit card)': dict(
	caps = ["SIGNON", "CCSTMT"],
	fid = "10898",
	fiorg = "B1",
	url = "https://ofx.chase.com",
),

'Los Alamos National Bank': dict(
	caps = ['SIGNON', 'BASTMT'],
	fid = '107001012',
	fiorg = 'LANB',
	url = 'https://ofx.lanb.com/ofx/ofxrelay.dll',
	bankid = '107001012',
),

'Fidelity Investments': dict(
	caps = ['SIGNON', 'INVSTMT'],
	fid = '7776',
	fiorg = 'fidelity.com',
	url = 'https://ofx.fidelity.com/ftgw/OFX/clients/download',
),

'American Funds': dict(
	caps = ['SIGNON', 'INVSTMT'],
	fiorg = 'INTUIT',
	fid = '7779',
	url = 'https://ofx.financialtrans.com/tf/OFXServer?tx=OFXController&'
		'cz=702110804131918&cl=3000518',
),

'Vanguard': dict(
	caps = ['SIGNON', 'INVSTMT'],
	fiorg = 'The Vanguard Group',
	fid = '1358',
	url = 'https://vesnc.vanguard.com/us/OfxDirectConnectServlet',
),

'Citibank': dict(
	caps = ['SIGNON', 'CCSTMT'],
	fiorg = 'Citigroup',
	url = 'https://secureofx2.bankhost.com/citi/cgi-forte/ofx_rt?'
		'servicename=ofx_rt&pagename=ofx',
	fid = '24909',
),

}
