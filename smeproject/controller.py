import pickle
import pathlib

# [[4,1,0,0,1,1,0,0,1,0,0,1,1,0]]
def predict(data):
    # if size(data)==14 :
    print(data)
    p = pathlib.Path(__file__).parent.resolve()
    with open(p.joinpath('./model.pkl'), 'rb') as pickle_file:
        model = pickle.load(pickle_file)
    return model.predict(data)
    # else:
        # return -1