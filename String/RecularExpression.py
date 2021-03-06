# 문자 클래스 []
# [abc]는 abc중 어느 한 개의 문자와도 맞으면 매치
# [a-z]는 소문자[a-zA-Z]는 알파벳 모두 [0-9]는 숫자
# 대괄호 안에서 [^] 는 반대의 의미를 지님 [^0-9]는 숫자가 아닌 문자만 매치

# Dot(.)
# 줄바꿈 문자 '\n'을 제외한 모든 문자와 매칭
# a.b 는 a와 b 사이에 어떤 문자가 들어와도 모두 매칭

# 반복 (*)
# 별은 반복을 뜻함. 단 *앞에 오는 문자가 0개를 포함하여 몇 개가 오든 모두 매치한다.
# lo*l 이면 ll, lol, looool (O), lbl (X)

# 반복 (+)
# 별과는 다르게 +는 최소 1번이상 반복되어야 함.
# lo+l 이면 ll(X) lol lool(O)

# ? 없거나 하나있거나.
# lo?l 이면 ll, lol (O)    lool(X)

# {m,n} 반복 횟수 지정
# lo{3,5}l 이면 ll, lol, lool(X)     loool, loooool(O)     looooool(X)

# | (or)
# a|b|c 이면 a나b나c중에 하나 있으면 매치
# a, b, c, a b, a b c  (O)        d (X)

# 시작^ 괄호 밖에서의 ^는 반대가 아니라 시작을 의미, (여러줄의 문자열일 경우 첫 줄만 적용되지만, re.MULTILINE옵션을 추가하면 각 줄의 첫문자 적용)
# ^a 는 a로 시작하는 것을 뜻함
# a, aaa (O)  b, baaa, 1aaa(X)

# 끝$  끝나는 문자 매치. (여러줄의 문자열일 경우 첫 줄만 적용되지만, re.MULTILINE옵션을 추가하면 각 줄의 첫문자 적용)
# a$는 a로 끝나는 것과 매치
# a, aa, baa(O)         aabb(X)

# \A는 ^와 동일하지만 re.MULTILINE 옵션을 무시하고 항상 문자열 첫 줄의 시작문자만 검사.
# \Z는 $와 동일하지만 re.MULTILINE 옵션을 무시하고 항상 문자열 첫 줄의 시작문자만 검사.

###########################################################################################################################

# 조건이 있는 표현식

# 표현식1(?=표현식2) 는 표현식1뒤의 문자열이 표현식2와 매치되면 "표현식1" 을 매치한다.
# 'hello(?=world)' 를 예로들면
# helloworld (O) byeworld(X) helloJames(X)

# (?<=표현식1)표현식2 는 표현식2 앞의 문자열이 표현식1과 매치되면 "표현식2" 을 매치한다.
# '(?<=hello)world' 를 예로들면
# helloworld(O) byeworld(X) helloJames(X)

# (?<!표현식1)표현식2 는 표현식2 앞의 문자열이 표현식1과 "매치되지 않으면" "표현식2" 을 매치한다.
# '(?<!hello)world' 를 예로들면
# helloworld(X) byeworld(O) helloJames(X)

# ======================================================================================================
# match, search, findall, finditer

# 파이썬에서는 정규표현식 사용을 위해 "import re" 를 통해 re모듈을 임포트 해서 사용한다.
# 매치타입은 "변수 = re.compile('정규표현식')" 을 통해 변수로 저장하여 사용할 수도 있고
# 컴파일하지않고 바로 사용도 할 수 있다.

# 컴파일을 하게되면 예를 들어. p = re.compile('[a-z]+')라고 지정해주면 p는 알파벳 소문자로 시작하면서 하나이상 반복되는 문자열을 캐치하는 패턴이다.
# p.match('aaaaa'), p.match('baaaa')는 매치되고 p.match('1aaaa')는 매치하지 않는다.
# p.match는 문자열의 처음부터 검색하여 일치하는 패턴을 매칭하는데, 반드시 시작부터 일치해야 한다.

# p.search는 match와 비슷하지만 처음부터 매치할 필요는 없다. 전체 문자열에서 검색한다.(처음 일치하는 패턴)    (match와 search는 매치오브젝트로 반환)

# p.findall은 패턴과 일치되는 모든 부분을 찾아 "리스트로 반환"
# p.finditer은 findall과 비슷하지만 "매치오브젝트"로 반환

# p.fullmatch은 문자열이 남는부분 없이 완벽하게 일치하는지 검사 (매치오브젝트 반환)

#########################################################################################################################

# 매치 오브젝트의 함수들

# group() : 매치된 문자열 출력
# start() : 매치 시작지점 인덱스 출력
# end()   : 매치 끝지점 인덱스 출력
# span    : (start(),end())를 튜플로 출력

# ex) p = re.compile('[a-z]+')
#     result = p.search('1aaa11aaa1')
#     result.group()의 결과는 aaa
#     result.start()의 결과는 1, result.end()의 결과는 4, result.span()의 결과는(1,4)

# 그룹화 ( groups )
# p = re.search('(hello)(world)' , 'helloworld)
# grouping = p.groups()
# print(grouping) ===>  ('hello', 'world') 로 튜플로 출력
# p.group()과 p.group(0)은 매치된 전체(helloworld)를 출력
# p.group(1)은 hello p.group(2)는 world를 출력

# 컴파일 옵션
# re.compile('정규식')으로만 쓸 수도 있지만 re.compile('정규식', re.옵션)을 줄 수도 있다.

# re.DOTALL or re.S (\n까지 포함하는 옵션)
# 예를 들어, p = re.compile('.') / result = p.findall('1a\nbc')는 ['1', 'a', 'b', 'c'] 이지만
# p = re.compile('.', re.DOTALL) 은 \n까지 ['1', 'a', '\n', 'b', 'c'] 이다.

# re.IGNORECASE 옵션은 대소문자 구분 없이 소문자와 대문자 모두 매치

# re.MULTILINE or re.M 은 여러 줄의 문자열에 ^와 $를 적용
# re.MULTILINE이 없으면 첫 줄에만 적용됨

# 백슬래시 문제
# \는 메타문자를 일반 리터럴 문자로 취급하게 끔 해준다.
# 예를들어, [ 는 메타문자이지만 \[ 로 처리하면 일반 대괄호 문자'['로 취급하게 해준다.
# \section 이라는 문자열을 찾기 위한 정규식을 찾는다고 할 때
# \\section이라고 해야 할 것 같지만, 파이썬에서는 \\가 \로 해석되기 때문에 \\\\section이라고 해야한다.
# 하지만 너무 번거롭기 때문에 r'\\section'이라고 하면 된다.

# 정규식앞에 r을 붙여주면 문자열 구성 그대로.  출력('\n')도 출력

#======================================================================================
# 자주 사용하는 문자 클래스
# \d = [0-9]
# \D = [^0-9]
# \s = [ \t\n\r\f\v] 즉 whitespace와 일치
# \S = [^ \t\n\r\f\v] 즉 not whitespace와 일치
# \w = [a-zA-Z0-9_] 와 일치. 즉 문자+숫자
# \W = [^a-zA-Z0-9_] 와 일치. 즉 문자+숫자가 아닌 문자와 매치

