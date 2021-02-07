from flask import Flask, request, jsonify
from scipy.io import loadmat
import os
import json
import numpy as np
import matlab.engine

app = Flask(__name__)

class MatEncode(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding='gbk')
        return json.JSONEncoder.default(self, obj)

@app.route('/', methods=['POST','GET'])
def api() -> str:
    # xm0 = request.args.get('x')
    # ym0 = request.args.get('y')
    # hm0 = request.args.get('z')
    # vx0 = -1000
    # vy0 = 0
    # vh0 = 0
    # TF0 = 0.1
    # h = 0.01
    # if xm0 == None or ym0 == None or hm0 == None:
    #     return "参数错误"
    # # 执行matlab函数
    # eng = matlab.engine.connect_matlab()
    # tr = eng.target_hit_v2_1_3(h,TF0,xm0,ym0,hm0,vx0,vy0,vh0)
    # a = eng.area(tr)#tr是class的实例，eng.area是调用tr的实例化方法
    # print(a)
    load_data = loadmat("/Users/zhoufeng/Documents/MATLAB/out.mat")
    mm = json.dumps(load_data,cls=MatEncode,indent=4)
    resp = jsonify(request.args)
    # print(resp)
    return mm
    # return resp
    #return .items().__str__() 
    # return "没有get请求"
    


if __name__ == '__main__':
    app.run(debug=True,port=8001)