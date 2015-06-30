import pickle

def write_file(filename, doc, type):
    #open a file
    fo = open(filename,type)
    pickle.dump(doc, fo)
    # Close opend file
    fo.close()

def read_file_header(filename, type):

     # Open a file
    fo = open(filename, type)
    doc = pickle.load(fo)

    # Close opend file
    fo.close()

    return doc

def read_file(filename, type):

    loaded_objects = []

     # Open a file
    with open(filename, type) as fo:
     for _ in range(pickle.load(fo)):
        loaded_objects.append(pickle.load(fo))

    # Close opend file
    fo.close()

    return loaded_objects