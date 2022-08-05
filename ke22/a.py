from suds import client

cli = client.Client("http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl")
# print(cli)

# 调用服务端接口getDatabaseInfo
# print(cli.service.getDatabaseInfo())

# getMobileCodeInfo   mobileCode = 字符串
print(cli.service.getMobileCodeInfo(mobileCode="15302222009"))
