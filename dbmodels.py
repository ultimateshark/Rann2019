import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class AdminsTable(db.Model):
	__tablename__="badelog"
	a_id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),nullable=False)
	email=db.Column(db.String(100),unique=True)
	passwd=db.Column(db.String(200),nullable=False)
	authority=db.Column(db.String(100),nullable=False)

class TempCompetitors(db.Model):
	__tablename__="tempcompetitors"
	c_id=db.Column(db.Integer,primary_key=True)
	email=db.Column(db.String(100),unique=True)
	passwd=db.Column(db.String(200),nullable=False)
	name=db.Column(db.String(50),nullable=False)
	father_name=db.Column(db.String(50),nullable=False)
	roll_no=db.Column(db.String(12),nullable=False)
	college=db.Column(db.String(200),nullable=False)
	branch=db.Column(db.String(50),nullable=False)
	year=db.Column(db.Integer,nullable=False)
	gender=db.Column(db.String(1),nullable=False)
	mob_no=db.Column(db.String(13),nullable=False)
	otp=db.Column(db.String(7),unique=True)


class Competitors(db.Model):
	__tablename__="competitors"	
	c_id=db.Column(db.Integer,primary_key=True)
	email=db.Column(db.String(100),unique=True)
	passwd=db.Column(db.String(200),nullable=False)
	name=db.Column(db.String(50),nullable=False)
	father_name=db.Column(db.String(50),nullable=False)
	roll_no=db.Column(db.String(12),nullable=False)
	college=db.Column(db.String(200),nullable=False)
	branch=db.Column(db.String(50),nullable=False)
	year=db.Column(db.Integer,nullable=False)
	gender=db.Column(db.String(1),nullable=False)
	mob_no=db.Column(db.String(13),nullable=False)

class Members(db.Model):
	__tablename__="teammembers"	
	m_id=db.Column(db.Integer,primary_key=True)
	captain_id=db.Column(db.Integer,nullable=False)
	aadhar=db.Column(db.String(100),unique=True,nullable=False)
	name=db.Column(db.String(50),nullable=False)
	food_lodge=db.Column(db.Boolean,nullable=False)
	events_participated=db.Column(db.String(150),nullable=False)

class Events(db.Model):
	__tablename__="events"
	event_id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(50),nullable=False)
	min_participants=db.Column(db.Integer,nullable=False)
	max_participants=db.Column(db.Integer,nullable=False)
	types=db.Column(db.String(200),nullable=False)
	rules=db.Column(db.String(10000),nullable=False)
	stu_co=db.Column(db.String(50),nullable=False)
	stu_co_contact=db.Column(db.String(100),nullable=False)
	teach_co=db.Column(db.String(50),nullable=False)
	amount=db.Column(db.String(50),nullable=False)

class Participation(db.Model):
	__tablename__="participation"
	p_id=db.Column(db.Integer,primary_key=True)
	captain_id=db.Column(db.Integer,nullable=False)
	event_id=db.Column(db.Integer,nullable=False)
	team_id=db.Column(db.Integer,nullable=False)

class BasketBall(db.Model):
	__tablename__="basketBall"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False)
	captain_id=db.Column(db.Integer,nullable=False,unique=True)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=False)
	member2_id=db.Column(db.Integer,nullable=False)
	member3_id=db.Column(db.Integer,nullable=False)
	member4_id=db.Column(db.Integer,nullable=False)
	member5_id=db.Column(db.Integer,nullable=False)
	member6_id=db.Column(db.Integer,nullable=False)
	member7_id=db.Column(db.Integer,nullable=False)
	member8_id=db.Column(db.Integer,nullable=True)
	member9_id=db.Column(db.Integer,nullable=True)
	member10_id=db.Column(db.Integer,nullable=True)
	member11_id=db.Column(db.Integer,nullable=True)

class FootBall(db.Model):
	__tablename__="footBall"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=False)
	member2_id=db.Column(db.Integer,nullable=False)
	member3_id=db.Column(db.Integer,nullable=False)
	member4_id=db.Column(db.Integer,nullable=False)
	member5_id=db.Column(db.Integer,nullable=False)
	member6_id=db.Column(db.Integer,nullable=False)
	member7_id=db.Column(db.Integer,nullable=False)
	member8_id=db.Column(db.Integer,nullable=False)
	member9_id=db.Column(db.Integer,nullable=False)
	member10_id=db.Column(db.Integer,nullable=False)
	member11_id=db.Column(db.Integer,nullable=False)
	member12_id=db.Column(db.Integer,nullable=False)
	member13_id=db.Column(db.Integer,nullable=True)
	member14_id=db.Column(db.Integer,nullable=True)

class Cricket(db.Model):
	__tablename__="cricket"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=False)
	member2_id=db.Column(db.Integer,nullable=False)
	member3_id=db.Column(db.Integer,nullable=False)
	member4_id=db.Column(db.Integer,nullable=False)
	member5_id=db.Column(db.Integer,nullable=False)
	member6_id=db.Column(db.Integer,nullable=False)
	member7_id=db.Column(db.Integer,nullable=False)
	member8_id=db.Column(db.Integer,nullable=False)
	member9_id=db.Column(db.Integer,nullable=False)
	member10_id=db.Column(db.Integer,nullable=False)
	member11_id=db.Column(db.Integer,nullable=False)
	member12_id=db.Column(db.Integer,nullable=False)
	member13_id=db.Column(db.Integer,nullable=True)
	member14_id=db.Column(db.Integer,nullable=True)

class Khokho(db.Model):
	__tablename__="khokho"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=False)
	member2_id=db.Column(db.Integer,nullable=False)
	member3_id=db.Column(db.Integer,nullable=False)
	member4_id=db.Column(db.Integer,nullable=False)
	member5_id=db.Column(db.Integer,nullable=False)
	member6_id=db.Column(db.Integer,nullable=False)
	member7_id=db.Column(db.Integer,nullable=False)
	member8_id=db.Column(db.Integer,nullable=False)
	member9_id=db.Column(db.Integer,nullable=False)
	member10_id=db.Column(db.Integer,nullable=False)
	member11_id=db.Column(db.Integer,nullable=False)

class VollyBall(db.Model):
	__tablename__="vollyBall"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=False)
	member2_id=db.Column(db.Integer,nullable=False)
	member3_id=db.Column(db.Integer,nullable=False)
	member4_id=db.Column(db.Integer,nullable=False)
	member5_id=db.Column(db.Integer,nullable=False)
	member6_id=db.Column(db.Integer,nullable=False)
	member7_id=db.Column(db.Integer,nullable=False)
	member8_id=db.Column(db.Integer,nullable=True)
	member9_id=db.Column(db.Integer,nullable=True)
	member10_id=db.Column(db.Integer,nullable=True)
	member11_id=db.Column(db.Integer,nullable=True)

class Tabletennis(db.Model):
	__tablename__="tabletennis"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	team_type=db.Column(db.String(50),nullable=False)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=True)
	member2_id=db.Column(db.Integer,nullable=True)
	member3_id=db.Column(db.Integer,nullable=True)

class Pool(db.Model):
	__tablename__="pool"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	team_type=db.Column(db.String(50),nullable=False)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=True)

class Chess(db.Model):
	__tablename__="chess"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	team_type=db.Column(db.String(50),nullable=False)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=True)
	member2_id=db.Column(db.Integer,nullable=True)
	member3_id=db.Column(db.Integer,nullable=True)
	member4_id=db.Column(db.Integer,nullable=True)

class Lawntennis(db.Model):
	__tablename__="lawntennis"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	team_type=db.Column(db.String(50),nullable=False)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=True)

class Badminton(db.Model):
	__tablename__="badminton"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	team_type=db.Column(db.String(50),nullable=False)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=False)
	member2_id=db.Column(db.Integer,nullable=True)
	member3_id=db.Column(db.Integer,nullable=True)
	member4_id=db.Column(db.Integer,nullable=True)
	member5_id=db.Column(db.Integer,nullable=True)
	member6_id=db.Column(db.Integer,nullable=True)

class Carrom(db.Model):
	__tablename__="carrom"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	team_type=db.Column(db.String(50),nullable=False)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=True)
	member2_id=db.Column(db.Integer,nullable=True)
	member3_id=db.Column(db.Integer,nullable=True)
	member4_id=db.Column(db.Integer,nullable=True)





#new Changes

class Pubg(db.Model):
	__tablename__="pubg"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)
	member1_id=db.Column(db.Integer,nullable=True)
	member2_id=db.Column(db.Integer,nullable=True)
	member3_id=db.Column(db.Integer,nullable=True)


class Fifa(db.Model):
	__tablename__="fifa"
	team_id=db.Column(db.Integer,primary_key=True)
	team_name=db.Column(db.String(100),nullable=False,unique=True)
	captain_id=db.Column(db.Integer,nullable=False)
	noc=db.Column(db.Boolean,nullable=False)
	amt_paid=db.Column(db.Integer,nullable=False)
	payment=db.Column(db.Boolean,nullable=False)
	transaction_id=db.Column(db.String(100),nullable=True)

class Pendingpayment(db.Model):
	__tablename__="pendingpayment"
	p_id=db.Column(db.Integer,primary_key=True)
	cust_id=db.Column(db.String(100),nullable=False)
	order_id=db.Column(db.String(100),nullable=False,unique=True)
	amount=db.Column(db.String(100),nullable=False)
	status=db.Column(db.String(100),nullable=False)