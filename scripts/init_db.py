from login_db.functions.user import insert_user
from login_db.enums import UserStatus

if __name__ == '__main__':
    users = [{"username": "user1", "email": "user1@user1.com", "password": "password1", "status": UserStatus.ACTIVE},
             {"username": "user2", "email": "user2@user2.com", "password": "password2", "status": UserStatus.ACTIVE}
            ]
    for userdata in users:
        insert_user(userdata)