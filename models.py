from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class DDepartment(Base):
    __tablename__ = 'd_department'

    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)


class DDigitalSign(Base):
    __tablename__ = 'd_digital_sign'

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, nullable=False)
    record_id = Column(Integer, nullable=False)
    sign_1 = Column(String(50), nullable=False)
    sign_2 = Column(String(50), nullable=False)


class DDoctorInfo(Base):
    __tablename__ = 'd_doctor_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(8), nullable=False)
    department_id = Column(Integer, nullable=False)
    gender = Column(Integer, server_default=text("'0'"))
    age = Column(Integer)
    priviate_key_id = Column(Integer, nullable=False)


class DMedicalRecord(Base):
    __tablename__ = 'd_medical_record'

    id = Column(Integer, primary_key=True)
    r_name = Column(String(8), nullable=False)
    company = Column(String(32), nullable=False)
    gender = Column(Integer, nullable=False)
    address = Column(String(128), nullable=False)
    age = Column(Integer, nullable=False)
    department_id = Column(Integer, nullable=False)
    nation = Column(String(10), nullable=False)
    r_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    symptom = Column(String(256), nullable=False)
    conclusion = Column(String(256), nullable=False)


class DPrivateKey(Base):
    __tablename__ = 'd_private_key'

    id = Column(Integer, primary_key=True)
    key_y = Column(String(308), nullable=False)
    key_g = Column(String(308), nullable=False)
    key_p = Column(String(308), nullable=False)
    key_q = Column(String(308), nullable=False)
    key_x = Column(String(308), nullable=False)


class DUser(Base):
    __tablename__ = 'd_user'

    id = Column(Integer, primary_key=True)
    username = Column(String(12), nullable=False)
    pwd = Column(String(64), nullable=False)
    salt = Column(String(32), nullable=False)
    doctor_info_id = Column(Integer, nullable=False)


from CONFIG import config

connect = create_engine(
    'mysql+mysqlconnector://' + config.DATABASE_USER + ':' + config.DATABASE_PASSWORD + '@' + config.DATABASE_HOST + ':' + str(
        config.DATABASE_PORT) + '/' + config.DATABASE_NAME + '?charset='+config.DATABASE_ENCODING)
