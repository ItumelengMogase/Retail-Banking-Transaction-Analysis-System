import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from faker import Faker
import os

class SABankingDataGenerator:
    def __init__(self, num_transactions=200000, start_date='2023-01-01', end_date='2024-11-23'):
        self.fake = Faker('en_US')
        self.num_transactions = num_transactions
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        
        # South African specific data
        self.sa_provinces = ['Gauteng', 'Western Cape', 'KwaZulu-Natal', 'Eastern Cape', 
                           'Free State', 'Mpumalanga', 'North West', 'Limpopo', 'Northern Cape']
        self.sa_cities = ['Johannesburg', 'Cape Town', 'Durban', 'Pretoria', 'Gqeberha',
                         'Bloemfontein', 'Mbombela', 'Kimberley', 'Polokwane', 'East London']
        
        # South African banks data
        self.sa_banks = {
            'ABSA': {
                'bank_code': '632005',
                'swift_code': 'ABSAZAJJ',
                'branches': ['Sandton', 'Cape Town CBD', 'Durban Central', 'Pretoria Central']
            },
            'Standard Bank': {
                'bank_code': '051001',
                'swift_code': 'SBZAZAJJ',
                'branches': ['Rosebank', 'Century City', 'Umhlanga', 'Brooklyn']
            },
            'FNB': {
                'bank_code': '250655',
                'swift_code': 'FIRNZAJJ',
                'branches': ['Fourways', 'Tyger Valley', 'Gateway', 'Menlyn']
            },
            'Nedbank': {
                'bank_code': '198765',
                'swift_code': 'NEDSZAJJ',
                'branches': ['Rivonia', 'V&A Waterfront', 'Musgrave', 'Hatfield']
            },
            'Capitec': {
                'bank_code': '470010',
                'swift_code': 'CABLZAJJ',
                'branches': ['Midrand', 'Claremont', 'Pinetown', 'Centurion']
            },
            'Discovery Bank': {
                'bank_code': '679000',
                'swift_code': 'DISCJJ',
                'branches': ['Sandton', 'Sea Point', 'Ballito', 'Lynnwood']
            },
            'TymeBank': {
                'bank_code': '678910',
                'swift_code': 'TYMEZAJJ',
                'branches': ['Digital']
            }
        }
        
        self.account_types = ['Savings', 'Current', 'Credit Card', 'Investment', 'Home Loan']
        self.transaction_types = ['Deposit', 'Withdrawal', 'EFT', 'Debit Order', 'Card Payment',
                                'ATM Withdrawal', 'Online Payment', 'Cash Deposit']
        
        # South African public holidays
        self.sa_holidays = {
            '2023-01-01': "New Year's Day",
            '2023-01-02': "New Year's Day (observed)",
            '2023-03-21': 'Human Rights Day',
            '2023-04-07': 'Good Friday',
            '2023-04-10': 'Family Day',
            '2023-04-27': 'Freedom Day',
            '2023-05-01': 'Workers Day',
            '2023-06-16': 'Youth Day',
            '2023-08-09': "National Women's Day",
            '2023-09-24': 'Heritage Day',
            '2023-09-25': 'Heritage Day (observed)',
            '2023-12-16': 'Day of Reconciliation',
            '2023-12-25': 'Christmas Day',
            '2023-12-26': 'Day of Goodwill',
            '2024-01-01': "New Year's Day",
            '2024-03-21': 'Human Rights Day',
            '2024-03-29': 'Good Friday',
            '2024-04-01': 'Family Day',
            '2024-04-27': 'Freedom Day',
            '2024-05-01': 'Workers Day',
            '2024-06-16': 'Youth Day',
            '2024-06-17': 'Youth Day (observed)',
            '2024-08-09': "National Women's Day",
            '2024-09-24': 'Heritage Day',
            '2024-12-16': 'Day of Reconciliation',
            '2024-12-25': 'Christmas Day',
            '2024-12-26': 'Day of Goodwill'
        }

    def generate_bank_details(self):
        """Generate random bank details"""
        bank_name = random.choice(list(self.sa_banks.keys()))
        bank_info = self.sa_banks[bank_name]
        branch = random.choice(bank_info['branches'])
        return {
            'bank_name': bank_name,
            'bank_code': bank_info['bank_code'],
            'swift_code': bank_info['swift_code'],
            'branch_name': branch
        }

    def generate_sa_id_number(self):
        """Generate a valid format South African ID number"""
        year = random.randint(60, 99)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        gender = random.randint(0, 9)
        citizenship = random.randint(0, 1)
        race = 8
        checksum = random.randint(0, 9)
        
        return f"{year:02d}{month:02d}{day:02d}{gender}{citizenship}{race}{checksum}"

    def generate_sa_phone_number(self):
        """Generate a South African format phone number"""
        mobile_prefixes = ['060', '061', '062', '063', '064', '065', '066', '067', '068', 
                          '071', '072', '073', '074', '076', '078', '079', '081', '082', '083', '084']
        prefix = random.choice(mobile_prefixes)
        suffix = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        return f"+27{prefix}{suffix}"

    def generate_customers(self, num_customers=10000):
        """Generate customer data"""
        customers = []
        for _ in range(num_customers):
            age = random.randint(18, 85)
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()
            bank_details = self.generate_bank_details()
            
            customers.append({
                'customer_id': f'CUS{str(random.randint(10000, 99999))}',
                'first_name': first_name,
                'last_name': last_name,
                'id_number': self.generate_sa_id_number(),
                'date_of_birth': self.fake.date_of_birth(minimum_age=age, maximum_age=age),
                'gender': random.choice(['M', 'F']),
                'email': f"{first_name.lower()}.{last_name.lower()}@{random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])}",
                'phone_number': self.generate_sa_phone_number(),
                'province': random.choice(self.sa_provinces),
                'city': random.choice(self.sa_cities),
                'postal_code': str(random.randint(1000, 9999)),
                'income_bracket': random.choice(['0-100K', '100K-250K', '250K-500K', '500K-1M', '1M+']),
                'employment_status': random.choice(['Employed', 'Self-employed', 'Retired', 'Student']),
                'credit_score': random.randint(300, 850),
                'primary_bank': bank_details['bank_name'],
                'primary_branch': bank_details['branch_name']
            })
        return pd.DataFrame(customers)

    def generate_accounts(self, customers_df):
        """Generate account data for customers"""
        accounts = []
        for _, customer in customers_df.iterrows():
            num_accounts = random.randint(1, 4)
            for _ in range(num_accounts):
                account_type = random.choice(self.account_types)
                bank_details = self.generate_bank_details()
                
                accounts.append({
                    'account_id': f'ACC{str(random.randint(100000, 999999))}',
                    'customer_id': customer['customer_id'],
                    'bank_name': bank_details['bank_name'],
                    'branch_name': bank_details['branch_name'],
                    'bank_code': bank_details['bank_code'],
                    'swift_code': bank_details['swift_code'],
                    'account_type': account_type,
                    'opening_date': self.fake.date_between(
                        start_date=self.start_date - timedelta(days=365*3),
                        end_date=self.end_date
                    ),
                    'balance': round(random.uniform(1000, 1000000), 2),
                    'status': random.choice(['Active', 'Active', 'Active', 'Dormant', 'Closed']),
                    'interest_rate': round(random.uniform(3.5, 12.0), 2),
                    'currency': 'ZAR'
                })
        return pd.DataFrame(accounts)

    def generate_transactions(self, accounts_df):
        """Generate transaction data for accounts"""
        transactions = []
        active_accounts = accounts_df[accounts_df['status'] == 'Active']
        
        for _ in range(self.num_transactions):
            account = active_accounts.sample(n=1).iloc[0]
            transaction_type = random.choice(self.transaction_types)
            amount = round(random.uniform(10, 50000), 2)
            
            while True:
                transaction_date = self.fake.date_time_between(
                    start_date=self.start_date,
                    end_date=self.end_date
                )
                if transaction_date.weekday() < 5 or random.random() < 0.2:
                    break
            
            merchant_name = None
            if transaction_type in ['Card Payment', 'Online Payment']:
                merchant_categories = ['Retail', 'Restaurant', 'Grocery', 'Entertainment', 'Travel']
                category = random.choice(merchant_categories)
                merchant_name = f"{self.fake.company()} {category}"

            transactions.append({
                'transaction_id': f'TRX{str(random.randint(1000000, 9999999))}',
                'account_id': account['account_id'],
                'bank_name': account['bank_name'],
                'transaction_type': transaction_type,
                'amount': amount,
                'currency': 'ZAR',
                'transaction_date': transaction_date,
                'status': random.choice(['Completed', 'Completed', 'Completed', 'Pending', 'Failed']),
                'description': self.fake.text(max_nb_chars=50),
                'merchant_name': merchant_name,
                'reference': f'REF{str(random.randint(100000, 999999))}',
                'transaction_category': random.choice(['Food & Dining', 'Shopping', 'Transport', 
                                                     'Bills & Utilities', 'Entertainment', 'Healthcare'])
            })
        
        return pd.DataFrame(transactions)

    def generate_time_dimension(self):
        """Generate time dimension table with South African specific details"""
        time_start = datetime(self.start_date.year, 1, 1)
        time_end = datetime(self.end_date.year, 12, 31)
        
        dates = []
        current_date = time_start
        
        while current_date <= time_end:
            date_str = current_date.strftime('%Y-%m-%d')
            
            is_weekend = current_date.weekday() >= 5
            is_holiday = date_str in self.sa_holidays
            is_business_day = not (is_weekend or is_holiday)
            
            fiscal_year = current_date.year if current_date.month >= 4 else current_date.year - 1
            fiscal_quarter = (current_date.month - 4) % 12 // 3 + 1
            
            dates.append({
                'date_id': int(current_date.strftime('%Y%m%d')),
                'full_date': date_str,
                'day_name': current_date.strftime('%A'),
                'day_of_week': current_date.weekday() + 1,
                'day_of_month': current_date.day,
                'day_of_year': int(current_date.strftime('%j')),
                'week_of_year': int(current_date.strftime('%V')),
                'month': current_date.month,
                'month_name': current_date.strftime('%B'),
                'month_year': current_date.strftime('%B %Y'),
                'quarter': (current_date.month - 1) // 3 + 1,
                'year': current_date.year,
                'fiscal_year': fiscal_year,
                'fiscal_quarter': fiscal_quarter,
                'fiscal_period': f'FY{str(fiscal_year)[2:]}-Q{fiscal_quarter}',
                'is_weekend': is_weekend,
                'is_holiday': is_holiday,
                'holiday_name': self.sa_holidays.get(date_str, None),
                'is_business_day': is_business_day,
                'is_month_end': current_date.month != (current_date + timedelta(days=1)).month,
                'is_quarter_end': current_date.month in [3, 6, 9, 12] and current_date.month != (current_date + timedelta(days=1)).month,
                'is_year_end': current_date.month == 12 and current_date.day == 31,
                'is_fiscal_year_end': current_date.month == 3 and current_date.day == 31
            })
            
            current_date += timedelta(days=1)
        
        return pd.DataFrame(dates)

    def save_to_csv(self, dataframe, filename):
        """Save dataframe to CSV file"""
        output_dir = 'generated_data'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        filepath = os.path.join(output_dir, filename)
        dataframe.to_csv(filepath, index=False)
        print(f"Saved {filename} with {len(dataframe)} records")

    def generate_all_datasets(self):
        """Generate all datasets and save them to CSV files"""
        print("Generating time dimension data...")
        time_df = self.generate_time_dimension()
        self.save_to_csv(time_df, 'time.csv')
        
        print("Generating customer data...")
        customers_df = self.generate_customers()
        self.save_to_csv(customers_df, 'customers.csv')

        print("Generating account data...")
        accounts_df = self.generate_accounts(customers_df)
        self.save_to_csv(accounts_df, 'accounts.csv')

        print("Generating transaction data...")
        transactions_df = self.generate_transactions(accounts_df)
        self.save_to_csv(transactions_df, 'transactions.csv')

        return {
            'time': time_df,
            'customers': customers_df,
            'accounts': accounts_df,
            'transactions': transactions_df
        }

if __name__ == "__main__":
    print("Starting South African Banking Data Generator...")
    try:
        generator = SABankingDataGenerator(num_transactions=100000)
        datasets = generator.generate_all_datasets()
        print("\nProcess completed successfully!")
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        print("Please make sure all required packages are installed correctly.")