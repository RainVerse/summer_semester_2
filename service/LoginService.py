from sqlalchemy.orm import sessionmaker
from models import connect, DUser
from Crypto.Hash import SHA256

session_class = sessionmaker(bind=connect)


class LoginService:
    def login(self, username, password):
        session = session_class()
        user = session.query(DUser).filter_by(username=username).first()
        if user is None:
            ret = False, '用户不存在！'
        else:
            salt = user.salt
            e_pwd = user.pwd
            if SHA256.new((password + salt).encode("utf8")).hexdigest() == e_pwd:
                ret = True, '登陆成功'
            else:
                ret = False, '用户名或密码错误！'
        session.close()
        return ret


# print(LoginService().login('admin', '1234567'))
