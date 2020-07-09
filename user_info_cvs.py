
# TODO_0 : csv 모듈 불러오기
import csv
with open ('user_info.csv', 'r', newline='') as csvfile:
     user = csv.reader(csvfile, delimiter=' ', quotechar='|')
print(user)

def user_input():
    try:
        id, pw = map(str, input("아이디와 비밀번호를 차례로 입력해주세요 : ").split())
        return id, pw
    except:
        print("올바르지 않은 입력입니다!")
        id, pw = user_input()
        return id, pw

# TODO_1 : signin 함수를 구현해서 로그인 시키기
# 1. csv 파일에서 존재하는 아이디인지 확인하기
# 2. 존재하면 비밀번호 맞는지 체크
# 3. 비밀번호도 맞으면 로그인성공 출력하기


with open('user_info.csv', 'r') as csvfile:
    user=csv.DictReader(csvfile)

import user_input()

def signin():
    
    for id in user['id']:

        # 아이디 존재하는지 찾기
        if user['id'] == user_input['id']:

            if user['password'] == user_input['password']:
                print('로그인에 성공하셨습니다.!')

            # 비밀번호 틀린 경우
            else:
                print('비밀번호를 확인해주세요!')
                return 'wrong_password'

        else:
            print('존재하지 않는 아이디 입니다 !')
            return 'no_exist_id'

    return

# TODO_2 : csvfile 에 유저가 존재하는지 확인하는 함수 구현해서 호출하기
# 1. 아이디를 기준으로 존재하는 유저인지 확인
# 2. 존재한다면 다시 아이디를 입력받고,
# 3. 존재하지 않는다면 다음 단계로 넘겨주기

def check_id():
    with open ('user_info.csv', 'r') as csvfile:
        read_user = csv.reader (csvfile, delimiter=' ', quotechar='|')
        import user_input
        for row in read_user:
           if user_input['id'] in row:
                a=input('다시 아이디를 입력해주세요:')


# TODO_3 : csvfile 에 등록되어있는 형태로 유저 등록하는 함수 구현하기
# 1. 아이디와 비밀번호를 그냥 데이터로 받아서 추가해보기
# 2. 아이디와 비밀번호를 '딕셔너리' 형태로 받아서 추가해보기 (프로그래밍 실력의 기본은 구글링! 최대한 구글링 해보세요!!)

#1
def file_add_data():
    new_id=input('새로운 아이디를 입력해주세요:')
    new_pw=input('새로운 비밀번호를 입력해주세요:')

    f = open('user_info.csv', 'a')
    wr = csv.writer(f)
    wr.writerrow([new_id, new_pw])

    f.close()

#2
def file_add_dic():
    dic={}
    new_id=[]
    #key값
    new_id.append(input('새로운 아이디를 입력해주세요:'))
    dic=dic.fromkeys(new_id)

    #value값
    new_pw=input('새로운 비밀번호를 입력해주세요:')
    dic=dic.fromkeys(new_id,new_pw)
    return dic

    #입력
    with open('user_info.csv','w') as f:
        w = csv.writer(f)
        w.writerow(dic.keys())
        w.writerow(dic.values())


def userlist():
    print("현재 존재하는 유저 :")

    # TODO_4 : csvfile 에서 현재 가입되어 있는 유저 전부 출력하기

    with open ('user_info.csv', 'r') as csvfile:
         user_list = csv.DictReader(csvfile, delimiter=' ', quotechar='|')
         for row in user_list:
             print(row['id'])



def exitcheck():
    stop = int(input("\n계속하시려면 0, 종료하시려면 1을 눌러주세요. : "))
    if stop == 0:
        start()
    elif stop == 1:
        exit()


def start():
    print('csv 로 데이터 다루기 로그인 예제')

    signup_or_login = input('1 - 로그인 / 2 - 회원가입 : \n')

    if signup_or_login == 1:
        id, pw = user_input()
        # TODO_5 : 위의 TODO1 참고 후 signin 함수 실행하기
        # signin(id, pw)
        import signin


    elif signup_or_login == 2:
      # TODO_6 : 회원가입을 아이디와 비밀번호만 받아서 진행할 것
      # 1. 존재하는지 확인 (위의 TODO_2의 함수 활용)
      # 2. 문제 없으면 회원가입 완료 후 userlist() 함수 구현
        import check_id
        import userlist


        dict_user = {
            "id": id,
            "pw": pw
        }
        # signup(id, pw)
        # signup(dict_user)
        userlist()
    else:
        print("올바른 숫자를 입력하세요!")

    exitcheck()


start()

# TODO_7 : 깃헙에 업로드하고 깃헙 주소 제출!
