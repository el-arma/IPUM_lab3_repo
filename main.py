import os
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    dotenv_file = f".env.{environment}"

    if not os.path.exists(dotenv_file):
        raise FileNotFoundError(
            f" .env file for environment '{environment}' not found: {dotenv_file}"
        )

    load_dotenv(dotenv_file)
    print(f" Loaded environment variables from {dotenv_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", os.environ["API_KEY"])
