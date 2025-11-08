from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any
from uuid import UUID
''''
Pydantic for data validation formats (basemodel)
datetime for work with data and hours
typing for chose a type of our variables (conditional variable, for low memory use)
UUID for genered random universal identificator (security)
'''

class MemoryBase(BaseModel):
    '''
    base class for all memories (structure)
    fields:
        title (string), content (string - obrigatory), type (sting - standart note), metadate (dict)
    '''
    title: Optional[str] = None
    content: str
    type: str = "note"
    metadata: Optional[Dict[str, Any]] = None

class MemoryCreate(MemoryBase):
    '''
    inherits memoryBase
    empity
    '''
    pass

class Memory(MemoryBase):
    '''
    inherits PlanBase
    model for creation of new  complete memory
    fields:
        id (uuid), sumary (string), created_at (datetime)
    '''
    id: UUID
    summary: Optional[str] = None
    created_at: datetime

    class Config:
        '''
        intern class for pydantic
        try complete field with atributes or methods, 
        instand of use simple  correlation of names od atributes
        '''
        from_attributes = True