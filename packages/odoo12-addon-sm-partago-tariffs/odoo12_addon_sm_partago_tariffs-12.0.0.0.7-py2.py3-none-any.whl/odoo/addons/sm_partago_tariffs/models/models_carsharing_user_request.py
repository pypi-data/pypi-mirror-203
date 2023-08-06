# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _


class carsharing_user_request(models.Model):
    _name = 'sm_partago_user.carsharing_user_request'
    _inherit = 'sm_partago_user.carsharing_user_request'

    tariffs_ids = fields.One2many(
        comodel_name='smp.sm_carsharing_tariff',
        inverse_name='related_carsharing_user_request_id',
        string=_("CS tariffs"))
