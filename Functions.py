import re
# Find Hashtags or any string start with #
def get_find_hashtags(text):
    hashtags = re.findall(r"(#)((?:[\w][\.]{0,1})*[\w]){1,29}", text)
    hashtags = ' '.join(map(lambda x: str(x[0]) + '' + str(x[1]),hashtags))
    return hashtags

def removeDuplicate(list):
    return list(dict.fromkeys(list))