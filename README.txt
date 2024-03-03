-----------------------------------------------
 　悪用厳禁です！！！！               
 　社内セキュリティを高める目的のみに使用してください。
-----------------------------------------------


【概要】
    ・http GETリクエストを使用し、データをwebサーバへ送信するパッケージ

    ・以下のデータを送信できる
        ・テキスト
        ・テキストファイル
        ・csvファイル
        ・画像ファイル

    ・基本以下の2つのみ使用する
        ・SendMassageByGetRequestのmain関数(ファイルをbase64にエンコードして、webサーバへGETリクエストする)
        ・MakeMeassageByAccessLogのmain関数(webサーバのaccess.logから、ファイルを復元する)

【クラス】
    ・SendMassageByGetRequest.py
        ・base64にエンコードしたstr型のテキストや画像、csvファイルを送信するクラス
        ・mainクラスに適切な引数を与えると、str型のdataをURIに含め、webサーバへGETリクエストを送る

    ・MakeMeassageByAccessLog.py
        ・Apacheのアクセスログから、GETリクエストを使用して送信されたdataをかき集め、本来のデータに戻すクラス
        ・mainクラスに適切な引数を与えると、accessログからデータを復元する

    ・Base64Converter.py
        ・テキストや画像ファイルをbase64にエンコードしたり、デコードしたりするクラス



----------------------------------------------------------------------------

-------------------------------------------
　　Abuse is prohibited!!!!
　　Use only to improve internal security. 
-------------------------------------------

【Overview】
    ・A package for sending data to a web server using HTTP GET requests.
    ・Can send the following types of data:
        ・Text
        ・Text files
        ・CSV files
        ・Image files

    ・Primarily utilizes the following two functions:
        ・main function in SendMassageByGetRequest (Encodes files to base64 and sends a GET request to the web server)
        ・main function in MakeMeassageByAccessLog (Restores files from the web server's access.log)

【Classes】
    ・SendMassageByGetRequest.py
        A class for sending base64-encoded strings of text, images, or CSV files via HTTP GET requests.
        When appropriate arguments are provided to the main method, it includes the string data in the URI and sends a GET request to the web server.

    ・MakeMeassageByAccessLog.py
        A class that gathers data sent via GET requests from Apache access logs and restores the original data.
        When appropriate arguments are provided to the main method, it restores data from the access log.

    ・Base64Converter.py
        A class for encoding or decoding text and image files to/from base64.

