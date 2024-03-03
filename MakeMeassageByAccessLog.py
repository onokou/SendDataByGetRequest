
import base64
from PIL import Image
from Base64Converter import Base64Converter


class MakeMessageByAccessLog:
    """アクセスログのパスと、ip,keyを入れると、ログのデータをかき集めて一つのデータにして返してくれるクラス"""
    def __init__(self):
        pass

    def main(self,message_type,output_file_path,access_log_path,ip,key):
        """
        massage_type:text,imageから選んでください。（csvもtextで大丈夫です）
        output_file_path:拡張子まで書いてください。
        access_log_file_path:apacheのアクセスログを想定しています。
        ip:送信元（webサーバへデータを送信するPC）のIPアドレス。
        key:送信する際に作成した、データを識別するためのkeyを入れてください。
        """
        base64_converter = Base64Converter()
        #アクセスログからメッセージ取得
        message = self.make_message_by_access_log(access_log_path,ip,key)

        #メッセージタイプによって、生成するファイル変更
        if message_type == "text":
            base64_converter.base64_to_text(message,output_file_path)
        if message_type == "image":
            base64_converter.base64_to_image(message,output_file_path)


    def make_message_by_access_log(self,access_log_path,ip,key):
        # テキストファイルを一行ずつ読み込んでリストに格納する
        with open(access_log_path, 'r') as file:
            logs = file.readlines()
        # リストの内容を表示してみる
        base64_data = ""
        for log in logs:
            log_data = log.split(" ")
            sender_ip = log_data[0]
            try:
                if sender_ip == ip:
                    data = log.split("/"+key+"/")[1]
                    base64_data += data
            except:
                pass
        return base64_data


#Usage
ins =MakeMessageByAccessLog()
access_log_file_path = "apache access log filepath"
output_file_path = ""
ip = "Source IP address"
key="test_key"  #key is set by SendMessageByGetRequest
ins.main("text",output_file_path,access_log_file_path,ip,key)
#ins.main("image","image_output_file_path.png",access_log_file_path,ip,"test_key_for_image")

