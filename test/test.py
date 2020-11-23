import matplotlib.pyplot as plt
from faker import Faker
from public.public import Public


class Test(object):
    def __init__(self):
        self.fake = Faker("zh_CN")
        self.forTest = Public()
        self.hospital = []
        self.department = ['急诊科', '内科', '外科']
        self.doctor = []
        self.patient = []
        for _ in range(20):
            self.hospital.append(self.fake.company())
            self.doctor.append(self.fake.name())
            self.patient.append(self.fake.name())

    def test(self):
        count = 1
        self.time_index = []
        self.time_traversal = []
        self.x = []
        for hospital in self.hospital:
            for department in self.department:
                for doctor in self.doctor:
                    for patient in self.patient:
                        item = {
                            'hospital': hospital,
                            'department': department,
                            'doctor': doctor,
                            'patient': patient,
                            'content': str(count)}
                        self.forTest.new_transaction(item)
                        # 每插入100个查询一次
                        if count % 100 == 0:
                            # 得到查询时间
                            times = self.forTest.search_transaction(item)
                            # 加入坐标
                            self.x.append(count)
                            self.time_index.append(times[0])
                            self.time_traversal.append(times[1])
                        count += 1

    def paint(self):
        plt.plot(self.x, self.time_index, 'r--', label='time_index')
        plt.plot(self.x, self.time_traversal, 'g--', label='time_traversal')
        plt.xlabel('records')
        plt.ylabel('time')
        plt.legend()
        plt.show()
