import random
import uuid
import pandas as pd
import datetime
import  numpy as np
from faker import Faker

from random import randint,randrange
class Simulate:
  def __init__(self, n_house,sub_dis_path,pro_path,dis_path):
    self.sub_district_df = pd.read_csv(sub_dis_path).replace(r'\N' ,np.nan).dropna()
    self.pro_df = pd.read_csv(pro_path).dropna()
    self.dis_df = pd.read_csv(dis_path).dropna()

    self.business_type_lst = ["Sole Proprietorship","Partnership","Limited Liability Company","Corporation"]
    self.n_house = n_house
    self.n_people = 3*n_house
    self.house_id = [uuid.uuid4().hex[:6].upper() for i in range(self.n_house)]




  def random_ab(self,min_range,max_range):
    b = randrange(min_range, max_range-1)
    a = randrange(b+1, max_range)

    return a,b

  def gen_address(self,min_range,max_range):
      a,b = self.random_ab(min_range,max_range)
      province = np.random.choice(self.pro_df['name_en'])
      district = np.random.choice(self.dis_df['name_en'])
      sub_district = np.random.choice(self.sub_district_df['name_en'])
      address = '{a}/{b} {province} {district} {sub_district} '.format(a=a,b=b,province=province,district=district,sub_district=sub_district)
      return address

  def make_house(self):
    house_df=  {
      'house_id': self.house_id,
      'address': [self.gen_address(100,999) for i in range(self.n_house)],
      'tax_status': [ random.randint(0, 1) for i in range(self.n_house)],
      'business_status': [ random.randint(0, 1) for i in range(self.n_house)],
      'business_type': [random.choice(self.business_type_lst) for i in range(self.n_house)],
      'owner_id':  [uuid.uuid4().hex[:3].upper() for i in range(self.n_house)],
      'area': [round(random.uniform(30.00,120.00), 3) for i in range(self.n_house) ],
      'latitude': [np.random.choice(self.sub_district_df['lat'])  for i in range(self.n_house)],
      'longitude': [np.random.choice(self.sub_district_df['long'])  for i in range(self.n_house)],
    }
    return pd.DataFrame(house_df)

  def make_people(self):
    faker = Faker()
    people_df = {
      'people_id': [uuid.uuid4().hex[:8].upper() for i in range(self.n_people)],
      'house_id': [np.random.choice(self.house_id) for i in range(self.n_people)],
      'first_name': [faker.first_name() for i in range(self.n_people)],
      'last_name': [faker.last_name() for i in range(self.n_people)],
      'dob': [datetime.datetime.now() for i in range(self.n_people)],
      'father_name': [faker.first_name() for i in range(self.n_people)],
      'mother_name': [faker.first_name() for i in range(self.n_people)],
    }
    return pd.DataFrame(people_df)


















