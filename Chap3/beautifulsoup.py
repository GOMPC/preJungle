# 선택자를 사용하는 방법 (copy selector)
soup.select('태그명')
soup.select('.클래스명')
soup.select('#아이디명')

soup.select('상위태그명 > 하위태그명 > 하위태그명')
soup.select('상위태그명.클래스명 > 하위태그명.클래스명')

# 태그와 속성값으로 찾는 방법
soup.select('태그명[속성="값"]')

# 한 개만 가져오고 싶은 경우
soup.select_one('위와 동일')

# a < div .tit5 < td .title < tr < tbody < table .list_ranking < div #old_content < div #cbody .type_1
# < div .old_layout old_super_db < div .article < div #content < div #container < div #wrap .fix < body

# 제목은 a태그의 텍스트.