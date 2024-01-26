# 전체 템플릿 구조
email_template = """
<html lang="ko">

<head>
    <title>마음의 소리</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
    <meta name="title" content="비글즈, bigglz, 투아이센터" />
    <meta name="author" content="비글즈, bigglz, 투아이센터" />
    <meta name="keywords" content="비글즈, bigglz, 투아이센터, 펫, 인증메일, 고객센터, 휴면회원" />
</head>

<body>
    <div style="max-width:580px; width:100%; margin:0 auto; font-weight:400; line-height:1.2; font-family: 'nexon', Dotum, sans-serif;">
        <div style="display:block; margin:0; padding:0; border:0; font-weight:400; line-height:1.2;">
            <div style="display:block; margin:0; padding:0; border:0; font-weight:400; line-height:1.2;">
                <header style="display:flex; height:69px; padding-left:32px; background:#ffed00; font-weight:400; line-height:1.2;">
                    <h1 style="height:48px; margin:0; padding:0; border:0; font-weight:400; line-height:1.2;">
                        <a href="https://www.bigglz.com/" target="_blank" style="display:block; width:115px; height:48px; margin:8px 0 0; padding:0; border:0; background:url('https://d2w7ph9vouh9tr.cloudfront.net/Email/images/header_logo.png') no-repeat 0 0/100%; font-weight:400; line-height:1.2; text-indent:-9999px;"></a>
                    </h1>
                </header>
                <div style="display:block; padding:31px 16px 26px; font-weight:400; line-height:1.2;">
                    <div style="display:block; margin:0; padding:0; border:0; font-weight:400; line-height:1.2;">
                        <div style='text-align: center;'>
                            <p style="font-size: 30px;">💌</p>
                            <br/>
                            <h2 style="margin:0; padding-bottom:18px; font-family:'nexon', Dotum, sans-serif; font-size:20px; line-height:22px; color:#333;">
                                {date} 마음의 소리가 도착했어요!
                            </h2>
                            <p>{intro_text}</p>
                            <br/>
                        </div>
                        <div style="display:block; font-family:'nexon', Dotum, sans-serif; font-size:13px; line-height:1.539;">
                            <ul style="padding: 0; list-style-type: none;">
                                {data_list}
                            </ul>
                        </div>
                        <br />
                        <p style="margin:0; padding:0; font-family:'nexon', Dotum, sans-serif; font-size:13px; line-height:1.667;">본 메일은 발신전용 메일이오니 문의사항 있으시면 <strong>고객센터</strong>를 이용해 주시기 바랍니다.</p>
                    </div>
                </div>
            </div>
            <footer style="width:calc(100% - 32px); margin:0 auto; padding:30px 0; border-top:1px solid #333; font-weight:400; line-height:1.2; text-align:center;">
                <h1 style="display:block; margin:0; padding:0; border:0; font-weight:400; line-height:1.2;">
                    <a href="https://www.bigglz.com/" target="_blank" style="display:block; width:52px; height:20px; margin:0; padding:0; border:0; background:url('https://d2w7ph9vouh9tr.cloudfront.net/Email/images/footer_logo.png') no-repeat 0 0/100%; font-weight:400; line-height:1.2; text-indent:-9999px;"></a>
                </h1>
                <div style="margin:0; padding:14px 0 6px; font-weight:400; line-height:1.2;">
                    <div style="margin:0; color:#333; font-family:'nexon', Dotum, sans-serif; font-size:11px; font-weight:400; line-height:1.2; letter-spacing:-1px;">
                        주식회사 
                        <span style="display:inline-block; width:1px; height:11px; margin:1px 5px; background:#333; font-weight:400; line-height:1.2; vertical-align:text-bottom;"></span>
                        비글즈 경기도 성남시 분당구 벌말로 50번길 41 투아이센터 5층 
                        <span style="display:inline-block; width:1px; height:11px; margin:1px 5px; background:#333; font-weight:400; line-height:1.2; vertical-align:text-bottom;"></span>
                        고객센터 070-7618-5339
                    </div>
                </div>
                <div style="display:block; margin:0; padding:0; color:#333; font-family:'nexon', Dotum, sans-serif; font-size:11px; font-weight:400; line-height:1.2;">Copyright ⓒ bigglz Corporation all rights reserved</div>
            </footer>
        </div>
    </div>
</body>

</html>
"""

# 각각의 데이터를 템플릿에 추가할 부분
data_template = """
<li>
    <div style='border: 1px solid #ccc;padding: 15px;width: 68%;margin: 20px;margin-left: auto;margin-right: auto;text-align: center;'>
        <div style='font-size: 12px;margin-bottom: 10px;text-align: left;'>
            {nickname}
        </div>
        <div style='font-size: 13px;text-align: left;margin-bottom: 10px;'>
            {message}
        </div>
        <div style='font-size: 10px;text-align: right;color: #666;'>
            {date}
        </div>
    </div>
</li>
"""
