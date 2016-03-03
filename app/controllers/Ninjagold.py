"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random, datetime  
class Ninjagold(Controller):
    def __init__(self, action):
        super(Ninjagold, self).__init__(action)

    def index(self):
       
        return self.load_view('index.html', gold = session['gold'], status= session['status'])
   
    def process_money(self):

        if 'gold' not in session:
            session['status'] = []
            session['gold'] = 0 

        if request.form['building'] == 'farm':
            session['farm'] =  random.randrange(10,21)
            session['gold'] += session['farm']
            # session['status'] = " you have earned " +str(session['farm']) + " gold"
            session['status'].append("Earned " + str(session['farm']) + " "+"gold from the farm" + " "+ str(datetime.datetime.now())) 

        elif request.form['building'] == 'cave':
            session['cave'] = random.randrange(5,11)
            session['gold'] += session['cave']
            session['status'].append("Earned " + str(session['cave']) + " "+"gold from the cave" + " "+ str(datetime.datetime.now())) 

        elif request.form['building'] == 'house':
            session['house'] = random.randrange(2,6)
            session['gold'] += session['house']
            session['status'].append("Earned " + str(session['house']) + " "+"gold from the house"+ " "+ str(datetime.datetime.now()))


        elif request.form['building'] == 'casino':
            session['casino'] = random.randrange(-51,51)
            session['gold'] += session['casino']

        if session['casino'] > 0 :
            session['status'].append("Earned " + str(session['casino']) + " "+"gold from the casino"+ " "+ str(datetime.datetime.now()))
        else:
            session['status'].append("Lost " + str(-1 * session['casino']) + " "+"gold from the casino"+ " "+ str(datetime.datetime.now()))




        return redirect('/')