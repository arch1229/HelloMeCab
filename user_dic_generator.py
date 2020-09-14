import sys
import os
import csv

current_working_directory = os.getcwd()
if os.path.basename(current_working_directory) != "lexical_analysis":
    print("Wrong Directory Error: DO NOT RUN THIS FILE IN THIS DIRECTORY!")
    sys.exit(1)

def consonant_checker(word):    #아스키(ASCII) 코드 공식에 따라 입력된 단어의 마지막 글자 받침 유무를 판단해서 뒤에 붙는 조사를 리턴하는 함수
    last = word[-1]     #입력된 word의 마지막 글자를 선택해서
    criteria = (ord(last) - 44032) % 28     #아스키(ASCII) 코드 공식에 따라 계산 (계산법은 다음 포스팅을 참고하였습니다 : http://gpgstudy.com/forum/viewtopic.php?p=45059#p45059)
    if criteria:       #나머지가 0이면 받침이 없는 것
        return True
    return False

ACCESS_DIRECTORY = "mecab-ko-dic-2.1.1-20180720"
ENTITY_LIST = "entity-list"
USER_DIC = "user-dic"
SOURCE_DIRECTORY = os.path.join(current_working_directory,ACCESS_DIRECTORY,ENTITY_LIST)
TARGET_DIRECTORY = os.path.join(current_working_directory,ACCESS_DIRECTORY,USER_DIC)

source_file = open(os.path.join(SOURCE_DIRECTORY, "input_entity.csv"), 'r', encoding='utf-8')
target_file = open(os.path.join(TARGET_DIRECTORY, "output_entity.csv"), 'w', encoding='utf-8')
wr = csv.writer(target_file, delimiter=',',lineterminator='\n')
for line in csv.reader(source_file):
    consonant = 'T' if consonant_checker(line[0]) else 'F'
    wr.writerow([line[0],'','',0,'NNP','*',consonant,'ENTITY','*','*','*','*','*'])

source_file.close()
target_file.close()