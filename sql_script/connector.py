import mysql.connector
from mysql.connector.errors import Error


class Connector:
    def __init__(self,host,user,password,port,database):
        self.user = user
        self.password = password
        self.db= database
        try:
            super(Connector, self).__init__()
            self.connection = mysql.connector.connect(host=host, user=user, password=password, port=port,database=database)
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
        except Error as err:
            print("Database connection error: {}".format(err))

    def close_connection(self):
        return self.connection.close()

    def insert_houses(self,house_df):
        for i, row in house_df.iterrows():
            self.insert_house(row['house_id'],
                            row['address'],
                            row['tax_status'],
                            row['business_status'],
                            row['business_type'],
                            row['owner_id'],
                            row['area'],
                            row['latitude'],
                            row['longitude'])


    def insert_house(self, house_id, address, tax_status, business_status, business_type, owner_id, area, latitude,longitude):
        query = (
            "INSERT INTO house(house_id, address,tax_status,business_status,business_type,owner_id,area,latitude,longitude)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        self.cursor.execute(query,
                            [house_id, address, tax_status, business_status, business_type, owner_id, area, latitude,
                             longitude])

        self.connection.commit()

    def insert_many_people(self, people_df):
        for i, row in people_df.iterrows():
            self.insert_people(row['people_id'],
                              row['first_name'],
                              row['last_name'],
                              row['dob'],
                              row['father_name'],
                              row['mother_name'],
                              row['house_id'],
                        )

    def insert_people(self, people_id, first_name,last_name,dob,father_name,mother_name,house_id):
        query = (
            "INSERT INTO people(people_id, first_name,last_name,dob,father_name,mother_name,house_id)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s)")
        self.cursor.execute(query,
                            [people_id, first_name,last_name,dob,father_name,mother_name,house_id])

        self.connection.commit()

    def read_script(self,path):
        try:
            with open(path,'r') as sql_file:
                self.cursor.execute(sql_file.read(),multi=True)
        except Error as err:
            print("Error while reading: {}".format(err))


