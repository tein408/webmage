# 서비스 소개
- 만다라트로 소통하는 SNS

# 개발 기간
2023.10.17 ~ 2023.11.02

# 주요 라이브러리
1. Django
    - Python으로 제작된 오픈소스 웹 프레임워크
    - MVT pattern 사용, ORM 지원
2. Django Rest Framework
    - RESTful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
3. Swagger
    - DRF용 API 문서 자동화 라이브러리
4. Coverage
    - 테스트코드 커버리지 측정을 위한 라이브러리


# 실행
- 스웨거 접속
    ```shell
    $] docker build -t webmage .
    $] docker run -d -p 8000:8000 webmage

    # http://localhost:8000/swagger 로 확인
    ```

- 테스트 코드 실행

    ```shell
    # 테스트코드 실행
    $] coverage run manage.py test

    # 커버리지 확인
    $] coverage html

    # 프로젝트 폴더 > htmlcov 폴더 > index.html 확인
    ```



# 개발팀 소개
<table>
    <tr>
        <td align="center" width="150px">
        <a href="https://github.com/tein408" target="_blank"></a>
            <img src="https://avatars.githubusercontent.com/u/75615404?v=4" alt="강은하 프로필">
        </a>
        </td>
        <td align="center" width="150px">
        <a href="https://github.com/KimChaeHong" target="_blank"></a>
            <img src="https://avatars.githubusercontent.com/u/49267413?v=4" alt="김채홍 프로필">
        </a>
        </td>
        <td align="center" width="150px">
        <a href="https://github.com/Junhyung-Lee27" target="_blank"></a>
            <img src="https://avatars.githubusercontent.com/u/61534393?v=4" alt="이준형 프로필">
        </a>
        </td>
    </tr>
    <tr>
        <td align="center">
            <a href="https://github.com/tein408" target="_blank">
                강은하
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/KimChaeHong" target="_blank">
                김채홍
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/Junhyung-Lee27" target="_blank">
                이준형
            </a>
        </td>
    </tr>
    <tr>
        <td>
            - Mandalart API <br>
            - User API <br>
            - Test Code <br>
            - Docker setting
        </td>
        <td>
            - Feed API <br>
            - Todo List API
        </td>
        <td>
            - 검색 API
        </td>
    </tr>
</table>

# Commit Convention

- 새로운 기능 생성
    - `Add <작성한 사람 : 추가한 부분>`
- 추가
    - `Update  <작성한 사람 : 수정한 부분>`
- 삭제
    - `Delete <작성한 사람 : 삭제한 부분>`
- 파일명 수정
    - `Rename <작성한 사람 : 수정 전 -> 수정 후>`
- 수정
    - `Modify <작성한사람 : 수정한 부분>`
