def cookie_deal():
    # 复制粘贴从浏览器登陆好的cookie
    cookie = '''
    first_visit_datetime_pc=2019-08-25+14%3A01%3A13; p_ab_id=9; p_ab_id_2=9; p_ab_d_id=1694137774; _ga=GA1.2.866933958.1566709288; c_type=21; a_type=0; b_type=0; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; yuid_b=FJM4ZYQ; login_ever=yes; privacy_policy_agreement=1; ki_r=; ki_s=199710%3A0.0.0.0.0; device_token=77d8391731d4ec28a0e5557daccf534e; _td=9fc539df-f6f3-4f3d-91b2-39289e882fd6; first_visit_datetime=2019-10-25+21%3A20%3A08; webp_available=1; cto_lwid=2e502312-403e-468e-82ab-a1cd0356e62e; OX_plg=pm; __utmc=235335808; limited_ads=%7B%22t_header%22%3A%22%22%2C%22t_footer%22%3A%22%22%2C%22responsive%22%3A%22%22%7D; categorized_tags=BU9SQkS-zU~EZQqoW9r8g~HLWLeyYOUF~IVwLyT8B6k~Ig5OcZugU6~K0rq4tmPAD~OEXgaiEbRa~b8b4-hqot7~kP7msdIeEU~mIFanJgKGQ~pvU1D1orJa~uG0wcfxlfN~y8GNntYHsi; p_b_type=2; _gid=GA1.2.1412704915.1574474714; login_bc=1; is_sensei_service_user=1; __utmz=235335808.1574580710.36.2.utmcsr=accounts.pixiv.net|utmccn=(referral)|utmcmd=referral|utmcct=/login; user_language=zh; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^6=user_id=43368280=1^9=p_ab_id=9=1^10=p_ab_id_2=9=1^11=lang=zh=1^20=webp_available=yes=1; tag_view_ranking=RTJMXD26Ak~kP7msdIeEU~Lt-oEicbBr~BU9SQkS-zU~OT4SuGenFI~pbqmgYwTBU~uusOs0ipBx~jhuUT0OJva~nQRrj5c6w_~y8GNntYHsi~ZXFMxANDG_~LJo91uBPz4~GmdMh9y_Yz~3mLXnunyNA~pa4LoD4xuT~KvAGITxIxH~EZQqoW9r8g~-98s6o2-Rp~NpsIVvS-GF~eVxus64GZU~RNN9CgGExV~2R7RYffVfj~8Le-BdaoRB~_iaP-J1xu4~3W4zqr4Xlx~gooMLQqB9a~9ODMAZ0ebV~K0rq4tmPAD~jH0uD88V6F~kGYw4gQ11Z~b4Y9BH1Uvf~uuDvas31_7~E4jq9C8BXA~ETjPkL0e6r~uG0wcfxlfN~qz6SsESFCr~i83OPEGrYw~NBK37t_oSE~-sp-9oh8uv~YaGonwdUdf~fg8EOt4owo~afM5Sp3Id1~w8XcfDlrBy~R3lr4__Kr8~2-ZLcTJsOe~Oa9b6mEc1T~JBFbzljAuI~hc6v46nm9F~xZ6jtQjaj9~1Xn1rApx2-~PwDMGzD6xn~cFYMvUloX0~_pwIgrV8TB~rYZfDSxU_2~mQVDvIYDNh~10UDTvA5ck~0xsDLqCEW6~inTd0S7PQX~mIFanJgKGQ~Ac_mADAVwx~hmdh8vZA4c~OV71ZK8lkv~Jzua5TXeUz~IwusmDZJk3~8xgPGBjUTg~NXxDJr1D_u~1LN8nwTqf_~EFThcDH3Eu~Pp-MGp6661~P7RASjZeLd~qJriAz4JX7~TtyNSRZ03f~YRDwjaiLZn~mFW848gK6h~7Y-OaPrqAv~ENFdTUvMv9~BMk-A0Hof7~6RcLf9BQ-w~BYbAF8suC-~caRNpu6o-9~d73AdVrO-6~R-EFi7fMtD~o7hvUrSGDN~_fMf86iA_3~zrgumzY7ph~8XX2eqWqNX~0IjmUoDdsx~CQrmDvf4c6~QwQ3wReUTs~XoXIjxuZvN~mf6rICH32i~F3i71J9-ai~W_bg4-89sF~43DoAn1Cyu~VihadKMfX9~3gt_hemo9s~ZKN-2Y85vy~h9r9YX0n2U~zamoiem15e~qNQ253s6b0; __utma=235335808.866933958.1566709288.1574587279.1574645262.38; __utmt=1; tags_sended=1; PHPSESSID=43368280_c5cece62686c83017cf10f40bc0841af; __utmb=235335808.5.9.1574645464175; ki_t=1566711057922%3B1574645274729%3B1574645481470%3B13%3B43
    '''

    cookieList = cookie.split(';')
    cookieDict = {}
    for cookie in cookieList:
        name = cookie.split('=', maxsplit=1)[0].strip()
        value = cookie.split('=', maxsplit=1)[1].strip()
        cookieDict[name] = value

    return cookieDict


if __name__ == '__main__':
    cookie_deal()