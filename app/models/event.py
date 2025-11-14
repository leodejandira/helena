from pydantic import BaseModel 
from datetime import datetime, date
from typing import Optional, Dict, Any
from uuid import UUID
''''
Pydantic for data validation formats (basemodel)
datetime for work with data and hours
typing for chose a type of our variables (conditional variable, for low memory use)
UUID for genered random universal identificator (security)
'''


class PlanBase(BaseModel):
    '''
    base class for all plans (structure)
    fields:
        name (string - obrigatory), description (string), contect (sting)
    '''
    name: str
    description: Optional[str] = None
    context: Optional[Dict[str, Any]] = None

class PlanCreate(PlanBase):
    '''
    inherits PlanBase
    empity
    '''
    pass

class Plan(PlanBase):
    '''
    inherits Planbase
    Principal plan model
    fields
        id (uuid), status (string),  created_at (datetime), updated_at: (datetime - register of last used time of this plan)
    '''
    id: UUID
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        '''
        intern class for pydantic
        try complete field with atributes or methods, 
        instand of use simple  correlation of names od atributes
        '''
        from_attributes = True

class TaskBase(BaseModel):
    '''
    inherits BaseModel
    base class for all tasks (structure)
    fields:
        description (string), due_date (datetime), priority (int, 1 is the lowerest value)
    '''
    description: str
    due_date: Optional[date] = None
    priority: int = 1

class TaskCreate(TaskBase):
    '''
    inherits taskbase
    add field plan_id (uuid)
    '''
    plan_id: UUID

class Task(TaskBase):
    '''
    inherists taskbase
    Principal task model
    fields
        id (uuid), plan_id (uuid), status (string),  created_at (datetime), updated_at: (datetime - register of last used time of this plan)
    '''
    id: UUID
    plan_id: UUID
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        '''
        intern class for pydantic
        try complete field with atributes or methods, 
        instand of use simple  correlation of names od atributes
        '''
        from_attributes = True