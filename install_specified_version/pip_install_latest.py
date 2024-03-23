import requests
from bs4 import BeautifulSoup

def get_install_commands(package_names):

    with open('requirements.txt', 'w', encoding='utf-8') as file:
        for package_name in package_names:

            html = requests.get(f"https://pypi.org/project/{package_name}/").text
            soup = BeautifulSoup(html, 'html.parser')

            h1_tag = soup.find('h1', class_='package-header__name')

            if h1_tag:
                file.write(h1_tag.text.strip().replace(" ", "==") + "\n")
            else:
                file.write(f"Package name {package_name} not found.\n")

if __name__ == "__main__":
    package_names = ["pandas", "numpy", "requests"]
    get_install_commands(package_names)
