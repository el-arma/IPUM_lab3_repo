import os
import yaml
import subprocess
from pydantic_settings import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_secrets()

    @validator("ENVIRONMENT")
    def validate_environment(cls, value):
        allowed = {"dev", "test", "prod"}
        if value not in allowed:
            raise ValueError(
                f"ENVIRONMENT must be one of {allowed}, got '{value}' instead."
            )
        return value

    def load_secrets(self, file_path: str = "secrets.yaml") -> None:
        """Decrypt a SOPS-encrypted YAML file and load its contents into environment variables."""

        try:
            decrypted = subprocess.run(
                f"sops --decrypt {file_path}", capture_output=True
            )
            decrypted_yaml = decrypted.stdout

            # Set each key-value pair as an environment variable:
            for key, value in yaml.safe_load(decrypted_yaml).items():
                os.environ[key] = str(value)

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to decrypt secrets file: {e}")

        return None
