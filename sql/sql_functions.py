from sqlalchemy.orm import sessionmaker
from models import connect, DDepartment, DUser, DDoctorInfo

session_class = sessionmaker(bind=connect)


def get_next_id(table_name):
    session = session_class()
    ret = session.execute(
        'select AUTO_INCREMENT from INFORMATION_SCHEMA.TABLES  where TABLE_NAME = \'' + table_name + '\'')
    next_id = [(dict(row.items())) for row in ret][0].get('AUTO_INCREMENT')
    session.close()
    return next_id


def get_department_list():
    session = session_class()
    ret = session.query(DDepartment).all()
    session.close()
    return [(d.name, d.id) for d in ret]


def get_user_name_by_id(user_id):
    session = session_class()
    user = session.query(DUser).filter_by(id=user_id).first()
    if user is None:
        return ''
    info = session.query(DDoctorInfo).filter_by(id=user.doctor_info_id).first()
    if info is None:
        return ''
    session.close()
    return info.name


# print(get_department_list())
