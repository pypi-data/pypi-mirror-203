from . import schemas
from odoo.addons.component.core import Component


class CrmLeadService(Component):
    _inherit = "crm.lead.service"
    _name = "crm.lead.service"

    def _validator_create(self):
        validator_schema = super()._validator_create().copy()
        validator_schema.update(schemas.S_CRM_LEAD_CREATE)
        return validator_schema

    def _prepare_create(self, params):
        create_dict = super()._prepare_create(params)
        subscription_request_id = params.get(
            'subscription_request_id')
        if subscription_request_id:
            create_dict['subscription_request_id'] = subscription_request_id
            sr_record = self.env[
                'subscription.request'
            ].browse(subscription_request_id)
            if sr_record:
                if sr_record.partner_id:
                    create_dict['partner_id'] = sr_record.partner_id.id
        return create_dict
