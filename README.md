
# Back-end: FastAPI 상태 시퀀스

- 상태 시퀀스에 관한 back-end 부분입니다.
- 해당 프로젝트는 FastAPI로 작성하였습니다. 

 [Fastapi 공식문서](https://fastapi.tiangolo.com/)

## 시작하기
1. 프로젝트 폴더 생성
2. 해당 폴더로 이동
3. 파이썬 가상환경 설치
```
python -m venv venv
```
4. 가상환경 실행
```
cd venv\Script
activate
```
5. 프로젝트 폴더로 이동
6. 패키지 설치
```
pip install -r requirements.txt
```
7. 실행
```
uvicorn main:app --reload
```

### 주의
- 파이썬의 가상 환경 모듈인 'venv'를 사용하려면 파이썬 버젼이 3.3이상이어야 합니다.
- 작업은 가상환경에서 실행하도록 합니다.

<br>

## 다른 프로젝트와 함께 사용하기

- 바닐라 자바스크립트 상태 관리 시퀀스: https://github.com/Yeo616/vanilla-javascript-sequence

<br>

## 기능
- 데이터 조회
- 데이터 입력하여 DB에 저장

## 사용된 기술
- FastAPI
- MongoDB

## 스크린샷
여기서 DB는 mongoDB의 test DB의 user_db 컬렉션을 말합니다.

### /get-email 
> - method: GET
> - 기능: 유저의 이메일을 이용하여, 다른 데이터가 DB에 저장 되어있는지 확인합니다. 
> - 해당 예제에서는 phone_number가 있는지 확인하였습니다. 

![enter image description here](https://user-images.githubusercontent.com/102447800/226251866-d1364614-0602-4035-85db-ed5ab203266e.png)

> email: 입력받아야할 유저 정보
> excute: API 실행
> code: 200 응답에 성공
> response body: 응답하는 바디 내용

<br/>

### /post-info
> - method: POST
> - 기능: 인증된 이메일로, 찾고자 하는 유저의 데이터가 DB에 없을 경우, 추가합니다. 
> - 해당 예제에서는 phone_number가 있는지 확인하였습니다. 
> 
![enter image description here](https://user-images.githubusercontent.com/102447800/226253461-205c917e-174e-4c6f-a8c0-9b03f521d2bc.gif)

<br>

### /delete-info 
> - method: POST
	> -- DB document를 삭제하는 것이 아닌, 하나의 필드만 삭제하여, update기능을 사용했기 때문에 method는 POST입니다.	
> - 기능: 정보를 삭제합니다.
	> -- 유저의 document는 그대로 두고, 원하는 정보만 삭제했습니다. 해당 프로젝트에서는 유저 아이디에 해당하는 phone_number 필드만 삭제했습니다.

![enter image description here](https://user-images.githubusercontent.com/102447800/226522523-153edcf8-c080-4121-9dfb-5c08423eb992.gif)

> 성공적으로 삭제 기능이 수행되면,{"status": "info deleted"} 응답을 받습니다.


<br>

## 프로젝트 제작자 연락처
guswls9281@gmail.com
