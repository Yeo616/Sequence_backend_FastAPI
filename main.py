from fastapi import FastAPI,HTTPException, Form, Query,Body # => FastAPI 클래스의 인스턴스 생성
from bson.objectid import ObjectId
import logging
import pymongo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() # => FastAPI 클래스의 인스턴스 생성

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

logger = logging.getLogger('info_test')                                               # Logger 인스턴스 생성, 命名
logger.setLevel(logging.DEBUG)                                                       # Logger 출력 기준
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')# Formatter 생성, log 출력 형식

# log 출력
StreamHandler = logging.StreamHandler()                                              # 콘솔 출력 핸들러 생성
StreamHandler.setFormatter(formatter)                                                
logger.addHandler(StreamHandler)      

# CORS: 허용 origin
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "192.168.1.101:54526",
    "192.168.1.100:54526",
    "exp://192.168.110.111:19000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # 요청을 허용해야하는 origin목록
    # allow_origins=origins,
    allow_credentials=True,     # ORIGIN 간 요청에 대해 쿠키를 지원해야 함. 기본값은 FALSE, 
    allow_methods=["*"],        # 허용되어야하는 http 메서드 목록, 기본값은 GET
    allow_headers=["*"],        # HTTP 요청 헤더 목록, 기본값은 [], 
)
# https://fastapi.tiangolo.com/tutorial/cors/
@app.get("/")
def read_root():
    logger.info(f"Hello : World")

    return {"Hello": "World"}

@app.get('/get-email') # 입력 받은 이메일로, 해당 데이터 있는 지 확인
async def read_info(email: str = Query(...)):
    logger.info(f"email : {email}")

    # DB연결
    db = myclient["test"]["user_db"]

    try:
        content = db.find_one({"email": email})
        # 해당 정보 찾고, 그러고 나서, 다른 정보가 있는 지 확인하기
        if content is None:
            raise HTTPException(status_code=404, detail="info not found")    

        logger.info(f"content : {content}")

        # 다른 정보가 있는지 확인
        if "phone_number" not in content or content["phone_number"] is None:
            logger.info("no phone number ")
            return{"status": "non-exist", "email": email}

        elif content["phone_number"]:
            logger.info("it has number ")
            return{"status": "exists", "email": email}

    except IndexError:
        raise HTTPException(status_code=404, detail="info not found")    

@app.post("/post-info") 
def post_info(info = Form(...), email = Form(...)):
    logger.info(f"{info} posted")

    #프로그램 관련 DB 연결
    db = myclient['test']['user_db']

    try:
         # program_info_db = list(program_info_db)
        updated = db.update_one({"email": email},
                    {"$set":{"phone_number" : info}})
        content = db.find_one({"email": email})

        logger.info(f"updated : {updated}")

        return {"status": f"{content}"}

    except IndexError:
        logger.info("no matched email")
        raise HTTPException(status_code=404, detail="Post not found")

@app.post("/post-info-body") 
def post_info(info = Body(...) , email= Body(...)):
    logger.info(f"{info} posted")

    #프로그램 관련 DB 연결
    db = myclient['test']['user_db']

    try:
         # program_info_db = list(program_info_db)
        updated = db.update_one({"email": email},
                    {"$set":{"phone_number" : info}})
        content = db.find_one({"email": email})

        logger.info(f"updated : {updated}")

        return {"status": f"{content}"}

    except IndexError:
        logger.info("no matched email")
        raise HTTPException(status_code=404, detail="Post not found")

@app.post("/delete-info")
async def delete_post(email: str = Query(...)):

    db = myclient["test"]["user_db"]
    try:
        deleted_info = db.update_one(
            {"email": email},
            {"$unset":{"phone_number":""}}) 
        logger.info(f"content_to_delete : {deleted_info}")

        return {"status":"info deleted"}
        
    except IndexError:
        raise HTTPException(status_code=404, detail="email not found")