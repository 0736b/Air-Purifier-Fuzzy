from fuzzy.mamdani import AirPurifier_Mamdani

if __name__ == "__main__":
    fis = AirPurifier_Mamdani(10.0,54.0)
    fis.run()
    print(fis.get_crisp_value())