import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import operator


app = Flask(__name__)
model = pickle.load(open('batsman_model.pkl', 'rb'))

app = Flask(__name__)
model2 = pickle.load(open('bowler_model.pkl', 'rb'))

app = Flask(__name__)
model3 = pickle.load(open('allrounder_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bowl/')
def bowl():
    return render_template('bowl.html')

@app.route('/allrounder/')
def allrounder():
    return render_template('allrounder.html')

@app.route('/predict3',methods=['POST'])
def predict3():
    '''
    For rendering results on HTML GUI
    '''
    prediction3=[]
    z3=list()
    for i in range(4):
        if i==0:
            int_features=[165,187,0]
        elif i==1:
            int_features=[73,27,16]
        elif i==2:
            int_features=[54,54,15]
        else:
            int_features=[12,4,15]
            
        for x in request.form.values():        
            if x=='Bay Oval':
                int_features.extend((1,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Chandigarh':
                int_features.extend((0,1,0,0,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Delhi':
                int_features.extend((0,0,1,0,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Edgbaston':
                int_features.extend((0,0,0,1,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Headingley':
                int_features.extend((0,0,0,0,1,0,0,0,0,0,0,0,0,0,0))
            elif x=='Hyderabad':
                int_features.extend((0,0,0,0,0,1,0,0,0,0,0,0,0,0,0))
            elif x=='Mclean Park':
                int_features.extend((0,0,0,0,0,0,1,0,0,0,0,0,0,0,0))
            elif x=='Old Trafford':
                int_features.extend((0,0,0,0,0,0,0,1,0,0,0,0,0,0,0))
            elif x=='Ranchi':
                int_features.extend((0,0,0,0,0,0,0,0,1,0,0,0,0,0,0))
            elif x=='Seddon Park':
                int_features.extend((0,0,0,0,0,0,0,0,0,1,0,0,0,0,0))
            elif x=='Southampton':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,1,0,0,0,0))
            elif x=='The Oval':
                 int_features.extend((0,0,0,0,0,0,0,0,0,0,0,1,0,0,0))
            elif x=='Trinidad':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,0,0,1,0,0))
            elif x=='Vidharbha':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,0,0,0,1,0))
            elif x=='Wellington':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,0,0,0,0,1))
            elif x=='Batting':
                int_features.extend((1,0,0,0,0,0,0))
            elif x=='Bounce and Pace':
                int_features.extend((0,1,0,0,0,0,0))
            elif x=='Bowling':
                int_features.extend((0,0,1,0,0,0,0))
            elif x=='Pace and Bounce':
                int_features.extend((0,0,0,1,0,0,0))
            elif x=='Slow':
                int_features.extend((0,0,0,0,0,0,0))
            elif x=='Slow and Low':
                int_features.extend((0,0,0,0,0,1,0))
            elif x=='Swinging':
                int_features.extend((0,0,0,0,0,0,1))
            elif x=='Afghanistan':
                int_features.extend((1,0,0,0,0,0,0,0))
            elif x=='Australia':
                int_features.extend((0,1,0,0,0,0,0,0))
            elif x=='Bangladesh':
                int_features.extend((0,0,1,0,0,0,0,0))
            elif x=='England':
                int_features.extend((0,0,0,1,0,0,0,0))
            elif x=='New Zealand':
                int_features.extend((0,0,0,0,1,0,0,0))
            elif x=='South Africa':
                int_features.extend((0,0,0,0,0,1,0,0))
            elif x=='Sri Lanka':
                int_features.extend((0,0,0,0,0,0,1,0))
            elif x=='West Indies':
                int_features.extend((0,0,0,0,0,0,0,1))
            elif x=='Cold':
                int_features.extend((1,0))
            elif x=='Hot and humid':
                int_features.extend((0,1))
            elif x=='Away':
                int_features.extend((0,1))
            elif x=='Home':
                int_features.extend((1,0))
        final_features3 = [np.array(int_features)]
        z3.append(final_features3)
        prediction3.append(np.around(model3.predict(z3[i])))

        #output = round(prediction[0], 2)
    print(prediction3)


    dictPrd={"RA Jadeja":prediction3[0][0] ,
          "KM Jadhav":prediction3[1][0] ,
          "H Pandya":prediction3[2][0] ,
          "V Shankar":prediction3[3][0] }

    srt = sorted(dictPrd.items(), key=operator.itemgetter(1),reverse=True)

    oput = ""
    flag = 0 
    for i in srt:
        
        flag += 1
           
        if flag == 5:
               break

        oput += str(i[0])+" | "

    print(oput)        
        
    return render_template('result.html', prediction_text=oput , title='All Rounder Analysis')

def predict2():
    '''
    For rendering results on HTML GUI
    '''
    prediction2=[]
    z2=list()
    for i in range(6):
        if i==0:
            int_features=[114,5,132]
        elif i==1:
            int_features=[77,5,144]
        elif i==2:
            int_features=[11,5,15]
        elif i==3:
            int_features=[51,5,88]
        elif i==4:
            int_features=[63,4,104]
        else:
            int_features=[60,5,104]
            
        for x in request.form.values():        
            if x=='Bay Oval':
                int_features.extend((1,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Chandigarh':
                int_features.extend((0,1,0,0,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Delhi':
                int_features.extend((0,0,1,0,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Edgbaston':
                int_features.extend((0,0,0,1,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Headingley':
                int_features.extend((0,0,0,0,1,0,0,0,0,0,0,0,0,0,0))
            elif x=='Hyderabad':
                int_features.extend((0,0,0,0,0,1,0,0,0,0,0,0,0,0,0))
            elif x=='Mclean Park':
                int_features.extend((0,0,0,0,0,0,1,0,0,0,0,0,0,0,0))
            elif x=='Old Trafford':
                int_features.extend((0,0,0,0,0,0,0,1,0,0,0,0,0,0,0))
            elif x=='Ranchi':
                int_features.extend((0,0,0,0,0,0,0,0,1,0,0,0,0,0,0))
            elif x=='Seddon Park':
                int_features.extend((0,0,0,0,0,0,0,0,0,1,0,0,0,0,0))
            elif x=='Southampton':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,1,0,0,0,0))
            elif x=='The Oval':
                 int_features.extend((0,0,0,0,0,0,0,0,0,0,0,1,0,0,0))
            elif x=='Trinidad':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,0,0,1,0,0))
            elif x=='Vidharbha':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,0,0,0,1,0))
            elif x=='Wellington':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,0,0,0,0,1))
            elif x=='Batting':
                int_features.extend((1,0,0,0,0,0,0))
            elif x=='Bounce and Pace':
                int_features.extend((0,1,0,0,0,0,0))
            elif x=='Bowling':
                int_features.extend((0,0,1,0,0,0,0))
            elif x=='Pace and Bounce':
                int_features.extend((0,0,0,1,0,0,0))
            elif x=='Slow':
                int_features.extend((0,0,0,0,0,0,0))
            elif x=='Slow and Low':
                int_features.extend((0,0,0,0,0,1,0))
            elif x=='Swinging':
                int_features.extend((0,0,0,0,0,0,1))
            elif x=='Afghanistan':
                int_features.extend((1,0,0,0,0,0,0,0))
            elif x=='Australia':
                int_features.extend((0,1,0,0,0,0,0,0))
            elif x=='Bangladesh':
                int_features.extend((0,0,1,0,0,0,0,0))
            elif x=='England':
                int_features.extend((0,0,0,1,0,0,0,0))
            elif x=='New Zealand':
                int_features.extend((0,0,0,0,1,0,0,0))
            elif x=='South Africa':
                int_features.extend((0,0,0,0,0,1,0,0))
            elif x=='Sri Lanka':
                int_features.extend((0,0,0,0,0,0,1,0))
            elif x=='West Indies':
                int_features.extend((0,0,0,0,0,0,0,1))
            elif x=='Cold':
                int_features.extend((1,0))
            elif x=='Hot and humid':
                int_features.extend((0,1))
            elif x=='Away':
                int_features.extend((0,1))
            elif x=='Home':
                int_features.extend((1,0))
        final_features2 = [np.array(int_features)]
        z2.append(final_features2)
        prediction2.append(np.around(model2.predict(z2[i])))

        #output = round(prediction[0], 2)
    print(prediction2)


    dictPrd={"B Kumar":prediction2[0][0] ,
          "M Shami":prediction2[1][0] ,
          "KK Ahmed":prediction2[2][0] ,
          "YS Chahal":prediction2[3][0] ,
          "J Bumrah":prediction2[4][0] ,
          "K Yadav":prediction2[5][0]}

    srt = sorted(dictPrd.items(), key=operator.itemgetter(1),reverse=True)

    oput = ""
    flag = 0 
    for i in srt:
        
        flag += 1
           
        if flag == 5:
               break

        oput += str(i[0])+" | "

    print(oput)        
        
    return render_template('result.html', prediction_text=oput, title='Bowler Analysis')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    pt = request.form["pred_type"]
    if pt == "bat":
        return predict1()
    elif pt =="bowl":
        return predict2()
    else:
        return predict3()
    

def predict1():
    '''
    For rendering results on HTML GUI
    '''
    prediction=[]
    z=list()
    for i in range(9):
        if i==0:
            int_features=[1,218,42,27,49]
        elif i==1:
            int_features=[2,133,27,17,45]
        elif i==2:
            int_features=[3,239,54,43,60]
        elif i==3:
            int_features=[5,350,73,10,50]
        elif i==4:
            int_features=[6,54,4,0,35]
        elif i==5:
            int_features=[4,12,0,0,23]
        elif i==6:
            int_features=[5,9,4,0,49]
        elif i==7:
            int_features=[6,68,6,2,43]
        else:
            int_features=[4,23,4,2,43]
            
        for x in request.form.values():        
            if x=='Bay Oval':
                int_features.extend((1,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Chandigarh':
                int_features.extend((0,1,0,0,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Delhi':
                int_features.extend((0,0,1,0,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Edgbaston':
                int_features.extend((0,0,0,1,0,0,0,0,0,0,0,0,0,0,0))
            elif x=='Headingley':
                int_features.extend((0,0,0,0,1,0,0,0,0,0,0,0,0,0,0))
            elif x=='Hyderabad':
                int_features.extend((0,0,0,0,0,1,0,0,0,0,0,0,0,0,0))
            elif x=='Mclean Park':
                int_features.extend((0,0,0,0,0,0,1,0,0,0,0,0,0,0,0))
            elif x=='Old Trafford':
                int_features.extend((0,0,0,0,0,0,0,1,0,0,0,0,0,0,0))
            elif x=='Ranchi':
                int_features.extend((0,0,0,0,0,0,0,0,1,0,0,0,0,0,0))
            elif x=='Seddon Park':
                int_features.extend((0,0,0,0,0,0,0,0,0,1,0,0,0,0,0))
            elif x=='Southampton':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,1,0,0,0,0))
            elif x=='The Oval':
                 int_features.extend((0,0,0,0,0,0,0,0,0,0,0,1,0,0,0))
            elif x=='Trinidad':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,0,0,1,0,0))
            elif x=='Vidharbha':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,0,0,0,1,0))
            elif x=='Wellington':
                int_features.extend((0,0,0,0,0,0,0,0,0,0,0,0,0,0,1))
            elif x=='Batting':
                int_features.extend((1,0,0,0,0,0,0))
            elif x=='Bounce and Pace':
                int_features.extend((0,1,0,0,0,0,0))
            elif x=='Bowling':
                int_features.extend((0,0,1,0,0,0,0))
            elif x=='Pace and Bounce':
                int_features.extend((0,0,0,1,0,0,0))
            elif x=='Slow':
                int_features.extend((0,0,0,0,0,0,0))
            elif x=='Slow and Low':
                int_features.extend((0,0,0,0,0,1,0))
            elif x=='Swinging':
                int_features.extend((0,0,0,0,0,0,1))
            elif x=='Afghanistan':
                int_features.extend((1,0,0,0,0,0,0,0))
            elif x=='Australia':
                int_features.extend((0,1,0,0,0,0,0,0))
            elif x=='Bangladesh':
                int_features.extend((0,0,1,0,0,0,0,0))
            elif x=='England':
                int_features.extend((0,0,0,1,0,0,0,0))
            elif x=='New Zealand':
                int_features.extend((0,0,0,0,1,0,0,0))
            elif x=='South Africa':
                int_features.extend((0,0,0,0,0,1,0,0))
            elif x=='Sri Lanka':
                int_features.extend((0,0,0,0,0,0,1,0))
            elif x=='West Indies':
                int_features.extend((0,0,0,0,0,0,0,1))
            elif x=='Cold':
                int_features.extend((1,0))
            elif x=='Hot and humid':
                int_features.extend((0,1))
            elif x=='Away':
                int_features.extend((0,1))
            elif x=='Home':
                int_features.extend((1,0))
        final_features = [np.array(int_features)]
        z.append(final_features)
        prediction.append(np.around(model.predict(z[i])))

        #output = round(prediction[0], 2)
    print(prediction)


    dictPrd={"RG Sharma":prediction[0][0] ,
          "Dhawan":prediction[1][0] ,
          "V Kohli":prediction[2][0] ,
          "MS Dhoni":prediction[3][0] ,
          "H Pandya":prediction[4][0] ,
          "RR Pant":prediction[5][0] ,
          "SS Iyer":prediction[6][0] ,
          "KM Jadhav":prediction[7][0] ,
          "KL Rahul":prediction[8][0]}

    srt = sorted(dictPrd.items(), key=operator.itemgetter(1),reverse=True)

    oput = ""
    flag = 0 
    for i in srt:
        
        flag += 1
           
        if flag == 5:
               break

        oput += str(i[0])+" | "

    print(oput)        
        
    return render_template('result.html', prediction_text=oput, title='Batsmen Analysis')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
