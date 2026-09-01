from src.utils.common import (
    read_yaml_file,
    save_object,
    load_object,
    create_directories,
)


# 1. Test create_directories
create_directories([
    "artifacts/test",
    "artifacts/models",
])


# 2. Test save/load object
sample_object = {
    "project": "Customer Churn Prediction",
    "model": "Logistic Regression",
    "version": 1,
}

object_path = "artifacts/test/test_object.pkl"

save_object(object_path, sample_object)

loaded_object = load_object(object_path)

print("Original object:")
print(sample_object)

print("\nLoaded object:")
print(loaded_object)

print("\nObjects equal:")
print(sample_object == loaded_object)


# 3. Test YAML
yaml_data = read_yaml_file("config/schema.yaml")

print("\nYAML data:")
print(yaml_data)