from flask import Flask,request,make_response
import hashlib
import xmltodict
import time
import itchat
import requests

def get_response(_info):
    print(_info)
    api_url='http://www.tuling123.com/openapi/api'
    data={
        'key':'a3daf62f7b3145cf9261d079d0767dea',
        'info':_info,
        'userid':'robot'
    }
    r=requests.post(api_url,data=data).json()
    return r.get('text')

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
        content=xml_dict.get('Content')
        content=get_response(content)
        if msg_type=='text':
            resp_dict={'xml':{
                  'ToUserName':xml_dict.get('FromUserName'),
                  'FromUserName':xml_dict.get('ToUserName'),
                  'CreateTime':int(time.time()),
                  'MsgType':'text',
                  'Content':content
            }
        }

            resp_xml_str=xmltodict.unparse(resp_dict)
            return resp_xml_str

        

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
