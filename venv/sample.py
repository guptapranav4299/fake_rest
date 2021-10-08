import xmltodict
import requests
from datetime import datetime, date
import http.client

class MaxBupaHandler:
    min_quote_map = {"tem:GetPremiumForHealthRecharge_IIHRv2":{}}
    root_map = {
        'soapenv:Envelope':{
            '@xmlns:soapenv': "http://schemas.xmlsoap.org/soap/envelope/",
            '@xmlns:tem': "http://tempuri.org/",
            'soapenv:Header': '',
            'soapenv:Body':{},
        }
    }

    request_header = {"Content-Type": "text/xml","SOAPAction": "http://tempuri.org/GetPremiumForHealthRecharge_IIHRv2"}
    request_url = "http://serviceuat.maxbupa.com/GetProductPricesV2/GetProductPrices.asmx"
    base_url = "serviceuat.maxbupa.com"
    PLAN_ID = {
        "1A": "2719811",
        "2A": "2719841",
        "1A 1C": "2719812",
        "2A 2C": "2719843",
        "2A 2C CI": ""
    }

    CI_COVERED_MAPPING = {
        "2734147": "1",  # CI 1A3C
        "2735310": "2",  # CI 2A
    }

    RELATION_MAPPING = {
        "spouse": "S",
        "fiancee": "9",
        "son": "C",
        "daughter": "D",
        "father": "F",
        "mother": "M",
        "brother": "B",
        "sister": "I"
    }

    def __init__(self,request_data):
        self.request_data = request_data
        self.payload = request_data['payload']
        print(self.request_data)
        self.age_list = []
        self.members = None
        self.sum_insured = None
        self.quote_response = {}
        self.add_ons = []
        self.uid = None
        self.quote_response_list = []
        self.premium_list = []
        self.proposal_request_data = request_data
        self.proposer_id = None
        self.co_pay = False
        self.period_wise_data = {}
        self.min_quote = False
        self.min_quote_response = []


    def get_plan_id(self,adults,kids=0):
        if adults == 2:
            no_of_members = "2A"
            if no_of_members in self.PLAN_ID:
                return self.PLAN_ID[no_of_members]
        elif adults == 1:
            no_of_members = "1A"
            if no_of_members in self.PLAN_ID:
                return self.PLAN_ID[no_of_members]
        else:
            raise Exception("Currently the plans are mapped for either 2 adults or 1 adult(self) ")


    def check_policy_years(self, premium, period):
        period = int(period)
        if period == 2:
            premium = round(premium * 2 * .925)
        if period == 3:
            premium = round(premium * 3 * .9)
        return period, premium


    def member_calculate(self):
        for member in self.members:
            if member['type'] == 'adult':
                dob = member['dob']
                age_list_1 = self.calculate_age(dob)
                self.sum_insured = member['sum_insured']
        return True


    def get_dob(self):
        dob_list = []
        for member in self.members:
            if member['type'] == 'adult':
                dob_list.append(member['dob'])
        return dob_list


    def calculate_age(self, dob):
        dob_obj = datetime.datetime.strptime(dob, '%d/%m/%Y')
        today = date.today()
        age = today.year - dob_obj.year
        self.age_list.append(age)
        return self.age_list


    def get_relationship(self):
        member_list = []
        for member in self.members:
            if member['member_type'].lower() == "proposer":
                member_list.append("self")
            else:
                member_list.append(member['member_type'])
        return member_list


    def get_sum_insured(self):
        sum_list = []
        for member in self.members:
            sum_list.append(member['sum_insured'])
        return sum_list


    def get_pi_dob(self):
        pi_dob = ""
        for member in self.members:
            if member['member_type'] == 'proposer':
                pi_dob = member['dob']
        return pi_dob


    def construct_xml(self,min_quote_map):
        print("REQUEST XML====>")
        self.root_map['soapenv:Envelope']['soapenv:Body'] = min_quote_map
        xml_request = xmltodict.unparse(self.root_map,pretty=True)
        print(xml_request)
        return xml_request

    def make_request_using_http_client(self,data, url, method="POST"):
        conn = http.client.HTTPConnection(self.base_url)
        headers = {"Content-Type": "text/xml","SOAPAction": "http://tempuri.org/GetPremiumForHealthRecharge_IIHRv2"}
        print("Headers",headers)
        conn.request(method, url, data['data'], headers)
        res = conn.getresponse()
        data = res.read()
        data_dict = xmltodict.parse(data)
        print("DATA DICT========>",data_dict)
        return data.decode("utf-8")
    def quick_quote(self):
        try:
            self.period_wise_data = {1: [], 2: [], 3: []}
            self.uid = self.request_data['unique_identifier']
            self.min_quote = self.request_data['min_quote']
            self.members = self.payload.get('members')
            print("MEMBERS=======>",self.members)
            # self.member_calculate()
            # self.age_list.sort(reverse=True)
            # premium_age = self.age_list[0]
            # if int(premium_age) > 60:
            #     self.co_pay = True
            adults = self.payload['adults']
            kids = self.payload['kids']
            plan_id = self.get_plan_id(adults,kids)
            self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:planId'] = plan_id

            dob_list = self.get_dob()
            print("DOB_LIST=========>",dob_list)
            self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:dobCollection'] = dob_list

            membership_list = self.get_relationship()
            print("MEMBER LIST",membership_list)
            self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:dobRelation'] = membership_list

            self.sum_insured = self.get_sum_insured()
            print("SUM_INSURED=======>", self.sum_insured)

            self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:discountFactor'] = "O"

            tenure = self.payload['duration_years']
            if tenure == 1:
                self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:billCycle'] = "Y"
            elif tenure == 2:
                self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:billCycle'] = "2"
            elif tenure == 3:
                self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:billCycle'] = "3"
            else:
                raise Exception("Only 3 years of tenure are valid")
            print("TENURE========>",tenure)

            calculation_date = date.today()
            date1 = calculation_date.strftime("%d/%m/%Y")
            self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:premiumCalDate'] = date1
            print("START DATE=======>",date1)

            print("PROPOSER DOB======>",self.get_pi_dob())
            self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:piDob'] = self.get_pi_dob()

            # if ci is selected for 2A then we need to pass it
            self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:pisDob'] = ""

            # mapped as Mumbai for staging env..to write for production env
            self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:cityName'] = "Mumbai"

            self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:branchCode'] = 521101

            self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:paSumInsured'] = 0
            self.min_quote_map["tem:GetPremiumForHealthRecharge_IIHRv2"]['tem:ciSumInsured'] = 0

            # self.min_quote_map['tem:AccessKey'] = "UseQlVYMBLMRfIVQoTGm8oboCDRYTlEqK58DvKTWbYdChxJppMvbc+uRDRzuL7Bar9c1Bo5v2M9pgQ4a81ifAsNT7yQOmgB2yLT9YtyddFx3g5nGt85InFIz4O7YMomapmLTlz//uAQzpooex1jm0eBNfi1o2D+TINCsrpXiI5i7BDUwGF6rZTOYqWY0L/2XbNGocRkzfV6SjdM8de9yKqiIVMCgxVuiwORIQ92ex3Nwej7EK97kVqVXGaj+fviPJ8EDn7FOE7FDo/CaGC4YJkfdnfo7grNWzXIWKuWT6wTocPv1GxoS2rIAw4IvU4hE"
            if 'add_ons' in self.payload and self.payload['add_ons']:
                for addon in self.payload['add_ons']:
                    self.add_ons.append(addon)
            print("ADD-ONS",self.add_ons)

            print("DICT======>",self.min_quote_map)

            request_xml = self.construct_xml(self.min_quote_map)
            # save_data_to_common_externaldump(self.uid, request_xml, 'quotation_request_xml', 1)
            # req = bytes(request_xml, 'utf-8')
            # req1 = req.decode('utf-8')
            dta = {
                "status":True,
                "data":request_xml
            }
            response = self.make_request_using_http_client(dta,"/GetProductPricesV2/GetProductPrices.asmx")
            print("RESPONSE",response)

        except Exception as e:
            print('Exception Found', str(e))
            return 400, 'Exception found', []


request_data = {'request_id': 'add749b88a38fd85367657af65bc4bfe', 'payload': {'request_id': 'add749b88a38fd85367657af65bc4bfe', 'insurer_logo': 'https://etimg.etb2bimg.com/thumb/msid-77869972,width-1200,resizemode-4/.jpg', 'kids': 0, 'plan_type': 'INDIVIDUAL', 'duration_years': 1, 'insurance_name': 'max bupa health insurance', 'insurer_code': 'MXBPHLTH', 'unique_identifier': '5ded252d06b445fed90e82c3c5f4472b', 'include_proposer': 0, 'adults': 1, 'members': [{'sum_insured': 500000, 'nomineeDetails': {}, 'proposer': 1, 'medical_history': [], 'type': 'adult', 'gender': 'M', 'dob_to_display': '2003-09-09T18:30:00.000Z', 'pincode': 834001, 'city_name': 'RANCHI', 'member_type': 'proposer', 'nationality': 'Indian', 'state_name': 'JHARKHAND', 'dob': '10/09/2003'}], 'dump_id': 94160}, 'unique_identifier': '5ded252d06b445fed90e82c3c5f4472b', 'min_quote': True}
obj = MaxBupaHandler(request_data)
obj.quick_quote()
