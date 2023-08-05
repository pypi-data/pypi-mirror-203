from requests import Session as rSession
from bs4 import BeautifulSoup

from digiDownload.AdBlockCookiePolicy import AdBlockPolicy
from digiDownload.Book import Book
from urllib.parse import quote


class Session:
    def __init__(self, email, password, remember_login=False):
        self.client = rSession()
        self.client.cookies.set_policy(AdBlockPolicy())

        resp = self.client.post("https://digi4school.at/br/xhr/login",
                                headers={"Content-Type": "application/x-www-form-urlencoded"},
                                data=f"email={quote(email)}&password={quote(password)}&indefinite={int(remember_login)}")

        assert resp.status_code == 200 and resp.content == b"OK", f"Login failed. Are you sure you entered the correct credentials? {resp.status_code}: {resp.reason}"

    def get_books(self):
        resp = self.client.get("https://digi4school.at/ebooks")
        soup = BeautifulSoup(resp.text, "html.parser")

        return [Book(self.client, b) for b in soup.find("div", {"id": "shelf"})]

    def redeem_code(self, code):
        resp = self.client.post("https://digi4school.at/br/xhr/einloesen", headers={"Content-Type": "application/x-www-form-urlencoded"}, data=f"code={code}").json()

        if resp["err"] != 0: return resp["msg"].split(':')[1][1:]
