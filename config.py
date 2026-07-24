from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    secret_key: SecretStr
    algorithim : str  = "HS256"
    access_token_expire_miniutes : int = 30

    max_upload_size_bytes: int = 5 *1024 *1024

    reset_token_expires_minutes: int = 60

    mail_server: str ="localhost"
    mail_port: int =587
    mail_username : str =""
    mail_password : SecretStr = SecretStr("")
    mail_from : str = "noreplyexample.com"
    mail_use_tls: bool =True
    frontend_url: str = "http://localhost:8000"

    
settings= Settings()
 