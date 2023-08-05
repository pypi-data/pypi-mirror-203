from LTIParser import LTIForm
from threading import Thread
from time import sleep
from sys import maxsize


class Book:
    urls = {
        "https://a.digi4school.at": "https://a.digi4school.at/ebook/{book_id}/{page}.svg",
        "https://a.hpthek.at": "https://a.hpthek.at/ebook/{book_id}/{page}/{page}.svg"
    }

    def __init__(self, client, html_content):
        self.client = client

        self.publisher = html_content.find("span", {"class": "publisher"}).text
        self.title = html_content.find("h1").text
        self.cover = html_content.find("img")["src"]
        self.code = html_content["data-code"]
        self.id = html_content["data-id"]

        resp = LTIForm(self.client.get(f"https://digi4school.at/ebook/{self.code}").content)
        first_form = LTIForm(resp.send(self.client).content)
        second_form = first_form.send(self.client)

        self.url = '/'.join(second_form.url.split("/")[0:3])
        self.content_id = first_form["resource_link_id"]

    def _get_page(self, page):
        url = self.urls[self.url].format(book_id=self.content_id, page=page)
        resp = self.client.get(url, stream=True)

        return resp

    def _get_pages(self):
        for i in range(1, maxsize):
            resp = self._get_page(i)

            if resp.status_code == 404: break
            assert resp.status_code == 200, f"Page not found. Are you sure you entered the correct book id? ({self.id})"
            assert resp.headers["Content-Type"] == "image/svg+xml", f"Response is not of svg type. {resp.status_code}: {resp.reason}"

            yield resp

    def get_content(self):
        content = []
        remaining_threads = []

        for i, page in enumerate(self._get_pages()):
            remaining_threads.append(Thread(target=lambda idx, p: content.insert(idx, p.content), args=(i, page)))
            remaining_threads[-1].start()

            while len(remaining_threads) > 10:
                sleep(0.5)
                remaining_threads = [t for t in remaining_threads if t.is_alive()]

        for t in remaining_threads: t.join()

        return content
