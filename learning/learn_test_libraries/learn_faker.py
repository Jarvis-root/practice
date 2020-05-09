import faker

f = faker.Faker('zh-CN')

for i in range(2):
    print(f.last_name())

for i in range(2):
    print(f.address())

for i in range(2):
    print(f.pyiterable())

for i in range(2):
    print(f.email())

for i in range(2):
    print(f.location_on_land())