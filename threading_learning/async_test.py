import logging
import os


class token_cache():
    @classmethod
    def get(cls,token):
        pass

    @classmethod
    def set(self,token,value):
        pass

def async_fetch_token():
    pass

def get_token_cache(f):
    @wraps(f)
    async def wrap(*args,**kwargs):
        try:
            token= token_cache.get('token')
            if token:
                os.environ['token'] = token
                return await f(*args,**kwargs)
            else:
                token = await async_fetch_token()
                token_cache.set('token',token)
                return await f(*args,**kwargs)
        except Exception as e:
            logging.exception(e)
    return wrap

@get_token_cache
async def do_push(push_data):
    logging.info(f"[HYX]开始推送检查信息[seriesid]:{push_data['seriesidex']}")
    #hyx_status = -1
    # -1:接口请求异常
    # 200 :关联成功
    # 201 关联失败
    # 202 该影像已有关联检查
    # 203 设备类型不匹配
    client = tornado.httpclient.AsyncHTTPClient()
    try:
        hyx_conf = setting.get("THIRDPARTY",{}).get('hyx',{})
        url = parse.urljoin(hyx_conf.get('url'),'/hyxpacs/pacsMatch/create')
        response = await  client.fetch(url,method="POST",
                                       body=json.dumps(push_data,cls=JsonEncoderX),
                                       headers={'Content-Type':'application/json',
                                                'X-Authorization':os.environ.get('token','')},
                                       request_timeout=10)
        logging.info(f"[HYX]开始推送信息成功:{response.body}")
        push_ok = True
        result = json.loads(response.body)
        hyx_status = result.get('status',"")
        errordesc="associationid="#关联id
        if hyx_status==200:
            associationid = result.get('result','')
        else:
            errordesc = result.get('result','')
        update_push_state(push_data,errordesc,push_ok,hyx_status,associationid)
    except tornado.httpclient.HTTPClientError as e:
        if e.code in [401,403]:
            logging.error('[HYX]token失效:%d,重新获取token',e.code) #await
