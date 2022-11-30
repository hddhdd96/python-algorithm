def solution(cacheSize, cities):
    answer = 0
    t = 0
    cache = []
    if cacheSize == 0:
        return 5 * len(cities)
    for i in cities:
        city = i.upper()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if t < cacheSize:
                cache.append(city)
                t+=1
            else:
                cache.pop(0)
                cache.append(city)
    return answer