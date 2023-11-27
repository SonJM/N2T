from utils.dotdict import dotdict

cfg = dotdict(
    TISTORY=dotdict(
        ID='wingk98@naver.com',
        PW='02631a',
        BLOG_NAME='blisle',
        SECRET_KEY='e49f9f3f18210237ce4cff41518928ad614bc7db1550646b46b5e52b8e19064ff7dd080e',
        CLIENT_ID='e49f9f3f18210237ce4cff41518928ad',
        REDIRECT_URI='https://blisle.tistory.com',
    ),

    NOTION=dotdict(
        TOKEN_V2='v02%3Auser_token_or_cookies%3AShQ_qAygVsdPPprvYTfpDJqJqa6GmvCbw1UCzCSxCBQ8KgGVRCw07PobWnQLQcu-plfZKNV89XMEw8ZpXkh7WdQPOr05-pZRN16D0BeYyG7OaM2kEPPI9MnARnMK5jNcdUPh',
        TABLE_PAGE_URL='https://www.notion.so/5a5b95210b4949eb993f2c43c326efe4?v=a0846834dd6a4fca8d3c3b9c51910750&pvs=4',
        DOWNLOAD_DIR='~/.n2t',
        CODE_BLOCK_THEME='atom-one-dark',

        COLUMN=dotdict(
            TITLE='제목',
            CATEGORY='카테고리',
            TAG='태그',
            STATUS='상태',
            URL='링크'
        ),

        POST=dotdict(
            UPLOAD_VALUE='발행 요청',
            MODIFY_VALUE='수정 요청',
            COMPLETE_VALUE='발행 완료',
        ),
    ),

    MAIL=dotdict(
        ID='wingk98@gmail.com',
        KEY='wege ecbq gccz gjpc',
    )
)
