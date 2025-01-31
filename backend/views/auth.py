from flask import jsonify, request, Blueprint
from models import Users, Admins, db, TokenBlocklist, Loans
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from datetime import datetime, timedelta, timezone
from flask_mail import  Message
from app import mail



auth_bp = Blueprint("auth_bp", __name__)

# LOGIN USER
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    user = Users.query.filter_by(email=email).first()
    admin = Admins.query.filter_by(email=email).first()

    if user:
        if check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id, additional_claims={'is_user': True}) # Do more research on addition_claims

            current_date = datetime.now().strftime("%d-%m-%Y")
            msg = Message('Successful Login', sender='david.kakhayanga@student.moringaschool.com', recipients=[email])

            msg.html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Successful Login</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f9;
                        margin: 0;
                        padding: 0;
                    }}
                    .container {{
                        width: 100%;
                        max-width: 600px;
                        margin: 0 auto;
                        padding: 20px;
                        background-color: #ffffff;
                        border-radius: 8px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    }}
                    .header {{
                        text-align: center;
                        padding-bottom: 20px;
                    }}
                    .header h1 {{
                        color: #11172b;
                        font-size: 24px;
                    }}
                    .body-content {{
                        font-size: 16px;
                        line-height: 1.6;
                        margin-bottom: 20px;
                    }}
                    .footer {{
                        font-size: 14px;
                        color: #777;
                        text-align: center;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Successful Login</h1>
                    </div>
                    <div class="body-content">
                        <p>Hello {user.first_name} {user.last_name},</p>
                        <p>You have successfully logged in to your Delta Bank account.</p>
                        <p>If you did not initiate this login, please contact us immediately.</p>
                        <p>Thank you for using Delta Bank!</p>
                    </div>
                    <div class="footer">
                        <p><i>Sent on: {current_date}</i></p>
                    </div>
                </div>
            </body>
            </html>
            """

            mail.send(msg)
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"error": "Incorrect Password "}), 404

    elif admin:
        if check_password_hash(admin.password, password):
            access_token = create_access_token(identity=admin.id, additional_claims={'is_admin': True}) # Do more research on addition_claims 
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"error": "Incorrect Admin Password"}), 404
    else:
        return jsonify({"error": "Email not found for both User or Admin"}), 404


# CURRENT USER
@auth_bp.route("/current_user", methods=["GET"])
@jwt_required()
def current_user():
    current_user_id = get_jwt_identity()
    claims = get_jwt()  # This will retrieve the JWT claims

    if claims.get('is_admin'):
        admin = Admins.query.get(current_user_id)
        if admin:
            admin_data = {
                'id': admin.id,
                'first_name': admin.first_name,
                'last_name': admin.last_name,
                'email': admin.email,
                'phone': admin.phone,
                'is_admin': True 
            }
            return jsonify(admin_data), 200
        else:
            return jsonify({"message": "Admin not found"}), 404

    elif claims.get("is_user"):
        user = Users.query.get(current_user_id)
        if user:
            user_data = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone,
                'is_user': True 
            }
            return jsonify(user_data), 200
    else:
        return jsonify({"message": "User not found"}), 404


# LOG OUT CURRENT USER
@auth_bp.route("/logout", methods=["DELETE"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    db.session.add(TokenBlocklist(jti=jti, created_at=now))
    db.session.commit()
    return jsonify({"success": "Logged Out successfully"}), 200