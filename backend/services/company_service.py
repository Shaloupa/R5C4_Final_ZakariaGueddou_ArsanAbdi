from repositories import company_repository

def get_all_companies():
    return company_repository.get_all_companies()

def get_company(company_id):
    return company_repository.get_company_by_id(company_id)

def create_company(company_data):
    return company_repository.add_company(company_data)

def update_company(company_id, company_data):
    return company_repository.update_company(company_id, company_data)