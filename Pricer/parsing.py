#scraper
import json

import requests


def get_data():

    cookies = {
        '__lhash_': '7520e1ac529da22a77658f52d3667ec5',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'MAIN_PAGE_VARIATION_1': '2',
        'MVID_2_exp_in_1': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CATALOG_STATE': '1',
#If you need to change MVID_CITY_ID, look at mvideo.com params\network\seo?categoryid...\body\cities\data
        'MVID_CITY_ID': 'CityCZ_2246',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20912963097',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '5400000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '2',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_MENU_BUTTON': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '29',
        'MVID_REGION_SHOP': 'S955',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'old',
        'MVID_TIMEZONE_OFFSET': '7',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'bIPs': '1949759381',
        'flacktory': 'no',
        'searchType2': '1',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        'admitad_uid': 'mvideo',
        'utm_term': 'mvideo',
        '__SourceTracker': 'yandex__cpc',
        'admitad_deduplication_cookie': 'yandex__cpc',
        '__sourceid': 'yandex',
        '__cpatrack': 'yandex_cpc',
        '__allsource': 'yandex',
        'SMSError': '',
        'authError': '',
        'partnerSrc': 'yandex',
        '_gid': 'GA1.2.766930626.1655706975',
        '_ym_uid': '1655706976309338047',
        '_ym_d': '1655706976',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '0f735a50-6369-4bfa-a1a1-0d3e0f0c923e',
        'advcake_track_id': '04acd028-7430-0eb8-8c47-6c5d9a57ad8b',
        'advcake_session_id': '579db073-b65e-5509-8a4a-a235b67c5543',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Novosibirsk_Image_Name_Pure_search_desktop%26utm_content%3Dpid%7C21914422520_%7Ccid%7C54501841%7Cgid%7C4285491799%7Caid%7C9547806981%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C65%7Cregion_name%7C%25D0%259D%25D0%25BE%25D0%25B2%25D0%25BE%25D1%2581%25D0%25B8%25D0%25B1%25D0%25B8%25D1%2580%25D1%2581%25D0%25BA%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3Dmvideo%26reff%3Dyandex_cpc_ipr_Novosibirsk_Image_Name_Pure_Search%26etext%3D2202.9AnZ16GbVwWk9tYXerff-25pYWhoampydHlpcmR6bWc.9efec5051df293566499aede6be7d25cb30844bb%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTg0MTs5NTQ3ODA2OTgxO3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D3426265524895277955',
        'advcake_utm_partner': 'ipr_Novosibirsk_Image_Name_Pure_search_desktop',
        'advcake_utm_webmaster': 'pid%7C21914422520_%7Ccid%7C54501841%7Cgid%7C4285491799%7Caid%7C9547806981%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C65%7Cregion_name%7C%25D0%259D%25D0%25BE%25D0%25B2%25D0%25BE%25D1%2581%25D0%25B8%25D0%25B1%25D0%25B8%25D1%2580%25D1%2581%25D0%25BA%7Ccoef_goal%7C0%7Cdesktop',
        'advcake_click_id': '',
        'tmr_lvid': '9c42f76a36a36c0abcb661671df5307b',
        'tmr_lvidTS': '1655706976402',
        'st_uid': '6e8d62e55f940c101a8a1ff5b267a4ea',
        'afUserId': 'fdc87fdc-b099-48a1-a462-940bba92986f-p',
        '_ym_isad': '2',
        'AF_SYNC': '1655706981069',
        'flocktory-uuid': 'd5e8e445-dcb1-44af-967f-72b22c6dfc1c-5',
        'BIGipServeratg-ps-prod_tcp80': '2416237578.20480.0000',
        'adrdel': '1',
        'adrcid': 'AiWOCGGW5DiI-znxgIeJUxw',
        'uxs_uid': '4fc1c410-f063-11ec-a9df-0f09ad035113',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '2416237578.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        'cfidsgib-w-mvideo': 'Yidqb/3iXOoH6WD1l/JhMBFtW33XsbGOB6yxg5vZO3YxQh12Ui+ouDE9wNHsqicpERiZDt5gDwg0juMh0OmPtBI+iTz8REciz66E9wG23PAOeCtH3thPRozonQyOD3EeCuLJZl0ZOQZ9DV4NTNpOgx5CKLskjWUn+Oa/vQ==',
        'cfidsgib-w-mvideo': 'Yidqb/3iXOoH6WD1l/JhMBFtW33XsbGOB6yxg5vZO3YxQh12Ui+ouDE9wNHsqicpERiZDt5gDwg0juMh0OmPtBI+iTz8REciz66E9wG23PAOeCtH3thPRozonQyOD3EeCuLJZl0ZOQZ9DV4NTNpOgx5CKLskjWUn+Oa/vQ==',
        'gsscgib-w-mvideo': 'j7Da8yz4WGTDarxZwYb49DYHEYJhmbr33H1TU5fPx2uSLDc97GxNRzEQJlC96Sr+frn9tYfhtdIWLHFn9BlsqM4bGuw3Gd9sy6CxBPbjp5by9OTXuVgsn3jCg/1sDzdcc1GspLPYyMQ00CsE0gOhaDvTKBzeoEhyesiIuW+xDzrfmYFWcg/aplLPSGleQsM6I4Zrgsd8xn8b3bbUN9Y3JM4U/KURe8jGCy24mJ1uiVIsB5Trh/S4f51S7thVf0g=',
        'gsscgib-w-mvideo': 'j7Da8yz4WGTDarxZwYb49DYHEYJhmbr33H1TU5fPx2uSLDc97GxNRzEQJlC96Sr+frn9tYfhtdIWLHFn9BlsqM4bGuw3Gd9sy6CxBPbjp5by9OTXuVgsn3jCg/1sDzdcc1GspLPYyMQ00CsE0gOhaDvTKBzeoEhyesiIuW+xDzrfmYFWcg/aplLPSGleQsM6I4Zrgsd8xn8b3bbUN9Y3JM4U/KURe8jGCy24mJ1uiVIsB5Trh/S4f51S7thVf0g=',
        'cfidsgib-w-mvideo': 'KxO8p2oMZWqzfpXz/snHaZuD+DqNygcKGewOFMD9fYZjTnAnp613mmlBOQFUJH/VDZtqzyUsaOjTSH7LRoP8wo5c0b7oY4dtvhA1HMCGJsABn1ZnEIplzTA7R8gQQolRvnYg/1h54ewZNE5I9Vh8bpeC2afZI6Wvxs2T8g==',
        'mindboxDeviceUUID': '018a677a-285a-40e3-9cdf-f565ed298022',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22018a677a-285a-40e3-9cdf-f565ed298022%22%7D',
        '_ga': 'GA1.2.60321221.1655706975',
        'tmr_detect': '0%7C1655709784097',
        'tmr_reqNum': '44',
        '_ga_CFMZTSS5FM': 'GS1.1.1655706975.1.1.1655710462.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1655706975.1.1.1655710462.60',
        'MVID_GEOLOCATION_NEEDED': 'false',
        'JSESSIONID': 'VZSxvwzZr2qrd9Jqlh7twvvr6XVhv1Tyq0XbtQmyMyvfcnQ88820!-743647156',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VPZRBlLRYrSQ1XFkNZIitAL1tWS1IpCwtzI09zMx4LGCIfaw8ZImJiLkg5WQpFLGNFSW9zGjhsIWJNXSZEWlNqJh8WfHIkUw8LZEVGb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5CZiFnSFwjQ1xJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=6eJcww==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VPZRBlLRYrSQ1XFkNZIitAL1tWS1IpCwtzI09zMx4LGCIfaw8ZImJiLkg5WQpFLGNFSW9zGjhsIWJNXSZEWlNqJh8WfHIkUw8LZEVGb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5CZiFnSFwjQ1xJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=6eJcww==',
        'CACHE_INDICATOR': 'false',
        'fgsscgib-w-mvideo': 'h0ZV612a8c1c6075cc34a7a1b3e234b08cdb6833',
        'fgsscgib-w-mvideo': 'h0ZV612a8c1c6075cc34a7a1b3e234b08cdb6833',
        'MVID_ENVCLOUD': 'primary',
        'ADRUM_BT': 'R:91|g:e34bdc4b-e611-41b4-abee-867e6a380442195564',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=7520e1ac529da22a77658f52d3667ec5; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MAIN_PAGE_VARIATION_1=2; MVID_2_exp_in_1=2; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_2246; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20912963097; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=5400000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=2; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=29; MVID_REGION_SHOP=S955; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=old; MVID_TIMEZONE_OFFSET=7; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; bIPs=1949759381; flacktory=no; searchType2=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; admitad_uid=mvideo; utm_term=mvideo; __SourceTracker=yandex__cpc; admitad_deduplication_cookie=yandex__cpc; __sourceid=yandex; __cpatrack=yandex_cpc; __allsource=yandex; SMSError=; authError=; partnerSrc=yandex; _gid=GA1.2.766930626.1655706975; _ym_uid=1655706976309338047; _ym_d=1655706976; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=0f735a50-6369-4bfa-a1a1-0d3e0f0c923e; advcake_track_id=04acd028-7430-0eb8-8c47-6c5d9a57ad8b; advcake_session_id=579db073-b65e-5509-8a4a-a235b67c5543; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Novosibirsk_Image_Name_Pure_search_desktop%26utm_content%3Dpid%7C21914422520_%7Ccid%7C54501841%7Cgid%7C4285491799%7Caid%7C9547806981%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C65%7Cregion_name%7C%25D0%259D%25D0%25BE%25D0%25B2%25D0%25BE%25D1%2581%25D0%25B8%25D0%25B1%25D0%25B8%25D1%2580%25D1%2581%25D0%25BA%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3Dmvideo%26reff%3Dyandex_cpc_ipr_Novosibirsk_Image_Name_Pure_Search%26etext%3D2202.9AnZ16GbVwWk9tYXerff-25pYWhoampydHlpcmR6bWc.9efec5051df293566499aede6be7d25cb30844bb%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTg0MTs5NTQ3ODA2OTgxO3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D3426265524895277955; advcake_utm_partner=ipr_Novosibirsk_Image_Name_Pure_search_desktop; advcake_utm_webmaster=pid%7C21914422520_%7Ccid%7C54501841%7Cgid%7C4285491799%7Caid%7C9547806981%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C65%7Cregion_name%7C%25D0%259D%25D0%25BE%25D0%25B2%25D0%25BE%25D1%2581%25D0%25B8%25D0%25B1%25D0%25B8%25D1%2580%25D1%2581%25D0%25BA%7Ccoef_goal%7C0%7Cdesktop; advcake_click_id=; tmr_lvid=9c42f76a36a36c0abcb661671df5307b; tmr_lvidTS=1655706976402; st_uid=6e8d62e55f940c101a8a1ff5b267a4ea; afUserId=fdc87fdc-b099-48a1-a462-940bba92986f-p; _ym_isad=2; AF_SYNC=1655706981069; flocktory-uuid=d5e8e445-dcb1-44af-967f-72b22c6dfc1c-5; BIGipServeratg-ps-prod_tcp80=2416237578.20480.0000; adrdel=1; adrcid=AiWOCGGW5DiI-znxgIeJUxw; uxs_uid=4fc1c410-f063-11ec-a9df-0f09ad035113; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=2416237578.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; cfidsgib-w-mvideo=Yidqb/3iXOoH6WD1l/JhMBFtW33XsbGOB6yxg5vZO3YxQh12Ui+ouDE9wNHsqicpERiZDt5gDwg0juMh0OmPtBI+iTz8REciz66E9wG23PAOeCtH3thPRozonQyOD3EeCuLJZl0ZOQZ9DV4NTNpOgx5CKLskjWUn+Oa/vQ==; cfidsgib-w-mvideo=Yidqb/3iXOoH6WD1l/JhMBFtW33XsbGOB6yxg5vZO3YxQh12Ui+ouDE9wNHsqicpERiZDt5gDwg0juMh0OmPtBI+iTz8REciz66E9wG23PAOeCtH3thPRozonQyOD3EeCuLJZl0ZOQZ9DV4NTNpOgx5CKLskjWUn+Oa/vQ==; gsscgib-w-mvideo=j7Da8yz4WGTDarxZwYb49DYHEYJhmbr33H1TU5fPx2uSLDc97GxNRzEQJlC96Sr+frn9tYfhtdIWLHFn9BlsqM4bGuw3Gd9sy6CxBPbjp5by9OTXuVgsn3jCg/1sDzdcc1GspLPYyMQ00CsE0gOhaDvTKBzeoEhyesiIuW+xDzrfmYFWcg/aplLPSGleQsM6I4Zrgsd8xn8b3bbUN9Y3JM4U/KURe8jGCy24mJ1uiVIsB5Trh/S4f51S7thVf0g=; gsscgib-w-mvideo=j7Da8yz4WGTDarxZwYb49DYHEYJhmbr33H1TU5fPx2uSLDc97GxNRzEQJlC96Sr+frn9tYfhtdIWLHFn9BlsqM4bGuw3Gd9sy6CxBPbjp5by9OTXuVgsn3jCg/1sDzdcc1GspLPYyMQ00CsE0gOhaDvTKBzeoEhyesiIuW+xDzrfmYFWcg/aplLPSGleQsM6I4Zrgsd8xn8b3bbUN9Y3JM4U/KURe8jGCy24mJ1uiVIsB5Trh/S4f51S7thVf0g=; cfidsgib-w-mvideo=KxO8p2oMZWqzfpXz/snHaZuD+DqNygcKGewOFMD9fYZjTnAnp613mmlBOQFUJH/VDZtqzyUsaOjTSH7LRoP8wo5c0b7oY4dtvhA1HMCGJsABn1ZnEIplzTA7R8gQQolRvnYg/1h54ewZNE5I9Vh8bpeC2afZI6Wvxs2T8g==; mindboxDeviceUUID=018a677a-285a-40e3-9cdf-f565ed298022; directCrm-session=%7B%22deviceGuid%22%3A%22018a677a-285a-40e3-9cdf-f565ed298022%22%7D; _ga=GA1.2.60321221.1655706975; tmr_detect=0%7C1655709784097; tmr_reqNum=44; _ga_CFMZTSS5FM=GS1.1.1655706975.1.1.1655710462.0; _ga_BNX5WPP3YK=GS1.1.1655706975.1.1.1655710462.60; MVID_GEOLOCATION_NEEDED=false; JSESSIONID=VZSxvwzZr2qrd9Jqlh7twvvr6XVhv1Tyq0XbtQmyMyvfcnQ88820!-743647156; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VPZRBlLRYrSQ1XFkNZIitAL1tWS1IpCwtzI09zMx4LGCIfaw8ZImJiLkg5WQpFLGNFSW9zGjhsIWJNXSZEWlNqJh8WfHIkUw8LZEVGb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5CZiFnSFwjQ1xJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=6eJcww==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VPZRBlLRYrSQ1XFkNZIitAL1tWS1IpCwtzI09zMx4LGCIfaw8ZImJiLkg5WQpFLGNFSW9zGjhsIWJNXSZEWlNqJh8WfHIkUw8LZEVGb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5CZiFnSFwjQ1xJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=6eJcww==; CACHE_INDICATOR=false; fgsscgib-w-mvideo=h0ZV612a8c1c6075cc34a7a1b3e234b08cdb6833; fgsscgib-w-mvideo=h0ZV612a8c1c6075cc34a7a1b3e234b08cdb6833; MVID_ENVCLOUD=primary; ADRUM_BT=R:91|g:e34bdc4b-e611-41b4-abee-867e6a380442195564',
        'referer': 'https://www.mvideo.ru/komputernye-komplektuushhie-5427/videokarty-5429/f/collection_top=rtx',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Opera";v="87"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45 (Edition Yx 05)',
        'x-set-application-id': 'aa13f214-92da-4beb-81bb-b7ca50256825',
    }

    params = {

        'categoryId': '5429',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJjb2xsZWN0aW9uX3RvcCIsIiIsInJ0eCJd',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    #print(response)

    products_ids = response.get('body').get('products')

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()
    print(response)
    with open('item.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

def main():
    get_data()

if __name__ == '__main__':
    main()

