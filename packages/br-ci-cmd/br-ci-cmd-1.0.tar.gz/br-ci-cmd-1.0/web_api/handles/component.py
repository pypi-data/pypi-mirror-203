from datetime import datetime

from mongoengine.queryset.visitor import Q

from ..models.Component import Component
from ..schemas import component as ComponentSchemas


# 新增component
def add_component(data: ComponentSchemas.Component):
    dateNow = datetime.now()
    data.updatedTime = dateNow
    component = Component(**data.dict())
    component.save()
    return component


# 根据parent获取子components
def get_component_list_by_parent(query: ComponentSchemas.QueryComponent):
    q = Q()
    if query.parentComponent:
        q &= Q(parentComponent=query.parentComponent)
    return {Component.objects(q)}


# 获取父级component
def get_components():
    return {Component.objects}
