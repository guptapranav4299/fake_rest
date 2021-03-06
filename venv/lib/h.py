import collections
import dicttoxml
from lxml import etree as ET
from lxml.etree import CDATA


quotation_request_data = '<Root><Uid>122422421224287</Uid><VendorCode>webagg</VendorCode><VendorUserId>webagg</VendorUserId><POS_MISP><Type></Type><PanNo></PanNo></POS_MISP><Risk><Vehicle><VehicleClass>A1</VehicleClass><TypeOfVehicle>O</TypeOfVehicle><RTOCode>JH01</RTOCode><ModelCode>BA0097</ModelCode><Make>BAJAJ</Make><BodyType>GODC</BodyType><EngineNo>AHH027159P</EngineNo><RegistrationNo>MH01HN0287</RegistrationNo><ChassiNo>MBIAA22E9HRA72601</ChassiNo><CubicCapacity>150</CubicCapacity><SeatingCapacity>2</SeatingCapacity><FuelType>P</FuelType><GrossWeigh>770</GrossWeigh><ValidPUC>Y</ValidPUC><CNGOrLPG><InbuiltKit></InbuiltKit><IVDOfCNGOrLPG></IVDOfCNGOrLPG></CNGOrLPG><CarriageCapacityFlag>S</CarriageCapacityFlag><RegistrationDate>01/01/2019</RegistrationDate><ManufacturingYear>2019</ManufacturingYear><TrailerTowedBy></TrailerTowedBy><TrailerRegNo></TrailerRegNo><NoOfTrailer></NoOfTrailer><TrailerValLimPaxIDVDays></TrailerValLimPaxIDVDays><TrailerChassisNo></TrailerChassisNo><TrailerMfgYear></TrailerMfgYear></Vehicle><AdditionalBenefit><CPAReq></CPAReq><NPAReq>Y</NPAReq><CPA></CPA><NPA><NPANomName>Legal Heir</NPANomName><NPAName>Legal Heir</NPAName><NPALimit></NPALimit><NPANomAge>21</NPANomAge><NPANomAgeDet>Y</NPANomAgeDet><NPARel></NPARel><NPAAppinteeName></NPAAppinteeName><NPAAppinteeRel></NPAAppinteeRel></NPA><Addon></Addon><LegalLiabilitytoPaidDriver>0</LegalLiabilitytoPaidDriver><LegalLiabilityForOtherEmployees>0</LegalLiabilityForOtherEmployees><NCB>20</NCB><GeographicalArea>0</GeographicalArea><FibreGlassTank>0</FibreGlassTank><LegalLiabilityForNonFarePayingPassengers>0</LegalLiabilityForNonFarePayingPassengers><UseForHandicap>0</UseForHandicap><AntiThiefDevice>0</AntiThiefDevice></AdditionalBenefit><AddonReq>N</AddonReq><Addon><CoverCode></CoverCode></Addon><PreviousInsDtls><UsedCarList><PurchaseDate>01/01/2019</PurchaseDate><InspectionRptNo></InspectionRptNo><InspectionDt></InspectionDt></UsedCarList><UsedCar>Y</UsedCar><NewVehicle>N</NewVehicle><RollOver>Y</RollOver><RollOverList><PolicyNo></PolicyNo><InsuredName>Acko General Insurance</InsuredName><PreviousPolExpDt>31/07/2021</PreviousPolExpDt><ClientCode></ClientCode><Address1></Address1><Address2></Address2><Address3></Address3><Address4></Address4><Address5></Address5><PinCode></PinCode><InspectionRptNo></InspectionRptNo><InspectionDt></InspectionDt><ClaimInExpiringPolicy>Y</ClaimInExpiringPolicy><NCBInExpiringPolicy>20</NCBInExpiringPolicy></RollOverList><PurchaseDate>01/01/2019</PurchaseDate></PreviousInsDtls></Risk></Root>'
SOAP_NS = 'http://schemas.xmlsoap.org/soap/envelope/'
tem = 'http://tempuri.org/'
lead_request = "http://xmlns.oracle.com/new_jws/LeadManagementService/LeadManagementBPEL"
ns_map = {'soapenv': SOAP_NS, 'tem': tem}
lead_request_map = {None: lead_request}
env = ET.Element(ET.QName(SOAP_NS, 'Envelope'), nsmap=ns_map)
head = ET.SubElement(env, ET.QName(SOAP_NS, 'Header'))
body = ET.SubElement(env, ET.QName(SOAP_NS, 'Body'))
tem_createpolicy = ET.SubElement(body, ET.QName(tem, 'CreatePolicy'))
tem_prod = ET.SubElement(tem_createpolicy, ET.QName(tem, 'Product'))
tem_prod.text = "Motor"
val = ET.SubElement(tem_createpolicy, ET.QName(tem, 'XML'))
val.text = CDATA(quotation_request_data)
tree = ET.ElementTree(env)
tree.write('quotation_output.xml', pretty_print=True, xml_declaration=False, encoding="utf-8")