import abc
import contextvars
from dataclasses import dataclass
from typing import Optional
from uuid import uuid4


@dataclass
class Tenant:
    """Class for keeping track of the current user"""

    company_id: str
    user_id: str
    intuit_tid: str = str(uuid4())
    token: Optional[str] = None


_tenant_context: contextvars.ContextVar[Optional[Tenant]] = contextvars.ContextVar(
    "tenant_context", default=None
)


class CurrentTenantFacade(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "getTenant")
            and callable(subclass.getTenant)
            and hasattr(subclass, "setTenant")
            and callable(subclass.setTenant)
            and hasattr(subclass, "clearTenant")
            and callable(subclass.clearTenant)
            or NotImplemented
        )

    @abc.abstractmethod
    def getTenant(self) -> Tenant:
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def setTenant(self, tenant: Tenant):
        """Extract text from the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def clearTenant(self):
        raise NotImplementedError


class CurrentTenantFacadeContextImpl(CurrentTenantFacade):
    def getTenant(self) -> Tenant:
        currentTenant = _tenant_context.get()
        if currentTenant is not None:
            return currentTenant
        else:
            raise Exception("Tenant is unset")

    def setTenant(self, tenant: Tenant):
        _tenant_context.set(tenant)

    def clearTenant(self):
        _tenant_context.set(None)


# TODO: Maybe move this to a globals file or a dependency injection container file
currentTenantFacade: CurrentTenantFacade = CurrentTenantFacadeContextImpl()
