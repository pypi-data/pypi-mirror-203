from datetime import datetime

from ..models.TestCase import TestCase
from ..schemas import test_case as TestCaseSchema


# 添加test case数据
def add_test_case(data: TestCaseSchema.TestCase):
    dateNow = datetime.now()
    data.updatedTime = dateNow
    test_case = TestCase(**data.dict())
    test_case.save()
    return test_case
