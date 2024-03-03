import base64
from PIL import Image

class Base64Converter:
    def __init__(self):
            pass
    #####################   Encoder  ######################
    def textfile_to_base64(self,textfile_path):
        """テキストファイルをBase64に変換する関数"""
        #ファイルからテキスト読み込み
        text = self._read_text_file(textfile_path)
        # テキストをバイト列にエンコードしてからBase64に変換
        encoded_bytes = base64.b64encode(text.encode('utf-8'))
        # Base64エンコードされたバイト列を文字列に変換
        encoded_text = encoded_bytes.decode('utf-8')
        return encoded_text

    def text_to_base64(self,text):
        """テキストをBase64に変換する関数"""
        # テキストをバイト列にエンコードしてからBase64に変換
        encoded_bytes = base64.b64encode(text.encode('utf-8'))
        # Base64エンコードされたバイト列を文字列に変換
        encoded_text = encoded_bytes.decode('utf-8')
        return encoded_text

    def _read_text_file(self,file_path):
        """テキストファイルを読み込み、内容を文字列として返す関数"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text_content = file.read()
            return text_content
        except FileNotFoundError:
            return f"Error: File not found - {file_path}"
        except Exception as e:
            return f"Error: {e}"


    def image_to_text(self,image_path):
        """画像ファイルをBase64にエンコードして文字列として返す関数"""
        try:
            with open(image_path, 'rb') as image_file:
                encoded_image = base64.b64encode(image_file.read())
            return encoded_image.decode('utf-8')
        except Exception as e:
            return f"Error: {e}"

    ######################   Decoder  #######################


    def base64_to_image(self,encoded_text, output_file_path):
        """Base64エンコードされた文字列をデコードして画像に保存する関数"""
        try:
            decoded_image = base64.b64decode(encoded_text)
            with open(output_file_path, 'wb') as output_file:
                output_file.write(decoded_image)
            print(f"Successfully saved the image to {output_file_path}")
        except Exception as e:
            print(f"Error: {e}")

    def base64_to_text(self,base64_string, output_file_path):
        """Base64エンコードされた文字列をデコードし、テキストファイルとして保存する関数"""
        try:
            # Base64デコードしてバイナリデータに変換
            decoded_bytes = base64.b64decode(base64_string)
            # バイナリデータを文字列に変換
            decoded_text = decoded_bytes.decode('utf-8')
            # テキストファイルに保存
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(decoded_text)
            print(f"Successfully saved the text to {output_file_path}")
        except Exception as e:
            print(f"Error: {e}")
