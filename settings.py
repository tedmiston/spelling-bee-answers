from pydantic import BaseSettings


class Settings(BaseSettings):

    display_puzzle_output = True

    display_generated_readme_output: bool = False

    display_generated_readme_table: bool = True


settings = Settings()
