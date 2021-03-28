from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from flask_sqlalchemy import SQLAlchemy
#import secrets
from datetime import date,datetime,timedelta
#import request
import json
import io
import base64
import numpy as np
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import time
import ast
app = Flask(__name__)
'''app.css.append_css({
    "external_url": "https://ShashankR.pythonanywhere.com/mysite/static/style.css"
})'''


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="securitest",
    password="passwordsup123",
    hostname="securitest.mysql.pythonanywhere-services.com",
    databasename="securitest$default",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5rcb'

db = SQLAlchemy(app)

class Names(db.Model):

    __tablename__ = "names"

    #id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096), primary_key=True)
    score = db.Column(db.Integer)
    date = db.Column(db.String(4096), primary_key=True)





class Admins(db.Model):

    __tablename__ = "admins"

    #id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096), primary_key=True)
    password = db.Column(db.String(4096), not_null=True, default='CSE')

class Questions(db.Model):

    __tablename__ = "questions"

    link = db.Column(db.String(4096), primary_key=True)
    ans = db.Column(db.String(4096))


class IP(db.Model):

    __tablename__ = "ipadd"

    ip = db.Column(db.String(4096), primary_key=True)
    date = db.Column(db.String(4096), primary_key=True)
    name = db.Column(db.String(4096))




glastupdated=''

auth=False
@app.route('/', methods=['GET','POST'])
def home():
		if request.method == 'POST':
			print(str(request.form))
			if 'Admin' in request.form:
				return redirect(url_for('admin'))
			elif 'Answers' in request.form:
				return redirect(url_for('question'))


			elif 'bruv' in request.form:
				print('bruhhh')
				details = request.form
				b = details['bruv']

				print(b)
			return render_template('index.html')

		else:
		    global auth
		    auth=False
		    return render_template('index.html')









'''
		print('lalalal')
		details = request.form
		namez = details['name']
		namez=Names(name=namez,)
		db.session.add(namez)
		db.session.commit()
'''

@app.route('/adminack', methods=['GET','POST'])
def adminack():
	if request.method == 'POST':
	    details = request.form
	    un = details['name']
	    up = details['pass']
	    admindata = Admins.query.filter(Admins.name == un).first()
	    if admindata != None:
	        if admindata.password == up:
	            global auth
	            auth = True

	            return redirect(url_for('admin'))
	        else:
	            return render_template('AdminAck.html',text = 'Wrong Username/Password')

	    else:
	        return render_template('AdminAck.html',text = 'Wrong Username/Password')
	else:
	    return render_template('AdminAck.html',text = '')












@app.route('/admin', methods=['GET','POST'])
def admin():
    global auth
    if auth == False:
        return redirect(url_for('adminack'))
    else:

        return render_template('About.html')







@app.route('/about', methods=['GET','POST'])
def about():
    lastupdated=''

    if request.method == 'POST':

        if 'Answers' in request.form:
        	return redirect(url_for('question'))
        elif 'Home' in request.form:
        	return redirect(url_for('home'))


        #elif 'files' in request.form:
        print('fileeeeeee')
        db.session.query(Questions).delete()
        db.session.commit()
        f = request.files['file']
        f.save('questions.txt')
        f = open('questions.txt')
        for line in f:
            if '#!' in line:
                l = line[2:].split()
                a = l[0]
                q = l[1]

                qz=Questions(link=q, ans=a)
                db.session.add(qz)
                db.session.commit()












        lastupdated = str(date.today())
        return redirect(url_for('admin'))
    glastupdated = lastupdated





'''
		print('lalalal')
		details = request.form
		namez = details['name']
		namez=Names(name=namez,)
		db.session.add(namez)
		db.session.commit()


'''



@app.route('/submitques', methods=['GET','POST'])
def submitques():
    if request.method == 'POST':
        link = request.form['link']
        ans = request.form['ans']
        ques=Questions(link=link, ans=ans)
        db.session.add(ques)
        db.session.commit()
        return render_template('QuesSub.html')
    else:
        return render_template('QuesSub.html')








qlist=[]


@app.route('/question', methods=['GET','POST'])
def question():

	ans = dict()
	global auth
	auth=False
	score=0
	incorrect=dict()
	ind1=0
	ind2=0
	ind3=0
	ansdesc = dict()
	flag=False
	dt = ''

	if request.method == 'POST':






		print('req ',request.form)
		if len(request.form) == 0:
		    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
		    print('empty ',ip)
		    curdate = str(date.today())
		    ipdeets = IP.query.filter_by(ip=ip).filter_by(date=curdate).first()
		    print('ipppppppp', ipdeets)
		    if ipdeets == None:
		        print('ippppp none')
		        ipz = IP(ip=str(ip),date = curdate,name = '')
		        db.session.add(ipz)
		        db.session.commit()









		details = request.form
		print('post')
		qlist=[]
		count=1
		ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
		qf = open('allottedQ.txt')
		queslist=[]
		for qline in qf:
		    if qline[:qline.index('~')] == ip:
		        ql = qline[qline.index('~')+2:]
		        queslist = ast.literal_eval(ql)
		        break

		if len(queslist) == 0:
		    return 'Error. Please try again.'
		for Q in queslist:
			givenans = details.get(str(Q),False)
			q = Questions.query.filter_by(link = Q).first()

			#print('GIVEN: ',str(givenans)+' CORRECT: ',q.ans)
			if givenans == q.ans:
				score += 1
				incorrect[q.link] = ['Correct',givenans,count]
			else:
				incorrect[q.link] = ['Incorrect',givenans,count]
			count+=1

		usn = details.get('usn',False)
		deets = Names.query.filter_by(name = usn).first()
		if deets != None:
		    details = Names.query.filter_by(name = usn).all()
		    olddate = [a.date for a in details]

		    curdate = str(date.today())


		    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

		    try:
		        ipz = IP(ip=str(ip),date = curdate,name = str(usn) )
		        db.session.add(ipz)
		        db.session.commit()
		        print('348 ', ip)
		    except:
		        qlist=[]
		        text = "You have already submitted your answers today!"
		        return render_template('Questions.html', ques=qlist if len(qlist )>0 else 'None',score='', inc = '' , ans = qlist,anschoice='',text = text,allc='',last='',cnt=len(qlist),ip='')







		    if curdate not in olddate:

		        namez=Names(name=usn, score=score ,date = curdate)

		        db.session.add(namez)
		        db.session.commit()
		    else:
		        text = "You have already submitted your answers today!"
		        qlist=[]
		        return render_template('Questions.html', ques=qlist if len(qlist )>0 else 'None',score='', inc = '' , ans = qlist,anschoice='',text = text,allc='',last='',cnt=len(qlist),ip='')
		else:

		    curdate = str(date.today())
		    print(curdate,' ttt ',usn)


		    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

		    ipdeets = IP.query.filter_by(ip=ip).filter_by(date=curdate).first()
		    if ipdeets!=None:
		        text = "You have already submitted your answers today!"
		        qlist=[]
		        return render_template('Questions.html', ques=qlist if len(qlist )>0 else 'None',score='', inc = '' , ans = qlist,anschoice='',text = text,allc='',last='',cnt=len(qlist),ip='')
		    else:
		        ipz = IP(ip=str(ip),date = curdate,name = str(usn) )
		        db.session.add(ipz)
		        db.session.commit()
		        print('375 ', ip)







		    namez=Names(name=usn, score=score,date = curdate)
		    db.session.commit()
		    db.session.add(namez)
		    db.session.commit()
		qlist=[]
		return render_template('Questions.html', ques='',score=score, inc = incorrect if len(incorrect)>0 else '', ans = qlist,anschoice='',text = '', last = '',allc='',cnt='',ip='')


	f = open('questions.txt')
	contents = f.read().split()
	cc = contents[-1]
	f.close()
	index=0
	f = open('questions.txt')
	if len(contents)>0:
	    contents = contents[0]
	else:
	    contents=''
	for line in f:

		if '@' in line:
			l = line[1:].split()
			ind1 += int(l[0])

			#print(ind1,' ',ind2,' ',ind3)














	qtypes={'T':ind1}


	if 2<1:
	    qlist=[]
	    return render_template('Questions.html',ques=qlist if len(qlist)>0 else 'None' , score='', inc='',ans=qlist,text='',anschoice='', last = contents,allc='',cnt=len(qlist),ip='')
	else:
	    qlist=[]
	    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
	    qf1 = open('allottedQ.txt')
	    prevdata = False
	    for ln in qf1:
	        if ln[:ln.index('~')] == ip:
	            prevdata=True
	            ql = ln[ln.index('~')+2:]
	            qlist = ast.literal_eval(ql)

	            break




	    qf1.close()
	    if prevdata==False:
	        for qt in qtypes.keys():
	            questions = Questions.query.all()
	            if len(questions) <= qtypes[qt]:
	                qlist.extend([qu.link for qu in questions])
	            else:
	                qlist.extend(random.sample([qu.link for qu in questions],int(qtypes[qt])))






	        qf = open('allottedQ.txt','a+')
	        write_in_file = str(ip) + '~ ' + str(qlist) + '\n'
	        qf.write(write_in_file)






	    return render_template('Questions.html',ques=qlist if len(qlist)>0 else 'None' , score='', inc='',ans=qlist,text='',anschoice='', last = contents,allc='',cnt=len(qlist),ip='')























		#print('lalalal')



















@app.route('/question_start', methods=['GET','POST'])
def questionStart():
	if request.method=='POST':
		return redirect(url_for('question'))
	f = open('questions.txt')
	contents = f.read()
	f.close()
	global auth
	auth=False
	ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
	if (len(contents))>0:
	    contents = contents.split()[-1]
	    contents = contents.replace('_',' ')
	    c = datetime.strptime(str(contents), '%b %d %Y %I:%M %p') + timedelta(hours=5,minutes=30)
	    print('c ',contents)
	    print( datetime.strptime(datetime.now().strftime('%b %d %Y %I:%M %p'),'%b %d %Y %I:%M %p'))
	    if (datetime.strptime(str(contents), '%b %d %Y %I:%M %p') - datetime.strptime(datetime.now().strftime('%b %d %Y %I:%M %p'),'%b %d %Y %I:%M %p')).days < 0:
	        print('over')
	        ff = open('questions.txt','w')
	        ff.close()
	        return redirect(url_for('questionStart'))
	    return render_template('Questions.html', ques=(str(c)),score='', inc = '' , ans = '',anschoice='',text = '', allc='Y',last='',cnt='',ip=ip)
	else:

	    return render_template('Questions.html', ques='None',score='', inc = '' , ans = '',anschoice='',text = '', allc='Y',last='',cnt='',ip=ip)















@app.route('/stats', methods=['GET','POST'])
def stats():
    global auth
    auth=False
    if request.method == 'POST':
        score=[]
        dates=[]
        cnt=0
        un = request.form['usn']
        nm = Names.query.filter_by(name=un).all()
        if len(nm) == 0:
            return render_template('Stats.html',stats='',cnt = '', un = '', im = 'Invalid User.' )
        print('ok1')
        fig = Figure()
        print('ok2')
        axis = fig.add_subplot(1, 1, 1)
        print('ok3')
        axis.set_title("Your Performance")
        axis.set_xlabel("Date")
        axis.set_ylabel("Score")
        print('ok4')
        print(nm,' ')
        for i in range(len(nm)):
            score.append(nm[i].score)
            dates.append(nm[i].date)
        if len(nm)==1:
            score.append(0);
            dates.append('');

        axis.bar(dates, score, color="maroon",width=0.2)
        axis.set_ylim([0,30])




        # Convert plot to PNG image
        pngImage = io.BytesIO()
        print('ok6')
        FigureCanvas(fig).print_png(pngImage)
        print('ok7')

        # Encode PNG image to base64 string
        pngImageB64String = "data:image/png;base64,"
        print('ok8')
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
        print('ok9')

        return render_template('Stats.html',stats=nm,cnt = len(nm), un = un, im = pngImageB64String ,ub='')

    return render_template('Stats.html',stats='',cnt = '',un = '',im = '',ub='')



if __name__ == '__main__':
    app.run(debug=True)


