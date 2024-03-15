import random
import string

class Random_Generator():
    def __init__(self, seed) -> None:
        random.seed(seed)

    def sample_one(self, length):
        return random.getrandbits(length*4)
        
    def generate_random_json(self):
        # Define a basic structure for the JSON with some random fields
        json_structure = {}
        
        # Determine the number of fields
        number_of_fields = random.randint(5, 10)
        
        for _ in range(number_of_fields):
            # Generate a random field name
            field_name = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))
            
            # Decide on the type of content for this field
            content_type = random.choice(['string', 'number', 'boolean'])
            
            if content_type == 'string':
                # Generate a random string
                content = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(5, 20)))
            elif content_type == 'number':
                # Generate a random number
                content = random.randint(0, 10000)
            else:  # boolean
                # Choose a random boolean value
                content = random.choice([True, False])
            
            # Add the field to the JSON structure
            json_structure[field_name] = content
        
        return json_structure

    def random_num(self, range):
        return random.randint(1, range)

class Log():
    def __init__(self, dir) -> None:
        self.dir = dir
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)

    def dump(self):
        with open(self.dir, "w") as f:
            for i, line in enumerate(self.lines):
                # f.write(f'{i}===================\n')
                f.write(line)
                # f.write('===================\n')
        f.close()