import sys
import openai
from dotenv import load_dotenv
import os
from rich.console import Console

def main():

    load_dotenv()

    # Check if OPENAI_API_KEY is set in the environment
    if not os.getenv("OPENAI_API_KEY"):

        # Prompt user for OPENAI_API_KEY value
        openai_api_key = input("Please enter your OpenAI API key: ")

        # Write value to .env file
        env_file_path = os.path.join(os.path.dirname(__file__), ".env")
        with open(env_file_path, "w") as f:
            f.write(f"OPENAI_API_KEY={openai_api_key}")
        
        load_dotenv()

    openai.api_key = os.getenv("OPENAI_API_KEY")

    error_message = input("Please paste your error code here: ")

    console = Console()

    if sys.version_info < (3, 7):
        console.print("[bold red]Error:[/bold red] BUGE requires Python 3.7 or higher to run.")
        console.print("Please update to a newer version of Python.\n")
        console.print("[bold]Suggestions:[/bold]")
        console.print("- Install the latest version of Python 3 from the official Python website (https://www.python.org/downloads/).")
        console.print("- Use a Python version manager like pyenv to easily switch between multiple versions of Python.\n")
        sys.exit(1)

    def get_error_explanation(error_message):
        base_prompt = (f"Explain the following error code in simple terms: `{error_message}`")
        base_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=base_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        base_response_text = base_response.choices[0].text.strip()

        # second prompt
        secondary_prompt = (f"Suggest multiple possible causes for this error code:`{error_message}`")
        secondary_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=secondary_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        secondary_response_text = secondary_response.choices[0].text.strip()

        # third prompt
        third_prompt = (f"Suggest multiple possible solutions for the following error code:`{error_message}`")
        third_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=third_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        third_response_text = third_response.choices[0].text.strip()

        print('----------')
        print("")
        print("Meaning:")
        print(base_response_text)
        print("")
        print("Possible Causes:")
        print(secondary_response_text)
        print("")
        print("Possible Solutions:")
        print(third_response_text)
        print("")
        print('----------')

    get_error_explanation(error_message)

if __name__ == '__main__':
    main()