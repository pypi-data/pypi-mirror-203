from http.cookiejar import DefaultCookiePolicy


class AdBlockPolicy(DefaultCookiePolicy):
    def set_ok(self, cookie, request):
        return cookie.name != "ad_session_id"
