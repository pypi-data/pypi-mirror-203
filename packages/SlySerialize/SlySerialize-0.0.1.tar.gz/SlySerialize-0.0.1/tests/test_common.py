from dataclasses import asdict, dataclass
from enum import Enum
from datetime import datetime
from typing import Generic, TypeVar
from SlySerialize import Loader, DesCtx, JsonType, from_json, COMMON_CONVERTER

def test_de_simple():
    for x in (None, 1, 2.5, "hi", True):
        assert x == from_json(type(x), x)

def test_de_list():
    x: list[JsonType] = [1, 2, 3]
    assert x == from_json(list[int], x)

def test_de_set():
    x = {1, 2, 3}
    assert x == from_json(set[int], list(x))

def test_de_tuple():
    x = (1, 2.5, "hi")
    assert x == from_json(tuple[int, float, str], list(x))

def test_de_dict():
    x: JsonType = {"a": 1, "b": 2, "c": 3}
    assert x == from_json(dict[str, int], x)

def test_de_enum():
    class Test(Enum):
        A = 1
        B = 2

    x = Test.A
    assert x == from_json(Test, x.value)

def test_de_union():
    x = 1
    assert x == from_json(int | str, x)

def test_de_dataclass():
    @dataclass
    class Test:
        a: int
        b: str
        c: JsonType

    x = Test(1, "hi", {'x': 1, 'y': {}, 'z': [None, 2.5]})
    assert x == from_json(Test, asdict(x))

T = TypeVar('T')
U = TypeVar('U')

ListSet = tuple[list[T], set[T]]

def test_de_generic_alias():
    x: ListSet[int] = ([1, 2, 2], {1, 2})
    assert x == from_json(ListSet[int], list(map(list, x)))

def test_de_generic_generic_arg():
    @dataclass
    class Test(Generic[T]):
        a: T
    x = Test[Test[int]](Test[int](1))
    assert x == from_json(Test[Test[int]], asdict(x))
    x = Test[list[int]]([1, 2, 3])
    assert x == from_json(Test[list[int]], asdict(x))

def test_de_delayed_generic():
    @dataclass
    class Test(Generic[T]):
        a: 'list[T]'
        b: 'T'
    x = Test[Test[int]]([Test[int]([1], 2)], Test[int]([3], 4))
    assert x == from_json(Test[Test[int]], asdict(x))
    x = Test[list[int]]([[1, 2, 3]], [])
    assert x == from_json(Test[list[int]], asdict(x))

def test_de_dataclass_generic():

    @dataclass
    class Test(Generic[T]):
        a: T
        b: list[T]
        c: dict[str, T]

    x = Test[int](1, [2, 3], {'x': 1, 'y': 2, 'z': 3})
    assert x == from_json(Test[int], asdict(x))

def test_de_datetime():
    x = datetime.now()
    assert x == from_json(datetime, x.isoformat())
    assert x == from_json(datetime, x.timestamp())

@dataclass
class SimpleDataclass:
    shortcode: str
    visible_in_picker: bool

@dataclass
class NestedDataclass:
    username: str
    locked: bool
    created_at: datetime
    emojis: list[SimpleDataclass]
    fields: list[SimpleDataclass]

class EnumExample(Enum):
    PUBLIC = "public"
    UNLISTED = "unlisted"
    PRIVATE = "private"
    DIRECT = "direct"

@dataclass
class NestedDataclassWithRecursiveDelayedAnnotation:
    id: str
    created_at: str
    account: NestedDataclass
    visibility: EnumExample
    sensitive: bool
    spoiler_text: str
    media_attachments: list[JsonType]
    application: JsonType|None
    mentions: list[JsonType]
    tags: list[JsonType]
    emojis: list[SimpleDataclass]
    reblogs_count: int
    favourites_count: int
    replies_count: int
    url: str|None
    in_reply_to_id: str|None
    in_reply_to_account_id: str|None
    reblog: 'DerivedDataclass|None'
    poll: JsonType|None
    card: JsonType|None
    language: str|None
    edited_at: str|None

@dataclass
class DerivedDataclass(NestedDataclassWithRecursiveDelayedAnnotation):
    content: str

def test_de_derived():

    x: JsonType = {
        'id': '109958407801025523', 
        'created_at': '2023-03-03T08:29:10.291Z',
        'in_reply_to_id': None, 'in_reply_to_account_id': None,
        'sensitive': False, 'spoiler_text': '', 'visibility': 'public',
        'language': 'en',
        'url': 'https://mastodon.skye.vg/@dunkyl/109958407801025523', 
        'replies_count': 0, 'reblogs_count': 0, 'favourites_count': 0, 
        'edited_at': None, 'content': '<p>test 4</p>', 'reblog': None, 
        'application': {
            'name': 'SlyMastodon Test', 
            'website': 'https://github.com/dunkyl/SlyMastodon'
        },
        'account': {
            'username': 'dunkyl', 'locked': False, 
            'created_at': '2022-11-05T00:00:00.000', 'emojis': [], 'fields': []
        }, 
        'media_attachments': [], 'mentions': [], 'tags': [], 'emojis': [], 
        'card': None, 'poll': None,
    }

    from_json(DerivedDataclass|None, x)


def test_custom_converter():

    class X:
        xx: int
        def __init__(self, x: int):
            self.xx = x
        def __eq__(self, other: object):
            return isinstance(other, X) and self.xx == other.xx

    class XLoader(Loader[JsonType]):

        def can_load(self, cls: type): return cls is X

        def des(self, ctx: DesCtx[JsonType], value: JsonType, cls: type[X]) -> X:
            if not isinstance(value, int):
                raise ValueError(f"expected int, got {value!r}")
            return X(value)

    loader = COMMON_CONVERTER.with_(XLoader())

    x = [X(1)]

    x_de = from_json(list[X], [1], loader=loader)

    assert x == x_de

def test_union_of_classes():

    @dataclass
    class A:
        aa: int
        bb: int

    @dataclass
    class B: bb: int

    b = from_json(A | B, {'bb': 1}, allow_extra_keys=True)

    assert isinstance(b, B)