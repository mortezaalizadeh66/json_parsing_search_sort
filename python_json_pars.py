import json
import random
from datetime import datetime, timedelta
from fuzzywuzzy import fuzz
#pip install fuzzywuzzy


# Generate 20 people with random names and families
people = []
for i in range(20):
    name = 'Person{}'.format(i+1)
    family = random.choice(['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Miller'])
    timestamp = (datetime.now() - timedelta(days=random.randint(0, 365), hours=random.randint(0, 23),
                                             minutes=random.randint(0, 59), seconds=random.randint(0, 59))).strftime('%Y-%m-%d %H:%M:%S')
    people.append({'name': name, 'family': family, 'timestamp': timestamp})

# Save the people to a JSON file
with open('people.json', 'w') as f:
    json.dump(people, f)
    print(people)

    sorted_data_time = sorted(people, key=lambda item: item['timestamp'])

    print("newwwwwwwwwwwwww")
    # Print the sorted data
    for item in sorted_data_time:
        print(item)
    print("newwwwwwwwwwwwww")
    sorted_data_name = sorted(people, key=lambda item: item['name'])
    for item in sorted_data_name:
        print(item)
    # Search for a name in the data
    name = input("Enter name to search for: ")
    for record in people:
        similarity_score = fuzz.ratio(record['name'], name)
        if similarity_score > 50:
        #if record['name'] == name:
            print(record)
            break
    else:
            print(f"No record found for name '{name}'")
