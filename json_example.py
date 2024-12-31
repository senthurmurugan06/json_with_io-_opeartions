import json
def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data written successfully to {file_path}")
def print_data(data):
    for i in loaded_data:
        print(f" {i}")
if __name__ == "__main__":
    file_path = "/Users/senthurmurugan/Documents/pyth1/data.json"
    data_to_write =[
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Alice", "age": 25, "city": "Wonderland"},
        {"name": "Bob", "age": 28, "city": "Paris"},
        {"name": "Charlie", "age": 35, "city": "London"}
    ]

    write_json(file_path, data_to_write)
    loaded_data = read_json(file_path)

    print_data(loaded_data)

