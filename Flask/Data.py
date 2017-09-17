class Data:
    def __init__(self):
        #all or state ID
        self.location = None
        #string containing service
        self.service = None
        #3 items for axies
        self.data = []
        #range to grab data from
        self.dateRange = None

    def setLocation(self, local):
        self.location = local

    def setService(self, serv):
        services = ["Ambulance (Emergency)", "Ambulance (Non-Emergency)", "Ambulance (Emergency & Non-Emergency)",
                    "Chiropractic Services",
                    "Clinical Laboratory (Billing Independently)", "Home Health", "Hospice",
                    "Independent Diagnostic Testing Facility Pt A",
                    "Independent Diagnostic Testing Facility Pt B", "Long-Term Care Hospitals",
                    "Physical & Occupational Therapy",
                    "Skilled Nursing Facility"]
        for i in range(len(services)):
            if serv == services[i]:
                self.service = serv
                return
        print("Could not find service")

    def setAxisX(self, x):
        types = ["average_number_of_providers_per_county", "average_number_of_users_per_provider",
                 "number_of_fee_for_service_beneficiaries",
                 "number_of_providers", "number_of_users",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_0_to_2_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_10_to_19_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_20_or_more_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_3_to_4_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_5_to_9_providers",
                 "percentage_of_users_out_of_ffs_beneficiaries"]
        for i in range(len(types)):
            if x == types[i]:
                self.data.append(x)
                return
        print("Could not find type X")

    def setAxisY(self, y):
        types = ["average_number_of_providers_per_county","average_number_of_users_per_provider","number_of_fee_for_service_beneficiaries",
                 "number_of_providers","number_of_users","percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_0_to_2_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_10_to_19_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_20_or_more_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_3_to_4_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_5_to_9_providers",
                 "percentage_of_users_out_of_ffs_beneficiaries"]
        for i in range(len(types)):
            if y == types[i]:
                self.data.append(y)
                return
        print("Could not find type Y")

    def setAxisZ(self, z):
        types = ["average_number_of_providers_per_county","average_number_of_users_per_provider","number_of_fee_for_service_beneficiaries",
                 "number_of_providers","number_of_users","percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_0_to_2_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_10_to_19_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_20_or_more_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_3_to_4_providers",
                 "percentage_of_ffs_beneficiaries_by_number_of_providers_serving_county_5_to_9_providers",
                 "percentage_of_users_out_of_ffs_beneficiaries"]
        for i in range(len(types)):
            if z == types[i]:
                self.data.append(z)
                return
        print("Could not find type Z")

    def setDateRange(self, date):
        if date == 0:
            self.dateRange = "2014-10-01 to 2015-09-30"
        elif date == 1:
            self.dateRange = "2015-01-01 to 2015-12-31"
        elif date == 2:
            self.dateRange = "2015-04-01 to 2016-03-31"
        elif date == 3:
            self.dateRange = "2015-07-01 to 2016-06-30"
        elif date == 4:
            self.dateRange = "2015-10-01 to 2016-09-30"
        elif date == 5:
            self.dateRange = '*'
