from pydantic import BaseSettings

class Settings(BaseSettings):
    redis_url:str ="redis://redis"
    whatever:str =" what?"
    
    class Config:
        env_file = '.env'
        env_file_encoding = "utf-8"
    
print(Settings().dict())