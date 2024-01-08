
from login_db.models import User
from login_db.exceptions import DatabaseInsertionError
#from api.logger import get_logger
from passlib.hash import bcrypt
from sqlalchemy.orm import Session

#logger = get_#logger(__name__)


def insert_user(userdata: dict, session=Session):
    """
    Insert a new user into the users table.

    :param session: The session to use for the database connection.
    :param userdata: A dictionary containing the user data.
    :raises DatabaseInsertionError: If insertion into the database fails.
    """
    try:
        username = userdata["username"]
        user_in_db = session.query(User).filter_by(username=username).first()
        if user_in_db is not None: 
            raise DatabaseInsertionError(f"User with username '{username}' already exists.")
        
        email = userdata["email"]
        email_in_db = session.query(User).filter_by(email=email).first()        
        if email_in_db is not None:
            raise DatabaseInsertionError(f"User with email '{email}' already exists.")
    
        userdata["password"] = bcrypt.hash(userdata["password"])
        new_user = User(**userdata)
        session.add(new_user)
        session.commit()
        #logger.info(f"User with username '{username}' successfully inserted into the database.")
    
    except Exception as e:
        #logger.error(e)
        raise e
    
    
def modify_user_password(username_id: str, password: str, session=Session):
    """
    Modify the password of an existing user.

    :param username_id: The username_id of the user.
    :param password: The raw password of the user which will be hashed before storage.
    :raises DatabaseInsertionError: If insertion into the database fails.
    """
    try:
        user = session.query(User).filter(User.id == username_id).first()
        user.password = bcrypt.hash(password)
        session.commit()
        #logger.info(f"Password for user with username_id '{username_id}' successfully modified.")

    except Exception as e:
        #logger.error(e)
        raise e


def retrieve_user(username_or_email: str, session=Session) -> User: # TODO: type session
    """
    Retrieve a user from the users table.

    :param username_id: The username_id of the user.
    :return: The user object. None if the user does not exist.
    """
    try:
        mask = (User.username == username_or_email) | (User.email == username_or_email)
        user = session.query(User).filter(mask).first()
        return user
    except Exception as e:
        #logger.error(e)
        raise e
    

def is_username_password_valid(username_or_email:str, password:str, session=Session) -> bool:
    """
    Check if the given username or email and password are valid.

    :param username_or_email: The username or email to check.
    :param password: The password to check.
    :return: True if the username and password are valid, False otherwise.
    """
    user = retrieve_user(username_or_email, session)
    return bcrypt.verify(password, user.password) if user is not None else False