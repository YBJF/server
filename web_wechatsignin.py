from flask import Flask,request,make_response
import hashlib


WX_TOKEN='yebanjifeng'
app=Flask(__name__)

@app.route('/')
def index():
    return 'this is my flask website'

@app.route('/wechat_api',methods=['GET','POST'])
def wechat():
    if request.method=='GET':
        token = WX_TOKEN
        data=request.args
        signature=data.get('signature','')
        timestamp=data.get('timestamp','')
        nonce=data.get('nonce','')
        echostr=data.get('echostr','')
        s=sorted([timestamp,nonce,token])
        s=''.join(s)
    if hashlib.sha1(s.encode('utf-8')).hexdigest()==signature:
        response=make_response(echostr)
        return response

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
