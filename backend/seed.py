from app import app
from models import db, Users, Loans, Admins
from werkzeug.security import generate_password_hash
from datetime import datetime




with app.app_context():

    # Delete all rows in the Loan and User tables
    Loans.query.delete()
    Users.query.delete()
    Admins.query.delete()

    # Create an empty list
    users = []
    loans = []
    admins = []

    # data = request.get_json()
    password = "1234"
    
    # Users seeds
    users.append(Users(first_name="Hamza", last_name="Ali", email="hamza.ali@gmail.com", phone=1234567890, password=generate_password_hash(password)))
    # users.append(Users(first_name="Elijah", last_name="Nzelu", email="elijah.nzelu@student.moringaschool.com", phone=1234567891, password=generate_password_hash(password)))
    # users.append(Users(first_name="Antony", last_name="Wambugu", email="antony.wambugu@student.moringaschool.com", phone=1234567892, password=generate_password_hash(password)))
    # users.append(Users(first_name="Abdimalik", last_name="Abdullahi", email="abdimalik.abdullahi@student.moringaschool.com", phone=1234567893, password=generate_password_hash(password)))
    # users.append(Users(first_name="George", last_name="Golder", email="george.golder@student.moringaschool.com", phone=1234567894, password=generate_password_hash(password)))
    # users.append(Users(first_name="Prince", last_name="Karanja", email="prince.karanja@student.moringaschool.com", phone=1234567895, password=generate_password_hash(password)))
    # users.append(Users(first_name="Evans", last_name="Kabiru", email="evans.kabiru@student.moringaschool.com", phone=1234567896, password=generate_password_hash(password)))
    # users.append(Users(first_name="Asmaa", last_name="Abdi", email="asmaa.abdi@student.moringaschool.com", phone=1234567897, password=generate_password_hash(password)))
    # users.append(Users(first_name="Melissa", last_name="Kiptoo", email="melissa.kiptoo@student.moringaschool.com", phone=1234567898, password=generate_password_hash(password)))
    # users.append(Users(first_name="Emmaculate", last_name="Mwikali", email="emmaculate.mwikali@student.moringaschool.com", phone=1234567899, password=generate_password_hash(password)))
    # users.append(Users(first_name="Brian", last_name="Joseph1", email="brian.joseph1@student.moringaschool.com", phone=1234567800, password=generate_password_hash(password)))
    # users.append(Users(first_name="Brian", last_name="Kamau1", email="brian.kamau1@student.moringaschool.com", phone=1234567801, password=generate_password_hash(password)))
    # users.append(Users(first_name="Luqman", last_name="Bashir", email="luqman.bashir@student.moringaschool.com", phone=1234567802, password=generate_password_hash(password)))
    # users.append(Users(first_name="Paul", last_name="Kamau2", email="Paul.kamau2@student.moringaschool.com", phone=1234567803, password=generate_password_hash(password)))
    # users.append(Users(first_name="Mubarak", last_name="Nassib", email="mubarak.nassib@student.moringaschool.com", phone=1234567804, password=generate_password_hash(password)))
    # users.append(Users(first_name="Samson", last_name="Wanjiru", email="samson.wanjiru@student.moringaschool.com", phone=1234567805, password=generate_password_hash(password)))
    # users.append(Users(first_name="Charles", last_name="Njoroge", email="charles.njoroge@student.moringaschool.com", phone=1234567806, password=generate_password_hash(password)))
    # users.append(Users(first_name="Adan", last_name="Abdullahi", email="adan.abdullahi@student.moringaschool.com", phone=1234567807, password=generate_password_hash(password)))
    # users.append(Users(first_name="Victor", last_name="Kichwen", email="victor.kichwen@student.moringaschool.com", phone=1234567808, password=generate_password_hash(password)))
    # users.append(Users(first_name="Sharon", last_name="Cherono", email="sharon.cherono@student.moringaschool.com", phone=1234567809, password=generate_password_hash(password)))
    # users.append(Users(first_name="Mwangi", last_name="Brian", email="mwangi.brian@student.moringaschool.com", phone=1234567810, password=generate_password_hash(password)))
    # users.append(Users(first_name="Faith", last_name="Njau", email="faith.njau@student.moringaschool.com", phone=1234567811, password=generate_password_hash(password)))
    # users.append(Users(first_name="Abdimalik", last_name="Omar1", email="abdimalik.omar1@student.moringaschool.com", phone=1234567812, password=generate_password_hash(password)))
    # users.append(Users(first_name="Owor", last_name="Ularé", email="owour.ulare@student.moringaschool.com", phone=1234567813, password=generate_password_hash(password)))
    # users.append(Users(first_name="Ashley", last_name="Natasha1", email="ashley.natasha1@student.moringaschool.com", phone=1234567814, password=generate_password_hash(password)))
    # users.append(Users(first_name="Eugine", last_name="Odera", email="eugine.odera@student.moringaschool.com", phone=1234567815, password=generate_password_hash(password)))
    # users.append(Users(first_name="Collins", last_name="Kathurima", email="collins.kathurima@student.moringaschool.com", phone=1234567816, password=generate_password_hash(password)))
    # users.append(Users(first_name="Iris", last_name="Macharia", email="iris.macharia@student.moringaschool.com", phone=1234567817, password=generate_password_hash(password)))
    # users.append(Users(first_name="Robin", last_name="Adhola", email="robin.adhola@student.moringaschool.com", phone=1234567818, password=generate_password_hash(password)))
    # users.append(Users(first_name="Anthony", last_name="Mwaura", email="anthony.mwaura@student.moringaschool.com", phone=1234567819, password=generate_password_hash(password)))
    # users.append(Users(first_name="Suudi", last_name="Abdisalan1", email="suudi.abdisalan1@student.moringaschool.com", phone=1234567820, password=generate_password_hash(password)))
    # users.append(Users(first_name="Roselyne", last_name="Mwaniki", email="roselyne.mwaniki@student.moringaschool.com", phone=1234567821, password=generate_password_hash(password)))
    # users.append(Users(first_name="Anne", last_name="Muriuki", email="anne.muriuki@student.moringaschool.com", phone=1234567822, password=generate_password_hash(password)))
    # users.append(Users(first_name="Kevin", last_name="Bett3", email="kevin.bett3@student.moringaschool.com", phone=1234567823, password=generate_password_hash(password)))
    # users.append(Users(first_name="Abdurizak", last_name="Abubakar", email="abdurizak.abubakar@student.moringaschool.com", phone=1234567824, password=generate_password_hash(password)))
    # users.append(Users(first_name="Elvis", last_name="Kuria", email="elvis.kuria@student.moringaschool.com", phone=1234567825, password=generate_password_hash(password)))
    # users.append(Users(first_name="Marion", last_name="Okondo", email="marion.okondo@student.moringaschool.com", phone=1234567826, password=generate_password_hash(password)))
    # users.append(Users(first_name="Samuel", last_name="Gitau1", email="samuel.gitau1@student.moringaschool.com", phone=1234567827, password=generate_password_hash(password)))
    # users.append(Users(first_name="Maxwel", last_name="Kirimi", email="maxwel.kirimi@student.moringaschool.com", phone=1234567828, password=generate_password_hash(password)))
    # users.append(Users(first_name="Zuruel", last_name="Kamande", email="zuruel.kamande@student.moringaschool.com", phone=1234567829, password=generate_password_hash(password)))
    # users.append(Users(first_name="Habsa", last_name="Abdirizack", email="habsa.abdirizack@student.moringaschool.com", phone=1234567830, password=generate_password_hash(password)))
    # users.append(Users(first_name="Peter", last_name="Mutua", email="peter.mutua@student.moringaschool.com", phone=1234567831, password=generate_password_hash(password)))
    # users.append(Users(first_name="Faith", last_name="Nguli", email="faith.nguli@student.moringaschool.com", phone=1234567832, password=generate_password_hash(password)))
    # users.append(Users(first_name="Erick", last_name="Tembo", email="erick.tembo@student.moringaschool.com", phone=1234567833, password=generate_password_hash(password)))
    # users.append(Users(first_name="Bradley", last_name="Ochieng", email="bradley.ochieng@student.moringaschool.com", phone=1234567834, password=generate_password_hash(password)))
    # users.append(Users(first_name="James", last_name="Kimani3", email="James.kimani3@student.moringaschool.com", phone=1234567835, password=generate_password_hash(password)))
    # users.append(Users(first_name="Sherlyne", last_name="Ochieng", email="sherlyne.ochieng@student.moringaschool.com", phone=1234567836, password=generate_password_hash(password)))
    # users.append(Users(first_name="Blessed", last_name="Wesonga", email="blessed.wesonga@student.moringaschool.com", phone=1234567837, password=generate_password_hash(password)))

    



    
    # Loans seeds
    loans.append(Loans(amount=5000000, interest_rate=1.2, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-01-20", "%Y-%m-%d").date(), loan_status="Active", user_id=1))
    # loans.append(Loans(amount=6000000, interest_rate=1.5, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-01-21", "%Y-%m-%d").date(), loan_status="Active", user_id=2))
    # loans.append(Loans(amount=7500000, interest_rate=1.3, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-01-22", "%Y-%m-%d").date(), loan_status="Paid", user_id=3))
    # loans.append(Loans(amount=4500000, interest_rate=1.4, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-01-23", "%Y-%m-%d").date(), loan_status="Active", user_id=4))
    # loans.append(Loans(amount=9000000, interest_rate=1.2, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-01-24", "%Y-%m-%d").date(), loan_status="Active", user_id=5))
    # loans.append(Loans(amount=3200000, interest_rate=1.6, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-01-25", "%Y-%m-%d").date(), loan_status="Paid", user_id=3))
    # loans.append(Loans(amount=4000000, interest_rate=1.5, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-01-26", "%Y-%m-%d").date(), loan_status="Active", user_id=2))
    # loans.append(Loans(amount=8500000, interest_rate=1.4, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-01-27", "%Y-%m-%d").date(), loan_status="Active", user_id=4))
    # loans.append(Loans(amount=1000000, interest_rate=1.3, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-01-28", "%Y-%m-%d").date(), loan_status="Active", user_id=5))
    # loans.append(Loans(amount=7000000, interest_rate=1.6, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-01-29", "%Y-%m-%d").date(), loan_status="Paid", user_id=5))
    # loans.append(Loans(amount=5500000, interest_rate=1.4, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-01-30", "%Y-%m-%d").date(), loan_status="Active", user_id=2))
    # loans.append(Loans(amount=6500000, interest_rate=1.2, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-02-01", "%Y-%m-%d").date(), loan_status="Paid", user_id=3))
    # loans.append(Loans(amount=8000000, interest_rate=1.7, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-02-02", "%Y-%m-%d").date(), loan_status="Active", user_id=4))
    # loans.append(Loans(amount=3600000, interest_rate=1.5, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-02-03", "%Y-%m-%d").date(), loan_status="Paid", user_id=5))
    # loans.append(Loans(amount=5200000, interest_rate=1.3, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-02-04", "%Y-%m-%d").date(), loan_status="Active", user_id=2))
    # loans.append(Loans(amount=9200000, interest_rate=1.4, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-02-05", "%Y-%m-%d").date(), loan_status="Paid", user_id=1))
    # loans.append(Loans(amount=9200000, interest_rate=1.4, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-02-05", "%Y-%m-%d").date(), loan_status="Paid", user_id=1))
    # loans.append(Loans(amount=5000000, interest_rate=3.2, start_date=datetime.strptime("15/02/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-03-15", "%Y-%m-%d").date(), loan_status="Pending", user_id=2))
    # loans.append(Loans(amount=7500000, interest_rate=2.1, start_date=datetime.strptime("25/03/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-04-25", "%Y-%m-%d").date(), loan_status="Pending", user_id=3))
    # loans.append(Loans(amount=6800000, interest_rate=2.5, start_date=datetime.strptime("05/04/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-05-05", "%Y-%m-%d").date(), loan_status="Paid", user_id=4))
    # loans.append(Loans(amount=9100000, interest_rate=1.8, start_date=datetime.strptime("10/05/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-06-10", "%Y-%m-%d").date(), loan_status="Pending", user_id=5))
    # loans.append(Loans(amount=10200000, interest_rate=2.9, start_date=datetime.strptime("15/06/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-07-15", "%Y-%m-%d").date(), loan_status="Paid", user_id=6))
    # loans.append(Loans(amount=6500000, interest_rate=2.3, start_date=datetime.strptime("20/07/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-08-20", "%Y-%m-%d").date(), loan_status="Pending", user_id=7))
    # loans.append(Loans(amount=7800000, interest_rate=3.0, start_date=datetime.strptime("30/08/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-09-30", "%Y-%m-%d").date(), loan_status="Paid", user_id=8))
    # loans.append(Loans(amount=8500000, interest_rate=1.7, start_date=datetime.strptime("05/09/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-10-05", "%Y-%m-%d").date(), loan_status="Pending", user_id=9))
    # loans.append(Loans(amount=9300000, interest_rate=2.4, start_date=datetime.strptime("10/10/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-11-10", "%Y-%m-%d").date(), loan_status="Paid", user_id=10))
    # loans.append(Loans(amount=7400000, interest_rate=2.8, start_date=datetime.strptime("15/11/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-12-15", "%Y-%m-%d").date(), loan_status="Pending", user_id=11))
    # loans.append(Loans(amount=9200000, interest_rate=2.2, start_date=datetime.strptime("20/12/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-01-20", "%Y-%m-%d").date(), loan_status="Paid", user_id=12))
    # loans.append(Loans(amount=8600000, interest_rate=2.0, start_date=datetime.strptime("10/01/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-02-10", "%Y-%m-%d").date(), loan_status="Pending", user_id=13))
    # loans.append(Loans(amount=9900000, interest_rate=3.5, start_date=datetime.strptime("15/02/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-03-15", "%Y-%m-%d").date(), loan_status="Paid", user_id=14))
    # loans.append(Loans(amount=10500000, interest_rate=1.6, start_date=datetime.strptime("25/03/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-04-25", "%Y-%m-%d").date(), loan_status="Pending", user_id=15))
    # loans.append(Loans(amount=8900000, interest_rate=2.7, start_date=datetime.strptime("05/04/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-05-05", "%Y-%m-%d").date(), loan_status="Paid", user_id=16))
    # loans.append(Loans(amount=7200000, interest_rate=2.3, start_date=datetime.strptime("15/05/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-06-15", "%Y-%m-%d").date(), loan_status="Pending", user_id=17))
    # loans.append(Loans(amount=9400000, interest_rate=2.1, start_date=datetime.strptime("20/06/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-07-20", "%Y-%m-%d").date(), loan_status="Paid", user_id=18))
    # loans.append(Loans(amount=8800000, interest_rate=1.9, start_date=datetime.strptime("30/07/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-08-30", "%Y-%m-%d").date(), loan_status="Pending", user_id=19))
    # loans.append(Loans(amount=9200000, interest_rate=3.0, start_date=datetime.strptime("10/08/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-09-10", "%Y-%m-%d").date(), loan_status="Paid", user_id=20))
    # loans.append(Loans(amount=7700000, interest_rate=2.5, start_date=datetime.strptime("15/09/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-10-15", "%Y-%m-%d").date(), loan_status="Pending", user_id=21))
    # loans.append(Loans(amount=8600000, interest_rate=2.2, start_date=datetime.strptime("20/10/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-11-20", "%Y-%m-%d").date(), loan_status="Paid", user_id=22))
    # loans.append(Loans(amount=9600000, interest_rate=3.1, start_date=datetime.strptime("10/11/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-12-10", "%Y-%m-%d").date(), loan_status="Pending", user_id=23))
    # loans.append(Loans(amount=8500000, interest_rate=1.8, start_date=datetime.strptime("15/12/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-01-15", "%Y-%m-%d").date(), loan_status="Paid", user_id=24))
    # loans.append(Loans(amount=9200000, interest_rate=2.4, start_date=datetime.strptime("20/01/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-02-20", "%Y-%m-%d").date(), loan_status="Pending", user_id=25))
    # loans.append(Loans(amount=9800000, interest_rate=2.0, start_date=datetime.strptime("10/02/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-03-10", "%Y-%m-%d").date(), loan_status="Paid", user_id=26))
    # loans.append(Loans(amount=7700000, interest_rate=2.3, start_date=datetime.strptime("25/03/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-04-25", "%Y-%m-%d").date(), loan_status="Pending", user_id=27))
    # loans.append(Loans(amount=8600000, interest_rate=1.7, start_date=datetime.strptime("05/04/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-05-05", "%Y-%m-%d").date(), loan_status="Paid", user_id=28))
    # loans.append(Loans(amount=9300000, interest_rate=3.3, start_date=datetime.strptime("15/05/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-06-15", "%Y-%m-%d").date(), loan_status="Pending", user_id=29))
    # loans.append(Loans(amount=8100000, interest_rate=2.1, start_date=datetime.strptime("20/06/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-07-20", "%Y-%m-%d").date(), loan_status="Paid", user_id=30))
    # loans.append(Loans(amount=9300000, interest_rate=2.9, start_date=datetime.strptime("30/07/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-08-30", "%Y-%m-%d").date(), loan_status="Pending", user_id=31))
    # loans.append(Loans(amount=8700000, interest_rate=1.5, start_date=datetime.strptime("10/08/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-09-10", "%Y-%m-%d").date(), loan_status="Paid", user_id=32))
    # loans.append(Loans(amount=8400000, interest_rate=2.4, start_date=datetime.strptime("20/09/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-10-20", "%Y-%m-%d").date(), loan_status="Pending", user_id=33))
    # loans.append(Loans(amount=8800000, interest_rate=3.0, start_date=datetime.strptime("10/10/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-11-10", "%Y-%m-%d").date(), loan_status="Paid", user_id=34))
    # loans.append(Loans(amount=9500000, interest_rate=2.5, start_date=datetime.strptime("15/11/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-12-15", "%Y-%m-%d").date(), loan_status="Pending", user_id=35))
    # loans.append(Loans(amount=9900000, interest_rate=3.7, start_date=datetime.strptime("05/12/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-01-05", "%Y-%m-%d").date(), loan_status="Paid", user_id=36))
    # loans.append(Loans(amount=8800000, interest_rate=2.8, start_date=datetime.strptime("15/01/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-02-15", "%Y-%m-%d").date(), loan_status="Pending", user_id=37))
    # loans.append(Loans(amount=8100000, interest_rate=1.9, start_date=datetime.strptime("25/02/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-03-25", "%Y-%m-%d").date(), loan_status="Paid", user_id=38))
    # loans.append(Loans(amount=9400000, interest_rate=3.1, start_date=datetime.strptime("10/03/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-04-10", "%Y-%m-%d").date(), loan_status="Pending", user_id=39))
    # loans.append(Loans(amount=9900000, interest_rate=2.6, start_date=datetime.strptime("15/04/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-05-15", "%Y-%m-%d").date(), loan_status="Paid", user_id=40))
    # loans.append(Loans(amount=9700000, interest_rate=2.3, start_date=datetime.strptime("25/05/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-06-25", "%Y-%m-%d").date(), loan_status="Pending", user_id=41))
    # loans.append(Loans(amount=8800000, interest_rate=3.2, start_date=datetime.strptime("05/06/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-07-05", "%Y-%m-%d").date(), loan_status="Paid", user_id=42))
    # loans.append(Loans(amount=9500000, interest_rate=2.9, start_date=datetime.strptime("15/07/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-08-15", "%Y-%m-%d").date(), loan_status="Pending", user_id=43))
    # loans.append(Loans(amount=9200000, interest_rate=2.0, start_date=datetime.strptime("25/08/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-09-25", "%Y-%m-%d").date(), loan_status="Paid", user_id=44))
    # loans.append(Loans(amount=8900000, interest_rate=2.6, start_date=datetime.strptime("10/09/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-10-10", "%Y-%m-%d").date(), loan_status="Pending", user_id=45))
    # loans.append(Loans(amount=9800000, interest_rate=3.4, start_date=datetime.strptime("20/10/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-11-20", "%Y-%m-%d").date(), loan_status="Paid", user_id=46))
    # loans.append(Loans(amount=8700000, interest_rate=2.3, start_date=datetime.strptime("15/11/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-12-15", "%Y-%m-%d").date(), loan_status="Pending", user_id=47))
    # loans.append(Loans(amount=9200000, interest_rate=1.4, start_date=datetime.strptime("20/01/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-02-05", "%Y-%m-%d").date(), loan_status="Paid", user_id=1))
    # loans.append(Loans(amount=15000000, interest_rate=2.1, start_date=datetime.strptime("15/02/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-05-20", "%Y-%m-%d").date(), loan_status="Pending", user_id=2))
    # loans.append(Loans(amount=7000000, interest_rate=1.8, start_date=datetime.strptime("10/03/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-07-10", "%Y-%m-%d").date(), loan_status="Approved", user_id=3))
    # loans.append(Loans(amount=11000000, interest_rate=1.5, start_date=datetime.strptime("25/03/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-12-25", "%Y-%m-%d").date(), loan_status="Pending", user_id=4))
    # loans.append(Loans(amount=5300000, interest_rate=1.9, start_date=datetime.strptime("05/04/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-04-05", "%Y-%m-%d").date(), loan_status="Paid", user_id=5))
    # loans.append(Loans(amount=6000000, interest_rate=2.3, start_date=datetime.strptime("18/05/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-08-30", "%Y-%m-%d").date(), loan_status="Approved", user_id=6))
    # loans.append(Loans(amount=4500000, interest_rate=1.7, start_date=datetime.strptime("30/06/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-06-30", "%Y-%m-%d").date(), loan_status="Pending", user_id=7))
    # loans.append(Loans(amount=8000000, interest_rate=2.0, start_date=datetime.strptime("20/07/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-09-20", "%Y-%m-%d").date(), loan_status="Approved", user_id=8))
    # loans.append(Loans(amount=14000000, interest_rate=2.5, start_date=datetime.strptime("15/08/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-01-15", "%Y-%m-%d").date(), loan_status="Paid", user_id=9))
    # loans.append(Loans(amount=7500000, interest_rate=1.6, start_date=datetime.strptime("02/09/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-03-02", "%Y-%m-%d").date(), loan_status="Pending", user_id=10))

    # loans.append(Loans(amount=9800000, interest_rate=1.9, start_date=datetime.strptime("10/10/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2026-10-10", "%Y-%m-%d").date(), loan_status="Approved", user_id=11))
    # loans.append(Loans(amount=11500000, interest_rate=2.2, start_date=datetime.strptime("20/11/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-11-20", "%Y-%m-%d").date(), loan_status="Pending", user_id=12))
    # loans.append(Loans(amount=7600000, interest_rate=1.7, start_date=datetime.strptime("05/12/2025", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-06-05", "%Y-%m-%d").date(), loan_status="Paid", user_id=13))
    # loans.append(Loans(amount=13200000, interest_rate=2.0, start_date=datetime.strptime("17/01/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-03-17", "%Y-%m-%d").date(), loan_status="Approved", user_id=14))
    # loans.append(Loans(amount=8500000, interest_rate=1.8, start_date=datetime.strptime("28/02/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-02-28", "%Y-%m-%d").date(), loan_status="Pending", user_id=15))
    # loans.append(Loans(amount=10500000, interest_rate=2.3, start_date=datetime.strptime("10/03/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-03-10", "%Y-%m-%d").date(), loan_status="Paid", user_id=16))
    # loans.append(Loans(amount=9500000, interest_rate=1.6, start_date=datetime.strptime("15/04/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-04-15", "%Y-%m-%d").date(), loan_status="Approved", user_id=17))
    # loans.append(Loans(amount=12500000, interest_rate=2.0, start_date=datetime.strptime("23/05/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-05-23", "%Y-%m-%d").date(), loan_status="Pending", user_id=18))
    # loans.append(Loans(amount=6700000, interest_rate=1.9, start_date=datetime.strptime("30/06/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-06-30", "%Y-%m-%d").date(), loan_status="Paid", user_id=19))

    # loans.append(Loans(amount=9500000, interest_rate=1.7, start_date=datetime.strptime("10/07/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-07-10", "%Y-%m-%d").date(), loan_status="Approved", user_id=20))
    # loans.append(Loans(amount=13000000, interest_rate=2.1, start_date=datetime.strptime("17/08/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-08-17", "%Y-%m-%d").date(), loan_status="Paid", user_id=21))
    # loans.append(Loans(amount=8800000, interest_rate=1.8, start_date=datetime.strptime("20/09/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-09-20", "%Y-%m-%d").date(), loan_status="Pending", user_id=22))
    # loans.append(Loans(amount=7700000, interest_rate=2.0, start_date=datetime.strptime("01/10/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-10-01", "%Y-%m-%d").date(), loan_status="Approved", user_id=23))
    # loans.append(Loans(amount=11500000, interest_rate=2.4, start_date=datetime.strptime("12/11/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-11-12", "%Y-%m-%d").date(), loan_status="Paid", user_id=24))
    # loans.append(Loans(amount=8000000, interest_rate=1.6, start_date=datetime.strptime("30/12/2026", "%d/%m/%Y").date(), due_date=datetime.strptime("2027-12-30", "%Y-%m-%d").date(), loan_status="Pending", user_id=25))
    # loans.append(Loans(amount=10500000, interest_rate=2.2, start_date=datetime.strptime("15/01/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-01-15", "%Y-%m-%d").date(), loan_status="Approved", user_id=26))
    # loans.append(Loans(amount=6800000, interest_rate=1.9, start_date=datetime.strptime("05/02/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-02-05", "%Y-%m-%d").date(), loan_status="Paid", user_id=27))
    # loans.append(Loans(amount=8500000, interest_rate=2.0, start_date=datetime.strptime("15/03/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-03-15", "%Y-%m-%d").date(), loan_status="Pending", user_id=28))

    # loans.append(Loans(amount=12500000, interest_rate=2.3, start_date=datetime.strptime("01/04/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-04-01", "%Y-%m-%d").date(), loan_status="Approved", user_id=29))
    # loans.append(Loans(amount=9200000, interest_rate=1.8, start_date=datetime.strptime("10/05/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-05-10", "%Y-%m-%d").date(), loan_status="Paid", user_id=30))
    # loans.append(Loans(amount=13400000, interest_rate=2.1, start_date=datetime.strptime("20/06/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-06-20", "%Y-%m-%d").date(), loan_status="Pending", user_id=31))
    # loans.append(Loans(amount=6700000, interest_rate=1.7, start_date=datetime.strptime("02/07/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-07-02", "%Y-%m-%d").date(), loan_status="Approved", user_id=32))
    # loans.append(Loans(amount=10000000, interest_rate=2.4, start_date=datetime.strptime("14/08/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-08-14", "%Y-%m-%d").date(), loan_status="Paid", user_id=33))
    # loans.append(Loans(amount=12500000, interest_rate=2.0, start_date=datetime.strptime("25/09/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-09-25", "%Y-%m-%d").date(), loan_status="Pending", user_id=34))
    # loans.append(Loans(amount=8900000, interest_rate=1.9, start_date=datetime.strptime("05/10/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-10-05", "%Y-%m-%d").date(), loan_status="Approved", user_id=35))
    # loans.append(Loans(amount=10300000, interest_rate=2.2, start_date=datetime.strptime("15/11/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-11-15", "%Y-%m-%d").date(), loan_status="Paid", user_id=36))

    # loans.append(Loans(amount=7300000, interest_rate=1.8, start_date=datetime.strptime("25/12/2027", "%d/%m/%Y").date(), due_date=datetime.strptime("2028-12-25", "%Y-%m-%d").date(), loan_status="Pending", user_id=37))
    # loans.append(Loans(amount=9000000, interest_rate=2.1, start_date=datetime.strptime("10/01/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-01-10", "%Y-%m-%d").date(), loan_status="Approved", user_id=38))
    # loans.append(Loans(amount=11000000, interest_rate=2.0, start_date=datetime.strptime("20/02/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-02-20", "%Y-%m-%d").date(), loan_status="Paid", user_id=39))
    # loans.append(Loans(amount=12400000, interest_rate=2.3, start_date=datetime.strptime("01/03/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-03-01", "%Y-%m-%d").date(), loan_status="Pending", user_id=40))
    # loans.append(Loans(amount=7600000, interest_rate=1.7, start_date=datetime.strptime("10/04/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-04-10", "%Y-%m-%d").date(), loan_status="Approved", user_id=41))
    # loans.append(Loans(amount=13000000, interest_rate=2.5, start_date=datetime.strptime("25/05/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-05-25", "%Y-%m-%d").date(), loan_status="Paid", user_id=42))
    # loans.append(Loans(amount=6900000, interest_rate=1.6, start_date=datetime.strptime("10/06/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-06-10", "%Y-%m-%d").date(), loan_status="Pending", user_id=43))
    # loans.append(Loans(amount=9800000, interest_rate=2.2, start_date=datetime.strptime("20/07/2028", "%d/%m/%Y").date(), due_date=datetime.strptime("2029-07-20", "%Y-%m-%d").date(), loan_status="Approved", user_id=44))


        
    # ADMIN SEEDS
    admins.append(Admins(first_name = "David", last_name = "Parsley", email = "davidparsley.kakhayanga@gmail.com", phone = 1111111 , password=generate_password_hash(password)))

    # Insert each Loan and User in the list into the database tables
    db.session.add_all(users)
    db.session.add_all(loans)
    db.session.add_all(admins)


    # Commit the transaction
    db.session.commit()