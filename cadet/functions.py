def getObjKeyList(obj):
    keys = []
    for field in obj._meta.fields:
        keys.append(field.name.split('.')[-1])
    return keys

def getJSObjectsFromQSet(set, objClass, withRelated=False):
    objAttrs = getObjKeyList(objClass)
    json = []
    for obj in set:
        item = {}
        for attr in objAttrs:
            val = getattr(obj, attr)
            #if withRelated | type(val).__name__.find('model') == -1:
            item[attr] = val
        json.append(item)
    return json
