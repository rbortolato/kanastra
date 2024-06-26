from app.entities.cache import Cache

def test_cache_exists():
    cache = Cache()
    cache.add('123')
    assert cache.exists('123')

def test_cache_not_exists():
    cache = Cache()
    assert not cache.exists('1234')
