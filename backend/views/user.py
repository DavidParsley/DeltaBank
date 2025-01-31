from flask import jsonify, request, Blueprint
from models import Users, db, Loans
from flask_jwt_extended import  jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash
from flask_mail import  Message
from datetime import datetime
from app import mail


user_bp = Blueprint("user_bp", __name__)

# REGISTERED A USER
@user_bp.route("/user", methods=["POST"])
def register_user():
    data = request.get_json()
    first_name = data["first_name"]
    last_name = data["last_name"]
    email = data["email"]
    password = data["password"]
    phone = data["phone"]

    check_email = Users.query.filter_by(email=email).first()
    print("email", check_email)
    if check_email:
        return jsonify({"error": "Email exists"}), 404
    
    check_phone = Users.query.filter_by(phone=phone).first()
    print("phone", check_phone)
    if check_phone:
        return jsonify({"error": "Phone Number exists"}), 404
    
    else:
        new_user = Users(first_name=first_name, last_name=last_name, email=email, password=generate_password_hash(password), phone=phone)
        db.session.add(new_user)
        db.session.commit()

        current_date = datetime.now().strftime("%d-%m-%Y")
        msg = Message('Welcome to Delta Bank', sender='david.kakhayanga@student.moringaschool.com', recipients=[email])

        msg.html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Delta Bank</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #333;
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
                }}
                .body-content {{
                    font-size: 16px;
                    line-height: 1.6;
                    margin-bottom: 20px;
                }}
                .footer {{
                    text-align: center;
                    font-size: 14px;
                    color: #777;
                }}
                .cta-button {{
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #1E90FF;
                    color: #ffffff;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Welcome to Delta Bank !</h1>
                </div>
                <div class="body-content">
                    <p>Hello {first_name} {last_name},</p>
                    <p>Welcome aboard 🎉 ! We're excited to have you with us at Delta Bank.</p>
                    <p>At Delta Bank, we prioritize your financial success. We're here to ensure all your transactions are smooth, secure, and hassle-free. Should you have any questions or require assistance, feel free to reach out to our friendly support team anytime.</p>
                    <p>We're looking forward to being part of your financial journey!</p>
                </div>
                <div class="footer">
                    <p>Best regards,<br>The Delta Bank Team</p>
                    <p><i>Sent on: {current_date}</i></p>
                </div>
            </div>
        </body>
        </html>
        """

        mail.send(msg)
        
        return jsonify({"msg": "User Registered Successfully"}), 200