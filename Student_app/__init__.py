'''
this is to create some randon students

    from faker import Faker
    import random

    # Create a Faker instance
    fake = Faker()

    # Initialize an empty list to store student records
    student_records = []

    # Generate 30 random student records
    for _ in range(150):
        name = fake.name()
        dob = fake.date_of_birth(minimum_age=5, maximum_age=18)  # Generate DOB for students between 5 and 18 years old
        address = fake.address()
        mobile = fake.phone_number()
        parent_mobile = fake.phone_number()

        student_record = [name, dob, address, mobile[:10], parent_mobile[:10]]
        student_records.append(student_record)

    enr = {3: 226340316001,
    1: 236340316001,
    5: 216340316001}
    for stu in student_records:
        sem = random.choice([1,3,5])
        enroll = enr[sem]
        enr[sem]+= 1
        appstu.objects.create(
        stu_name= stu[0],
        stu_enroll = enroll,
        stu_sem = sem,
        stu_DOB = stu[1],
        stu_branch = 'Informtion Technology',
        stu_mobile_num = stu[3],
        stu_parents_mobile_num = stu[4],
        stu_address = stu[2]
        )
        enroll += 1
'''

