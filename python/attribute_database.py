import mysql.connector

from colors import green
from attribute_data import query_single_attribute, get_collection_overview

# Replace the following with your MySQL credentials
db_config = {
    "host": "localhost",
    "port": 3001,
    "user": "your_user",
    "password": "joeynfTits!",
    "database": "attribute_data",
}

def create_table():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attribute_data (
            id INT collectionAddress VARCHAR(255),
            collectionAddress VARCHAR(255),
            attribute VARCHAR(255),
            attributeType VARCHAR(255),
            attributeCount INT,
            attributePercent DECIMAL(15, 2),
            floor DECIMAL(15, 2),
            usdFloor VARCHAR(255)
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

def insert_data(data):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    for item in data:
        cursor.execute("""
            INSERT INTO attribute_data (
                collectionAddress, attribute, attributeType, attributeCount, attributePercent, floor, usdFloor
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            item["collectionAddress"], item["attribute"], item["attributeType"],
            item["attributeCount"], item["attributePercent"], item["floor"], item["usdFloor"]
        ))

    connection.commit()
    cursor.close()
    connection.close()

def main():
    create_table()
    collection_address = "0xb5d5b4cd4303d985d83c228644b9ed10930a8152"
    attributes = get_collection_overview(collection_address)
    all_results = []
    for attribute in attributes["attributes"]:
        results = query_single_attribute(attribute, collection_address)
        for result in results:
            result["collectionAddress"] = collection_address
        all_results.extend(results)

    insert_data(all_results)

    print(green + 'Data successfully inserted into database.')

if __name__ == "__main__":
    main()
