from .constraints import *

def classify(msg):
    splited_phrase = msg.lower().split()
    
    positive = [word for word in splited_phrase if word in positive_avaliation]
    negative = [word for word in splited_phrase if word in negative_avaliation]
    inapropriate = [word for word in splited_phrase if word in innapropriate_avaliation]

    if positive and negative:
        with open(f"avaliaçoes_negativas.txt", 'a') as f:
            f.write(msg + '\n')
        return True
    
    elif positive:
        with open(f"avaliaçoes_positivas.txt", 'a') as f:
            f.write(msg + '\n')
        return True
    
    elif negative:
        with open(f"avaliaçoes_negativas.txt", 'a') as f:
            f.write(msg + '\n')
        return True
    
    elif inapropriate:
        with open(f"avaliaçoes_impróprias.txt", 'a') as f:
            f.write(msg + '\n')
        return True
    
    else:
        return False