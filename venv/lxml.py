import xmltodict
import dicttoxml
import json
fileptr = open("sample.xml","r")
#
xml_content1 = fileptr.read()
print("XML content is: ")
print(xml_content1)
# xml_content = xml_content.replace('&lt;', '<')
# xml_content = xml_content.replace('&gt;', '>')
# # print(xml_content)
json_resp = json.loads(json.dumps(xmltodict.parse(xml_content1)))
# print(json_resp)
# policy_obj = json_resp["s:Envelope"]["s:Body"]["CreatePolicyResponse"]["CreatePolicyResult"]

# print(xmltodict.parse(xml_content, process_namespaces=True) == {
#      'http://defaultns.com/:root': {
#          'http://defaultns.com/:x': '1',
#          'http://a.com/:y': '2',
#          'http://b.com/:z': '3',
#      }
#  }
# )

# mydict = {
#      'soapenv:Envelope': {
#          '@xmlns:soapenv':"http://schemas.xmlsoap.org/soap/envelope/",
#          '@xmlns:tem':"http://tempuri.org/",
#      }
#  }

# print(xmltodict.unparse(mydict, pretty=True))



# my_ordered_dict = xmltodict.parse(xml_content)
# print("ordered dictionary is: ")
# print(my_ordered_dict)

# obj = {'mylist': ['foo', 'bar', 'baz'], 'mydict': {'foo': 'bar', 'baz': 1}, 'ok': True}
# xml = dicttoxml.dicttoxml(obj, cdata=True)
# print(xml)

# print("year of plane is: ")
# print(my_ordered_dict['plane']['year'])

# my_plane = dict(my_ordered_dict['plane'])
# print('Created dictionary data is: ')
# print(my_plane)
# print("Year of plane is: ")
# print(my_plane['year'])

# dictionary to xml

# mydict = {'plane': {'year': '1977', 'make': 'Cessna', 'model': 'Skyhawk', 'color': 'Light blue and white'}}
# print("Orignal dictionary is: ")
# print(mydict)
#
# xml_format = xmltodict.unparse(my_ordered_dict, pretty=True)
# print("XML format data is: ")
# print(xml_format)
#

# xml to json

# import charade
#
# s = """
# <?xml version="1.0" encoding="utf-8"?>
# <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
#         <soapenv:Header></soapenv:Header>
#         <soapenv:Body>
#                 <tem:GetPremiumForHealthRecharge_IIHRv2>
#                         <tem:planId>2719841</tem:planId>
#                         <tem:dobCollection>01/09/2003</tem:dobCollection>
#                         <tem:dobCollection>02/09/2003</tem:dobCollection>
#                         <tem:dobRelation>self</tem:dobRelation>
#                         <tem:dobRelation>spouse</tem:dobRelation>
#                         <tem:discountFactor>O</tem:discountFactor>
#                         <tem:billCycle>Y</tem:billCycle>
#                         <tem:premiumCalDate>27/09/2021</tem:premiumCalDate>
#                         <tem:piDob>01/09/2003</tem:piDob>
#                         <tem:pisDob></tem:pisDob>
#                         <tem:cityName>Mumbai</tem:cityName>
#                         <tem:branchCode>521101</tem:branchCode>
#                         <tem:paSumInsured>0</tem:paSumInsured>
#                         <tem:ciSumInsured>0</tem:ciSumInsured>
#                 </tem:GetPremiumForHealthRecharge_IIHRv2>
#         </soapenv:Body>
# </soapenv:Envelope>
# """

# if isinstance(s, str):
#             print("in if")
#             s1 = (bytes(s,'utf-8'))
#             print(charade.detect(s.encode()))
#         # detecting the string
# else:
#     print("in else")
#     print(charade.detect(s))


##################################################################

# 2. `

