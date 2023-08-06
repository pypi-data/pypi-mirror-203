from typing import List, Optional

from pydantic import BaseModel


class GetLineManagerInfoList(BaseModel):
    EmployeeNo: Optional[List[str]] = []
