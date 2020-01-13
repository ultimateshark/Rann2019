from flask import Flask,render_template,url_for,request,session,flash,redirect,jsonify
from passlib.hash import sha256_crypt
from dbmodels import *
from functools import wraps
from random import randint
from flask_mail import Mail,Message
import printteamdetails as ptd

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:mom0511@localhost/Rann2019"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
db.app=app

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='rann@kiet.edu'
app.config['MAIL_PASSWORD']='RANN2K19'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)


@app.route("/sponsors")
def sponsors():
	return render_template("sponsors.html")


@app.route("/")
def Home():
	try:
		if session['logged_in']:
			return redirect("/user/home")
		else:
			return render_template("main.html")
	except:
		return render_template("main.html")

@app.route("/rann2k19/k/admins/loginpage")
def AdminLoginpage():
 	return render_template("login.html",redir="rann2k19/k/admins/ka/login")

@app.route("/check-email",methods=["GET","POST"])
def check_email():
	results = ["No"]
	email_id = request.form.get('aadhar_no')
	if Competitors.query.filter_by(email=email_id).count()>0:
		results=["Yes"]
	return jsonify(results)

@app.route("/check-teamname",methods=["GET","POST"])
def check_teamname():
	results = ["No"]
	team = request.form.get('team')
	event = request.form.get('event')
	if event=="Pool":
		if Pool.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="Carrom":
		if Carrom.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="Chess":
		if Chess.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="FootBall":
		if FootBallo.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="BasketBall":
		if BasketBall.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="Cricket":
		if Cricket.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="Volleyball":
		if Vollyball.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="Tabletennis":
		if Tabletennis.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="Lawntennis":
		if Lawntennis.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="Khokho":
		if Khokho.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="Badminton":
		if Badminton.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="Pubg":
		if Pubg.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	elif event=="Fifa":
		if Fifa.query.filter_by(team_name=team).count()>0:
			results=["Yes"]
	return jsonify(results)


@app.route("/check-part",methods=["GET","POST"])
def check_part():
	results = ["No"]
	aadhar = request.form.get('aadhar_no')
	event = request.form.get('event')
	eventtype = request.form.get('eventtype')
	if event=="Pool":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="Double" or eventtype=="MixedDouble":
				if ("pool"+eventtype) in mem.events_participated.split("-"):
					results=["Yes"]
			elif eventtype=="Single":
				if "poolS" in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="Carrom":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="TeamEvent":
				if "carrom" in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="Chess":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="TeamEvent":
				if "chessT" in mem.events_participated.split("-"):
					results=["Yes"]
			elif eventtype=="Single":
				if "chessS" in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="FootBall":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="TeamEvent":
				if "football" in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="BasketBall":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="TeamEvent":
				if "basketball" in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="Cricket":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="TeamEvent":
				if "cricket" in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="Volleyball":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="TeamEvent":
				if "volleyball" in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="Tabletennis":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="Single":
				if "tabletennis" in mem.events_participated.split("-"):
					results=["Yes"]
			elif eventtype=="Double":
				if ("tabletennis"+eventtype) in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="Lawntennis":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="Single":
				if "lawntennisS" in mem.events_participated.split("-"):
					results=["Yes"]
			elif eventtype=="Double" or eventtype=="MixedDouble":
				if ("lawntennis"+eventtype) in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="Khokho":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="TeamEvent":
				if "khokho" in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="Badminton":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="TeamEvent":
				if "badmintonT" in mem.events_participated.split("-"):
					results=["Yes"]
			elif eventtype=="MixedDouble":
				if "badminton" in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="Pubg":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="TeamEvent":
				if "pubg" in mem.events_participated.split("-"):
					results=["Yes"]
	elif event=="Fifa":
		if Members.query.filter_by(aadhar=aadhar).count()>0:
			mem=Members.query.filter_by(aadhar=aadhar).first()
			if eventtype=="Single":
				if "fifa" in mem.events_participated.split("-"):
					results=["Yes"]
	return jsonify(results)




@app.route("/user/<string:path>",methods=["GET","POST"])
def User_Profile(path):
	try:
		if session["logged_in"]:
			client_email=session["username"]
			client_data=Competitors.query.filter_by(email=client_email).first()
			path=path.split("-")
			if path[0]=="home":
				event_list=[]
				if Participation.query.filter_by(captain_id=client_data.c_id).count()>0:
					events_participated=Participation.query.filter_by(captain_id=client_data.c_id).all()
					for reg_event in events_participated:
						event_list+=[Events.query.filter_by(event_id=reg_event.event_id).first().name]
				return render_template("userpage.html",userdata=client_data,event_list=event_list)
			#payment changes
			elif path[0]=="makepayment":
				try:
					if path[1]=="Pool":
						pid=838280
						team=Pool.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Cricket":
						pid=789588
						team=Cricket.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Football":
						pid=678123
						team=FootBall.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Khokho":
						pid=771410
						team=Khokho.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Volleyball":
						pid=771417
						team=VolleyBall.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Chess":
						pid=789153
						team=Chess.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Pubg":
						pid=523984
						team=Pubg.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Basketball":
						pid=156987
						team=BasketBall.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Tabletennis":
						pid=624813
						team=Tabletennis.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Lawntennis":
						pid=852013
						team=Lawntennis.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Fifa":
						pid=852741
						team=Fifa.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Badminton":
						pid=205555
						team=Badminton.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
					elif path[1]=="Carrom":
						pid=173946
						team=Carrom.query.filter_by(team_id=path[3]).first()
						return redirect("https://www.kiet.edu/erp-apis/index.php/payment/do_transaction?APP_KEY=RANN_19_QAZPLA&CUST_ID="+str(pid)+str(team.team_id)+"&TXN_AMOUNT="+str(team.amt_paid)+"&CALLBACK_URL=http://rann.kiet.edu/verify-payment")
				except:
					return render_template("errorpage.html",error="Some Error Occured")

			elif path[0]=="register":
				if path[1]=="typeselection":
					types=Events.query.filter_by(name=path[2]).first().types
					if len(types.split("-"))==1:
						return redirect("/user/register-teamDetails-TeamEvent-"+path[2])
					else:
						return render_template("typeselection.html",types=types,eventname=path[2])
				elif path[1]=="teamDetails":
					captain=Competitors.query.filter_by(email=client_email).first()
					if path[2]=="Single":
						return render_template("teamDetails.html",captain=captain,members=0,min_members=0,eventtype=path[2],eventname=path[3])
					elif path[2]=="Doubles" or path[2]=="MixedDouble":
						return render_template("teamDetails.html",captain=captain,members=1,min_members=1,eventtype=path[2],eventname=path[3])
					else:
						if path[3]=="Badminton" and captain.gender=="F":
							max_participants=4
							min_participants=2
						else:
							members=Events.query.filter_by(name=path[3]).first()
							max_participants=members.max_participants-1
							min_participants=members.min_participants-1
						return render_template("teamDetails.html",captain=captain,members=max_participants,min_members=min_participants,eventtype=path[2],eventname=path[3])
				elif path[1]=="teaminfo":
					try:
						captain=Competitors.query.filter_by(email=client_email).first()
						if request.method=="POST":
							eventname=path[3]
							eventtype=path[2]
							eventdetails=Events.query.filter_by(name=eventname).first()
							if eventname=="Pool":
								if eventtype=="Double" or eventtype=="MixedDouble":
									amt_paid=400
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									member1_name=request.form["name1"]
									aadhar_no1=request.form["aadhar_no1"]
									food_lodge1=request.form["food_lodge1"]=="Yes"
									if food_lodge1:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated=("pool"+eventtype))
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if ("pool"+eventtype) in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+("-pool"+eventtype)
									if Members.query.filter_by(aadhar=aadhar_no1).count()==0:
										new_user=Members(name=member1_name,aadhar=aadhar_no1,captain_id=captain.c_id,food_lodge=food_lodge1,events_participated=("pool"+eventtype))
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no1).first()
										if ("pool"+eventtype) in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+("-pool"+eventtype)
									member1=Members.query.filter_by(aadhar=aadhar_no1).first()
									new_team=Pool(team_name=team_name,amt_paid=amt_paid,payment=False,team_type=eventtype,captain_id=captain.c_id,noc=True,member1_id=member1.m_id)
									db.session.add(new_team)
									#db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Pool.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									#flash("REGISTERED")
									return render_template("successpage.html",msg="REGISTERED")
								elif eventtype=="Single":
									amt_paid=200
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="poolS")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "poolS" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-poolS"
									member1=Members.query.filter_by(aadhar=aadhar_no).first()
									new_team=Pool(team_name=team_name,amt_paid=amt_paid,payment=False,team_type=eventtype,captain_id=captain.c_id,noc=True)
									db.session.add(new_team)
									#db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Pool.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
								else:
									return render_template("errorpage.html",error="Some Error Occured")
							elif eventname=="Carrom":
								if eventtype=="TeamEvent":
									amt_paid=1000
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="carrom")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "carrom" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-carrom"
									memId={}
									aadhar_no_check={}
									for i in range(1,5):
										name=request.form["name"+str(i)]
										aadhar=request.form["aadhar_no"+str(i)]
										food_lodge=request.form["food_lodge"+str(i)]=="Yes"
										if food_lodge:
											amt_paid+=600
										if Members.query.filter_by(aadhar=aadhar).count()==0:
											new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="carrom")
											db.session.add(new_user)
											#db.session.commit()
										else:
											mem=Members.query.filter_by(aadhar=aadhar).first()
											if "carrom" in mem.events_participated.split("-"):
												return str(mem.name)+" Participated In This Event"
											mem.events_participated=mem.events_participated+"-carrom"
											#db.session.commit()
										aadhar_no_check[str(i)]=aadhar
									db.session.commit()
									for i in range(1,5):
										memId[str(i)]=Members.query.filter_by(aadhar=aadhar_no_check[str(i)]).first().m_id
									new_team=Carrom(team_name=team_name,amt_paid=amt_paid,payment=False,team_type=eventtype,captain_id=captain.c_id,noc=True,member1_id=memId["1"],member2_id=memId["2"],member3_id=memId["3"],member4_id=memId["4"])
									db.session.add(new_team)
									#db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Carrom.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
							elif eventname=="Football":
								if eventtype=="TeamEvent":
									amt_paid=3500 if captain.gender=="M" else 1500
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="football")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "football" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-football"
									memId={}
									aadhar_no_check={}
									for i in range(1,13):
										name=request.form["name"+str(i)]
										aadhar=request.form["aadhar_no"+str(i)]
										food_lodge=request.form["food_lodge"+str(i)]=="Yes"
										if food_lodge:
											amt_paid+=600
										if Members.query.filter_by(aadhar=aadhar).count()==0:
											new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="football")
											db.session.add(new_user)
											#db.session.commit()
										else:
											mem=Members.query.filter_by(aadhar=aadhar).first()
											if "football" in mem.events_participated.split("-"):
												return str(mem.name)+" Participated In This Event"
											mem.events_participated=mem.events_participated+"-football"
										aadhar_no_check[str(i)]=aadhar
									db.session.commit()
									for i in range(1,13):
										memId[str(i)]=Members.query.filter_by(aadhar=aadhar_no_check[str(i)]).first().m_id
									for i in range(13,15):
										if len(request.form["aadhar_no"+str(i)])>0:
											name=request.form["name"+str(i)]
											aadhar=request.form["aadhar_no"+str(i)]
											food_lodge=request.form["food_lodge"+str(i)]=="Yes"
											if food_lodge:
												amt_paid+=600
											if Members.query.filter_by(aadhar=aadhar).count()==0:
												new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="football")
												db.session.add(new_user)
												db.session.commit()
											else:
												mem=Members.query.filter_by(aadhar=aadhar).first()
												if "football" in mem.events_participated.split("-"):
													return str(mem.name)+" Participated In This Event"
												mem.events_participated=mem.events_participated+"-football"
												db.session.commit()
											memId[str(i)]=Members.query.filter_by(aadhar=aadhar).first().m_id
										else:
											memId[str(i)]=None
									new_team=FootBall(team_name=team_name,amt_paid=amt_paid,payment=False,captain_id=captain.c_id,noc=True,member1_id=memId["1"],member2_id=memId["2"],member3_id=memId["3"],member4_id=memId["4"],member5_id=memId["5"],member6_id=memId["6"],member7_id=memId["7"],member8_id=memId["8"],member9_id=memId["9"],member10_id=memId["10"],member11_id=memId["11"],member12_id=memId["12"],member13_id=memId["13"],member14_id=memId["14"])
									db.session.add(new_team)
									db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=FootBall.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
							elif eventname=="Volleyball":
								if eventtype=="TeamEvent":
									amt_paid=2500
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="volleyball")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "volleyball" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-volleyball"
									memId={}
									aadhar_no_check={}
									for i in range(1,8):
										name=request.form["name"+str(i)]
										aadhar=request.form["aadhar_no"+str(i)]
										food_lodge=request.form["food_lodge"+str(i)]=="Yes"
										if food_lodge:
											amt_paid+=600
										if Members.query.filter_by(aadhar=aadhar).count()==0:
											new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="volleyball")
											db.session.add(new_user)
											#db.session.commit()
										else:
											mem=Members.query.filter_by(aadhar=aadhar).first()
											if "volleyball" in mem.events_participated.split("-"):
												return str(mem.name)+" Participated In This Event"
											mem.events_participated=mem.events_participated+"-volleyball"
										aadhar_no_check[str(i)]=aadhar
									db.session.commit()
									for i in range(1,8):
										memId[str(i)]=Members.query.filter_by(aadhar=aadhar_no_check[str(i)]).first().m_id
									for i in range(8,12):
										if len(request.form["aadhar_no"+str(i)])>0:
											name=request.form["name"+str(i)]
											aadhar=request.form["aadhar_no"+str(i)]
											food_lodge=request.form["food_lodge"+str(i)]=="Yes"
											if food_lodge:
												amt_paid+=600
											if Members.query.filter_by(aadhar=aadhar).count()==0:
												new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="volleyball")
												db.session.add(new_user)
												db.session.commit()
											else:
												mem=Members.query.filter_by(aadhar=aadhar).first()
												if "volleyball" in mem.events_participated.split("-"):
													return str(mem.name)+" Participated In This Event"
												mem.events_participated=mem.events_participated+"-volleyball"
												db.session.commit()
											memId[str(i)]=Members.query.filter_by(aadhar=aadhar).first().m_id
										else:
											memId[str(i)]=None
									new_team=VollyBall(team_name=team_name,amt_paid=amt_paid,payment=False,captain_id=captain.c_id,noc=True,member1_id=memId["1"],member2_id=memId["2"],member3_id=memId["3"],member4_id=memId["4"],member5_id=memId["5"],member6_id=memId["6"],member7_id=memId["7"],member8_id=memId["8"],member9_id=memId["9"],member10_id=memId["10"],member11_id=memId["11"])
									db.session.add(new_team)
									db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=VollyBall.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
							elif eventname=="Cricket":
								if eventtype=="TeamEvent":
									amt_paid=3500
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="cricket")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "cricket" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-cricket"
									memId={}
									aadhar_no_check={}
									for i in range(1,13):
										name=request.form["name"+str(i)]
										aadhar=request.form["aadhar_no"+str(i)]
										food_lodge=request.form["food_lodge"+str(i)]=="Yes"
										if food_lodge:
											amt_paid+=600
										if Members.query.filter_by(aadhar=aadhar).count()==0:
											new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="cricket")
											db.session.add(new_user)
											#db.session.commit()
										else:
											mem=Members.query.filter_by(aadhar=aadhar).first()
											if "cricket" in mem.events_participated.split("-"):
												return str(mem.name)+" Participated In This Event"
											mem.events_participated=mem.events_participated+"-cricket"
										aadhar_no_check[str(i)]=aadhar
									db.session.commit()
									for i in range(1,13):
										memId[str(i)]=Members.query.filter_by(aadhar=aadhar_no_check[str(i)]).first().m_id
									for i in range(13,15):
										if len(request.form["aadhar_no"+str(i)])>0:
											name=request.form["name"+str(i)]
											aadhar=request.form["aadhar_no"+str(i)]
											food_lodge=request.form["food_lodge"+str(i)]=="Yes"
											if food_lodge:
												amt_paid+=600
											if Members.query.filter_by(aadhar=aadhar).count()==0:
												new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="cricket")
												db.session.add(new_user)
												db.session.commit()
											else:
												mem=Members.query.filter_by(aadhar=aadhar).first()
												if "cricket" in mem.events_participated.split("-"):
													return str(mem.name)+" Participated In This Event"
												mem.events_participated=mem.events_participated+"-cricket"
												db.session.commit()
											memId[str(i)]=Members.query.filter_by(aadhar=aadhar).first().m_id
										else:
											memId[str(i)]=None
									new_team=Cricket(team_name=team_name,amt_paid=amt_paid,payment=False,captain_id=captain.c_id,noc=True,member1_id=memId["1"],member2_id=memId["2"],member3_id=memId["3"],member4_id=memId["4"],member5_id=memId["5"],member6_id=memId["6"],member7_id=memId["7"],member8_id=memId["8"],member9_id=memId["9"],member10_id=memId["10"],member11_id=memId["11"],member12_id=memId["12"],member13_id=memId["13"],member14_id=memId["14"])
									db.session.add(new_team)
									db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Cricket.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
							elif eventname=="Basketball":
								if eventtype=="TeamEvent":
									amt_paid=2500
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="basketball")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "basketball" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-basketball"
									memId={}
									aadhar_no_check={}
									for i in range(1,8):
										name=request.form["name"+str(i)]
										aadhar=request.form["aadhar_no"+str(i)]
										food_lodge=request.form["food_lodge"+str(i)]=="Yes"
										if food_lodge:
											amt_paid+=600
										if Members.query.filter_by(aadhar=aadhar).count()==0:
											new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="basketball")
											db.session.add(new_user)
											#db.session.commit()
										else:
											mem=Members.query.filter_by(aadhar=aadhar).first()
											if "basketball" in mem.events_participated.split("-"):
												return str(mem.name)+" Participated In This Event"
											mem.events_participated=mem.events_participated+"-basketball"
										aadhar_no_check[str(i)]=aadhar
									db.session.commit()
									for i in range(1,8):
										memId[str(i)]=Members.query.filter_by(aadhar=aadhar_no_check[str(i)]).first().m_id
									for i in range(8,12):
										if len(request.form["aadhar_no"+str(i)])>0:
											name=request.form["name"+str(i)]
											aadhar=request.form["aadhar_no"+str(i)]
											food_lodge=request.form["food_lodge"+str(i)]=="Yes"
											if food_lodge:
												amt_paid+=600
											if Members.query.filter_by(aadhar=aadhar).count()==0:
												new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="basketball")
												db.session.add(new_user)
												db.session.commit()
											else:
												mem=Members.query.filter_by(aadhar=aadhar).first()
												if "basketball" in mem.events_participated.split("-"):
													return str(mem.name)+" Participated In This Event"
												mem.events_participated=mem.events_participated+"-basketball"
												db.session.commit()
											memId[str(i)]=Members.query.filter_by(aadhar=aadhar).first().m_id
										else:
											memId[str(i)]=None
									new_team=BasketBall(team_name=team_name,amt_paid=amt_paid,payment=False,captain_id=captain.c_id,noc=True,member1_id=memId["1"],member2_id=memId["2"],member3_id=memId["3"],member4_id=memId["4"],member5_id=memId["5"],member6_id=memId["6"],member7_id=memId["7"],member8_id=memId["8"],member9_id=memId["9"],member10_id=memId["10"],member11_id=memId["11"])
									db.session.add(new_team)
									db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=BasketBall.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
							elif eventname=="Chess":
								if eventtype=="Single":
									amt_paid=200
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="chessS")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "chessS" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-chessS"
									member1=Members.query.filter_by(aadhar=aadhar_no).first()
									new_team=Chess(team_name=team_name,amt_paid=amt_paid,payment=False,team_type=eventtype,captain_id=captain.c_id,noc=True)
									db.session.add(new_team)
									#db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Chess.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
								elif eventtype=="TeamEvent":
									amt_paid=1000
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="chessT")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "chessT" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-chessT"
									memId={}
									aadhar_no_check={}
									for i in range(1,5):
										name=request.form["name"+str(i)]
										aadhar=request.form["aadhar_no"+str(i)]
										food_lodge=request.form["food_lodge"+str(i)]=="Yes"
										if food_lodge:
											amt_paid+=600
										if Members.query.filter_by(aadhar=aadhar).count()==0:
											new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="chessT")
											db.session.add(new_user)
											#db.session.commit()
										else:
											mem=Members.query.filter_by(aadhar=aadhar).first()
											if "chessT" in mem.events_participated.split("-"):
												return str(mem.name)+" Participated In This Event"
											mem.events_participated=mem.events_participated+"-chessT"
										aadhar_no_check[str(i)]=aadhar
									db.session.commit()
									for i in range(1,5):
										memId[str(i)]=Members.query.filter_by(aadhar=aadhar_no_check[str(i)]).first().m_id
									new_team=Chess(team_name=team_name,amt_paid=amt_paid,team_type=eventtype,payment=False,captain_id=captain.c_id,noc=True,member1_id=memId["1"],member2_id=memId["2"],member3_id=memId["3"],member4_id=memId["4"])
									db.session.add(new_team)
									db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Chess.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
							elif eventname=="Lawntennis":
								if eventtype=="Double" or eventtype=="MixedDouble":
									amt_paid=500
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									member1_name=request.form["name1"]
									aadhar_no1=request.form["aadhar_no1"]
									food_lodge1=request.form["food_lodge1"]=="Yes"
									if food_lodge1:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated=("lawntennis"+eventtype))
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if ("lawntennis"+eventtype) in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+("-lawntennis"+eventtype)
									if Members.query.filter_by(aadhar=aadhar_no1).count()==0:
										new_user=Members(name=member1_name,aadhar=aadhar_no1,captain_id=captain.c_id,food_lodge=food_lodge1,events_participated=("lawntennis"+eventtype))
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no1).first()
										if ("lawntennis"+eventtype) in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+("-lawntennis"+eventtype)
									member1=Members.query.filter_by(aadhar=aadhar_no1).first()
									new_team=Lawntennis(team_name=team_name,amt_paid=amt_paid,payment=False,team_type=eventtype,captain_id=captain.c_id,noc=True,member1_id=member1.m_id)
									db.session.add(new_team)
									#db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Lawntennis.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
								elif eventtype=="Single":
									amt_paid=250
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="lawntennisS")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "lawntennisS" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-lawntennisS"
									member1=Members.query.filter_by(aadhar=aadhar_no).first()
									new_team=Lawntennis(team_name=team_name,amt_paid=amt_paid,payment=False,team_type=eventtype,captain_id=captain.c_id,noc=True)
									db.session.add(new_team)
									#db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Lawntennis.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
								else:
									return render_template("errorpage.html",error="Some Error Occured")
							elif eventname=="Badminton":
								if eventtype=="TeamEvent":
									amt_paid=1200 if captain.gender=="M" else 1000
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="badmintonT")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "badmintonT" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-badmintonT"
									memId={}
									aadhar_no_check={}
									for i in range(1,3):
										name=request.form["name"+str(i)]
										aadhar=request.form["aadhar_no"+str(i)]
										food_lodge=request.form["food_lodge"+str(i)]=="Yes"
										if food_lodge:
											amt_paid+=600
										if Members.query.filter_by(aadhar=aadhar).count()==0:
											new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="badmintonT")
											db.session.add(new_user)
											#db.session.commit()
										else:
											mem=Members.query.filter_by(aadhar=aadhar).first()
											if "badmintonT" in mem.events_participated.split("-"):
												return str(mem.name)+" Participated In This Event"
											mem.events_participated=mem.events_participated+"-badmintonT"
										aadhar_no_check[str(i)]=aadhar
									db.session.commit()
									for i in range(1,3):
										memId[str(i)]=Members.query.filter_by(aadhar=aadhar_no_check[str(i)]).first().m_id
									for i in range(3,7):
										if len(request.form["aadhar_no"+str(i)])>0:
											name=request.form["name"+str(i)]
											aadhar=request.form["aadhar_no"+str(i)]
											food_lodge=request.form["food_lodge"+str(i)]=="Yes"
											if food_lodge:
												amt_paid+=600
											if Members.query.filter_by(aadhar=aadhar).count()==0:
												new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="badmintonT")
												db.session.add(new_user)
												db.session.commit()
											else:
												mem=Members.query.filter_by(aadhar=aadhar).first()
												if "badmintonT" in mem.events_participated.split("-"):
													return str(mem.name)+" Participated In This Event"
												mem.events_participated=mem.events_participated+"-badmintonT"
												db.session.commit()
											memId[str(i)]=Members.query.filter_by(aadhar=aadhar).first().m_id
										else:
											memId[str(i)]=None
									new_team=Badminton(team_name=team_name,amt_paid=amt_paid,team_type=eventtype,payment=False,captain_id=captain.c_id,noc=True,member1_id=memId["1"],member2_id=memId["2"],member3_id=memId["3"],member4_id=memId["4"],member5_id=memId["5"],member6_id=memId["6"])
									db.session.add(new_team)
									db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Badminton.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
								elif eventtype=="MixedDouble":
									amt_paid=600
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									member1_name=request.form["name1"]
									aadhar_no1=request.form["aadhar_no1"]
									food_lodge1=request.form["food_lodge1"]=="Yes"
									if food_lodge1:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="badminton")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "badminton" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-badminton"
									if Members.query.filter_by(aadhar=aadhar_no1).count()==0:
										new_user=Members(name=member1_name,aadhar=aadhar_no1,captain_id=captain.c_id,food_lodge=food_lodge1,events_participated="badminton")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no1).first()
										if "badminton" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-badminton"
									member1=Members.query.filter_by(aadhar=aadhar_no1).first()
									new_team=Badminton(team_name=team_name,amt_paid=amt_paid,payment=False,team_type=eventtype,captain_id=captain.c_id,noc=True,member1_id=member1.m_id)
									db.session.add(new_team)
									#db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Badminton.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
							elif eventname=="Tabletennis":
								if eventtype=="Double":
									amt_paid=500
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									member1_name=request.form["name1"]
									aadhar_no1=request.form["aadhar_no1"]
									food_lodge1=request.form["food_lodge1"]=="Yes"
									if food_lodge1:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated=("tabletennis"+eventtype))
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if ("tabletennis"+eventtype) in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+("-tabletennis"+eventtype)
									if Members.query.filter_by(aadhar=aadhar_no1).count()==0:
										new_user=Members(name=member1_name,aadhar=aadhar_no1,captain_id=captain.c_id,food_lodge=food_lodge1,events_participated=("tabletennis"+eventtype))
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no1).first()
										if ("tabletennis"+eventtype) in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+("-tabletennis"+eventtype)
									member1=Members.query.filter_by(aadhar=aadhar_no1).first()
									new_team=Tabletennis(team_name=team_name,amt_paid=amt_paid,payment=False,team_type=eventtype,captain_id=captain.c_id,noc=True,member1_id=member1.m_id)
									db.session.add(new_team)
									#db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Tabletennis.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
								elif eventtype=="Single":
									amt_paid=250
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="tabletennis")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "tabletennis" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-tabletennis"
									member1=Members.query.filter_by(aadhar=aadhar_no).first()
									new_team=Tabletennis(team_name=team_name,amt_paid=amt_paid,payment=False,team_type=eventtype,captain_id=captain.c_id,noc=True)
									db.session.add(new_team)
									#db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Tabletennis.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
								elif eventtype=="TeamEvent":
									amt_paid=1000
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="tabletennisT")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "tabletennisT" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-tabletennisT"
									memId={}
									aadhar_no_check={}
									for i in range(1,4):
										name=request.form["name"+str(i)]
										aadhar=request.form["aadhar_no"+str(i)]
										food_lodge=request.form["food_lodge"+str(i)]=="Yes"
										if food_lodge:
											amt_paid+=600
										if Members.query.filter_by(aadhar=aadhar).count()==0:
											new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="tabletennisT")
											db.session.add(new_user)
											#db.session.commit()
										else:
											mem=Members.query.filter_by(aadhar=aadhar).first()
											if "tabletennisT" in mem.events_participated.split("-"):
												return str(mem.name)+" Participated In This Event"
											mem.events_participated=mem.events_participated+"-tabletennisT"
										aadhar_no_check[str(i)]=aadhar
									db.session.commit()
									for i in range(1,4):
										memId[str(i)]=Members.query.filter_by(aadhar=aadhar_no_check[str(i)]).first().m_id
									new_team=Tabletennis(team_name=team_name,amt_paid=amt_paid,team_type=eventtype,payment=False,captain_id=captain.c_id,noc=True,member1_id=memId["1"],member2_id=memId["2"],member3_id=memId["3"])
									db.session.add(new_team)
									db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Tabletennis.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
								else:
									return render_template("errorpage.html",error="Some Error Occured")
							elif eventname=="Khokho":
								if eventtype=="TeamEvent":
									amt_paid=2000
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="khokho")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "khokho" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-khokho"
									memId={}
									aadhar_no_check={}
									for i in range(1,12):
										name=request.form["name"+str(i)]
										aadhar=request.form["aadhar_no"+str(i)]
										food_lodge=request.form["food_lodge"+str(i)]=="Yes"
										if food_lodge:
											amt_paid+=600
										if Members.query.filter_by(aadhar=aadhar).count()==0:
											new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="khokho")
											db.session.add(new_user)
											#db.session.commit()
										else:
											mem=Members.query.filter_by(aadhar=aadhar).first()
											if "khokho" in mem.events_participated.split("-"):
												return str(mem.name)+" Participated In This Event"
											mem.events_participated=mem.events_participated+"-khokho"
										aadhar_no_check[str(i)]=aadhar
									db.session.commit()
									for i in range(1,12):
										memId[str(i)]=Members.query.filter_by(aadhar=aadhar_no_check[str(i)]).first().m_id
									new_team=Khokho(team_name=team_name,amt_paid=amt_paid,payment=False,captain_id=captain.c_id,noc=True,member1_id=memId["1"],member2_id=memId["2"],member3_id=memId["3"],member4_id=memId["4"],member5_id=memId["5"],member6_id=memId["6"],member7_id=memId["7"],member8_id=memId["8"],member9_id=memId["9"],member10_id=memId["10"],member11_id=memId["11"])
									db.session.add(new_team)
									db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Khokho.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
							#changes
							elif eventname=="Fifa":
								if eventtype=="TeamEvent":
									amt_paid=100
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="fifa")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "fifa" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-fifa"
									member1=Members.query.filter_by(aadhar=aadhar_no).first()
									new_team=Fifa(team_name=team_name,amt_paid=amt_paid,payment=False,captain_id=captain.c_id,noc=True)
									db.session.add(new_team)
									#db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Fifa.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
							elif eventname=="Pubg":
								if eventtype=="TeamEvent":
									amt_paid=200
									team_name=request.form["team_name"]
									aadhar_no=request.form["aadhar_no"]
									food_lodge=request.form["food_lodge"]=="Yes"
									if food_lodge:
										amt_paid+=600
									if Members.query.filter_by(aadhar=aadhar_no).count()==0:
										new_user=Members(name=captain.name,aadhar=aadhar_no,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="pubg")
										db.session.add(new_user)
										#db.session.commit()
									else:
										mem=Members.query.filter_by(aadhar=aadhar_no).first()
										if "pubg" in mem.events_participated.split("-"):
											return str(mem.name)+" Participated In This Event"
										mem.events_participated=mem.events_participated+"-pubg"
									memId={}
									aadhar_no_check={}
									for i in range(1,4):
										name=request.form["name"+str(i)]
										aadhar=request.form["aadhar_no"+str(i)]
										food_lodge=request.form["food_lodge"+str(i)]=="Yes"
										if food_lodge:
											amt_paid+=600
										if Members.query.filter_by(aadhar=aadhar).count()==0:
											new_user=Members(name=name,aadhar=aadhar,captain_id=captain.c_id,food_lodge=food_lodge,events_participated="pubg")
											db.session.add(new_user)
											#db.session.commit()
										else:
											mem=Members.query.filter_by(aadhar=aadhar).first()
											if "pubg" in mem.events_participated.split("-"):
												return str(mem.name)+" Participated In This Event"
											mem.events_participated=mem.events_participated+"-pubg"
										aadhar_no_check[str(i)]=aadhar
									db.session.commit()
									for i in range(1,4):
										memId[str(i)]=Members.query.filter_by(aadhar=aadhar_no_check[str(i)]).first().m_id
									new_team=Pubg(team_name=team_name,amt_paid=amt_paid,payment=False,captain_id=captain.c_id,noc=True,member1_id=memId["1"],member2_id=memId["2"],member3_id=memId["3"])
									db.session.add(new_team)
									db.session.commit()
									new_part=Participation(captain_id=captain.c_id,event_id=Events.query.filter_by(name=path[3]).first().event_id,team_id=Pubg.query.filter_by(captain_id=captain.c_id).first().team_id)
									db.session.add(new_part)
									db.session.commit()
									return render_template("successpage.html",msg="REGISTERED")
							else:
								return render_template("errorpage.html",error="Some Error Occured")
					except Exception as e:
						return str(e)
		else:
			return redirect(url_for("Loginpage"))
	except Exception as e:
		return render_template("errorpage.html",error="Some Error Occured")


@app.route("/loginpage/<string:redir>")
def Loginpage(redir):
 	return render_template("login.html",redir=redir)


@app.route("/signuppage")
def Signuppage():
 	return render_template("signup.html")

@app.route("/signup",methods=["GET","POST"])
def Signup():
	try:
		if request.method=="POST":
			name=request.form["name"]
			father_name=request.form["father_name"]
			uname=request.form["uname"]
			passwd=sha256_crypt.encrypt(request.form["passwd"])
			institute=request.form["institute"]
			roll_no=request.form["roll_no"]
			year=request.form["year"]
			branch=request.form["branch"]
			aadhar_no=request.form["aadhar_no"]
			contact_no=str(request.form["contact_no"])
			gender=request.form["gender"]
			otp=randint(100000,999999)
			new_user=TempCompetitors(email=uname,passwd=passwd,name=name,father_name=father_name,roll_no=roll_no,college=institute,branch=branch,year=year,mob_no=contact_no,gender=gender,otp=otp)
			db.session.add(new_user)
			db.session.commit()
			msg=Message('FROM RANN-KIET',sender='rann@kiet.edu',recipients=[uname])
			msg.body="""Subject: Verification Otp
						Your OTP For Verification of Email At Rann2k19 Is
						"""+str(otp)
			mail.send(msg)
			return render_template("verifypage.html",email=uname)
		else:
			return render_template("errorpage.html",error="THAT WAS WRONG!!!")
	except:
		return render_template("errorpage.html",error="Some Error Occured")

@app.route("/verify-otp/<string:email>",methods=["GET","POST"])
def Verify_otp(email):
	try:
		if request.method=="POST":
			otp=request.form["otp"]
			ch_otp=TempCompetitors.query.filter_by(email=email).first()
			if otp==ch_otp.otp:
				new_user=Competitors(email=ch_otp.email,passwd=ch_otp.passwd,name=ch_otp.name,father_name=ch_otp.father_name,roll_no=ch_otp.roll_no,college=ch_otp.college,branch=ch_otp.branch,year=ch_otp.year,mob_no=ch_otp.mob_no,gender=ch_otp.gender)
				db.session.add(new_user)
				db.session.commit()
				db.session.delete(ch_otp)
				db.session.commit()
				return redirect("/loginpage/direct")
			else:
				return render_template("errorpage.html",error="WRONG OTP")
		else:
			return render_template("errorpage.html",error="That Was WRONG")
	except:
		return render_template("errorpage.html",error="Some Error Occured")

@app.route("/login/<string:redir>",methods=["GET","POST"])
def Login(redir):
	try:
		if request.method=="POST":
			uname=request.form["uname"]
			passwd=request.form["passwd"]
			if Competitors.query.filter_by(email=uname).count()>0:
				current_user=Competitors.query.filter_by(email=uname).first()
				if sha256_crypt.verify(passwd,current_user.passwd):
					session['logged_in'] = True
					session['username'] = current_user.email
					if redir=="direct":
						return redirect(url_for("User_Profile",path="home"))
					else:
						return redirect("/events/"+redir)
				else:
					return render_template("errorpage.html",error="WRONG Credntials")
			else:
				return render_template("errorpage.html",error="No Such User")
		else:
			return render_template("errorpage.html",error="That Was WRONG")
	except:
		return render_template("errorpage.html",error="Some Error Occured")
	

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			return redirect(url_for('Home'))
	return wrap

@app.route("/logout")
@login_required
def logout():
	try:
		client_email=session['username']
		session.pop('username',None)
		session["logged_in"]=False
		return redirect(url_for("Home"))
	except:
		flash("ALREADY LOGGED OUT")
		return redirect(url_for("Home"))


@app.route("/events/<string:eventname>")
def EventsList(eventname):
	redir="/loginpage/"+eventname
	try:
		if session["logged_in"]:
			redir="/user/register-typeselection-"+eventname
	except:
		pass
	if eventname=="Pool":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Pool.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Pool').first()
					participated_in=Pool.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/pool.jpg",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Pool').first()
					return render_template("events.html",event=eventdata,fname="images/pool.jpg",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Pool').first()
				return render_template("events.html",event=eventdata,fname="images/pool.jpg",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Pool').first()
			return render_template("events.html",event=eventdata,fname="images/pool.jpg",redir=redir,participated_in=[])
	elif eventname=="Carrom":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Carrom.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Carrom').first()
					participated_in=Carrom.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/CarromEp.png",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Carrom').first()
					return render_template("events.html",event=eventdata,fname="images/CarromEp.png",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Carrom').first()
				return render_template("events.html",event=eventdata,fname="images/CarromEp.png",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Carrom').first()
			return render_template("events.html",event=eventdata,fname="images/CarromEp.png",redir=redir,participated_in=[])
	elif eventname=="Football":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if FootBall.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Football').first()
					participated_in=FootBall.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/football.jpg",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Football').first()
					return render_template("events.html",event=eventdata,fname="images/football.jpg",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Football').first()
				return render_template("events.html",event=eventdata,fname="images/football.jpg",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Football').first()
			return render_template("events.html",event=eventdata,fname="images/football.jpg",redir=redir,participated_in=[])
	elif eventname=="Volleyball":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Vollyball.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Volleyball').first()
					participated_in=Vollyball.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/volleyball.png",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Volleyball').first()
					return render_template("events.html",event=eventdata,fname="images/volleyball.png",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Volleyball').first()
				return render_template("events.html",event=eventdata,fname="images/volleyball.png",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Volleyball').first()
			return render_template("events.html",event=eventdata,fname="images/volleyball.png",redir=redir,participated_in=[])
	elif eventname=="Cricket":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Cricket.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Cricket').first()
					participated_in=Cricket.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/cricket.jpg",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Cricket').first()
					return render_template("events.html",event=eventdata,fname="images/cricket.jpg",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Cricket').first()
				return render_template("events.html",event=eventdata,fname="images/cricket.jpg",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Cricket').first()
			return render_template("events.html",event=eventdata,fname="images/cricket.jpg",redir=redir,participated_in=[])
	elif eventname=="Basketball":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Basketball.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Basketball').first()
					participated_in=Basketball.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/basketball.jpg",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Basketball').first()
					return render_template("events.html",event=eventdata,fname="images/basketball.jpg",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Basketball').first()
				return render_template("events.html",event=eventdata,fname="images/basketball.jpg",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Basketball').first()
			return render_template("events.html",event=eventdata,fname="images/basketball.jpg",redir=redir,participated_in=[])
	elif eventname=="Chess":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Chess.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Chess').first()
					participated_in=Chess.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/chess.jpg",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Chess').first()
					return render_template("events.html",event=eventdata,fname="images/chess.jpg",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Chess').first()
				return render_template("events.html",event=eventdata,fname="images/chess.jpg",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Chess').first()
			return render_template("events.html",event=eventdata,fname="images/chess.jpg",redir=redir,participated_in=[])
	elif eventname=="Lawntennis":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Lawntennis.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Lawntennis').first()
					participated_in=Lawntennis.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/lawntennis.jpg",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Lawntennis').first()
					return render_template("events.html",event=eventdata,fname="images/lawntennis.jpg",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Lawntennis').first()
				return render_template("events.html",event=eventdata,fname="images/lawntennis.jpg",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Lawntennis').first()
			return render_template("events.html",event=eventdata,fname="images/lawntennis.jpg",redir=redir,participated_in=[])
	elif eventname=="Badminton":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Badminton.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Badminton').first()
					participated_in=Badminton.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/badminton.jpg",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Badminton').first()
					return render_template("events.html",event=eventdata,fname="images/badminton.jpg",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Badminton').first()
				return render_template("events.html",event=eventdata,fname="images/badminton.jpg",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Badminton').first()
			return render_template("events.html",event=eventdata,fname="images/badminton.jpg",redir=redir,participated_in=[])
	elif eventname=="Tabletennis":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Tabletennis.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Tabletennis').first()
					participated_in=Tabletennis.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/tabletennis.jpg",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Tabletennis').first()
					return render_template("events.html",event=eventdata,fname="images/tabletennis.jpg",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Tabletennis').first()
				return render_template("events.html",event=eventdata,fname="images/tabletennis.jpg",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Tabletennis').first()
			return render_template("events.html",event=eventdata,fname="images/tabletennis.jpg",redir=redir,participated_in=[])
	elif eventname=="Khokho":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Khokho.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Khokho').first()
					participated_in=Khokho.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/Khokho.jpg",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Khokho').first()
					return render_template("events.html",event=eventdata,fname="images/Khokho.jpg",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Khokho').first()
				return render_template("events.html",event=eventdata,fname="images/Khokho.jpg",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Khokho').first()
			return render_template("events.html",event=eventdata,fname="images/Khokho.jpg",redir=redir,participated_in=[])
	#changes
	elif eventname=="Pubg":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Pubg.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Pubg').first()
					participated_in=Pubg.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/pubg.jpg",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Pubg').first()
					return render_template("events.html",event=eventdata,fname="images/pubg.jpg",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Pubg').first()
				return render_template("events.html",event=eventdata,fname="images/pubg.jpg",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Pubg').first()
			return render_template("events.html",event=eventdata,fname="images/pubg.jpg",redir=redir,participated_in=[])
	elif eventname=="Fifa":
		try:
			if session["logged_in"]:
				client_data=Competitors.query.filter_by(email=session["username"]).first()
				if Fifa.query.filter_by(captain_id=client_data.c_id).count()>0:
					eventdata=Events.query.filter_by(name='Fifa').first()
					participated_in=Fifa.query.filter_by(captain_id=client_data.c_id).all()
					return render_template("events.html",event=eventdata,fname="images/fifa.jpg",redir=redir,participated_in=participated_in)
				else:
					eventdata=Events.query.filter_by(name='Fifa').first()
					return render_template("events.html",event=eventdata,fname="images/fifa.jpg",redir=redir,participated_in=[])
			else:
				eventdata=Events.query.filter_by(name='Fifa').first()
				return render_template("events.html",event=eventdata,fname="images/fifa.jpg",redir=redir,participated_in=[])
		except:
			eventdata=Events.query.filter_by(name='Fifa').first()
			return render_template("events.html",event=eventdata,fname="images/fifa.jpg",redir=redir,participated_in=[])
	else:
		return render_template("errorpage.html",error="No such Event Is Happening")


app.secret_key="Lalalalllalallla@lllallalalla2139644&&&&&"


eventdetailsEn={
	"Basketball":{"max":12,"min":8,"stu_co":"SUMIT BALIYAN","stu_co_contact":"9756403063-","teach_co":"SMARIKA SINGH","amount":"Team:Rs.2500","types":"TeamEvent",
		"rules":"Number of players maximum 12 minimum 8	-All the playing rules will be according to FIBA.-The refree’s decision will be final.-The teams are required to report 30 min before given time.-College/Institute ID card is mandatory with one Government Id proof."
		},
	"Carrom":{"max":5,"min":5,"stu_co":"AMAN TRIPATHI","stu_co_contact":"8765815182-","teach_co":"-","amount":"Team:Rs.1000","types":"TeamEvent",
		"rules":"Team Carrom- 5 players (4 Boys, 1 Girls)-All rules of the Indian federation of Carrom will be followed.-The player who complete pocketing all his C/M first wins the board-The value points are as follows:Queen: 3 points C/M: 1 points each-The C/M of the opponent on the C/B shall be the points gained by that player in the board-The player is entitled to be credited with the value of the Queen, only if he wins the board-    c) The player who looses the board is not credited with the value of queen,If he has pocketed and covered the queen-The maximum number of points that can be scored in a board is 12 only. Any due and penalty C/M shall automatically we written off-A game is of 25 points or 8 boards. The player who reaches 25 points first or leads at the conclusion of 8 board shall be the winner of the game.-In case the score is equal at the end of the 8 board, an extra board shall be played to decide the winner .Before the extra board their shall be a toss to choose break only.-Decision of referee will be final"
	},
	"Football":{
		"max":15,"min":11,"stu_co":"MOHIT KANDPAL","stu_co_contact":"7895123378-","teach_co":"UNNATI KALA","amount":"Boys:Rs.3500-Girls:Rs.1500","types":"TeamEvent",
		"rules":"Every team can have maximum of 15 players (11+4) and minimum of 11 players for boys and maximum of 9 players (6+3) and minimum of 6 players for girls.-The Referee’s decision is final and no argument should be done. Else the player or team will be penalized as the referee will think right to do.-Any misconduct on the field can lead to disqualification of the team.-Other rules regarding the match will be told on the field.-The above rules are applicable on both girls and boys football team.-All players are to honor the game rules and play in healthy competition."
	},
	"Cricket":{"min":11,"max":15,"stu_co":"YAMRAJ PANWAR","stu_co_contact":"8218897992-8604357522","teach_co":"PAWANDEEP YADAV","amount":"Team:Rs.3500","types":"TeamEvent",
		"rules":"Every team can have maximum of 15 players  (playing 11 + 4 extra).-The Team Captain is responsible for informing all of the teammates about when the team will be playing and on what dates. Our responsibility is to tell the Captain when his team will be playing.-Every team should be well dressed and shoes are compulsory in tournament.-During the power play, a maximum of 2  fielders should be outside the fielding circle.-Teams should report 30 minutes before the start of the play.-After the toss, the fielding team should set the fielding positions immediately to avoid any delay to begin the match. Batsmen will come to the crease only after the field arrangement.-Organizing committee will reserve full authority to intervene in such case off field and umpires will have full authority to intervene on field.Each captain should nominate his playing XI before the toss.- No player can be changed after the nomination without the consent of the opposing captain.-A new ball will be provided for each innings. In case of loss or damaged ball, umpire will replace the old ball with a new one/replacement ball and dead ball will give in case of out only. (Run out will not consider)-Umpires decisions will be final throughout the tournament. Any sort of misconducts by any players will result in direct suspension.-Organizers reserve the right to change the venue, date time and reduce the overs of matches at short notice.-A team must be ready to play two matches in a day, if required.-Substitute runners are not allowed, unless a batsman gets injured in the field during a particular match and the role of a substitute will be fielding only.-No Duckworth–Lewis method is applied for weather affected matches. Umpires will take the final decision to stop the match.-If any player have any query regarding boundary or about any rule he can directly contact to umpires or organizers before the match."
	},
	"Volleyball":{"min":8,"max":12,"stu_co":"SANIL SINGH","stu_co_contact":"9458518986-","teach_co":"NIDHI GUPTA","amount":"Team:Rs.2500","types":"TeamEvent",
		"rules":"The matches will be of 3 sets (25 each).-Final match will be of 5 sets (4 sets of 25 points and last set of 15 points).-Only Fixed position play (No Rotation).-Decision of the Referee will be final.-Any argument or misbehaviour with Referee as well as player may lead to disqualification of respective team.-For everything else standard volleyball rules apply.-All teams are required to report atleast 30 min before the given time."
	},
	"Pool":{"min":1,"max":2,"stu_co":"SUDHANSHU JANDIAL","stu_co_contact":"9419290029-8960651955","teach_co":"AKSHAY AGARWAL","amount":"Single:Rs.200-Double:Rs.400-Mixed:Rs.400","types":"Single-Double-MixedDouble",
		"rules":"Break shot will be decided by the toss.-During break if black ball gets pot than it is considered to be the golden break.-For a break to be a legal one is required that minimum 4 balls should touch the side cushion .-For a legal shot any ball after contact with some other ball must touch any of the side cushion .-Jump shots are foul.-Any king of foul by an opponent will result in ball in hand opportunity for the other opponent.-Decision of the match Referee will be final.-Any argument or misbehaviour with Referee as well as players may lead to disqualification of the respective team or an individual person.-All players are required to maintain the dignity and respect of the game as well as of other players."
	},
	"Badminton":{"min":2,"max":7,"stu_co":"HIMANSHU PANDEY","stu_co_contact":"7289868669-","teach_co":"SHRADDHA SINGH","amount":"Boys:Rs.1200-Girls:Rs.1000-Mixed:Rs.500","types":"MixedDouble-TeamEvent",
		"rules":"Men: The no. of players representing any college in a team can be maximum of 4 to 7 members.-Women: : The no. of players representing any college in a team can be maximum of 2 to 4 members.-Mixed Doubles Event will also be conducted.-The order of events shall be as follows: Men: Singles / Singles /Doubles /Singles /Doubles.Women: Singles/ Doubles/ Singles.-Each set will be of 21 points and there will be 5 sets for men and 3 sets for women.-Players must wear neat and clean non marking gum sole shoes.-Tie will be resolve by successively applying the following criteria:Individual matches won / lost .Games won/ lost by the team.Points for/ points against.-The tally for all the matches played in the lead fixture will be considered.-Any new rule or change in rules will be informed to the teams by the event coordinators prior to the beginning of match. In any case, the decision of referee and the officials shall be considered final.-In case of discrepancy, the decision of referees shall be considered final.-Late reporting may lead to disqualification."
	},
	"Tabletennis":{"min":1,"max":4,"stu_co":"PREKSHA AGRAWAL","stu_co_contact":"8430077184-","teach_co":"MANAN MITTAL","amount":"Singles:Rs.250-Double:Rs.500-Team:Rs.1000","types":"Single-Double-TeamEvent",
		"rules":"There will the three events in the tournament in both boys and girls – Singles and Doubles.-There will also be a Team Event.-For the events, this is an individual player registration sport.-Each match will have three sets of 11 points each.-Best of the three sets will decide the winner.-If the player fails to report the venue 15 minutes before the game, the opponent shall be given a win.-In any case, referee’s decision will be final."
	},
	"Lawntennis":{"min":1,"max":2,"stu_co":"HIMANSHU MISHRA","stu_co_contact":"7800680977-8006504488","teach_co":"PRAKAMYA SINGH","amount":"Single:Rs.250-Double:Rs.500--Mixed:Rs.500","types":"Single-Double-MixedDouble",
		"rules":"Men: This will be an individual event.-Women : This will  be an individual event.-Mixed Doubles - The no. of players representing any college in a team can be maximum of 2 members.-All matches will be of one set each-Tie will be enforced at 6 all-All ATP rules will be followed-Foul calls will be subject to linesman call-Any new rule or change in rules will be informed to the teams by the event coordinators prior to the beginning of match. In any case, the decision of referee and the officials shall be considered final.-In case of discrepancy, the decision of referees shall be considered final.-Late reporting may lead to disqualification."
	},
	"Khokho":{"min":12,"max":12,"stu_co":"SWEETY GUPTA","stu_co_contact":"9455604450-","teach_co":"KUMAR DIVYANSH","amount":"Team:Rs.2000","types":"TeamEvent",
		"rules":"Two equal teams, and then allocate one team as the chasers and one team as the defenders (let them know they’ll get to swap roles after seven minutes).-12 players per side, 9 in the field and 3 extra.-Chasers need to line up on the line down the middle, facing in alternate directions. They can only ‘chase’ on the side of the pitch they are facing and can only chase one at a time.-The defenders enter the field in groups of three and need to avoid being tagged by a chaser - They can run anywhere on the field, but they’re out if they get tagged.-The chaser at the pole starts and must try to tag one of the defenders on their side of the pitch, if a defender crosses the line to the other side, the chaser must tap the back of one of his teammates, who is sitting facing the other direction, and shout “Kho!”-The teammate must then try to tag the defender and the standing chaser sits in the team mates place so only one chaser is chasing.-Chasers can swap with a teammate every time the defender moves into the opposite side of the pitch or the chaser can run round one of the poles to get to the other side of the pitch.-The aim for chasers is to tag out the defenders the fastest.-Whichever team gets the defenders out the quickest wins."
	},
	"Chess":{"min":1,"max":5,"stu_co":"ALOK AGRAWAL","stu_co_contact":"8474958177-","teach_co":"DEEKSHA CHAUDHARY","amount":"Team:Rs.1000-Single:Rs.200","types":"Single-TeamEvent",
		"rules":"Team event :-1. The team comprises of 4 playing members and 1 extra (4+1).-2. No. of rounds will depend upon no. of participating teams.-3. A player gets 1 point on win, 0.5 on draw and 0 on losing a game.-4. All FIDE rules will be followed.-5. The time limit will be 30 minutes on each side.-6. Mixed team of boys and girls are allowed.-Individual event : -1. No. of rounds will depend upon no. of participating players.-2. The time limit will be 30 minutes on both sides. -3. A player gets 1 point on win, 0.5 on draw and 0 on losing a game.-4. All FIDE rules will be followed."
	},
	"Pubg":{"min":4,"max":4,"stu_co":"Avinash Pratap","stu_co_contact":"9621353531-7417900927","teach_co":"Piyush Pathak","amount":"Team:Rs.200","types":"TeamEvent",
		"rules":"THE SQUAD CAN HAVE ALL EMULATOR PLAYERS.-Make sure to grab the match Id and password before the match start time.-Make sure you join the room ASAP before the match starts otherwise, we won't be responsible for it and no refund in such case.-Match will start after 15 minutes of sharing room ID and password.-Don&#39;t share match ID and password with anyone else who has not registered for match, if found so you will be disqualified.-Griefing and teaming is against game rules.-Last standing man&#39;s squad gets the Chicken Dinner award.-Players need to bring their own gaming devices.-Less than four members are allowed in a squad.-The entry fees is for squad only.-While registration PubG username and playing media (i.e. mobile or emulator) of every member of squad must be mentioned.-Do not use any hacks.-If anyone found violating these rules then immediate action will be taken and whole squad will be disqualified and rewards may be abandoned."
	},
	"Fifa":{"min":1,"max":1,"stu_co":"Pratyush Chibber","stu_co_contact":"9456380784-9918049908","teach_co":"Sadiq Ansari","amount":"Single:Rs.100","types":"Single",
		"rules":"Game Tactics: Custom tactics allowed-Formations: Allowed-Injuries: Off-Referee: Random-Half Length: 5 minutes-Handball: Off-Weather: Clear-Season: Summer-FIFA Trainer: Off-Keeper Difficulty:legendary-Final decision would be our.-All matches would be knockout."
	}

}


@app.route("/committee")
def committee():
	return render_template("com.html")

@app.route("/manishpandey/enter-details-of-events/Rehne/Do/Tum")
def EnterDetailsOfEvents():
	for k in eventdetailsEn.keys():
		newevent=Events(name=k,types=eventdetailsEn[k]["types"],min_participants=eventdetailsEn[k]["min"],max_participants=eventdetailsEn[k]["max"],rules=eventdetailsEn[k]["rules"],stu_co=eventdetailsEn[k]["stu_co"],stu_co_contact=eventdetailsEn[k]["stu_co_contact"],teach_co=eventdetailsEn[k]["teach_co"],amount=eventdetailsEn[k]["amount"])
		db.session.add(newevent)
		db.session.commit()
	return "Done"


#new Changes

@app.route("/manishpandey/jaadu/<string:command>")
def manishadmin(command):
	try:
		if session["logged_in"]:
			if session["username"]=="manishpandey8858@gmail.com":
				cmnd=command.split("-")
				x=db.engine.execute(str(cmnd[1]))
				if cmnd[0]=="get":
					x=x.fetchall()
					return str(x)
				elif cmnd[0]=="set":
					db.session.commit()
					return "DONE"
			else:
				return "Not Authorised"
		else:
			return "Sorry Not Available"
	except:
		return "Sorry"

@app.route("/login/rann2k19/admin/get-details",methods=["GET","POST"])
def AdminLogin():
	try:
		if session["logged_in"]:
			if session["username"]=="manishpandey8858@gmail.com":
				event_list=["Football","Basketball","Vollyball","Cricket","Khokho","Lawntennis","Tabletennis","Chess","Badminton","Carrom","Pool","Pubg","Fifa"]
				return render_template("selecteventadmin.html",authority=event_list)
			else:
				return "Not Authorised"
		else:
			return "Sorry Not Available"
	except:
		return "Sorry"


@app.route("/rann2k19/k/admin",methods=["GET","POST"])
def Admin_Profile():
	#try:
	if session["logged_in"]:
		if session["username"]=="manishpandey8858@gmail.com":
			eventname=request.form["selected_event"]
			team_data={}
			if eventname=="Football":
				event_data=FootBall.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=15,eventname=eventname)
			elif eventname=="Vollyball":
				event_data=VollyBall.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=12,eventname=eventname)
			elif eventname=="Cricket":
				event_data=Cricket.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=15,eventname=eventname)
			elif eventname=="Khokho":
				event_data=Khokho.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=12,eventname=eventname)
			elif eventname=="Lawntennis":
				event_data=Lawntennis.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=2,eventname=eventname)
			elif eventname=="Tabletennis":
				event_data=Tabletennis.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=4,eventname=eventname)
			elif eventname=="Chess":
				event_data=Chess.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=5,eventname=eventname)
			elif eventname=="Badminton":
				event_data=Badminton.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=7,eventname=eventname)
			elif eventname=="Carrom":
				event_data=Carrom.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=5,eventname=eventname)
			elif eventname=="Pool":
				event_data=Pool.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=2,eventname=eventname)
			elif eventname=="Pubg":
				event_data=Pubg.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=4,eventname=eventname)
			elif eventname=="Fifa":
				event_data=Fifa.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=1,eventname=eventname)
			elif eventname=="Basketball":
				event_data=BasketBall.query.all()
				for x in event_data:
					team_data[x.captain_id]={}
					team_data[x.captain_id]["cap_details"]=Competitors.query.filter_by(c_id=x.captain_id).first()
				return render_template("printeventdetails.html",event_data=event_data,team_data=team_data,type=True,members=12,eventname=eventname)
			else:
				return render_template("errorpage.html",error="Not Available!!!")
		else:
			return "Hi"
	# except:
	# 	return render_template("errorpage.html",error="Some Error Occured")
@app.route("/Get-MemDetails",methods=["GET","POST"])
def Get_MemDetails():
	mem_id = int(request.form.get('member_id'))
	data=Members.query.filter_by(m_id=mem_id).first()
	if data.aadhar!="":
		return jsonify([data.name,data.aadhar,data.food_lodge])
	else:
		return jsonify(["","",""])


@app.route("/gallery")
def gallery():
	return render_template("gallery.html")

#end new changes

#next changes

@app.route("/verify-payment",methods=["GET","POST"])
def verify_payment():
	try:
		webdict=dict()
		webkeys=request.form.keys()
		for key in webkeys:
			value=request.form.get(key)
			webdict[key]=value
		new_pay=Pendingpayment(cust_id=webdict["CUST_ID"],order_id=webdict["ORDERID"],amount=webdict["TXNAMOUNT"],status=webdict["STATUS"])
		db.session.add(new_pay)
		db.session.commit()	
		cust_id=webdict["CUST_ID"]
		event_id_c=int(cust_id[:6])
		team_id_c=int(cust_id[6:])
		if webdict["STATUS"]=="TXN_SUCCESS" and webdict["IS_CHECKSUM_VALID"]=="Y" and webdict["RESPCODE"]=="01":
			if event_id_c==838280:
				team=Pool.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==789588:
				team=Cricket.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==678123:
				team=FootBall.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==771410:
				team=Khokho.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==771417:
				team=VolleyBall.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==789153:
				team=Chess.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==523984:
				team=Pubg.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==156987:
				team=BasketBall.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==624813:
				team=Tabletennis.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==852013:
				team=Lawntennis.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==205555:
				team=Badminton.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==852741:
				team=Fifa.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			elif event_id_c==173946:
				team=Carrom.query.filter_by(team_id=team_id_c).first()
				if team.amt_paid == int(float(webdict["TXNAMOUNT"])):
					team.transaction_id=webdict["ORDERID"]
					team.payment=True
					db.session.commit()
					return render_template("successpage.html",msg=webdict["RESPMSG"])
				else:
					return render_template("errorpage.html",error="Amount Paid Is Invalid")
			else:
				return render_template("errorpage.html",error=event_id_c)
		else:
			 return render_template("errorpage.html",error=webdict["RESPMSG"])
		return render_template("errorpage.html",error="Some Error Was There Please Contact Rann Technical Team")			
	except Exception as e:
		return render_template("errorpage.html",error=str(e)+"Report This Error To Team Rann")

#end next changes

if __name__=="__main__":
    app.run(debug="true",host="0.0.0.0")
