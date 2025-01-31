from flask import jsonify, request, Blueprint
from models import Loans, Users, db, Admins
from flask_jwt_extended import  jwt_required, get_jwt_identity, get_jwt
from datetime import datetime


loan_bp = Blueprint("loan_bp", __name__)

# ADD A LOAN
@loan_bp.route("/loan", methods=["POST"])
@jwt_required()
def add_loan():
    current_user_id = get_jwt_identity()
    admin = Admins.query.get(current_user_id)
  
    data = request.get_json()
    print(data)

    amount = data['amount']
    interest_rate = data['interest_rate']
    loan_status = data['loan_status']
    start_date = data['start_date']
    due_date = data['due_date']
    user_id = data['user_id']

    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

    chech_user_id = Users.query.get(user_id)

    if not chech_user_id:
        return jsonify({"error":"User doesn't exists"}),406
    
    if admin is None:
        return jsonify({"error":"Must be an admin to add a loan "}),406

    else:
        new_loan = Loans(amount=amount, interest_rate=interest_rate, loan_status=loan_status, start_date=start_date, user_id=user_id, due_date=due_date)
        
        db.session.add(new_loan)
        db.session.commit()
        return jsonify({"success":"Loan added successfully"}), 201
    

# ADMIN FETCHING ALL LOANS IN THE DB  and USER FETCHING ALL LOANS RELATED TO THEM WHILE LOGED IN
@loan_bp.route("/loans", methods=["GET"])
@jwt_required()
def fetch_loans():
    current_user_id = get_jwt_identity()
    claims = get_jwt()  

    if claims.get('is_admin'):  
        loans = Loans.query.all()
        loan_list = []
        for loan in loans:
            loan_list.append({     
                "id": loan.id,
                "amount": loan.amount,
                "interest_rate": loan.interest_rate,
                "loan_status": loan.loan_status,
                "start_date": loan.start_date,
                "due_date": loan.due_date,
                "user_id": {"id": loan.users.id, "First Name": loan.users.first_name, "Last Name": loan.users.last_name, "Email": loan.users.email, "Phone": loan.users.phone}
            })
        return jsonify(loan_list)

    else: 
        user = Users.query.get(current_user_id)
        if user:
            loans = Loans.query.filter_by(user_id=current_user_id).all()
            loan_list = []
            for loan in loans:
                loan_list.append({     
                    "id": loan.id,
                    "amount": loan.amount,
                    "interest_rate": loan.interest_rate,
                    "loan_status": loan.loan_status,
                    "start_date": loan.start_date,
                    "due_date": loan.due_date,
                    "user_id": {"id": loan.users.id, "First Name": loan.users.first_name, "Last Name": loan.users.last_name, "Email": loan.users.email, "Phone": loan.users.phone}
                })
            return jsonify(loan_list)
        else:
            return jsonify({"error": "User not found"}), 404    
        

# FETCH A SINGLE LOAN RELATED TO THE CURRENT USER LOGED IN
@loan_bp.route("/loan/<int:loan_id>", methods=["GET"])
@jwt_required()
def fetch_loan(loan_id):
    current_user_id = get_jwt_identity()
    loan = Loans.query.filter_by(id=loan_id, user_id=current_user_id).first()

    if loan:
        loan_data = {
            "id": loan.id,
            "amount": loan.amount,
            "interest_rate": loan.interest_rate,
            "loan_status": loan.loan_status,
            "start_date": loan.start_date,
            "due_date": loan.due_date,
            # "created_at": loan.created_at,
            "user_id": {
                "id": loan.users.id,
                "First Name": loan.users.first_name,
                "Last Name": loan.users.last_name,
                "Email": loan.users.email,
                "Phone": loan.users.phone
            }
          
        }

        return jsonify(loan_data)
    
    return jsonify({"error": f'Loan selected is not assigned to You'}), 406 


# UPDATE A LOAN
@loan_bp.route("/loan/<int:loan_id>", methods=["PATCH"])
@jwt_required()
def update_loan(loan_id):
    # current_user_id = get_jwt_identity()
    claims = get_jwt()  

    if claims.get('is_admin'):
        loan = Loans.query.get(loan_id)
        if loan:

            data = request.get_json()
            amount = data.get('amount', loan.amount)
            interest_rate = data.get('interest_rate', loan.interest_rate)
            loan_status = data.get('loan_status', loan.loan_status)
            # start_date = data.get('start_date', loan.start_date)
            due_date = data.get('due_date', loan.due_date)  
            # user_id = data.get('user_id', loan.user_id)

            # check_user_id = Users.query.get(user_id)

            # if not check_user_id:
            #     return jsonify({"error": "User doesn't exist"}), 404  
            
            # start_date = datetime.strptime(start_date, "%m-%d-%Y").date()
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            loan.amount = amount
            loan.interest_rate = interest_rate
            loan.loan_status = loan_status
            # loan.start_date = start_date
            loan.due_date = due_date
            # loan.user_id = user_id

            db.session.commit()
            return jsonify({"success": "Loan updated successfully"}), 200

    return jsonify({"error": "Must be an admin to update a loan!"}), 404  