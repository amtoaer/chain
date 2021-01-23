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
        # 使用 faker 随机生成数据
        for _ in range(20):
            self.hospital.append(self.fake.company())
            self.doctor.append(self.fake.name())
            self.patient.append(self.fake.name())
        self.x = []
        # 测试一
        self.time_index = []
        self.time_traversal = []
        # 测试二
        self.time_insert_data = []
        self.time_update_index = []
        # 测试三
        self.extra_time_ratio = []
        # 测试四
        self.time_index_by_position = []
        self.time_traversal_by_position = []

    def test(self):
        '''
        测试一：不断将数据写入链，每写100个查询一次，得到查询时间（索引/遍历）和数据量的关系
        测试二：不断将数据写入链，每写100个记录一次写入时间，得到写入时间（写入链时间/更新索引时间）和数据集大小的关系
        测试三：不断将数据写入链，每写100个记录一次更新索引时间/总写入时间之比，得到比值与数据集大小的关系
        测试四：将数据写入链后，每隔100个记录进行一次查询，得到查询时间与查找位置的关系
        '''
        count = 1
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
                        insert_data, update_index = self.forTest.new_transaction(
                            item)
                        # 每插入100个查询一次
                        if count % 100 == 0:
                            self.x.append(count)
                            # 测试二
                            self.time_insert_data.append(insert_data)
                            self.time_update_index.append(update_index)
                            # 测试三
                            self.extra_time_ratio.append(
                                update_index/(insert_data+update_index))
                            # 得到查询时间
                            time_traversal, time_index = self.forTest.search_transaction(
                                item)
                            # 测试一
                            self.time_index.append(time_index)
                            self.time_traversal.append(time_traversal)
                        count += 1
        count = 1
        for hospital in self.hospital:
            for department in self.department:
                for doctor in self.doctor:
                    for patient in self.patient:
                        if count % 100 == 0:
                            item = {
                                'hospital': hospital,
                                'department': department,
                                'doctor': doctor,
                                'patient': patient,
                                'content': str(count)}
                            time_traversal_by_position, time_index_by_position = self.forTest.search_transaction(
                                item)
                            self.time_traversal_by_position.append(
                                time_traversal_by_position)
                            self.time_index_by_position.append(
                                time_index_by_position)
                        count += 1

    def paint(self):
        plt.figure()
        plt.title('Figure 1')
        plt.plot(self.x, self.time_index, 'r--', label='time_index')
        plt.plot(self.x, self.time_traversal, 'g--', label='time_traversal')
        plt.xlabel('records')
        plt.ylabel('time')
        plt.legend()
        plt.figure()
        plt.title('Figure 2')
        plt.plot(self.x, self.time_insert_data,
                 'r--', label='time_insert_data')
        plt.plot(self.x, self.time_update_index,
                 'g--', label='time_update_index')
        plt.xlabel('records')
        plt.ylabel('time')
        plt.legend()
        plt.figure()
        plt.title('Figure 3')
        plt.plot(self.x, self.extra_time_ratio, 'r--',
                 label='time_update_index/time_total')
        plt.xlabel('records')
        plt.ylabel('radio')
        plt.legend()
        plt.figure()
        plt.title('Figure 4')
        plt.plot(self.x, self.time_index_by_position,
                 'r--', label='time_index')
        plt.plot(self.x, self.time_traversal_by_position,
                 'g--', label='time_traversal')
        plt.xlabel('records')
        plt.ylabel('time')
        plt.legend()
        plt.show()
