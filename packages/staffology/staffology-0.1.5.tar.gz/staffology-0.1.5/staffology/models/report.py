from enum import Enum


class Report(str, Enum):
    GROSSTONET = "GrossToNet"
    GROSSTONETCIS = "GrossToNetCis"
    PAYRUNPAYMENTS = "PayrunPayments"
    FURLOUGH = "Furlough"
    PENSIONCONTRIBS = "PensionContribs"
    JOURNAL = "Journal"
    HOURLYPAY = "HourlyPay"
    UMBRELLARECONCILIATION = "UmbrellaReconciliation"
    UMBRELLASTATEMENT = "UmbrellaStatement"
    STATUTORYPAY = "StatutoryPay"
    COSTANALYSIS = "CostAnalysis"
    COSTOFEMPLOYMENT = "CostOfEmployment"
    FULLSUMMARYOFPAY = "FullSummaryOfPay"
    P11 = "P11"
    P11D = "P11d"
    P30 = "P30"
    P32 = "P32"
    P45 = "P45"
    P60 = "P60"
    EMPLOYEEEXPORT = "EmployeeExport"
    RIGHTTOWORK = "RightToWork"
    AEOSTATEMENT = "AeoStatement"
    HOLIDAYALLOWANCES = "HolidayAllowances"
    HOLIDAYPAYACCRUALS = "HolidayPayAccruals"
    AEASSESSMENTS = "AeAssessments"
    CISSTATEMENT = "CisStatement"
    SUBCONTRACTORSUMMARY = "SubcontractorSummary"
    PAYROLLANALYSIS = "PayrollAnalysis"
    VARIANCEREPORT = "VarianceReport"
    P11DETAILED = "P11Detailed"
    NILETTERVALIDATION = "NiLetterValidation"
    YTD = "Ytd"
    TAXCODECHANGES = "TaxCodeChanges"
    EMPLOYEEBENEFITS = "EmployeeBenefits"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value):
        #  Staffology API sometimes sends the index value inside an enum instead of the value of the enum itself
        value_from_index = list(dict(cls.__members__).values())[int(value)]
        return cls(value_from_index)
