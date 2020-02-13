from flask import Flask,request,make_response
import hashlib
import xmltodict
import time

WX_TOKEN='yebanjifeng'
app=Flask(__name__)

@app.route('/')
def index():
    return 'This is my website'

@app.route('/wechat_api',methods=['GET','POST'])
def wechat():

    if request.method=='POST':
        xml_str=request.data
        if not xml_str:
            return ""
        xml_dict=xmltodict.parse(xml_str)
        xml_dict=xml_dict.get('xml')
        msg_type=xml_dict.get('MsgType')
        if msg_type=='text':
            resp_dict={'xml':{
                  'ToUserName':xml_dict.get('FromUserName'),
                  'FromUserName':xml_dict.get('ToUserName'),
                  'CreateTime':int(time.time()),
                  'MsgType':'text',
                  'Content':xml_dict.get('Content')
            }
        }

            resp_xml_str=xmltodict.unparse(resp_dict)
            return resp_xml_str

        

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
