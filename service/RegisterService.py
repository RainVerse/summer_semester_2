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
        y = str(key.__getattr__('y'))
        g = str(key.__getattr__('g'))
        p = str(key.__getattr__('p'))
        q = str(key.__getattr__('q'))
        x = str(key.__getattr__('x'))
        DPrivateKey(key_y=y, key_g=g, key_p=p, key_q=q, key_x=x)
        next_id = get_next_id('d_private_key')
        return DPrivateKey, next_id

    def register(self, username, password, doctor_info):
        session = session_class()
        user = session.query(DUser).filter_by(username=username).first()
        if user is None:
            salt = str(uuid.uuid4()).replace('-', '')
            print(salt)
            pwd = SHA256.new((password + salt).encode("utf8")).digest()
            key_data,key_id=self.private_key_generate()
            user_data = DUser(username=username, salt=salt, pwd=pwd, doctor_info_id=get_next_id('d_doctor_info'))
            info_data = DDoctorInfo(name='',department_id=0,gender=0,age=0,priviate_key_id=key_id)
            session.add(key_data)
            session.add(info_data)
            session.add(user_data)
            session.commit()
            session.close()
            return True
        return False

