import os


def create_env_file(discord_bot_token: str, sd_url: str) -> None:
    """
        creates a .env file in the current directory for sd_from_discord
    """
    with open('.env', 'w') as f:
        f.write(f'DISCORD_BOT_TOKEN={discord_bot_token}')
        f.write(f'STABLE_DIFFUTION_API_URL={sd_url}')


def file_exists() -> bool:
    """
        checks if .env file exists in the current directory
    """
    if '.env' in os.listdir():
        return True
    return False


def valid_keyinput(input: str) -> bool:
    """
        checks if the overwriting choice is valid
    """
    return input == 'Y' or input == 'n' or input == ''


def valid_token(token: str) -> bool:
    """
        checks if the token is valid
    """
    return len(token) == 59


def set_url(url: str) -> str:
    """
        sets the url to localhost:7860 if empty
    """
    return url if url else 'http://127.0.0.1:7860'


if __name__ == '__main__':
    if file_exists():
        choice = input(
            '''Looks like .env file already exists. \nDo you want to overwrite? (Y/n): '''
        )

    if not valid_keyinput(choice):
        raise ValueError('Inputs must be Y or n')

    if choice == 'n':
        print('Exiting...')
        exit()

    discord_bot_token = input('Enter your discord bot token: ')

    if not valid_token(discord_bot_token):
        raise ValueError('Invalid token. Token must be 59 characters long.')

    input_url = input('Enter the stable diffusion api url(if empty, localhost:7860 will be set): ')
    sd_url = set_url(input_url)

    create_env_file(discord_bot_token, sd_url)
