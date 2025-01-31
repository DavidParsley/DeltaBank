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