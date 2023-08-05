from bs4 import BeautifulSoup


class LTIForm:
    def __init__(self, content):
        soup = BeautifulSoup(content, "html.parser")

        assert soup.form["name"] == "ltiLaunchForm", "Not a lti launch form."

        self.url = soup.form["action"]
        self.method = soup.form["method"]
        self.content_type = soup.form["enctype"]

        self.data = {s['name']: s['value'] for s in soup.find_all("input")}

    def __getitem__(self, item):
        return self.data[item]

    def send(self, client):
        return client.request(self.method, self.url, headers={"Content-Type": self.content_type}, data=self.data)
