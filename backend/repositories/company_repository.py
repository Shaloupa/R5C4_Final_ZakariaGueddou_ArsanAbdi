from shared.peristence import load_data, save_data

DATA_PATH = './data/companies.json'

def get_all_companies():
    return load_data(DATA_PATH)

def get_company_by_id(company_id):
    companies = load_data(DATA_PATH)
    return next((c for c in companies if c['company_id'] == company_id), None)

def add_company(company_data):
    companies = load_data(DATA_PATH)
    company_data['company_id'] = max([c['company_id'] for c in companies] + [0]) + 1
    companies.append(company_data)
    save_data(DATA_PATH, companies)
    return company_data

def update_company(company_id, company_data):
    companies = load_data(DATA_PATH)
    company = next((c for c in companies if c['company_id'] == company_id), None)
    if company:
        company.update(company_data)
        save_data(DATA_PATH, companies)
    return company