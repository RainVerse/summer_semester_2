from sqlalchemy.orm import sessionmaker
from models import connect, DMedicalRecord, DDigitalSign, DDoctorInfo,DUser
from sql.sql_functions import get_department_list
from service.SignService import SignService

session_class = sessionmaker(bind=connect)


class RecordService:
    def add_record(self, record_info):
        session = session_class()
        record = session.query(DMedicalRecord).filter_by(r_name=record_info.get('name')).first()
        if record is None:
            record_data = DMedicalRecord(r_name=record_info.get('name'), company=record_info.get('company'),
                                         gender=record_info.get('gender'), address=record_info.get('address'),
                                         age=record_info.get('age'), department_id=record_info.get('department_id'),
                                         nation=record_info.get('nation'), symptom=record_info.get('symptom'),
                                         conclusion=record_info.get('conclusion'))
            try:
                session.add(record_data)
                session.commit()
            except:
                session.rollback()
                session.close()
                return False, '数据库错误'
            session.close()
            return True, '添加病历成功'
        return False, '用户病历已存在'

    @staticmethod
    def get_record_data(name):
        session = session_class()
        record = session.query(DMedicalRecord).filter_by(r_name=name).first()
        if record is None:
            session.close()
            return None
        department_list = get_department_list()
        department = None
        for d in department_list:
            if d[1] == record.department_id:
                department = d[0]
        if department is None:
            session.close()
            return None
        sign = session.query(DDigitalSign).filter_by(record_id=record.id).first()
        sign_doctor = None
        if sign is not None:
            user = session.query(DUser).filter_by(id=sign.doctor_id).first()
            if user is None:
                session.close()
                return None
            doctor_info=session.query(DDoctorInfo).filter_by(id=user.doctor_info_id).first()
            if doctor_info is not None:
                sign_doctor = doctor_info.name
            else:
                print('数据库错误')
                session.close()
                return None
        session.close()
        data = {'id': record.id, 'name': record.r_name, 'company': record.company, 'gender': record.gender,
                'address': record.address,
                'age': record.age, 'department': department, 'nation': record.nation, 'symptom': record.symptom,
                'date': str(record.r_date.year) + '.' + str(record.r_date.month) + '.' + str(record.r_date.day),
                'conclusion': record.conclusion, 'sign': sign_doctor}
        return data

    def update_record_data(self, user_id, record_id, updated_record_info):
        session = session_class()
        record = session.query(DMedicalRecord).filter_by(id=record_id).first()
        if record is None:
            session.close()
            return False, '病历不存在'
        is_signed = session.query(DDigitalSign).filter_by(record_id=record_id).first() is not None
        if not is_signed:
            record.symptom = updated_record_info.get('symptom')
            record.conclusion = updated_record_info.get('conclusion')
            try:
                session.commit()
                session.close()
                return True, '修改成功'
            except:
                session.rollback()
                session.close()
                return False, '数据库错误'
        else:
            session.close()
            updated_data = str(record.id) + record.r_name + record.company + str(record.gender) + record.address + str(
                record.age) + str(record.department_id) + record.nation + updated_record_info.get('symptom') + str(
                record.r_date.year) + '.' + str(record.r_date.month) + '.' + str(
                record.r_date.day) + updated_record_info.get('conclusion')
            state, result = SignService().validate(user_id, record_id, updated_data)
            if not state:
                return False, result
            else:
                if result:
                    return True, '验证通过，然而并没有修改'
                else:
                    return False, '验证失败，修改失败'


# print(RecordService().add_record(
#     {'name': 'cm', 'company': '419', 'gender': 1, 'address': 'ssdut419', 'age': 21, 'department_id': 1, 'nation': '汉族',
#      'symptom': '智障', 'conclusion': '没救了'}))
# print(RecordService().get_record_data('曹迈'))
print(RecordService().update_record_data(3, 1, {'symptom': '智障', 'conclusion': '没救了'}))
