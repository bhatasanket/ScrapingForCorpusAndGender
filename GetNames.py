import re


def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


def getName(txt):
    re1 = '.*?'  # Non-greedy match on filler
    re2 = '()'  # Tag 1
    re3 = '(From)'  # Word 1
    re4 = '(<\\/em>)'  # Tag 2
    re5 = '(:)'  # Any Single Character 1
    re6 = '( )'  # White Space 1
    re7 = '.*?'  # Non-greedy match on filler
    re8 = '(<)'  # Any Single Character 2
    re9 = '(a)'  # Variable Name 1
    re10 = '.*?'  # Non-greedy match on filler
    re11 = '(href)'  # Word 2

    rg = re.compile(re1 + re2 + re3 + re4 + re5 + re6 + re7 + re8 + re9 + re10 + re11, re.IGNORECASE | re.DOTALL)
    #
    m = rg.search(txt)

    if m:
        txt = remove_tags(txt)
        index = txt.index("From:")
        txt = txt[index:index + 40]
        firstName = txt.split(" ")[1]
        firstName = firstName.replace("&quot;", "").replace("&lt;", "").replace("&gt;", "")
        lastName = txt.split(" ")[2]
        lastName = lastName.replace("&quot;", "").replace("&lt;", "").replace("&gt;", "")
        # print(txt)
        return firstName, lastName
    else:
        return "Not found"
