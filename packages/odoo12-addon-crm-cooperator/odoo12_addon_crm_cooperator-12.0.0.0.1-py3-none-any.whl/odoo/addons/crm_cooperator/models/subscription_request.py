from odoo import api, fields, models


class SubscriptionRequest(models.Model):
    _inherit = "subscription.request"

    @api.constrains('partner_id')
    def _setup_crm_partner_id(self):
        self.ensure_one()
        related_crm_leads = self.env['crm.lead'].search([
            ('subscription_request_id', '=', self.id)
        ])
        if related_crm_leads.exists():
            for lead in related_crm_leads:
                if not lead.partner_id:
                    if self.partner_id:
                        lead.partner_id = self.partner_id.id
                    else:
                        lead.partner_id = False
