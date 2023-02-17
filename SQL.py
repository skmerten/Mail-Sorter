
def get_folders(cur):
    sql = '''SELECT * FROM folder'''
    cur.execute(sql)
    return cur.fetchall()

# return dictionary like this:
# dict = {
#   folder: (word list)
#   folder2: (word list2)
# }

def get_words(cur):
    sql = '''SELECT * FROM words'''
    cur.execute(sql)
    words = cur.fetchall()

    word_dict = {}

    for word in words:
        if word[1] not in word_dict.keys():
            word_dict[word[1]] = [word[0]]
        else:
            word_dict[word[1]].append(word[0])

    # translate to folder name
    folders = get_folders(cur)
    word_dict2 = {}
    for folderID in word_dict:
        for folder in folders:
            if folderID == folder[0]:
                word_dict2[folder[1]] = word_dict[folderID]
    return word_dict2
