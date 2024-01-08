import copy
import os
from datetime import datetime

from login_db.enums import TokenStatus, TokenType
from login_db.models import Token
#from api.logger import get_logger
from jose import jwt
from sqlalchemy.orm import Session

#logger = get_logger(__name__)

def insert_token(user_id: str, token: str, type: TokenType, expiration_time: datetime,
                          status: TokenStatus, session: Session):
    try:
        token = Token(user_id=user_id, token=token, type=type,
                      expiration_time=expiration_time, status=status)
        session.add(token)
        session.commit()
        #logger.info(f"Token for user with ID '{user_id}' successfully inserted into the database.")
    
    except Exception as e:
        #logger.error(e)
        raise e


def create_jwt_token(data: dict, session: Session) -> str:
    """
    Create a JWT token.
    """
    # TODO: try except?
    to_encode = copy.deepcopy(data)
    token = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    insert_token(user_id=data["sub"],
                 token=token,
                 type=TokenType.ACCESS,
                 status=TokenStatus.ACTIVE,
                 expiration_time=data["exp"],
                 session=session)
    return token