import pytest


# method to make dummy zone data
# entrey obj
def template_entry(url):
    template = {
        "$origin": f"{url}.",
        "$ttl": 3600,
        "soa": {
            "mname": "ns1.{url}.",
            "rname": "admin.{url}.",
            "serial": "{time}",
            "refresh": 3600,
            "retry": 600,
            "expire": 604800,
            "minimum": 86400,
        },
        "ns": [{"host": "ns1.{url}."}, {"host": "ns2.{url}."}],
        "a": [
            {"name": "@", "ttl": 400, "value": "255.255.255.255"},
            {"name": "@", "ttl": 400, "value": "127.0.0.1"},
            {"name": "@", "ttl": 400, "value": "127.0.0.1"},
            {"name": "@", "ttl": 400, "value": "127.0.0.1"},
            {"name": "@", "ttl": 400, "value": "10.10.10.10"},
        ],
    }
    return template

    def dig_request():
        return b"\xdd\xfa\x01 \x00\x01\x00\x00\x00\x00\x00\x01\tsomething\x03org\x00\x00\x01\x00\x01\x00\x00)\x10\x00\x00\x00\x00\x00\x00\x0c\x00\n\x00\x08\xd3\xfe+\x0c\x8e\xf8\xdeQ"

    def random_string(length):
        pool: str = string.ascii_letter

    @pytest.fixture(scope="module")
    def search_target(stack_size, needle):
        hay_stack = set()

        hay_stack.append(template(needle))
        while len(hay_stack) < stack_size:
            url = "".join(random.choice(pool) for i in range(20))
            hay_stack.add(template(url + ".com"))

        return (hay_stack, needle)
