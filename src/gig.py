import re


class GigSearcher:

    def get_setlist_id(self,url):
        setlist_id_pattern = re.compile(".*\-([A-z0-9]+\.html$")
        is_setlist_url = setlist_id_pattern.match(url.strip())
        if is_setlist_url:
            return is_setlist_url.groups(0)
        return None
