import Lib.Helper


class ScriptGenerator:
    def __init__(self):
        pass

    @staticmethod
    def make_data(filename):
        csv_rows = Lib.Helper.read_from_csv_as_dict(filename)
        state_address_map = {}
        state_gstin_map = {}
        state_name_map = {}
        state_city_map = {}
        state_pin_code_map = {}
        if csv_rows and len(csv_rows) > 0:
            for i in range(len(csv_rows)-1):
                j = i+1


if __name__ == '__main__':
    ScriptGenerator.make_data('../Data/input.csv')

