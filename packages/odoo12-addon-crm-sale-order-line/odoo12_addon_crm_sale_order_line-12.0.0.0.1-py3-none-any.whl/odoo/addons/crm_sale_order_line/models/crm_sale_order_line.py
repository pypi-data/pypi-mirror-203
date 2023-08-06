# -*- coding: utf-8 -*-
import json
from odoo import api, fields, models
from odoo.tools.translate import _


class CrmSaleOrderLine(models.Model):
    _name = "crm.sale.order.line"

    crm_lead_id = fields.Many2one('crm.lead', string=_("Related lead"))
    product_id = fields.Many2one('product.product', string=_("Product"))
    price_unit = fields.Float(string="Price unit")
    partner_id = fields.Many2one(
        'res.partner',
        compute="_get_partner_id",
        store=False
    )

    @api.depends('crm_lead_id')
    def _get_partner_id(self):
        self.ensure_one()
        if self.crm_lead_id:
            self.partner_id = self.crm_lead_id.id
