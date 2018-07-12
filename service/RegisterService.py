from sqlalchemy.orm import sessionmaker
from models import connect, DUser, DDoctorInfo, DPrivateKey
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA256
from sql.sql_functions import get_next_id
import uuid

session_class = sessionmaker(bind=connect)


class RegisterService:
    @staticmethod
    def private_key_generate():
        key = DSA.generate(1024)
        y = str(key.y)
        g = str(key.g)
        p = str(key.p)
        q = str(key.q)
        x = str(key.x)
        next_id = get_next_id('d_private_key')
        return [y, g, p, q, x], next_id

    def register(self, username, password, doctor_info):
        session = session_class()
        user = session.query(DUser).filter_by(username=username).first()
        if user is None:
            salt = str(uuid.uuid4()).replace('-', '')
            pwd = SHA256.new((password + salt).encode("utf8")).hexdigest()
            key, key_id = self.private_key_generate()
            key_data = DPrivateKey(key_y=key[0], key_g=key[1], key_p=key[2], key_q=key[3], key_x=key[4])
            user_data = DUser(username=username, salt=salt, pwd=pwd, doctor_info_id=get_next_id('d_doctor_info'))
            info_data = DDoctorInfo(name=doctor_info[0], department_id=doctor_info[1], gender=doctor_info[2],
                                    age=doctor_info[3], private_key_id=key_id)
            try:
                session.add(key_data)
                session.flush()
                session.add(info_data)
                session.flush()
                session.add(user_data)
                session.commit()
            except:
                session.rollback()
                print('数据库错误！')
                session.close()
                return False
            session.close()
            return True
        print('用户已存在')
        return False


# RegisterService().register(username='admin3', password='123456', doctor_info=['hkp', 1, 1, 22])
