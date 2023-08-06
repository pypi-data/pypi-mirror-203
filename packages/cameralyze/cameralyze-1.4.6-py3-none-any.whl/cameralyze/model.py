import requests
import filetype

from typing import Union, Any
from uuid import uuid4


class Connect:
    def __init__(self, api_key: str = None):
        self.model = None
        self.endpoint = None
        self.background_job = None
        self.flow = None
        self.beautify = False
        self.get_response = True
        self.base_domain = "https://api.server.cameralyze.co"
        self.test_temporary_image_domain = "https://tmp.cameralyze.co"
        self.upload_url = "https://platform.api.cameralyze.com/temporary-file/generate"
        self.platform_url = "https://platform.cameralyze.co"
        self.api_key = api_key
        self.configuration = None
        
    def beautify_response(self):
        self.beautify = True
        
        return self
        
    def open_response(self):
        self.get_response = True
        
        return self
        
    def close_response(self):
        self.get_response = False
        
        return self
        
    def set_api_key(self, api_key: str):
        self.api_key = api_key
        
        return self
        
    def set_model(self, model: str):
        """
        Args:
            model (str): Model UUID or model alias name
        """
        self.model = model
        
        return self
        
    def set_flow(self, flow: str):
        """
        Args:
            flow (str): Flow UUID or flow alias name
        """
        self.flow = flow
        
        return self
        
    def __get_presigned_upload_url(self, file_type: str, file_name: str) -> str:
        return requests.post(self.upload_url, json={"fileType": file_type, "fileName": file_name}).json()["data"]        

    def read_file(self, path: str) -> str:
        file_type = filetype.guess(path).mime
        file_name = str(uuid4())
        file = "{file_name}.{file_extension}".format(file_name=file_name, file_extension=path.split(".")[-1])

        self.__upload_file(path=path, file_type=file_type, file_name=file)

        return "{test_temporary_image_domain}/{file}".format(
            test_temporary_image_domain=self.test_temporary_image_domain, 
            file=file
        )

    def __upload_file(self, path: str, file_type: str, file_name: str):
        with open(path, 'rb') as local_file:
            local_file_body = local_file.read()

        requests.put(
            self.__get_presigned_upload_url(file_type=file_type, file_name=file_name), 
            data=local_file_body, 
            headers={'Content-Type': file_type, 'x-amz-acl': 'public-read'}
        )

    def __get_json(self, image: Union[str, tuple] = None, text:str = None, **kwargs: Any) -> dict:
        json={"apiKey": self.api_key, "rawResponse": not self.beautify, "getResponse": self.get_response, "input": kwargs}

        if image != None:
            if isinstance(image, tuple):
                json["fileId"] = image[0]
                json["fileType"] = image[1]
            elif image.startswith("http"):
                json["url"] = image
            elif image != None:
                json["image"] = image
            
        if text != None:
            json["text"] = text
            
        if self.endpoint:
            json["applicationUuid"] = self.endpoint
        
        if self.background_job:
            json["applicationUuid"] = self.background_job
        
        if self.configuration != None:
            json["configuration"] = self.configuration

        return json
    
    def __get_path(self) -> str:
        if self.flow:
            return "flow"
        
        return "model"
    
    def __get_unique_id(self) -> str:
        if self.flow:
            return self.flow
        
        return self.model

    def predict(self, image: Union[str, tuple] = None, text: str = None, **kwargs: Any) -> dict:
        api_call = requests.post(
            "{base_domain}/{path}/{unique_id}".format(base_domain=self.base_domain, path=self.__get_path(), unique_id=self.__get_unique_id()),
            json=self.__get_json(image=image, text=text, **kwargs)
        )

        return api_call.json() 

    def show_configuration(self):
        print(
            "You can see configuration in here:\n{platform_url}/model-detail/{model}".format(
                platform_url=self.platform_url,
                model=self.model
            )
        )
    
    def set_configuration(self, configuration: dict):
        self.configuration = configuration

        return self
