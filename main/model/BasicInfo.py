import datetime


# id: id
# tw_business_accounting_no: 台灣統編
# company_name: 公司名
# capital_stock_amount: 資本總額(登記)
# paid_in_capital_amount: 資本總額(實收)
# responsible_name: 負責人姓名
# company_location: 公司所在地
# register_organization_desc: 登記機關
# company_setup_date: 核准設立日期
# company_setup_date_int: 公司設立日期(int)
# change_of_approval_data: 最後核准變更日
# revoke_app_date: 公司撤銷日期
# industry_category: 產業類別
# case_status: 停復業狀況
# country: 國家
# create_date: 建立日期
# last_upd_date: 最後更新日

class BasicInfo:
    id: str
    tw_business_accounting_no: str
    company_name: str
    capital_stock_amount: float
    paid_in_capital_amount: float
    responsible_name: str
    company_location: str
    register_organization_desc: str
    company_setup_date: datetime
    company_setup_date_int: int
    change_of_approval_data: datetime
    revoke_app_date: datetime
    industry_category: str
    case_status: str
    country: str
    create_date: datetime
    last_upd_date: datetime
