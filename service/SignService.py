from sqlalchemy.orm import sessionmaker
from models import connect, DUser, DMedicalRecord, DPrivateKey, DDoctorInfo, DDigitalSign
from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA256

session_class = sessionmaker(bind=connect)


class SignService:
    def sign(self, user_id, record_id):
        session = session_class()
        digital_sign = session.query(DDigitalSign).filter_by(doctor_id=user_id, record_id=record_id).first()
        if digital_sign is not None:
            session.close()
            return False, '该病历已被签名'
        user = session.query(DUser).filter_by(id=user_id).first()
        if user is None:
            session.close()
            return False, '用户不存在'
        info = session.query(DDoctorInfo).filter_by(id=user.doctor_info_id).first()
        if user is None:
            session.close()
            return False, '用户信息不存在'
        private_key = session.query(DPrivateKey).filter_by(id=info.private_key_id).first()
        if private_key is None:
            session.close()
            return False, '用户密钥不存在'
        record = session.query(DMedicalRecord).filter_by(id=record_id).first()
        if record is None:
            session.close()
            return False, '病历不存在'
        plain_text = str(record.id) + record.r_name + record.company + str(record.gender) + record.address + str(
            record.age) + str(record.department_id) + record.nation + record.symptom + str(
            record.r_date.year) + '.' + str(record.r_date.month) + '.' + str(record.r_date.day) + record.conclusion
        print(len(plain_text), plain_text)
        hashed_text = SHA256.new(plain_text.encode('utf-8')).digest()
        print(len(hashed_text), hashed_text)
        key = DSA.construct(
            (int(private_key.key_y), int(private_key.key_g), int(private_key.key_p), int(private_key.key_q),
             int(private_key.key_x)))
        k = random.StrongRandom().randint(1, key.q - 1)
        sign = key.sign(hashed_text, k)
        sign_data=DDigitalSign(doctor_id=user_id,record_id=record_id,sign_1=str(sign[0]),sign_2=str(sign[1]))
        try:
            session.add(sign_data)
            session.commit()
            session.close()
            return True,'签名成功'
        except:
            session.rollback()
            session.close()
            return False,'数据库错误'


def validate(self):
    return False


print(SignService().sign(3, 1))
