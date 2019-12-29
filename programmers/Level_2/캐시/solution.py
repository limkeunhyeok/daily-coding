def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = []
    cities = [s.lower() for s in cities]
    count = 0
    
    for city in cities:
        if city in cache:
            count += 1
            cache.remove(city)
            cache.append(city)
            continue
        else:
            count += 5
            if len(cache) == cacheSize:
                cache.remove(cache[0])
                cache.append(city)
            else:
                cache.append(city)
    return count