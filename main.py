from sql_script.connector import Connector
from sql_script import config
from sql_script.simulate import Simulate
from valid_parentheses.valid_parentheses import ValidParentheses


if __name__ == '__main__':
    db = Connector(config.host, config.user, config.password, config.port,config.database)
    db.read_script(config.file_path)
    sm = Simulate(1000,config.sub_dis_path,config.pro_path,config.dis_path)
    house_df = sm.make_house()
    people_df = sm.make_people()
    db.insert_houses(house_df)
    db.insert_many_people(people_df)
    db.close_connection()
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([])}"
    s5 = "{([])}"
    print(ValidParentheses.valid_parenthesis(s1))

