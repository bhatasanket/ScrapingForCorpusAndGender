import urllib.request
import re
import GetNames
import json
import gender_guesser.detector as gender

data = []
name = ""
d = gender.Detector()


def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


def removeDateLine(txt):
    re1 = '.*?'  # Non-greedy match on filler
    re2 = '((?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3})))(?![\\d])'  # Year 1
    re3 = '.*?'  # Non-greedy match on filler
    re4 = ':'  # Uninteresting: c
    re5 = '.*?'  # Non-greedy match on filler
    re6 = '(:)'  # Any Single Character 1
    rg = re.compile(re1 + re2 + re3 + re4 + re5 + re6, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        return ''
    return txt


def removeBlockQuote(txt):
    re1 = '(<)'  # Any Single Character 1
    re2 = '((?:[a-z][a-z]+))'  # Word 1
    re3 = '(\\s+)'  # White Space 1
    re4 = '.*?'  # Non-greedy match on filler
    re5 = '(>)'  # Any Single Character 2
    re6 = '.*?'  # Non-greedy match on filler
    re7 = '(<)'  # Any Single Character 3
    re8 = '(\\/)'  # Any Single Character 4
    re9 = '(blockquote)'  # Word 2
    re10 = '(>)'  # Any Single Character 5
    rg = re.compile(re1 + re2 + re3 + re4 + re5 + re6 + re7 + re8 + re9 + re10, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        firsthalf = str(txt.split(r"<blockquote", 1)[0])
        lasthalf = str(txt.split(r"</blockquote>")[-1])
        return firsthalf + lasthalf
    return txt


def getPayload(html_page):
    sauce = urllib.request.urlopen(html_page).read()
    global name
    firstName, lastName = GetNames.getName(str(sauce))
    step = str(sauce).split("<!--X-Body-of-Message-->", 1)[1]
    step = removeBlockQuote(step)
    step1 = str(step.split(r"\n<br>\nEl", 1)[0])
    step2 = step1.replace(r"\n", "") \
        .replace(r"<br>\n<br>", "") \
        .replace(r"<br>", "\n") \
        .replace(r"&lt;", "<") \
        .replace(r"&gt;", ">").replace(r"\'", "'").replace(r"&quot;", '"')
    step2 = re.sub('(\\\\)' + '(x)' + '(.)' + '(.)', '', step2)  # remove all utf8 char
    lines = ""
    for line in step2.splitlines(True):
        if not line.strip().startswith(r'>'):
            line = removeDateLine(line)
            lines += remove_tags(line)
    lines = lines.replace('\n', ' ').split("-- ", 1)[0]
    return firstName, lastName, gender, lines


if __name__ == '__main__':
    main_page = 'https://listarchives.libreoffice.org/global/documentation/'
    filename = 'ResultwithNameGender'
    # for msg in range(4961):
    for msg in range(0, 999):
        print("--------", msg, "----------")
        html_page = main_page + 'msg' + '{:05d}'.format(msg) + '.html'
        firstName, lastName, gender, lines = getPayload(html_page)
        data.append({'name': firstName + " " + lastName, 'gender': d.get_gender(firstName), 'text': lines})
    with open(filename + '1' + '.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    data.clear()

    for msg in range(1000, 1999):
        print("--------", msg, "----------")
        html_page = main_page + 'msg' + '{:05d}'.format(msg) + '.html'
        firstName, lastName, gender, lines = getPayload(html_page)
        data.append({'name': firstName + " " + lastName, 'gender': d.get_gender(firstName), 'text': lines})
    with open(filename + '2' + '.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    data.clear()

    for msg in range(2000, 2999):
        print("--------", msg, "----------")
        html_page = main_page + 'msg' + '{:05d}'.format(msg) + '.html'
        firstName, lastName, gender, lines = getPayload(html_page)
        data.append({'name': firstName + " " + lastName, 'gender': d.get_gender(firstName), 'text': lines})
    with open(filename + '3' + '.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    data.clear()

    for msg in range(3000, 3999):
        print("--------", msg, "----------")
        html_page = main_page + 'msg' + '{:05d}'.format(msg) + '.html'
        firstName, lastName, gender, lines = getPayload(html_page)
        data.append({'name': firstName + " " + lastName, 'gender': d.get_gender(firstName), 'text': lines})
    with open(filename + '4' + '.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    data.clear()

    for msg in range(4000, 4961):
        print("--------", msg, "----------")
        html_page = main_page + 'msg' + '{:05d}'.format(msg) + '.html'
        firstName, lastName, gender, lines = getPayload(html_page)
        data.append({'name': firstName + " " + lastName, 'gender': d.get_gender(firstName), 'text': lines})
    with open(filename + '5' + '.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    data.clear()
# for checking only one msg
# html_page = main_page + 'msg' + '04961' + '.html'
# getPayload(html_page)
# print(name)
#
