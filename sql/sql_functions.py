from sqlalchemy.orm import sessionmaker
from models import connect, DDepartment

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
    return [(d.name,d.id) for d in ret]

# print(get_department_list())
