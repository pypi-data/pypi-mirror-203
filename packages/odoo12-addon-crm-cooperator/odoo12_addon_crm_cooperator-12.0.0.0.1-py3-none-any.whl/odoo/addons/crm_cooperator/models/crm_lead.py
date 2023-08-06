from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"
    subscription_request_id = fields.Many2one(
        "subscription.request", "Subscription Request"
    )

    @api.onchange('subscription_request_id')
    def _setup_partner_id(self):
        for record in self:
            if record.subscription_request_id:
                record.partner_id = \
                    record.subscription_request_id.partner_id.id
