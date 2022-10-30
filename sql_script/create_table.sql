

CREATE TABLE arv_test.house (
  house_id VARCHAR(45) NOT NULL,
  address TEXT(40) NOT NULL,
  tax_status BIT(1) NULL,
  business_status BIT(1) NULL,
  business_type VARCHAR(45) NOT NULL,
  owner_id VARCHAR(45) NULL,
  area FLOAT(5) NULL,
  latitude FLOAT(5) NULL,
  longitude FLOAT(5) NULL,
  PRIMARY KEY (`house_id`),
  UNIQUE INDEX `house_id_UNIQUE` (`house_id` ASC) VISIBLE);

CREATE TABLE arv_test.people (
    people_id VARCHAR(45) NOT NULL,
    first_name TEXT(20) NULL,
    last_name TEXT(20) NULL,
    dob TIMESTAMP NULL,
   father_name TEXT(20) NULL,
   mother_name TEXT(20) NULL,
   house_id VARCHAR(45) NULL,
  PRIMARY KEY (people_id),
  UNIQUE INDEX people_id_UNIQUE (people_id ASC) VISIBLE,
  INDEX house_id_idx (house_id ASC) VISIBLE,
  CONSTRAINT house_id
    FOREIGN KEY (house_id)
    REFERENCES arv_test.house (house_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
