import os 
from flask import Flask
from flask_migrate import Migrate
from models import db, TokenBlocklist
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_mail import Mail
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)
CORS(app)


app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://deltabankdb_rgxh_user:nmo0hmbUgnXsSsI4pJcP6JsCajiygWBt@dpg-cvubfj7gi27c73agotag-a.oregon-postgres.render.com/deltabankdb_rgxh'
migrate = Migrate(app, db)
db.init_app(app)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "fallbackSecretKey")  
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=55)

jwt = JWTManager(app)
jwt.init_app(app)

from views import *

app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(loan_bp)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None

# if __name__ == '__main__':
#     app.run(debug=True)
