from pydantic import BaseSettings


class Settings(BaseSettings):

    # todo: migrate this to be a pathlib.Path
    repo_root: str

    log_level: str = "INFO"

    display_puzzle_output: bool = True

    display_generated_readme_output: bool = False

    display_generated_readme_table: bool = True

    output_dir: str = "outputs"
    output_file_days: str = "Days.md"
    output_file_pangrams: str = "Pangrams.md"
    output_file_words: str = "Words.md"

    class Config:
        env_file = ".env"


settings = Settings()
