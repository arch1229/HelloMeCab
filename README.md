# HelloMeCab

***
## 아무것도 없는 Docker에서 MeCab-ko 시작하기
***

## 0. 기본
    apt-get update
    apt-get -y install g++ vim wget libtool autoconf make
    echo "export LC_ALL=ko_KR.UTF-8" >> ~/.bashrc

### 0.1. Hello C++ !!

    vi hello.c
        ```c++
        #include <stdio.h>
        
        int main()
        {
            printf("Hello C++ !!\n");
            return 0;
        }
        ```
    gcc hello.c -o hello
    ./hello

### 0.2 Hello Python !!

    apt-get install python3.6
    apt-get install python3-pip
    vi ~/.bashrc
        alias python=python3.6
        alias pip=pip3
    source ~/.bashrc
    python
        ```python
        print("Hello Python !!")
        print("한글도 출력 가능합니다.")
        exit()
        ```
    
## 1. 확장

### 1.1. MeCab 설치
    wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
    tar zxvf mecab-0.996-ko-0.9.2.tar.gz
    cd **myworkspace**/mecab-0.996-ko-0.9.2
    ./configure
    make

    ----------------------------minor errors----------------------------
        param.h:30:13: warning: 'Target {anonymous}::lexical_cast(Source) [with Target = std::__cxx11::basic_string<char>; Source = std::__cxx11::basic_string<char>]' defined but not used [-Wunused-function]
        std::string lexical_cast<std::string, std::string>(std::string arg) {
                    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        learner_tagger.cpp:25:7: warning: 'char* MeCab::{anonymous}::mystrdup(const string&)' defined but not used [-Wunused-function]
        char *mystrdup(const std::string &str) {
            ^~~~~~~~
    --------------------------------------------------------------------

    make check
    make install

### 1.2. MeCab-ko 설치
    wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
    tar zxfv mecab-ko-dic-2.1.1-20180720.tar.gz
    cd **myworkspace**/mecab-ko-dic-2.1.1-20180720
    autoreconf -v -f -i
        ----------------------------minor report----------------------------
        autoreconf: Entering directory `.'
        autoreconf: configure.ac: not using Gettext
        autoreconf: configure.ac: not using aclocal
        autoreconf: configure.ac: tracing
        autoreconf: configure.ac: not using Libtool
        autoreconf: running: /usr/bin/autoconf --force
        configure.ac:2: error: possibly undefined macro: AM_INIT_AUTOMAKE
            If this token and others are legitimate, please use m4_pattern_allow.
            See the Autoconf documentation.
        autoreconf: /usr/bin/autoconf failed with exit status: 1
    --------------------------------------------------------------------
    ./configure
    ./autogen.sh
    make
    ----------------------------minor errors----------------------------
    WARNING: `aclocal-1.11' is missing on your system.  You should only need it if
            you modified `acinclude.m4' or `configure.ac'.  You might want
            to install the `Automake' and `Perl' packages.  Grab them from
            any GNU archive site.
    cd . && /bin/bash /lexical_analysis/mecab-ko-dic-2.1.1-20180720/missing --run automake-1.11 --gnu
    /lexical_analysis/mecab-ko-dic-2.1.1-20180720/missing: line 52: automake-1.11: command not found
    
    WARNING: `automake-1.11' is missing on your system.  You should only need it if
            you modified `Makefile.am', `acinclude.m4' or `configure.ac'.
            You might want to install the `Automake' and `Perl' packages.
            Grab them from any GNU archive site.
    CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/bash /lexical_analysis/mecab-ko-dic-2.1.1-20180720/missing --run autoconf
    /lexical_analysis/mecab-ko-dic-2.1.1-20180720/missing: line 52: autoconf: command not found
    
    WARNING: `autoconf' is missing on your system.  You should only need it if
            you modified `configure.ac'.  You might want to install the
            `Autoconf' and `GNU m4' packages.  Grab them from any GNU
            archive site.
    --------------------------------------------------------------------
    ./configure
    mecab -d .
    ----------------------------MeCab result----------------------------
    root@2b9fbef96951:/lexical_analysis/mecab-ko-dic-2.1.1-20180720# mecab -d .
    MeCab이 정상적으로 실행되었습니다.
    MeCab	SL,*,*,*,*,*,*,*
    이	JKS,*,F,이,*,*,*,*
    정상	NNG,*,T,정상,*,*,*,*
    적	XSN,*,T,적,*,*,*,*
    으로	JKB,*,F,으로,*,*,*,*
    실행	NNG,행위,T,실행,*,*,*,*
    되	XSV,*,F,되,*,*,*,*
    었	EP,*,T,었,*,*,*,*
    습니다	EF,*,F,습니다,*,*,*,*
    .	SF,*,*,*,*,*,*,*
    EOS
    --------------------------------------------------------------------
### 1.3. MeCab-Python3 설치
    pip install mecab-python3
    vi /usr/local/etc/mecabrc
        dicdir = /lexical_analysis/mecab-ko-dic-2.1.1-20180720
    vi /etc/ld.so.conf
        /**myworkspace**/mecab-ko-dic-2.1.1-20180720
    ldconfig
    python
        import MeCab
            mecab = Mecab.Tagger()
            out = mecab.parse("Mecab-Python이 정상적으로 설치되었습니다.")
            print(out)

### 1.4 MeCab-ko 사용자 정의 사전 추가하기
    vim mecab-ko-dic-2.1.1-20180720/user-dic/**user_dic.csv**
        윤성탁,,,0,NNG,*,T,ENTITY,*,*,*,*,*
        ...
    ./mecab-ko-dic-2.1.1-20180720/tools/add-userdic.sh 
    
[user_dic_generator](user_dic_generator.py)
### 
