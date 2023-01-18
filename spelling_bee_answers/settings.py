from pydantic import BaseSettings


class Settings(BaseSettings):

    repo_root: str

    log_level: str = "INFO"

    display_puzzle_output: bool = True

    display_generated_readme_output: bool = False

    display_generated_readme_table: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
