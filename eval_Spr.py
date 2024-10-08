import yaml
from math import pi

def load_diameters():
    with open('config.yaml') as f:
        data = yaml.safe_load(f)
    data = data["diameters"]
    return [data[f"D{i}"]*10**(-3) for i in range(1, 5)]

def get_Sn():
    return [pi * di**2 / 4 for di in load_diameters()]

def eval_Spr():
    S1, S2, S3, S4 = get_Sn()
    return S2 * (
        (1 + (S4 - S3) / (S2 - S1) + (S3 - S2) / S2) / 
        (1 + (S4 - S3) / (S2 - S1))
    )



def main():
    print(eval_Spr())


if __name__ == '__main__':
    main()

