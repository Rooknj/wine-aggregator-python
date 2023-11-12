from typing import Optional

from utils.tenant import CurrentTenantFacade, Tenant


class CurrentTenantFacadeFakeImpl(CurrentTenantFacade):
    _tenant: Optional[Tenant] = None

    def getTenant(self) -> Tenant:
        currentTenant = self._tenant
        if currentTenant is not None:
            return currentTenant
        else:
            raise Exception("Tenant is unset")

    def setTenant(self, tenant: Tenant):
        self._tenant = tenant

    def clearTenant(self):
        self._tenant = None
